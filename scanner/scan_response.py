from enum import Enum, auto
from dataclasses import dataclass
from scanner.token import Token

class ScanResponseType(Enum):
    # when the passed character is a start of a new token
    VALID_TOKEN_COMPLETE = auto()

    # when the passed character still fits in the old token
    VALID_TOKEN_INCOMPLETE = auto()

    # when the passed character neither fit into the old token nor as a start of a new token
    INVALID = auto()

@dataclass(frozen=True, slots=True)
class ScanResponse():
    type: ScanResponseType
    token: Token
    nextTokenLiteral: str

    # when VALID_TOKEN_COMPLETE => pass complete token as token and new token as nextToken
    # when VALID_TOKEN_INCOMPLETE => pass token with a new char appended as token and None as nextToken
    # when INVALID => pass None as both token and nextToken