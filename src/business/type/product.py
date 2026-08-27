from enum import Enum 

class ProductName(Enum):
  ANTECIPACAO="ANTECIPACAO"
  PIX="PIX"
  TEF="TEF"
  UNICA="UNICA"

class Product:
  def __init__(self, name: ProductName):
    self.name = name

  @staticmethod
  def parse(value: str) -> 'Product':
    match value:
      case "ANTECIPACAO":
        return Product(ProductName.ANTECIPACAO)
      case "PIX":
        return Product(ProductName.PIX)
      case "TEF":
        return Product(ProductName.TEF)
      case "UNICA":
        return Product(ProductName.UNICA)
      case _:
        raise ValueError(f"Invalid product name: {value}")
