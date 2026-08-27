from src.business.domain.customer import CustomerBus
from src.business.domain.transaction import TransactionBus
from src.business.domain.product import ProductBus

from src.store.customer import CustomerDuckStore
from src.store.transaction import TransactionDuckStore
from src.store.product import ProductDuckStore

from src.app import App, AppConfig, BusConfig

from src.service.oportunity import OportunityService

import duckdb

def app():
  customer_db = duckdb.connect(database=':memory:')
  transaction_db = duckdb.connect(database=':memory:')
  product_db = duckdb.connect(database=':memory:')
  
  app_cfg = AppConfig(
    bus=BusConfig(
      customer_bus= CustomerBus(CustomerDuckStore(customer_db)),
      transaction_bus= TransactionBus(TransactionDuckStore(transaction_db)),
      product_bus= ProductBus(ProductDuckStore(product_db)),
    )
  )
  app = App(app_cfg)
  opportunity = OportunityService(app)
