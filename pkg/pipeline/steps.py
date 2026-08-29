from typing import Protocol

class Reader[T](Protocol):
  def read(self, resource_id: str) -> T:...

class Replacer[T](Protocol):   
  def replace(self, path: str, resource: T):...

class Appender[T](Protocol):   
  def append(self, path: str, resource: T):...

class Validator[T](Protocol):
  def __call__(self, resource: T) -> None: ...
  
class BasicStep[T, R]:
  def __init__(
    self, 
    source: Reader[T], 
    resource: str,
    target: R,
    path: str,
    validator: Validator[T]
  ):
    self.source = source
    self.resource = resource
    
    self.target = target
    self.path = path
    self.validator = validator

  def get_resource(self) -> T:
    resource = self.source.read(self.resource)
    self.validator(resource)
    return resource
    
class SourceReplacer[T](BasicStep[T, Replacer[T]]):
  def run(self):
    self.target.replace(self.path, self.get_resource())

class SourceAppender[T](BasicStep[T, Appender[T]]):
  def run(self):
    self.target.append(self.path, self.get_resource())
