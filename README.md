# TKiK-skaner

Skaner tokenów dla prostych wyrażeń matematycznych napisany w Python

Żeby uruchomić program należy użyć uv

`uv run main.py`

Wyrażenie do zeskanowania podawane jest przez standard input. Program wypisuje wszystkie tokeny w formacie `"[KOD]: [WARTOŚĆ]"`

## Tokeny

| **Nazwa** | **Wyrażenie regularne** | **Opis** |
|---|---|---|
| INTEGER | [0-9]+ | Liczba całkowita dodatnia, składająca się z samych cyfr |
| STRING | \"[^\"]*\" | Ciąg znaków, rozpoczęty i zakończony cudzysłowiem
| CHAR | '[^']' | Pojedynczy znak, rozpoczęty i zakończony pojedynczym cudzysłowiem
| ID | [a-zA-Z][a-zA-Z0-9] | Identyfikator składający się z jednej litery na początku a następnie ze znaków alfanumerycznych |
| PLUS | + | Znak dodawania |
| MINUS | - | Znak odejmowania |
| TIMES | * | Znak mnożenia |
| DIVIDE | / | Znak dzielenia |
| EQUALS | == | Znak równości |
| NOTEQUAL | != | Znak nierówności |
| GREATER_THAN | > | Znak większości |
| LESS_THAN | < | Znak mniejszości |
| OR | \|\| | Symbol lub |
| AND | && | Symbol i |
| NEGATE | ! | Znak negacji |
| LEFT_BRACKET | \\( | Otwarcie nawiasu |
| RIGHT_BRACKET | \\) | Zamknięcie nawiasu |
| LEFT_SQUARE_BRACKET | \\[ | Otwarcie nawiasu kwadratowego |
| RIGHT_SQUARE_BRACKET | \\] | Zamknięcie nawiasu kwadratowego |
| LEFT_BRACE | { | Otwarcie nawiasu klamrowego |
| RIGHT_BRACE | } | Zamknięcie nawiasu klamrowego |
| VARIABLE | var | Słowo kluczowe definiujące zmienną |
| FUNCTION | function | Słowo kluczowe definiujące funkcję |
| ASSIGN | = | Znak przypisania |
| DOT | \\. | Kropka |
| COMMA | , | Przecinek |
| SEMICOLON | ; | Średnik |
| IF | if | Słowo kluczowe instrukcji warunkowej if |
| ELSE | else | Słowo kluczowe instrukcji warunkowej else |
| FOR | for | Słowo kluczowe pętli for |
| WHILE | while | Słowo kluczowe pętli while |
| PRINT | print | Słowo kluczowe instrukcji print do wypisywania danych |
| INPUT | input | Słowo kluczowe instrukcji input do pobierania danych |
| COMMENT | \\/\\/[^\/\n]*\n | Komentarz |
| TAB | \t | Znak tabulacji |
| NEWLINE | \n | Znak nowej linii |