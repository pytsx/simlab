import duckdb

def pipeline():
  customer_db = duckdb.connect(database=':memory:')
  transaction_db = duckdb.connect(database=':memory:')
  product_db = duckdb.connect(database=':memory:')
