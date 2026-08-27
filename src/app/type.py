from dataclasses import dataclass


@dataclass 
class Customer:
  id: str
  name: str
  email: str
  phone: str

@dataclass 
class Product: 
  id: str
  name: str
  price: float

@dataclass 
class Transaction:
  id: str
  customer_id: str
  product_id: str
  datetime: str
  value: float
  tax: float
