import joblib
from sklearn.ensemble import RandomForestClassifier
from data_loader import load_and_clean

def train_model():
    df = load_and_clean('data/raw/global_supply_chain_risk_2026.csv')
    features = ['Geopolitical_Risk_Score', 'Fuel_Price_Index', 'Total_Risk_Index', 
                'Carrier_Reliability_Score', 'Weather_Enc', 'Transport_Enc']
    X, y = df[features], df['Disruption_Occurred']
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    joblib.dump(model, 'models/risk_model.pkl')
    print("✅ Model Trained and Saved to models/risk_model.pkl")
    return df

if __name__ == "__main__":
    train_model()