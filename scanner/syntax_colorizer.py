from scanner.token import TokenType, Token
from typing import List

def colorizeTokens(tokens: List[Token], outputFileName: str):
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