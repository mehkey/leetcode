import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values('recordDate', inplace=True)
    
    weather.sort_values('recordDate', inplace=True)
    return weather[((weather.temperature.diff() > 0) & (weather.recordDate.diff() == '1 days'))][['id']]

# Write your MySQL query statement below
SELECT w.id 
  FROM weather w , weather w_prev
 WHERE DATEDIFF(w.recordDate, w_prev.recordDate) = 1
   AND w.temperature    > w_prev.temperature;
   