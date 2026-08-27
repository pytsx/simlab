
from src.business.domain.customer import CustomerBus
from src.business.domain.transaction import TransactionBus
from src.business.domain.product import ProductBus

from src.store.customer import CustomerDuckStore
from src.store.transaction import TransactionDuckStore
from src.store.product import ProductDuckStore

from src.app import App, AppConfig, BusConfig

from src.service.oportunity import OportunityService

import duckdb

if __name__ == "__main__": 
  db = duckdb.connect(database=':memory:')

  cus_cfg = AppConfig(
    bus=BusConfig(
      customer_bus= CustomerBus(CustomerDuckStore(db)),
      transaction_bus= TransactionBus(TransactionDuckStore(db)),
      product_bus= ProductBus(ProductDuckStore(db)),
    )
  )

  app = App(cus_cfg)


  opportunity = OportunityService(app)
