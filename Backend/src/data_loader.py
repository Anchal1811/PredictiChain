import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_and_clean(path):
    df = pd.read_csv(path)
    # Feature Engineering: 2026 Risk Index
    df['Total_Risk_Index'] = (df['Geopolitical_Risk_Score'] * 0.6) + (df['Fuel_Price_Index'] * 0.4)
    
    # Categorical Encoding
    le = LabelEncoder()
    df['Weather_Enc'] = le.fit_transform(df['Weather_Condition'])
    df['Transport_Enc'] = le.fit_transform(df['Transport_Mode'])
    return df