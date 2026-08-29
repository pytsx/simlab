from src.app import App 

from typing import Protocol 

class Model(Protocol):
  def predict(self, data: object) -> object:...
  def train(self, data: object) -> None:...

class OportunityApp:
  def __init__(self, app: App):
    self._app = app
