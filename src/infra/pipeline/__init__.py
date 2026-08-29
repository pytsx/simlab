import dotenv
import os

from src.infra.providers.duckdb import DuckDBProvider
from src.infra.providers.tableau import TableauProvider, TableauConfig

from src.infra.pipeline.steps import SourceReplacer

dotenv.load_dotenv()

from pkg.runtime import Chain

def pipeline():
  tableau = TableauProvider(
    config=TableauConfig(
      server_address=os.getenv("TABLEAU_SERVER_ADDRESS", ''),
      use_server_version=os.getenv("TABLEAU_USE_SERVER_VERSION", "True").lower() == "true",
      http_options={
        "timeout": int(os.getenv("TABLEAU_HTTP_TIMEOUT", "1200"))
      },
      token_name=os.getenv("TABLEAU_TOKEN_NAME", ''),
      access_token=os.getenv("TABLEAU_ACCESS_TOKEN", ''),
      site_id=os.getenv("TABLEAU_SITE_ID", '')
    )
  )

  duckdb = DuckDBProvider(
    cfg=DuckDBProvider.Config(
      database="simlab.duckdb"
    )
  )
  
  Chain(
    lambda _: SourceReplacer(
      source=tableau.datasource(),
      resource="f42183d8-63a6-4580-826f-82ec91703529",
      target=duckdb,
      table="fattrnadq",
      schema={
        "BANDEIRA":   "string", 
        "CNPJ":       "string",
        "DAT_TRN":    "date",
        "PORTE":      "string",
        "TIP_TRN":    "string",
        "UF":         "string",
        "QTD_TRN":    "integer",
        "VLR_TRN":    "float",
        "VLR_DSC":    "float",
      }
    ).run(),
    final=lambda _: print("Pipeline completed successfully.")
  )

  