from scanner.scanner import scan
from scanner.scan_response import ScanResponse, ScanResponseType

toScan: str = "-2 2+3*435*(1-7)/ 12"

scan(toScan)