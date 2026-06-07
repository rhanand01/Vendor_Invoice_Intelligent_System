# Vendor Invoice Intelligence System

## Freight Cost Prediction & Invoice Risk Flagging

An end-to-end Machine Learning system designed to help finance and procurement teams:

- Predict expected freight costs for vendor invoices.
- Detect high-risk invoices requiring manual review.
- Reduce financial leakage and operational inefficiencies.
- Improve procurement planning and budgeting.

---

# Table of Contents

- Project Overview
- Business Objectives
- Data Sources
- Exploratory Data Analysis (EDA)
- Models Used
- Evaluation Metrics
- End-to-End Application
- Project Structure
- How to Run the Project
- Future Enhancements
- Author

---

# Project Overview

This project implements a complete machine learning pipeline for vendor invoice analytics.

The system consists of two predictive models:

### 1. Freight Cost Prediction (Regression)

Predicts the expected freight cost of an invoice based on purchase and inventory information.

### 2. Invoice Risk Flagging (Classification)

Identifies invoices that may require manual review because of unusual cost, freight, or operational patterns.

---

# Business Objectives

## Freight Cost Prediction

### Objective

Predict freight cost using:

- Quantity purchased
- Invoice value
- Historical purchasing behavior

### Business Value

- Better budgeting and forecasting
- Improved procurement planning
- Vendor cost negotiation support
- Freight cost optimization

---

## Invoice Risk Flagging

### Objective

Predict whether an invoice should be flagged for approval review.

### Business Value

- Detect abnormal invoices early
- Reduce financial risk
- Improve audit efficiency
- Reduce manual verification effort

---

# Data Sources

Data is stored in an SQLite database.

### Tables Used

#### vendor_invoice

Contains invoice-level information such as:

- Invoice amount
- Freight cost
- Invoice dates
- Vendor information

#### purchases

Contains item-level purchase details.

#### purchase_prices

Contains historical purchase pricing information.

#### begin_inventory

Beginning inventory records.

#### end_inventory

Ending inventory records.

---

# Exploratory Data Analysis (EDA)

EDA focuses on answering business-driven questions:

- Do flagged invoices have higher financial exposure?
- Does freight cost increase with quantity?
- Is there a linear relationship between quantity and freight?

### Statistical Analysis

- T-Test Analysis
- Correlation Analysis
- Distribution Analysis
- Outlier Detection

---

# Models Used

## Freight Cost Prediction (Regression)

### Baseline Model

- Linear Regression

### Advanced Models

- Decision Tree Regressor
- Random Forest Regressor (Final Model)

---

## Invoice Risk Flagging (Classification)

### Baseline Model

- Logistic Regression

### Advanced Models

- Decision Tree Classifier
- Random Forest Classifier (Final Model)

### Hyperparameter Tuning

- GridSearchCV
- Cross Validation
- F1 Score Optimization

---

# Evaluation Metrics

## Regression Metrics

Used for Freight Cost Prediction:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## Classification Metrics

Used for Invoice Risk Prediction:

- Accuracy
- Precision
- Recall
- F1-Score
- Classification Report
- Confusion Matrix
- Feature Importance Analysis

---

# End-to-End Application

A Streamlit application is developed to demonstrate the complete workflow.

### Features

- Enter invoice details
- Predict freight cost
- Evaluate invoice risk
- Real-time predictions
- User-friendly dashboard
- Explainable outputs

---

# Tech Stack

### Programming

- Python

### Database

- SQLite

### Machine Learning

- Scikit-Learn

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Deployment

- Streamlit

---

# Project Structure

```text
Vendor-Invoice-Intelligence-System/
│
├── data/
│   └── inventory.db
│
├── freight_cost_prediction/
│   ├── data_preprocessing.py
│   ├── train.py
│   ├── model_evaluation.py
│
├── invoice_flagging/
│   ├── data_preprocessing.py
│   ├── train.py
│   ├── model_evaluation.py
│
├── inference/
│   ├── predict_freight.py
│   └── predict_invoice_flag.py
│
├── models/
│   ├── predict_freight_model.pkl
│   ├── invoice_flagging.pkl
│   └── scaler.pkl
│
├── notebooks/
│   ├── Freight_Cost_Prediction.ipynb
│   └── Invoice_Flagging.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# How to Run the Project

## 1. Clone Repository

```bash
git clone https://github.com/yourusername/Vendor-Invoice-Intelligence-System.git
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Train Models

### Freight Prediction

```bash
python freight_cost_prediction/train.py
```

### Invoice Flagging

```bash
python invoice_flagging/train.py
```

---

## 4. Run Inference

### Freight Prediction

```bash
python inference/predict_freight.py
```

### Invoice Risk Prediction

```bash
python inference/predict_invoice_flag.py
```

---

## 5. Launch Streamlit Application

```bash
streamlit run app.py
```

---

# Future Enhancements

- XGBoost implementation
- LightGBM implementation
- SHAP explainability
- Vendor risk scoring
- Dashboard monitoring
- Cloud deployment (AWS/Azure)
- Automated retraining pipeline

---

# Results

### Freight Prediction

- Accurate freight cost forecasting
- Improved procurement planning

### Invoice Risk Flagging

- Early detection of suspicious invoices
- Reduced manual approval workload
- Better financial control

---

# Author

**Anand Hadapad**

Data Analyst | Data Scientist

- LinkedIn: [LinkedIn](https://www.linkedin.com/in/rhanand11)
- GitHub: [GitHub](https://github.com/rhanand01)
- Portfolio: [Portfolio](https://anand-analyst.netlify.app/)

---

## License

Anand Hadapad


