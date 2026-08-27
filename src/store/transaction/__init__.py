import duckdb
import pandas as pd 

class TransactionDuckStore:
  def __init__(self, db: duckdb.DuckDBPyConnection):
    self._db = db

  def query(self, query: str) -> pd.DataFrame:
    # Implement logic to execute a query and return results as a DataFrame
    self._db.execute(query)
    return self._db.fetchdf()

  def get(self, product_name: str, transaction_id: int) -> pd.DataFrame:
    # Implement logic to retrieve a specific customer by ID
    query = f"SELECT * FROM customers WHERE id = {transaction_id} AND product_name = '{product_name}'"
    return self.query(query)

  def list(self) -> pd.DataFrame:
    # Implement logic to list all customers
    query = "SELECT * FROM customers"
    return self.query(query)  
