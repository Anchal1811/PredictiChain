import pandas as pd
import numpy as np

def run_optimization(df):
    def calculate_ss(row):
        Z = 1.65
        avg_d = row['Weight_MT'] / 30
        # Disruption increases lead time variance (Sigma_LT)
        sigma_lt = 5.0 if row['Disruption_Occurred'] == 1 else 0.5
        sigma_d = avg_d * 0.1
        
        # Safety Stock Formula
        ss = Z * np.sqrt((row['Lead_Time_Days'] * (sigma_d**2)) + (avg_d**2 * sigma_lt**2))
        return round(ss, 2)

    df['Safety_Stock_MT'] = df.apply(calculate_ss, axis=1)
    df['Reorder_Point'] = round((df['Weight_MT']/30 * df['Lead_Time_Days']) + df['Safety_Stock_MT'], 2)
    df.to_csv('data/processed/final_analytics.csv', index=False)
    print("✅ Optimization Complete: Results saved to data/processed/final_analytics.csv")

if __name__ == "__main__":
    from data_loader import load_and_clean
    df = load_and_clean('data/raw/global_supply_chain_risk_2026.csv')
    run_optimization(df)