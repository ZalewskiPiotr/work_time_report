"""
Moduł obsługuje odczyt danych z plików źródłowych

Klasy:
- brak

Funkcje:
- line_is_start_day(line: str)
    Sprawdzenie czy podany tekst zawiera informację o dacie
- get_source_data(path_to_data_files: str) -> list[str]
    Odczyt listy plików z danymi
- get_source_data_from_one_file(src_data: str) -> list[list[str]]:
    Odczyt danych z jednego pliku źródłowego

Wyjątki:
- brak

Inne obiekty:
- brak

"""

# Standard library import
import os.path
from os import listdir


# Third party imports

# Local imports


def line_is_start_day(line: str) -> bool:
    """ Sprawdzenie czy podany tekst zawiera informację o dacie

    Funkcja przyjmuje jako parametr jedną linię tekstu i sprawdza czy podany tekst zawiera w sobie datę. Jeżeli tak, to
    zwracane jest True

    :param line: Tekst do sprawdzenia
    :type line: str
    :return: True - jeżeli podany tekst zawiera w sobie datę. False - jeżeli tekst nie zawiera daty
    :rtype: bool
    """
    if 'Today' in line \
            or 'Yesterday' in line \
            or 'Monday' in line \
            or 'Tuesday' in line \
            or 'Wednesday' in line \
            or 'Thursday' in line \
            or 'Friday' in line \
            or 'Saturday' in line \
            or 'Sunday' in line:
        return True
    else:
        return False


def get_source_data(path_to_data_files: str) -> list[list[str]]:
    """ Odczyt listy plików z danymi

    Funkcja przegląda katalog i z każdego znalezionego pliku odczytuje dane.

    :param path_to_data_files: Ścieżka do katalogu z plikami zawierającymi dane wejściowe
    :type path_to_data_files: str
    :return: Lista, której każda pozycja odpowiada danym dla jednego dnia z pliku źródłowego. Wewnętrzne pozycje listy są listami zawierającymi stringi
    :rtype: list[list[str]]
    """
    files_list = listdir(path_to_data_files)  # Pobranie listy plików z katalogu z danymi wejściowymi

    days_list = []
    for file_name in files_list:
        final_path_to_fata_file = path_to_data_files + file_name
        if os.path.isfile(final_path_to_fata_file):
            with open(final_path_to_fata_file, mode='r', encoding='utf-8') as src_file:
                src_data = src_file.read()
            data_one_file = get_source_data_from_one_file(src_data)
            if data_one_file is not None:
                days_list.extend(data_one_file)
    return days_list


def get_source_data_from_one_file(src_data: str) -> list[list[str]] | None:
    """ Odczyt danych z jednego pliku źródłowego

    Funkcja szuka linii z odpowiednią nazwą (patrz line_is_start_day()) i kolejne linie traktuje jako pozycje danego
    dnia. Funkcja zwraca listę, gdzie każda pozycja zawiera informacje z jednego dnia. Informacje z jednego dnia są w
    postaci listy stringów, np. list[poniedziałek['czynność 1','dana2'], wtorek['czynność x', 'dana x']]

    :param src_data: Zawartość pliku źródłowego
    :type src_data: str
    :return: None, jeżeli nie udało się odczytać danych wejściowych. Lista dni.
    :rtype: list[list[str]] lub None
    """
    if len(src_data) == 0:
        return None

    days_list = []
    positions_list = []
    for line in src_data.split('\n'):
        if line_is_start_day(line):
            if len(positions_list) > 0:
                days_list.append(positions_list.copy())
                positions_list.clear()
        positions_list.append(line)

    # Zapisanie na listę ostatniego dnia z pliku
    if len(positions_list) > 0:
        days_list.append(positions_list.copy())
        positions_list.clear()
    return days_list
