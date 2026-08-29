import pandas as pd 
from typing import Dict, Protocol

from src.infra.pipeline.validate import validate

class Reader(Protocol):
  def read(self, resource_id: str) -> pd.DataFrame:...

class Replacer(Protocol):   
  def replace(self, table: str, df: pd.DataFrame):...

class Appender(Protocol):   
  def append(self, table: str, df: pd.DataFrame):...

class BasicStep[R: Replacer | Appender]:
  def __init__(
    self, 
    source: Reader, 
    resource: str,
    target: R,
    table: str,
    schema: Dict[str, str]
  ):
    self.source = source
    self.resource = resource
    
    self.target = target
    self.table = table
    
    self.schema = schema
  
  def get_resource(self) -> pd.DataFrame:
    df = self.source.read(self.resource)
    print(df.head())
    validate(df, self.schema)
    return df 
    
class SourceReplacer(BasicStep[Replacer]):
  def run(self):
    self.target.replace(self.table, self.get_resource())

class SourceAppender(BasicStep[Appender]):
  def run(self):
    self.target.append(self.table, self.get_resource())
