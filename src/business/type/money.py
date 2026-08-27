from typing import Any, cast
from enum import Enum 

class CurrencyType(Enum):
  BRL="BRL"
  USD="USD"
  EUR="EUR"

class Money: 
  def __init__(self, currency: str, value: float):
    self.currency = currency
    self.value = value

  def __str__(self):
    return f"{self.currency} {self.value}"

  @staticmethod
  def parse(currency: str, value: float) -> 'Money':
    if currency not in CurrencyType.__members__:
      raise ValueError(f"Invalid currency type: {currency}")

    if not isinstance(cast(Any, value), (int, float)):
      raise ValueError(f"Invalid value type: {value}. Must be a number.")

    return Money(currency, value)
