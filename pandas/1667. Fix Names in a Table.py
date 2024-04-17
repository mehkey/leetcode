import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # Apply the str.capitalize() function to fix the names
    users['name'] = users['name'].str.capitalize()
    
    # Sort the result table by user_id in ascending order
    result_df = users.sort_values(by='user_id', ascending=True)
    
    return result_df


# Write your MySQL query statement below

UPDATE Users
SET name = CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2)));