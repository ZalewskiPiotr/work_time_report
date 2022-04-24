""" Moduł zawiera testy jednostkowe dla klasy Report z pliku report.py

Klasy:
- brak

Funkcje:
- test_activity_time()
    Sprawdzenie poprawności identyfikacji czasu
- test_month()
    Sprawdzenie poprawności zamiany nazwy miesiąca na numer

Wyjątki:
- brak

Inne obiekty:
- brak

"""
# Standard library imports
from datetime import datetime, timedelta, date as date_1
# Third party library imports
# Local imports
import pytest

from report import Report


def __prepare_one_day_for_report_good():
    one_day = [
        ['Thursday, 20 January7h 34m',
         'Realizacja zadań z poczty i Teams',
         'Stopwatch',
         '1h 3m	08:27 - 09:30	',
         'Zarządzanie sprintem - daily, planowanie, odbiór, zadania wynikające ze zdarzeń w sprincie',
         'Stopwatch',
         '39m	09:31 - 10:10	',
         'Rada Starszych - CI/CD',
         'Stopwatch',
         '2h 18m	10:10 - 12:28	',
         'Zadania organizacyjne - spotkania, rozmowy, planowanie zadań',
         'Stopwatch',
         '2h 20m	12:29 - 14:49	',
         'Realizacja zadań z poczty i Teams',
         'Stopwatch',
         '1h 12m	14:49 - 16:02	']
    ]
    return one_day


def __prepare_one_day_for_report_bad_date():
    one_day = [
        ['Thursday 20 January7h 34m',
         'Realizacja zadań z poczty i Teams',
         'Stopwatch',
         '1h 3m	08:27 - 09:30	',
         'Zarządzanie sprintem - daily, planowanie, odbiór, zadania wynikające ze zdarzeń w sprincie',
         'Stopwatch',
         '39m	09:31 - 10:10	',
         'Rada Starszych - CI/CD',
         'Stopwatch',
         '2h 18m	10:10 - 12:28	',
         'Zadania organizacyjne - spotkania, rozmowy, planowanie zadań',
         'Stopwatch',
         '2h 20m	12:29 - 14:49	',
         'Realizacja zadań z poczty i Teams',
         'Stopwatch',
         '1h 12m	14:49 - 16:02	']
    ]
    return one_day

def test_activity_time():
    """ Sprawdzenie poprawności identyfikacji czasu

    Test sprawdza czy funkcja identyfikująca czas w podanym stringu zwraca prawidłowe wartości
    """
    test_report = Report()
    value_hour = test_report._Report__get_activity_time('1h	08:13 - 09:13')
    value_hour_minute = test_report._Report__get_activity_time('1h 13m	08:13 - 09:13')
    value_minute = test_report._Report__get_activity_time('31m	08:13 - 09:13')
    value_no_time = test_report._Report__get_activity_time('31 08:13 - 09:13')
    value_2hour = test_report._Report__get_activity_time('1h 13h	08:13 - 09:13')
    value_empty = test_report._Report__get_activity_time('')

    assert value_hour == (1, 0)
    assert value_hour_minute == (1, 13)
    assert value_minute == (0, 31)
    assert value_no_time == (0, 0)
    assert value_2hour == (1, 0)
    assert value_empty == (0, 0)


def test_month():
    """ Sprawdzenie poprawności zamiany nazwy miesiąca na numer
    """
    test_report = Report()
    no_month = test_report._Report__get_month('Januaary or something else')
    january = test_report._Report__get_month('January')
    february = test_report._Report__get_month('February')
    march = test_report._Report__get_month('March')
    april = test_report._Report__get_month('April')
    may = test_report._Report__get_month('May')
    june = test_report._Report__get_month('June')
    july = test_report._Report__get_month('July')
    august = test_report._Report__get_month('August')
    september = test_report._Report__get_month('September')
    october = test_report._Report__get_month('October')
    november = test_report._Report__get_month('November')
    december = test_report._Report__get_month('December')

    assert no_month is None
    assert january == 1
    assert february == 2
    assert march == 3
    assert april == 4
    assert may == 5
    assert june == 6
    assert july == 7
    assert august == 8
    assert september == 9
    assert october == 10
    assert november == 11
    assert december == 12


def test_find_date_verify_today():
    """ Sprawdzenie poprawności zwracania daty dla dnia bieżącego
    """
    test_report = Report()
    result = test_report._Report__find_date('Today7h 33m')
    assert result == datetime.today().date()


def test_find_date_verify_yesterday():
    """ Sprawdzenie poprawności zwracania daty dla dnia wczorajszego
    """
    test_report = Report()
    result = test_report._Report__find_date('Yesterday7h 33m')
    assert result == datetime.today().date() - timedelta(days=1)


def test_find_date_verify_any_date():
    """ Sprawdzenie poprawności zwracania daty dla dnia z podaną konkretną datą
    """
    test_report = Report()
    result = test_report._Report__find_date('Friday, 26 November5h 48m')
    assert result == date_1(datetime.today().year, 11, 26)


def test_create_report_input_data_are_ok():
    """ Sprawdzenie czy przy podaniu prawidłowych danych raport się wykona
    """
    data_for_report = __prepare_one_day_for_report_good()
    test_report = Report()
    test_report.create_report(data_for_report)
    assert len(test_report._days_list) == 1
    assert len(test_report._days_list[0].position_list) == 4
    assert test_report._days_list[0].day == str(datetime.today().year) + '-01-20'
    assert test_report._days_list[0].hours_sum == 7
    assert test_report._days_list[0].minutes_sum == 32


def test_create_report_line_with_date_is_incorrect():
    """ Sprawdzenie czy zostanie zwrócony wyjątek ValueError, jeżeli linia z datą będzie zawierać nieprawidłowe dane
    """
    data_for_report = __prepare_one_day_for_report_bad_date()
    test_report = Report()
    with pytest.raises(ValueError):
        test_report.create_report(data_for_report)



