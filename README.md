# TKiK-skaner

Skaner tokenów dla prostych wyrażeń matematycznych napisany w Python

To run the project use uv

`uv run main.py`

## Tokeny

| **Nazwa**     | **Wyrażenie regularne** | **Opis**                                                                                        |
|---------------|-------------------------|-------------------------------------------------------------------------------------------------|
| INTEGER       | "[0-9]+"                | Liczba całkowita dodatnia, składająca się z samych cyfr                                         |
| ID            | "[a-zA-Z][a-zA-Z0-9]*"   | Identyfikator składający się z jednej litery na początku a następnie ze znaków alfanumerycznych |
| PLUS          | "\\+"                     | Znak dodawania                                                                                  |
| MINUS         | "-"                     | Znak odejmowania                                                                                |
| TIMES         | "\\*"                     | Znak mnożenia                                                                                   |
| DIVIDE        | "\\/"                     | Znak dzielenia                                                                                  |
| LEFT_BRACKET  | "\\("                     | Otwarcie nawiasu                                                                                |
| RIGHT_BRACKET | "\\)"                     | Zamknięcie nawiasu                                                                              |
| EMPTY         | ""                      | Pusty zbiór znaków                                                                              |