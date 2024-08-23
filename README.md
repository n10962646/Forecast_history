# Forecast_history

Analysis Summary
- Westpac had an average prediction error of approximately 109.02%.
- Joe Bloggs had an average prediction error of approximately 206.26%.
- Harry Spent had an average prediction error of approximately 152.85%.
  
Based on this analysis, Westpac was the most accurate forecaster overall, followed by Harry Spent, with Joe Bloggs having the largest average prediction error, indicating lower reliability.

The weighted accuracy scores for each forecaster, based on the inverse of their mean prediction errors, are as follows:

Westpac: 0.446 (44.6%)
Joe Bloggs: 0.236 (23.6%)
Harry Spent: 0.318 (31.8%)
Interpretation:
Westpac has the highest weighted score, indicating it is the most reliable forecaster according to this analysis. Harry Spent follows, with a moderate score, while Joe Bloggs has the lowest score, reflecting the highest average prediction error.

Challenges Faced:
- Data Inconsistencies: The dataset contained inconsistencies, such as missing values and erroneous entries (e.g., "I5%" instead of "15%"). 

- Outliers: Some forecasts, such as Joe Bloggs' "1500%" prediction in 2017, were extreme outliers that significantly impacted the average error calculation. Handling these outliers was crucial to avoid skewing the results.

- Different Forecast Horizons: The forecasts had different time horizons (e.g., 2-year, 4-year, 5-year), making direct comparisons challenging. This required careful consideration when interpreting the accuracy of each forecaster's predictions.
