import argparse

from typing import Callable

def cli(cmds: dict[str, Callable[[], None]]) -> None:
  parser = argparse.ArgumentParser()
  parser.add_argument(
    "command",
    choices=cmds.keys(),
    help="Popular o banco de dados com dados"
  )

  args = parser.parse_args()
  
  command = cmds[args.command]
  
  if command is not None:
    command()
