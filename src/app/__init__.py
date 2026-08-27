from dataclasses import dataclass 

from src.business.customer import CustomerBus
from src.business.transaction import TransactionBus
from src.business.product import ProductBus

@dataclass
class BusConfig:
  customer_bus: CustomerBus
  transactions_bus: TransactionBus
  products_bus: ProductBus

@dataclass
class AppConfig: 
  bus: BusConfig

class App:
  def __init__(self, cfg: AppConfig):
    self._cfg = cfg

__all__ = ["App", "AppConfig"]
