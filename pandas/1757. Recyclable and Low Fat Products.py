import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    result_df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return result_df[['product_id']]


# Write your MySQL query statement below
select product_id
from Products 
where low_fats = 'Y'
and recyclable = 'Y'