import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return pd.merge(sales, product, on='product_id')[['product_name', 'year', 'price']]

# Write your MySQL query statement below
     SELECT product_name, year, price 
       FROM Sales
 INNER JOIN Product ON
               Sales.product_id=Product.product_id;