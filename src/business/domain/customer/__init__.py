from typing import Protocol 
import pandas as pd 

from src.business.type import Document

class Store(Protocol):
  def query(self, query: str) -> pd.DataFrame:...
  def get(self, document: Document) -> pd.DataFrame:...
  def list(self) -> pd.DataFrame:...

class CustomerBus:
  def __init__(self, store: Store):
    self._store = store

  def has(self, document: Document) -> bool:
    # Implement logic to check if a customer exists in the store
    result = self._store.get(document)
    return not result.empty 

  def get(self, document: Document) -> pd.DataFrame:
    # Implement logic to retrieve a specific customer by ID from the store
    return self._store.get(document)

  def list(self) -> pd.DataFrame:
    # Implement logic to list all customers from the store
    return self._store.list()

  def query(self, query: str) -> pd.DataFrame:
    # Implement logic to query customers based on a specific condition
    return self._store.query(query)
