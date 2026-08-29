import pandas as pd
from pandas.api.types import (
  is_string_dtype,
  is_integer_dtype,
  is_float_dtype,
  is_bool_dtype,
  is_datetime64_any_dtype,
)


TYPE_VALIDATORS = {
  "string": is_string_dtype,
  "integer": is_integer_dtype,
  "float": is_float_dtype,
  "bool": is_bool_dtype,
  "datetime": is_datetime64_any_dtype,
  "date": is_datetime64_any_dtype,
}


def dataframe_schema_validator(
  df: pd.DataFrame,
  schema: dict[str, str]
) -> None:

  for column, expected_type in schema.items():

    if column not in df.columns:
      raise ValueError(
        f"Missing required column: {column}"
      )

    validator = TYPE_VALIDATORS.get(expected_type)

    if validator is None:
      raise ValueError(
        f"Unsupported schema type: {expected_type}"
      )

    if not validator(df[column]):
      raise TypeError(
        f"Invalid type for column '{column}': "
        f"expected '{expected_type}', "
        f"got '{df[column].dtype}'"
      )