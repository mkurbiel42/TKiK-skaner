from scanner.token import TokenType, Token, LanguageTokenType, LanguageToken
from typing import List

def colorizeTokensOld(tokens: List[Token], outputFileName: str):
    outStr = '<body style="background-color:#43464A;"><p style="font-family:arial;">'
    braketColors = [
        "#bd65e6",
        "#f039f0",
        "#aa1c74"
    ]
    bracketDepth = -1
    for token in tokens:
        if token.type == TokenType.LEFT_BRACKET: bracketDepth += 1
        outStr += f"""<span style=\"color:{
            "#ffffff" if token.type == TokenType.INTEGER else
            "#00ff00" if token.type == TokenType.ID else
            "#0084ff" if token.type in [
                TokenType.PLUS,
                TokenType.MINUS,
                TokenType.TIMES,
                TokenType.DIVIDE
            ] else
            braketColors[bracketDepth] if token.type in [
                TokenType.RIGHT_BRACKET,
                TokenType.LEFT_BRACKET
            ] else
            "#ff0000"
        };margin:2px;\">{token.value}</span>"""
        if token.type == TokenType.RIGHT_BRACKET: bracketDepth -= 1
    outStr += "</p></body>"
    with open(outputFileName, 'w') as f:
        f.write(outStr)

def colorizeTokens(tokens: List[Token], outputFileName: str):
    outStr = '<body style="background-color:#121314;"><pre><p style="font-family:arial;">'
    braketColors = [
        "#F0D703",
        "#DA639E",
        "#159FF0"
    ]
    bracketDepth = -1
    squareBracketDepth = -1
    braceDepth = -1
    for token in tokens:
        if token.type == LanguageTokenType.LEFT_BRACKET: bracketDepth += 1
        if token.type == LanguageTokenType.LEFT_SQUARE_BRACKET: squareBracketDepth += 1
        if token.type == LanguageTokenType.LEFT_BRACE: braceDepth += 1
        outStr += f"""<span style=\"color:{
            "#A6CE9A" if token.type == LanguageTokenType.INTEGER else
            "#A5D6FF" if token.type in [LanguageTokenType.STRING, LanguageTokenType.CHAR] else
            "#ffffff" if token.type == LanguageTokenType.ID else
            "#ffffff" if token.type in [
                LanguageTokenType.PLUS,
                LanguageTokenType.MINUS,
                LanguageTokenType.TIMES,
                LanguageTokenType.DIVIDE
            ] else
            "#ffffff" if token.type in [
                LanguageTokenType.EQUALS,
                LanguageTokenType.NOTEQUAL,
                LanguageTokenType.GREATER_THAN,
                LanguageTokenType.LESS_THAN,
                LanguageTokenType.ASSIGN
            ] else
            "#F1A17B" if token.type in [
                LanguageTokenType.OR,
                LanguageTokenType.AND,
                LanguageTokenType.NEGATE
            ] else
            braketColors[bracketDepth % len(braketColors)] if token.type in [
                LanguageTokenType.RIGHT_BRACKET,
                LanguageTokenType.LEFT_BRACKET
            ] else
            braketColors[squareBracketDepth % len(braketColors)] if token.type in [
                LanguageTokenType.RIGHT_SQUARE_BRACKET,
                LanguageTokenType.LEFT_SQUARE_BRACKET
            ] else
            braketColors[braceDepth % len(braketColors)] if token.type in [
                LanguageTokenType.RIGHT_BRACE,
                LanguageTokenType.LEFT_BRACE
            ] else
            "#38C9A1" if token.type in [LanguageTokenType.VARIABLE, LanguageTokenType.FUNCTION] else
            "#ffffff" if token.type in [
                LanguageTokenType.DOT,
                LanguageTokenType.COMMA,
                LanguageTokenType.SEMICOLON
            ] else
            "#C586C0" if token.type in [
                LanguageTokenType.IF,
                LanguageTokenType.ELSE,
                LanguageTokenType.FOR,
                LanguageTokenType.WHILE
            ] else
            "#C6A8D9" if token.type in [
                LanguageTokenType.PRINT,
                LanguageTokenType.INPUT
            ] else
            "#99BEB1" if token.type == LanguageTokenType.COMMENT else
            "#ff0000"
        };margin:2px;\">{token.value}</span>"""
        if token.type == LanguageTokenType.RIGHT_BRACKET: bracketDepth -= 1
        if token.type == LanguageTokenType.RIGHT_SQUARE_BRACKET: squareBracketDepth -= 1
        if token.type == LanguageTokenType.RIGHT_BRACE: braceDepth -= 1
    outStr += "</p></pre></body>"
    with open(outputFileName, 'w') as f:
        f.write(outStr)