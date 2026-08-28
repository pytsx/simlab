from src.infra.providers.duckdb import DuckDBProvider
from src.infra.providers.tableau import TableauProvider

from src.infra.pipeline.runner import runner
from src.infra.pipeline.steps import SourceReplacer

def pipeline():
  tableau = TableauProvider(
    config={}
  )

  duckdb = DuckDBProvider(
    cfg=DuckDBProvider.Config(
      database="simlab.duckdb"
    )
  )
  
  runner(
    SourceReplacer(
      source=tableau.datasource(),
      resource="datasource_id",
      target=duckdb,
      table="table_name",
      schema={"column1": "string", "column2": "int"}
    )
  )
  