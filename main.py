from scanner.scanner import scan
from scanner.syntax_colorizer import colorizeTokens
from scanner.scan_response import ScanResponse, ScanResponseType
from scanner.token import Token
from typing import List

print("Input the expression you want to scan: ")
toScan: str = input()

tokens: List[Token] = scan(toScan)

print("Podaj nazwę pliku do zapisania:")
outFileName: str = input()

colorizeTokens(tokens, outFileName)