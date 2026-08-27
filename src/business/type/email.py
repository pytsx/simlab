
from dataclasses import dataclass

@dataclass
class Email:
  local: str
  domain: str

  @classmethod 
  def parse(cls, value: str) -> 'Email':
    local, separator, domain = value.strip().partition("@")

    if not separator or not domain or not local:
      raise ValueError(f"Invalid email format: {value}")


    return cls(
      local=local, 
      domain=domain, 
    )

  def __str__(self):
    return f"{self.local}@{self.domain}"
