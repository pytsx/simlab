from dataclasses import dataclass

from src.business.type import id

@dataclass 
class Customer:
  id: id.ID
  name: str
  email: str
  phone: str
