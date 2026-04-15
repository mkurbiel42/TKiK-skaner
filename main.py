from scanner.scanner import scan
from scanner.scanner_language import scan as scan_l
from scanner.syntax_colorizer import colorizeTokens
from scanner.scan_response import ScanResponse, ScanResponseType
from scanner.token import Token, LanguageToken
from typing import List

scType = input("Wybierz rodzaj skanera: 1 - wyrażenie matematyczne, 2 - własny język: ")

toScan: str
if scType == "1":
    print("Podaj wyrażenie do zeskanowania: ")
    toScan: str = input()
    tokens: List[Token] = scan(toScan, fullLanguage=True)
elif scType == "2":
    print("Podaj nazwę pliku do zeskanowania: ")
    with open(input(), 'r') as f:
        toScan: str = f.read()
    tokens: List[LanguageToken] = scan_l(toScan, fullLanguage=True)

if scType == "2":
    print("Podaj nazwę pliku do zapisania:")
    outFileName: str = input()
    colorizeTokens(tokens, outFileName)