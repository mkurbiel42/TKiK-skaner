from scanner.scan_response import ScanResponse, ScanResponseType
from scanner.token import Token, TokenType, LanguageToken, LanguageTokenType
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

languageTokenValidators: dict[LanguageTokenType, Callable[[str], bool]] = {
    LanguageTokenType.INTEGER: lambda lit: lit.isnumeric(),
    LanguageTokenType.STRING: lambda lit: len(lit) >= 2 and lit[0] == '"' and lit[-1] == '"',
    LanguageTokenType.STRING_INCOMPLETE: lambda lit: len(lit) > 0 and lit[0] == '"' and '"' not in lit[1:],
    LanguageTokenType.CHAR: lambda lit: len(lit) == 3 and lit[0] == "'" and lit[-1] == "'",
    LanguageTokenType.CHAR_INCOMPLETE: lambda lit: len(lit) > 0 and lit[0] == "'" and "'" not in lit[1:],
    LanguageTokenType.PLUS: lambda lit: lit == "+",
    LanguageTokenType.MINUS: lambda lit: lit == "-",
    LanguageTokenType.TIMES: lambda lit: lit == "*",
    LanguageTokenType.DIVIDE: lambda lit: lit == "/",
    LanguageTokenType.EQUALS: lambda lit: lit == "==",
    LanguageTokenType.NOTEQUAL: lambda lit: len(lit)>0 and "!=".startswith(lit),
    LanguageTokenType.GREATER_THAN: lambda lit: len(lit)>0 and ">".startswith(lit),
    LanguageTokenType.LESS_THAN: lambda lit: lit == "<",
    LanguageTokenType.OR: lambda lit: len(lit)>0 and "||".startswith(lit),
    LanguageTokenType.AND: lambda lit: len(lit)>0 and "&&".startswith(lit),
    LanguageTokenType.NEGATE: lambda lit: lit == "!",
    LanguageTokenType.LEFT_BRACKET: lambda lit: lit == "(",
    LanguageTokenType.RIGHT_BRACKET: lambda lit: lit == ")",
    LanguageTokenType.LEFT_SQUARE_BRACKET: lambda lit: lit == "[",
    LanguageTokenType.RIGHT_SQUARE_BRACKET: lambda lit: lit == "]",
    LanguageTokenType.LEFT_BRACE: lambda lit: lit == "{",
    LanguageTokenType.RIGHT_BRACE: lambda lit: lit == "}",
    LanguageTokenType.VARIABLE: lambda lit: lit == "var",
    LanguageTokenType.FUNCTION: lambda lit: lit == "function",
    LanguageTokenType.ASSIGN: lambda lit: lit == "=",
    LanguageTokenType.DOT: lambda lit: lit == ".",
    LanguageTokenType.COMMA: lambda lit: lit == ",",
    LanguageTokenType.SEMICOLON: lambda lit: lit == ";",
    LanguageTokenType.IF: lambda lit: lit == "if",
    LanguageTokenType.ELSE: lambda lit: lit == "else",
    LanguageTokenType.FOR: lambda lit: lit == "for",
    LanguageTokenType.WHILE: lambda lit: lit == "while",
    LanguageTokenType.PRINT: lambda lit: lit == "print",
    LanguageTokenType.INPUT: lambda lit: lit == "input",
    LanguageTokenType.COMMENT: lambda lit: lit.startswith("//") and lit.endswith("\n"),
    LanguageTokenType.COMMENT_INCOMPLETE: lambda lit: lit.startswith("//") and "\n" not in lit,
    LanguageTokenType.TAB: lambda lit: lit == "\t",
    LanguageTokenType.NEWLINE: lambda lit: lit == "\n",
    LanguageTokenType.ID: lambda lit: len(lit) != 0 and lit[0].isalpha() and (len(lit) == 1 or lit[1:].isalnum()),
    LanguageTokenType.EMPTY: lambda lit: len(lit) == 0
}

tokensSpaceAllowed: List[LanguageTokenType] = [
    LanguageTokenType.STRING,
    LanguageTokenType.STRING_INCOMPLETE,
    LanguageTokenType.CHAR,
    LanguageTokenType.CHAR_INCOMPLETE,
    LanguageTokenType.COMMENT,
    LanguageTokenType.COMMENT_INCOMPLETE
]

def scan(toScan: str, fullyIgnoreWhitespace: bool = False, printTokens: bool = True, fullLanguage: bool = False) -> List[Token]:
    i: int = 0
    currentTokenLiteral: str = ""
    tokens: List[Token] = [] 

    while i < len(toScan):
        # print(i, toScan[i])
        # print("\n".join([str(t) for t in tokens]))
        if toScan[i] == " ":
            if fullyIgnoreWhitespace and i!=len(toScan)-1:
                i += 1
                continue
            currentToken = parseToken(currentTokenLiteral, fullLanguage)
            if currentToken.type not in tokensSpaceAllowed:
                if isValidToken(currentToken):
                    if currentToken.type != LanguageTokenType.EMPTY: tokens.append(currentToken)
                    currentTokenLiteral = ""
                else:
                    print(f"Invalid whitespace at position {i}")
                i += 1
                continue
        nextChar: str = toScan[i]
        
        resp: ScanResponse = getNextChar(nextChar, currentTokenLiteral, fullLanguage)

        match resp.type:
            case ScanResponseType.VALID_TOKEN_COMPLETE:
                currentTokenLiteral = resp.nextTokenLiteral
                if currentToken.type != LanguageTokenType.EMPTY: tokens.append(resp.token)

            case ScanResponseType.VALID_TOKEN_INCOMPLETE:
                if i == len(toScan) - 1:
                    if currentToken.type != LanguageTokenType.EMPTY: tokens.append(resp.token)
                    break
                currentTokenLiteral = resp.token.value
                i += 1

            case ScanResponseType.INVALID:
                print(f"Invalid char {nextChar} at position {i}")
                return

            case _:
                print("Something horrible happened")

    if printTokens: print("\n".join([str(t) for t in tokens]))
    return tokens
        

def getNextChar(char: str, currentTokenLiteral: str, fullLanguage: bool) -> ScanResponse:
    extendedTokenLiteral = currentTokenLiteral + char
    extendedToken = parseToken(extendedTokenLiteral, fullLanguage)

    if isValidToken(extendedToken):
        return ScanResponse(ScanResponseType.VALID_TOKEN_INCOMPLETE, extendedToken, None)
    
    currentToken = parseToken(currentTokenLiteral, fullLanguage)

    if not isValidToken(extendedToken) and isValidToken(currentToken) and currentToken.type != TokenType.EMPTY:
        return ScanResponse(ScanResponseType.VALID_TOKEN_COMPLETE, currentToken, "")
    
    if not isValidToken(extendedToken) and currentToken.type == TokenType.EMPTY:
        return ScanResponse(ScanResponseType.INVALID, None, None)
        
def isValidToken(token: Token) -> bool:
    return token.type != TokenType.INVALID

def parseToken(tokenLiteral: str, fullLanguage: bool) -> Token:
    for type, validator in (languageTokenValidators if fullLanguage else tokenValidators).items():
        if(validator(tokenLiteral)):
            return Token(type, tokenLiteral)

    return Token(TokenType.INVALID, tokenLiteral)