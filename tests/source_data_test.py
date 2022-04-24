""" Moduł zawiera testy jednostkowe dla funkcji z pliku source_data.py

Klasy:
- brak

Funkcje:
- test_get_source_data_from_one_file()
    Weryfikacja liczby zwracanych pozycji w liście
- def test_get_source_data_from_one_file_empty_src_data()
    Weryfikacja zwracanej wartości dla pustych danych wejściowych
- test_line_is_start_day_true()
    Weryfikacja czy zwracane jest True, jeżeli podano dzień
- test_line_is_start_day_false()
    Weryfikacja czy zwracane jest False, jeżeli nie podano dnia
- test_line_is_start_day_empty()
    Weryfikacja czy zwracane jest False gdy podano pustą wartość

Wyjątki:
- brak

Inne obiekty:
- brak

"""

# Standard library imports

# Third party library imports

# Local imports
from work_time_report import source_data

_test_data = "Today7h 33m\n" \
             "Realizacja zadań z poczty i Teams\n" \
            "Stopwatch\n" \
            "1h	08:13 - 09:13\n" \
            "Weryfikacja czasu pracy W1, W7\n" \
            "Stopwatch\n" \
            "1h 43m	09:13 - 10:57\n" \
            "Weryfikacja nowych zadań w Jirze: W1, W3, W7\n" \
            "Stopwatch\n" \
            "4m	10:57 - 11:02\n" \
            "Weryfikacja nowych zadań w Jirze: W1, W3, W7\n" \
            "Stopwatch\n" \
            "2m	11:03 - 11:05\n" \
            "Zadania organizacyjne - spotkania, rozmowy, planowanie zadań\n" \
            "Stopwatch\n" \
            "7m	11:05 - 11:13\n" \
            "Rozwój Wydziału Wytwarzania - rada starszych\n" \
            "Stopwatch\n" \
            "4h 35m	11:13 - 15:48\n" \
            "Yesterday6h 21m\n" \
            "Realizacja zadań z poczty i Teams\n" \
            "Stopwatch\n" \
            "40m	09:30 - 10:11\n" \
            "Rozwój Wydziału Wytwarzania - rada starszych\n" \
            "Stopwatch\n" \
            "1h 44m	10:11 - 11:56\n" \
            "Zadania organizacyjne - spotkania, rozmowy, planowanie zadań\n" \
            "Stopwatch\n" \
            "50m	11:56 - 12:46\n" \
            "Realizacja zadań z poczty i Teams\n" \
            "Stopwatch\n" \
            "3h 5m	12:46 - 15:52\n" \
            "Friday, 26 November5h 48m\n" \
            "Analiza pracy w nowej jirze z serwisem - mail od Doroty\n" \
            "Stopwatch\n" \
            "48m	08:03 - 08:52\n" \
            "Zlecenie przygotować dla Rafała\n" \
            "Stopwatch\n" \
            "10m	08:59 - 09:09\n" \
            "Weryfikacja czasu pracy W1, W3, W4, W7\n" \
            "Stopwatch\n" \
            "40m	09:10 - 09:50\n" \
            "Rozwój Wydziału Wytwarzania - rada starszych\n" \
            "Stopwatch\n" \
            "6m	09:50 - 09:57\n" \
            "Rozwój Wydziału Wytwarzania - rada starszych\n" \
            "Stopwatch\n" \
            "3h 20m	09:58 - 13:18\n" \
            "MAil od Gawła ze zgłoszeniami\n" \
            "Stopwatch\n" \
            "9m	13:38 - 13:48\n" \
            "Zrobić RETRO z protokołami\n" \
            "Stopwatch\n" \
            "32m	14:43 - 15:15\n"


def test_get_source_data_from_one_file():
    """ Weryfikacja liczby zwracanych pozycji w liście
    """
    data_list = source_data.get_source_data_from_one_file(_test_data)
    assert len(data_list) == 3


def test_get_source_data_from_one_file_empty_src_data():
    """ Weryfikacja zwracanej wartości dla pustych danych wejściowych
    """
    data_list = source_data.get_source_data_from_one_file('')
    assert data_list is None


def test_line_is_start_day_true():
    """ Weryfikacja czy zwracane jest True, jeżeli podano dzień
    """
    src_line = "Sunday, something else"
    is_start_day = source_data.line_is_start_day(src_line)
    assert is_start_day


def test_line_is_start_day_false():
    """ Weryfikacja czy zwracane jest False, jeżeli nie podano dnia
    """
    src_line = "Suinanday, something else"
    is_start_day = source_data.line_is_start_day(src_line)
    assert not is_start_day


def test_line_is_start_day_empty():
    """ Weryfikacja czy zwracane jest False gdy podano pustą wartość
    """
    src_line = ""
    is_start_day = source_data.line_is_start_day(src_line)
    assert not is_start_day
