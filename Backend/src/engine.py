import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib
import os

def run_predictichain_engine():
    # 1. LOAD DATA (Relative to Backend folder)
    raw_path = 'data/raw/global_supply_chain_risk_2026.csv'
    if not os.path.exists(raw_path):
        print(f"❌ Error: Could not find {raw_path}")
        return
        
    df = pd.read_csv(raw_path)
    
    # 2. DATA WRANGLING & CLEANING
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Feature Engineering: 2026 Vulnerability Score
    df['Vulnerability_Score'] = (df['Geopolitical_Risk_Score'] * 0.7) + (df['Fuel_Price_Index'] * 0.3)
    
    # Encoding categories for ML
    le = LabelEncoder()
    df['Weather_Enc'] = le.fit_transform(df['Weather_Condition'])
    df['Mode_Enc'] = le.fit_transform(df['Transport_Mode'])
    
    # 3. DEMAND FORECASTING (Simulated Prophet Logic)
    # We use a 7-day rolling average of 'Weight_MT' as the 'Predicted Demand'
    df = df.sort_values('Date')
    df['Predicted_Daily_Demand'] = df['Weight_MT'].rolling(window=7, min_periods=1).mean()
    df['Demand_Volatility'] = df['Weight_MT'].rolling(window=7, min_periods=1).std().fillna(df['Weight_MT'].mean() * 0.1)

    # 4. RISK MODEL (Backend AI)
    features = ['Geopolitical_Risk_Score', 'Fuel_Price_Index', 'Carrier_Reliability_Score', 'Distance_km', 'Weather_Enc', 'Mode_Enc']
    X = df[features]
    y = df['Disruption_Occurred']
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    
    os.makedirs('models', exist_ok=True)
    joblib.dump(model, 'models/risk_model.pkl')

    # 5. INVENTORY OPTIMIZATION (The "Gold" Feature)
    def calculate_metrics(row):
        Z = 1.65  # 95% Service Level
        avg_d = row['Predicted_Daily_Demand']
        sigma_d = row['Demand_Volatility']
        
        # Risk-Adjusted Lead Time Uncertainty (Sigma_LT)
        # If disruption predicted or occurred, uncertainty triples
        sigma_lt = 5.5 if row['Disruption_Occurred'] == 1 else 1.1
        
        # Safety Stock Formula: Z * sqrt( (LT * sigma_D^2) + (D^2 * sigma_LT^2) )
        ss = Z * np.sqrt((row['Lead_Time_Days'] * (sigma_d**2)) + (avg_d**2 * (sigma_lt**2)))
        
        # Financial impact: Carrying cost vs Revenue at risk
        carrying_cost = ss * 45  # $45 per MT
        revenue_at_risk = row['Weight_MT'] * 600 if row['Disruption_Occurred'] == 1 else 0
        
        return pd.Series([round(ss, 2), round(carrying_cost, 2), round(revenue_at_risk, 2)])

    df[['Safety_Stock_MT', 'Carrying_Cost', 'Revenue_at_Risk']] = df.apply(calculate_metrics, axis=1)
    
    # 6. OUTPUT FOR UI
    os.makedirs('data/processed', exist_ok=True)
    df.to_csv('data/processed/final_analytics.csv', index=False)
    print("✅ PredictiChain Backend: Optimization Complete and Model Saved.")

if __name__ == "__main__":
    run_predictichain_engine()