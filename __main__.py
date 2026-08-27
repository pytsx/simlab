
from src.business.customer import CustomerBus
from src.business.transaction import TransactionBus
from src.business.product import ProductBus

from src.store.customer import CustomerDuckStore
from src.store.transaction import TransactionDuckStore
from src.store.product import ProductDuckStore

from src.app import App, AppConfig, BusConfig

import duckdb

if __name__ == "__main__": 
  db = duckdb.connect(database=':memory:')

  cus_cfg = AppConfig(
    bus=BusConfig(
      customer_bus= CustomerBus(CustomerDuckStore(db)),
      transactions_bus= TransactionBus(TransactionDuckStore(db)),
      products_bus= ProductBus(ProductDuckStore(db)),
    )
  )

  app = App(cus_cfg)
