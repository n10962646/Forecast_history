# Import necessary libraries
import pandas as pd

# Load the data from the uploaded CSV file
df = pd.read_csv('/mnt/data/forecast_history.csv')

# Step 1: Data-Driven Accuracy Assessment
# Calculate actual percentage change year-over-year
df['Actual Change (%)'] = df['Median house price'].pct_change() * 100

# Clean percentage strings and convert to numeric
def clean_percentage(value):
    try:
        return float(value.strip('%').replace("I", "1"))
    except:
        return None

# Apply cleaning function to forecast columns
df['Westpac: 4 year forecast'] = df['Westpac: 4 year forecast'].apply(clean_percentage)
df['Joe Bloggs: 2 year forecast'] = df['Joe Bloggs: 2 year forecast'].apply(clean_percentage)
df['Harry Spent: 5 year forecast'] = df['Harry Spent: 5 year forecast'].apply(clean_percentage)

# Calculate prediction errors
df['Westpac Error (%)'] = (df['Westpac: 4 year forecast'] - df['Actual Change (%)']).abs()
df['Joe Bloggs Error (%)'] = (df['Joe Bloggs: 2 year forecast'] - df['Actual Change (%)']).abs()
df['Harry Spent Error (%)'] = (df['Harry Spent: 5 year forecast'] - df['Actual Change (%)']).abs()

# Step 2: Scenario-Based Evaluation

# Calculate mean errors for comparison (similar to weighting in Step 3)
mean_errors = {
    "Westpac": df['Westpac Error (%)'].mean(),
    "Joe Bloggs": df['Joe Bloggs Error (%)'].mean(),
    "Harry Spent": df['Harry Spent Error (%)'].mean()
}

# Step 3: Weighted Accuracy Scoring (Basic Implementation)
# Inverse of the mean error to give higher scores to more accurate forecasters

# Define weights based on the inverse of the mean errors
weights = {
    "Westpac": 1 / mean_errors["Westpac"],
    "Joe Bloggs": 1 / mean_errors["Joe Bloggs"],
    "Harry Spent": 1 / mean_errors["Harry Spent"]
}

# Normalize the weights to get a relative score out of 1
total_weight = sum(weights.values())
weighted_scores = {forecaster: weight / total_weight for forecaster, weight in weights.items()}

# Display results
print("Mean Errors by Forecaster:", mean_errors)
print("Weighted Accuracy Scores:", weighted_scores)
