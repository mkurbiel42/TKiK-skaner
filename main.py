from scanner.scanner import scan
from scanner.scanner_language import scan as scan_l
from scanner.syntax_colorizer import colorizeTokens
from typing import List

scType = input("Wybierz rodzaj skanera: 1 - wyrażenie matematyczne, 2 - własny język: ")

tokens: List[any] = None
toScan: str
if scType == "1":
    print("Podaj wyrażenie do zeskanowania: ")
    toScan: str = input()
    tokens = scan(toScan)
elif scType == "2":
    print("Podaj nazwę pliku do zeskanowania: ")
    with open(input(), 'r') as f:
        toScan: str = f.read()
    tokens = scan_l(toScan)

if scType == "2":
    print("Podaj nazwę pliku do zapisania:")
    outFileName: str = input()
    colorizeTokens(tokens, outFileName)