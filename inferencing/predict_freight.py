import joblib 
import pandas as pd
from pathlib import Path

# Resolve model path relative to this script's location
MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "predict_freight_cost.pkl"

def load_model(model_path = MODEL_PATH):
    """
    Load trained freight cost prediction model
    """
    with open(str(model_path),'rb') as f:
        model = joblib.load(f)
    return model

def predict_freight_cost(input_data):
    """
    predict freight cost for new vendor invoice.
    Parameters
    ------------
    input_data : dict

    return
    --------
    pd.DataFrame with predicted freight cost
    """
    model = load_model()
    input_df = pd.DataFrame(input_data)
    input_df['Predicted_Freight'] = model.predict(input_df).round()
    return input_df

if __name__ == "__main__":
    
    # example inference run (local testing)
    sample_data = {
        "Quantity" : [5,12,30,75],
        "Dollars" : [18500,9000,3000,200]
    }
    prediction = predict_freight_cost(sample_data)
    print(prediction)