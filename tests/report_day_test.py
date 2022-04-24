""" Moduł zawiera testy jednostkowe dla klasy ReportDay z pliku report_day.py

Klasy:
- brak

Funkcje:
- test_create_object_report_day()
    Sprawdzenie poprawności utworzenia obiektu klasy reportDay
- test_add_time()
    Sprawdzenie poprawności dodania czasu
- test_add_position()
    Sprawdzenie poprawności dodania pozycji o różnych nazwach
- test_join_position()
    Sprawdzenie poprawności dodania pozycji o takiej samej nazwie

Wyjątki:
- brak

Inne obiekty:
- brak

"""
# Standard library imports
from datetime import date

# Third party library imports

# Local imports
from work_time_report.report_day import ReportDay
from work_time_report.report_position import ReportPosition


def test_create_object_report_day():
    """ Sprawdzenie poprawności utworzenia obiektu klasy ReportDay
    """
    sd = ReportDay(date(2021, 12, 2))

    assert sd is not None
    assert type(sd) is ReportDay
    assert sd.day == '2021-12-02'
    assert len(sd.position_list) == 0


def test_add_time():
    """ Sprawdzenie poprawności dodania czasu

    Test sprawdza, czy prawidłowo sumują się godziny i minuty. Ważne jest tutaj sprawdzenie czy po przekroczeniu 59
    minut, prawidłowo zostaną zwiększone godziny i zmniejszone minuty
    """
    sd = ReportDay(date.today())
    sp = ReportPosition('aktywność 1', 1, 50)
    sd.add_position(sp)
    assert sd.hours_sum == 1
    assert sd.minutes_sum == 50

    sp1 = ReportPosition('aktywność 2', 2, 50)  # 1:50 + 2:50 = 4:40
    sd.add_position(sp1)
    assert sd.hours_sum == 4
    assert sd.minutes_sum == 40


def test_add_position():
    """ Sprawdzenie poprawności dodania pozycji o różnych nazwach

    Test sprawdza, czy lista pozycji obiektu zwraca prawidłową ilość pozycji. Powinny być dwie pozycje
    """
    sd = ReportDay(date.today())
    sp = ReportPosition('aktywność 1', 1, 50)
    sd.add_position(sp)

    sp1 = ReportPosition('aktywność 2', 1, 10)
    sd.add_position(sp1)

    assert len(sd.position_list) == 2

    assert sd.position_list[0].activity == 'aktywność 1'
    assert sd.position_list[0].minutes == 50
    assert sd.position_list[0].hours == 1

    assert sd.position_list[1].activity == 'aktywność 2'
    assert sd.position_list[1].minutes == 10
    assert sd.position_list[1].hours == 1

    assert sd.hours_sum == 3
    assert sd.minutes_sum == 0


def test_join_position():
    """ Sprawdzenie poprawności dodania pozycji o takiej samej nazwie

    Test sprawdza, czy lista pozycji obiektu zwraca prawidłową ilość pozycji oraz prawidłowy czas. Obydwie pozycje
    powinny się złączyć w jedną, a czas zsumować
    """
    sd = ReportDay(date.today())
    sp = ReportPosition('aktywność 1', 1, 50)
    sp1 = ReportPosition('aktywność 1', 1, 50)
    sd.add_position(sp)
    sd.add_position(sp1)

    assert len(sd.position_list) == 1
    assert sd.position_list[0].activity == 'aktywność 1'
    assert sd.position_list[0].minutes == 40
    assert sd.position_list[0].hours == 3

    assert sd.hours_sum == 3
    assert sd.minutes_sum == 40
