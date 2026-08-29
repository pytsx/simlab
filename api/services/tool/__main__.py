from api.services.tool.cli import cli

from src.infra.pipeline import pipeline

if __name__ == "__main__": 
  cli({
    "pipeline": pipeline,
  })