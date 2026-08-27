from dataclasses import dataclass
from enum import Enum

class DocumentType(Enum):
  CNPJ = "cnpj"
  CPF = "cpf"

@dataclass(frozen=True, slots=True)
class Document:

  value: str
  type: DocumentType

  @classmethod
  def parse(
    cls,
    value: str,
    type: DocumentType = DocumentType.CNPJ,
  ) -> "Document":
    digits = "".join(
      char
      for char in value
      if char.isdigit()
    )

    match type:
      case DocumentType.CNPJ:
        cls._validate_cnpj(digits)

      case DocumentType.CPF:
        cls._validate_cpf(digits)

      case _:
        raise ValueError(
            f"Unsupported document type: {type}"
        )

    return cls(
      value=digits,
      type=type,
    )

  # ---------------------------------------------------------
  # CNPJ
  # ---------------------------------------------------------

  @classmethod
  def _validate_cnpj(cls, value: str) -> None:
    if len(value) != 14:
      raise ValueError(f"Invalid CNPJ: {value}")

    if len(set(value)) == 1:
      raise ValueError(f"Invalid CNPJ: {value}")

    first_digit = cls._calculate_digit(
      value[:12],
      (5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2),
    )

    second_digit = cls._calculate_digit(
      value[:12] + first_digit,
      (6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2),
    )

    if value[-2:] != first_digit + second_digit:
      raise ValueError(f"Invalid CNPJ: {value}")

  # ---------------------------------------------------------
  # CPF
  # ---------------------------------------------------------

  @classmethod
  def _validate_cpf(cls, value: str) -> None:
    if len(value) != 11:
      raise ValueError(f"Invalid CPF: {value}")

    if len(set(value)) == 1:
      raise ValueError(f"Invalid CPF: {value}")

    first_digit = cls._calculate_digit(
      value[:9],
      (10, 9, 8, 7, 6, 5, 4, 3, 2),
    )

    second_digit = cls._calculate_digit(
      value[:9] + first_digit,
      (11, 10, 9, 8, 7, 6, 5, 4, 3, 2),
    )

    if value[-2:] != first_digit + second_digit:
      raise ValueError(f"Invalid CPF: {value}")

  # ---------------------------------------------------------
  # Shared
  # ---------------------------------------------------------

  @staticmethod
  def _calculate_digit(
    numbers: str,
    weights: tuple[int, ...],
  ) -> str:
    total = sum(
      int(number) * weight
      for number, weight in zip(numbers, weights)
    )

    remainder = total % 11

    return "0" if remainder < 2 else str(11 - remainder)

  # ---------------------------------------------------------
  # Representations
  # ---------------------------------------------------------

  @property
  def digits(self) -> str:
      return self.value

  @property
  def formatted(self) -> str:
    match self.type:
      case DocumentType.CNPJ:
        return (
          f"{self.value[:2]}."
          f"{self.value[2:5]}."
          f"{self.value[5:8]}/"
          f"{self.value[8:12]}-"
          f"{self.value[12:]}"
        )

      case DocumentType.CPF:
        return (
          f"{self.value[:3]}."
          f"{self.value[3:6]}."
          f"{self.value[6:9]}-"
          f"{self.value[9:]}"
        )

  def __str__(self) -> str:
      return self.formatted
