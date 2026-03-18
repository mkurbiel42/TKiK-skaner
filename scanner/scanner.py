from scanner.scan_response import ScanResponse, ScanResponseType
from scanner.token import Token, TokenType
from typing import Callable, List

tokenValidators: dict[TokenType, Callable[[str], bool]] = {
    TokenType.INTEGER: lambda lit: lit.isnumeric(),
    TokenType.ID: lambda lit: len(lit) != 0 and lit[0].isalpha() and (len(lit) == 1 or lit[1:].isalnum()),
    TokenType.PLUS: lambda lit: lit == "+",
    TokenType.MINUS: lambda lit: lit == "-",
    TokenType.TIMES: lambda lit: lit == "*",
    TokenType.DIVIDE: lambda lit: lit == "/",
    TokenType.LEFT_BRACKET: lambda lit: lit == "(",
    TokenType.RIGHT_BRACKET: lambda lit: lit == ")",
    TokenType.EMPTY: lambda lit: len(lit) == 0
}

def scan(toScan: str):
    i: int = 0
    currentTokenLiteral: str = ""
    tokens: List[Token] = [] 

    while i < len(toScan):
        if toScan[i] == " ":
            currentToken = parseToken(currentTokenLiteral)
            if isValidToken(currentToken):
                tokens.append(currentToken)
                currentTokenLiteral = ""
            else:
                print(f"Invalid whitespace at position {i}")

            i += 1
            continue
        nextChar: str = toScan[i]
        
        resp: ScanResponse = getNextChar(nextChar, currentTokenLiteral)

        match resp.type:
            case ScanResponseType.VALID_TOKEN_COMPLETE:
                currentTokenLiteral = resp.nextTokenLiteral
                tokens.append(resp.token)

            case ScanResponseType.VALID_TOKEN_INCOMPLETE:
                if i == len(toScan) - 1:
                    tokens.append(resp.token)
                    break
                currentTokenLiteral = resp.token.value
                i += 1

            case ScanResponseType.INVALID:
                print(f"Invalid char {nextChar} at position {i}")
                return

            case _:
                print("Something horrible happened")

    print("\n".join([str(t) for t in tokens]))
        

def getNextChar(char: str, currentTokenLiteral: str) -> ScanResponse:
    extendedTokenLiteral = currentTokenLiteral + char
    extendedToken = parseToken(extendedTokenLiteral)

    if isValidToken(extendedToken):
        return ScanResponse(ScanResponseType.VALID_TOKEN_INCOMPLETE, extendedToken, None)
    
    currentToken = parseToken(currentTokenLiteral)

    if not isValidToken(extendedToken) and isValidToken(currentToken) and currentToken.type != TokenType.EMPTY:
        return ScanResponse(ScanResponseType.VALID_TOKEN_COMPLETE, currentToken, "")
    
    if not isValidToken(extendedToken) and currentToken.type == TokenType.EMPTY:
        return ScanResponse(ScanResponseType.INVALID, None, None)
        
def isValidToken(token: Token) -> bool:
    return token.type != TokenType.INVALID

def parseToken(tokenLiteral: str) -> Token:
    for type, validator in tokenValidators.items():
        if(validator(tokenLiteral)):
            return Token(type, tokenLiteral)

    return Token(TokenType.INVALID, tokenLiteral)