import joblib
import pandas as pd
from pathlib import Path

# Resolve model path relative to this script's location
MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "predict_flag_invoice.pkl"

def load_model(model_path: str = MODEL_PATH):
    """
    Load trained classifier model.
    """
    with open(model_path, "rb") as f:
        model = joblib.load(f)

    return model


def predict_invoice_flag(input_data):
    """
    Predict invoice flag for new vendor invoices.

    Parameters
    ----------
    input_data : dict

    Returns
    -------
    pd.DataFrame with predicted flag
    """

    model = load_model()

    input_df = pd.DataFrame(input_data)

    input_df["Predicted_Flag"] = model.predict(input_df).round()

    return input_df


if __name__ == "__main__":
    input_data = {
        "invoice_quantity": [120],
        # "invoice_dollars": [5500],
        # "Freight": [100],
        # "total_item_quantity": [100],
        # "total_item_dollars": [5000]
    }

    print(predict_invoice_flag(input_data))