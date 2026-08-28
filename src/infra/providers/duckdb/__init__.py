from dataclasses import dataclass 
import duckdb
import pandas as pd 

class DuckDBProvider:
    @dataclass
    class Config: 
        database: str
        readonly: bool = False
        
    def __init__(self, cfg: Config):
        self.cfg = cfg

    def connect(self):
        return duckdb.connect(
            database=self.cfg.database,
            read_only=self.cfg.readonly
        )

    def replace(self, table: str, df: pd.DataFrame):
        ...
    
    def append(self, table: str, df: pd.DataFrame):
        ...