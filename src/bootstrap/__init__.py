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
  db = duckdb.connect("simlab.duckdb")
  
  app = App(
    cfg=AppConfig(
      bus=BusConfig(
        customer_bus= CustomerBus(CustomerDuckStore(db)),
        transaction_bus= TransactionBus(TransactionDuckStore(db)),
        product_bus= ProductBus(ProductDuckStore(db)),
      )
    )
  )

  opportunity = OportunityService(app)
