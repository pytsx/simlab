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

  def connect(self) -> duckdb.DuckDBPyConnection:
    return duckdb.connect(
      database=self.cfg.database,
      read_only=self.cfg.readonly
    )

  def replace(
    self,
    table: str,
    df: pd.DataFrame
  ) -> None:
    db = self.connect()

    try:
      db.register("_source", df)

      db.execute(
        f"""
        CREATE OR REPLACE TABLE "{table}"
        AS
        SELECT *
        FROM _source
        """
      )

    finally:
      db.close()

  def append(
    self,
    table: str,
    df: pd.DataFrame
  ) -> None:
    db = self.connect()

    try:
      db.register("_source", df)

      db.execute(
        f"""
        CREATE TABLE IF NOT EXISTS "{table}"
        AS
        SELECT *
        FROM _source
        LIMIT 0
        """
      )

      db.execute(
        f"""
        INSERT INTO "{table}" BY NAME
        SELECT *
        FROM _source
        """
      )

    finally:
      db.close()