from typing import Dict, Protocol

class Reader[T](Protocol):
  def read(self, resource_id: str) -> T:...

class Replacer[T](Protocol):   
  def replace(self, table: str, df: T):...

class Appender[T](Protocol):   
  def append(self, table: str, df: T):...

class BasicStep[T, R]:
  def __init__(
    self, 
    source: Reader[T], 
    resource: str,
    target: R,
    table: str,
  ):
    self.source = source
    self.resource = resource
    
    self.target = target
    self.table = table
    
  def get_resource(self) -> T:
    return self.source.read(self.resource) 
    
class SourceReplacer[T](BasicStep[T, Replacer[T]]):
  def run(self):
    self.target.replace(self.table, self.get_resource())

class SourceAppender[T](BasicStep[T, Appender[T]]):
  def run(self):
    self.target.append(self.table, self.get_resource())
