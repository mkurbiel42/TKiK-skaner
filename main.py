from scanner.scanner import scan
from scanner.scan_response import ScanResponse, ScanResponseType

print("Input the expression you want to scan: ")
toScan: str = input()

scan(toScan)