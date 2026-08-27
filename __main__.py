from bootstrap import app
from cli import cli

from src.infra.pipeline import pipeline

if __name__ == "__main__": 
  cli({
    "pipeline": pipeline,
    "app": app
  })