import duckdb
import pandas as pd 

from src.business.type import Document

class CustomerDuckStore:
  def __init__(self, db: duckdb.DuckDBPyConnection):
    self._db = db

  def query(self, query: str) -> pd.DataFrame:
    # Implement logic to execute a query and return results as a DataFrame
    self._db.execute(query)
    return self._db.fetchdf()

  def get(self, document: Document) -> pd.DataFrame:
    # Implement logic to retrieve a specific customer by ID
    query = f"SELECT * FROM customers WHERE id = {document}"
    return self.query(query)

  def list(self) -> pd.DataFrame:
    # Implement logic to list all customers
    query = "SELECT * FROM customers"
    return self.query(query)  
