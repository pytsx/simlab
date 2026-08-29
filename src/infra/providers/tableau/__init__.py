from dataclasses import dataclass
import pandas as pd
import tableauserverclient as TSC

from pathlib import Path 

class _WorkbookProvider:
    def read(self, resource_id: str) -> pd.DataFrame:
        # Implement the logic to read data from Tableau Workbook
        return pd.DataFrame()  # Placeholder for the actual DataFrame returned from Tableau

class _DatasourceProvider:
    def __init__(self, server: TSC.Server):
        self.server = server

    def download(self, ds_id: str, file_path: Path | None = None) -> Path:
        try:
            ds = self.server.datasources
            res = ds.download(ds_id, file_path)
            download_path = Path(res)

            if download_path.exists():
                id_path = file_path / Path(ds_id + ".tdsx") if file_path else Path(ds_id + ".tdsx")
                #remove se existe
                id_path.unlink(missing_ok=True)
                return download_path.rename(id_path)
            else:
                raise Exception(f"Failed to download datasource {ds_id}: File does not exist after download.")
        except Exception as e:
            raise Exception(f"Failed to download datasource {ds_id}: {e}")

    
    def read(self, resource_id: str) -> pd.DataFrame:
        downloaded_path = self.download(resource_id)
        # Implement the logic to read data from Tableau Datasource
        return pd.DataFrame()  # Placeholder for the actual DataFrame returned from Tableau

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

class TableauProvider:
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
        

    def login(self, auth: TSC.PersonalAccessTokenAuth = None):
        if not self.access_token and not auth:
            raise ValueError("No authentication method provided. Please provide either a default access token or an auth parameter.")

        try:
            if self.access_token:
                return self.server.auth.sign_in(self.access_token)
            if auth:
                return self.server.auth.sign_in(auth)
            else:
                raise Exception("Cannot connect to tableau without Credentials")
        except Exception as e:
            raise Exception(f"Failed to connect to Tableau: {e}")

        
    def workbook(self) -> _WorkbookProvider:
        # Implement the logic to get a TableauWorkbookProvider for the given resource_id
        return _WorkbookProvider()

    def datasource(self) -> _DatasourceProvider:
        # Implement the logic to get a TableauDatasourceProvider for the given resource_id
        return _DatasourceProvider(self.server)
