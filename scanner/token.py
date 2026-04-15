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

class LanguageTokenType(Enum):
    INTEGER = auto()
    STRING = auto()
    STRING_INCOMPLETE = auto()
    CHAR = auto()
    CHAR_INCOMPLETE = auto()
    ID = auto()
    PLUS = auto()
    MINUS = auto()
    TIMES = auto()
    DIVIDE = auto()
    EQUALS = auto()
    NOTEQUAL = auto()
    GREATER_THAN = auto()
    LESS_THAN = auto()
    OR = auto()
    OR_INCOMPLETE = auto()
    AND = auto()
    AND_INCOMPLETE = auto()
    NEGATE = auto()
    LEFT_BRACKET = auto()
    RIGHT_BRACKET = auto()
    LEFT_SQUARE_BRACKET = auto()
    RIGHT_SQUARE_BRACKET = auto()
    LEFT_BRACE = auto()
    RIGHT_BRACE = auto()
    VARIABLE = auto()
    FUNCTION = auto()
    ASSIGN = auto()
    DOT = auto()
    COMMA = auto()
    SEMICOLON = auto()
    IF = auto()
    ELSE = auto()
    FOR = auto()
    WHILE = auto()
    PRINT = auto()
    INPUT = auto()
    COMMENT = auto()
    COMMENT_INCOMPLETE = auto()
    TAB = auto()
    NEWLINE = auto()
    INVALID = auto()
    INCOMPLETE = auto()
    EMPTY = auto()

@dataclass(slots=True)
class Token():
    type: TokenType
    value: str

    def __str__(self):
        return f"{self.type.name}: {self.value}"

@dataclass(slots=True)
class LanguageToken():
    type: LanguageTokenType
    value: str

    def __str__(self):
        return f"{self.type.name}: {self.value}"