from typing import Protocol
 
class Step(Protocol):
  def run(self):...

def runner(*steps: Step):
  for step in steps:
    step.run()