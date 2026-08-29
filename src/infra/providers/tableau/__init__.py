from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Any
import pandas as pd
import tableauserverclient as TSC

from .snippets.datasource import download_tdsx, get_hyper_from_tdsx, read_hyper

from pkg.runtime import Chain

class _WorkbookProvider:
    def read(self, resource_id: str) -> pd.DataFrame:
        # Implement the logic to read data from Tableau Workbook
        return pd.DataFrame()  # Placeholder for the actual DataFrame returned from Tableau

class _DatasourceProvider:
    def __init__(self, auth: TableauAuth):
        self.auth = auth
    
    def _download_tdsx(self, resource_id: str) -> Path:
        with self.auth.login():
            download_path = download_tdsx(self.auth.server, resource_id)
            return download_path

    def read(self, resource_id: str) -> pd.DataFrame:
        return Chain(
            lambda _: self._download_tdsx(resource_id),
            lambda download_path:  get_hyper_from_tdsx(download_path, resource_id),
            final=lambda hyper_file: read_hyper(hyper_file, resource_id),
        )

@dataclass
class TableauConfig:
  server_address: str
  use_server_version: bool
  http_options: object
  token_name: str
  access_token: str
  site_id: str

class TableauAuth:
    def __init__(self, config: TableauConfig):
        self.server = TSC.Server(
            server_address=config.server_address,
            use_server_version=config.use_server_version, 
            http_options=config.http_options
        )  

        self.access_token = TSC.PersonalAccessTokenAuth(
            token_name=config.token_name,
            personal_access_token=config.access_token,
            site_id=config.site_id,
        )

    def login(self):
        if not self.access_token:
            raise ValueError("No authentication method provided. Please provide either a default access token or an auth parameter.")

        try:
            if self.access_token:
                return self.server.auth.sign_in(self.access_token)
            else:
                raise Exception("Cannot connect to tableau without Credentials")
        except Exception as e:
            raise Exception(f"Failed to connect to Tableau: {e}")

class TableauProvider:
    def __init__(self, config: TableauConfig):
        self.auth = TableauAuth(config)
        
    def workbook(self) -> _WorkbookProvider:
        # Implement the logic to get a TableauWorkbookProvider for the given resource_id
        return _WorkbookProvider()

    def datasource(self) -> _DatasourceProvider:
        # Implement the logic to get a TableauDatasourceProvider for the given resource_id
        return _DatasourceProvider(self.auth)
