from dataclasses import dataclass 

from src.business.domain import customer, transaction, product
from src.business.type import Document, DocumentType


@dataclass
class BusConfig:
  customer_bus: customer.CustomerBus
  transaction_bus: transaction.TransactionBus
  product_bus: product.ProductBus

@dataclass
class AppConfig: 
  bus: BusConfig

class App:
  def __init__(self, cfg: AppConfig):
    self._cfg = cfg

  def get_cutomer(self, doc: str):
    return self._cfg.bus.customer_bus.get(
      Document(doc, DocumentType.CNPJ)
    )

__all__ = ["App", "AppConfig", "BusConfig"]
