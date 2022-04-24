""" Moduł zawiera testy jednostkowe dla klasy ReportPosition z pliku report_position.py

Klasy:
- brak

Funkcje:
- test_create_object_report_position()
    Sprawdzenie poprawności utworzenia obiektu klasy ReportPosition
- test_bad_activity_name()
    Sprawdzenie poprawności nazwy czynności
- test_hours_not_number()
    Sprawdzenie czy godziny są liczbą
- test_minutes_not_number()
    Sprawdzenie czy minuty są liczbą
- test_minutes_out_of_range()
    Sprawdzenie poprawności wartości minut
- test_minutes_border_values()
    Sprawdzenie granicznych wartości minut

Wyjątki:
- brak

Inne obiekty:
- brak

"""
# Standard library imports

# Third party imports
import pytest

# Local imports
from work_time_report.report_position import ReportPosition


def test_create_object_report_position():
    """ Sprawdzenie poprawności utworzenia obiektu klasy ReportPosition
    """
    activity = 'Przygotowanie raportu'
    hours = 2
    minutes = 34

    sp = ReportPosition(activity, hours, minutes)

    assert sp is not None
    assert type(sp) is ReportPosition
    assert sp.activity == activity
    assert sp.hours == hours
    assert sp.minutes == minutes


def test_bad_activity_name():
    """ Sprawdzenie poprawności nazwy czynności

    Test sprawdza, czy utworzenie obiektu klasy ReportPosition zwróci wyjątek w przypadku gdy podany zostanie pusty ciąg
    zamiast nazwy czynności.
    """
    activity = ''
    hours = 2
    minutes = 34

    with pytest.raises(ValueError):
        ReportPosition(activity, hours, minutes)

    with pytest.raises(ValueError):
        ReportPosition(' ', hours, minutes)


def test_hours_not_number():
    """ Sprawdzenie czy godziny są liczbą

    Test sprawdza czy godziny podane w czasie tworzenia obiektu klasy ReportPosition są liczbą
    """
    activity = 'Nowa pozycja'
    hours = '34ala34'
    minutes = 34

    with pytest.raises(ValueError):
        ReportPosition(activity, hours, minutes)


def test_minutes_not_number():
    """ Sprawdzenie czy minuty są liczbą

    Test sprawdza czy godziny podane w czasie tworzenia obiektu klasy ReportPosition są liczbą
    """
    activity = 'Nowa pozycja'
    hours = 34
    minutes = 'minuty'

    with pytest.raises(ValueError):
        ReportPosition(activity, hours, minutes)


def test_minutes_out_of_range():
    """ Sprawdzenie poprawności wartości minut

    Test sprawdza czy w przypadku podania minut spoza zakresu 0-60 w czasie tworzenia obiektu klasy ReportPosition,
    zostanie wygenerowany wyjątek
    """
    activity = 'Nowa pozycja'
    hours = 34
    with pytest.raises(ValueError):
        ReportPosition(activity, hours, -1)

    with pytest.raises(ValueError):
        ReportPosition(activity, hours, 78)

    with pytest.raises(ValueError):
        ReportPosition(activity, hours, 60)


def test_minutes_border_values():
    """ Sprawdzenie granicznych wartości minut

    Test sprawdza zachowanie konstruktora w czasie tworzenia obiektu klasy ReportPosition dla granicznych wartości
    minut: 0 oraz 59
    """
    activity = 'Nowa pozycja'
    hours = 12
    minutes = 0
    minutes_1 = 59

    sp = ReportPosition(activity, hours, minutes)
    sp1 = ReportPosition(activity, hours, minutes_1)
    assert sp.minutes == minutes
    assert sp1.minutes == minutes_1
