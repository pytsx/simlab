from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PhoneNumber:
  country_code: str
  area_code: str
  number: str

  @classmethod
  def parse(
    cls,
    value: str,
    default_country_code: str = "55",
  ) -> "PhoneNumber":
    digits = "".join(char for char in value if char.isdigit())

    if not digits:
      raise ValueError(f"Invalid phone number: {value}")

    # Brasil sem DDI
    # 34999999999
    if len(digits) in (10, 11):
      country_code = default_country_code
      area_code = digits[:2]
      number = digits[2:]

    # Brasil com DDI
    # 5534999999999
    elif digits.startswith(default_country_code) and len(digits) in (12, 13):
      country_code = default_country_code
      area_code = digits[2:4]
      number = digits[4:]

    else:
      raise ValueError(f"Invalid phone number: {value}")

    return cls(
      country_code=country_code,
      area_code=area_code,
      number=number,
    )

  def __str__(self) -> str:
    return f"+{self.country_code}{self.area_code}{self.number}"
