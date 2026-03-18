from dataclasses import dataclass
from enum import Enum, auto

class TokenType(Enum):
    INTEGER = auto()
    ID = auto()
    PLUS = auto()
    MINUS = auto()
    TIMES = auto()
    DIVIDE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    INVALID = auto()
    INCOMPLETE = auto()
    EMPTY = auto()

@dataclass(slots=True)
class Token():
    type: TokenType
    value: str

    def __str__(self):
        return f"{self.type.name}: {self.value}"