from typing import Protocol 
import pandas as pd 

class Store(Protocol):
  def query(self, query: str) -> pd.DataFrame:...
  def get(self, product_name: str,transaction_id: int) -> pd.DataFrame:...
  def list(self) -> pd.DataFrame:...

class TransactionBus:
  def __init__(self, store: Store):
    self._store = store

  def has(self, product_name: str, transaction_id: int) -> bool:
    # Implement logic to check if a customer exists in the store
    result = self._store.get(product_name, transaction_id)
    return not result.empty 

  def get(self, product_name: str, transaction_id: int) -> pd.DataFrame:
    # Implement logic to retrieve a specific customer by ID from the store
    return self._store.get(product_name, transaction_id)

  def list(self) -> pd.DataFrame:
    # Implement logic to list all customers from the store
    return self._store.list()

  def query(self, query: str) -> pd.DataFrame:
    # Implement logic to query customers based on a specific condition
    return self._store.query(query)
