# Standard library import
import os.path
import sys
from datetime import datetime, timedelta, date
# Third party imports
# Local imports
import report_day
import report_position


class Report:
    """ Klasa reprezentuje cały raport

    Klasa odpowiada za przechowanie wszystkich odczytanych danych, które są potrzebne do przygotowania raportu. Klasa
    buduje taki raport i go zapisuje we wskazanym miejscu na dysku

    Atrybuty:
    ---------
    _days_list : list[report_day.ReportDay]
        Lista raportów dla poszczególnych dni

    Metody:
    -------
    create_report(self, data_for_report: list[list[str]])
        Utworzenie raportu na podstawie danych wejściowych
    save_report_to_file(self)
        Zapis raportu do pliku
    __find_date(cls, str_date: str) -> datetime.date
        Ustalenie daty na podstawie przekazanego tekstu
    __get_month(cls, date_string) -> int | None
        Funkcja ustala numer miesiąca
    __get_activity_time(cls, time_string) -> tuple[int, int]
        Funkcja ustala czas trwania aktywności.

    Wyjątki:
    --------
    ValueError
        Klasa zwraca wyjątek ValueError w metodzie create_report() w momencie, gdy otrzyma dane wejściowe w
        nieprawidłowym formacie.
    """

    def __init__(self):
        self._days_list: list[report_day.ReportDay] = []

    def create_report(self, data_for_report: list[list[str]]):
        """ Utworzenie raportu na podstawie danych wejściowych

        Funkcja tworzy raport na podstawie wszystkich odczytanych danych wejściowych.

        :param data_for_report: Dane na podstawie których utworzony zostanie raport
        :type data_for_report: list[list[str]]
        :return: ---
        :rtype: ---
        """
        for one_day_data in data_for_report:
            report_date = Report.__find_date(one_day_data[0])
            one_day = report_day.ReportDay(report_date)

            for index in range(1, len(one_day_data), 3):
                activity_name = one_day_data[index]
                if len(activity_name.strip()) > 0:
                    activity_hours, activity_minutes = Report.__get_activity_time(one_day_data[index + 2])
                    one_day.add_position(report_position.ReportPosition(activity_name, activity_hours,
                                                                        activity_minutes))

            self._days_list.append(one_day)

    def save_report_to_file(self, output_path: str):
        """ Zapis raportu do pliku

        Funkcja zapisuje wcześniej utworzony raport do pliku tekstowego.

        :param output_path: Ścieżka w której zostanie utworzony plik z raportem
        :type output_path: str
        :return: ---
        :rtype: ---
        """
        file_path = os.path.join(output_path, "report.txt")
        with open(file_path, 'w', encoding='UTF-8') as txt_file:
            for day in self._days_list:
                txt_file.write(day.day + "\n")
                for activity in day.position_list:
                    str_to_save = activity.activity + ';' + str(activity.hours) + 'h ' + str(activity.minutes) + 'm\n'
                    txt_file.write(str_to_save)

    @classmethod
    def __find_date(cls, str_date: str) -> datetime.date:
        """ Ustalenie daty na podstawie przekazanego tekstu

        Przekazany do funkcji tekst zawiera informacje o dacie. Tekst wygląda tak 'Friday, 26 November5h 48m' lub
        'Today7h 33m'. Jeżeli w tekście jest słowo 'Today' to funkcja ustala datę na podstawie bieżącej daty systemowej.
        Dla słowa 'Yesterday' funkcja ustala datę na podstawie daty systemowej i odejmuje jeden dzień. W pozostałych
        przypadkach data podana jest w przekazanym tekście

        :param str_date: Tekst, w którym należy szukać daty
        :type str_date: str
        :return: Ustalona data
        :rtype: datetime.date
        """
        if 'Today' in str_date:
            return datetime.today().date()
        elif 'Yesterday' in str_date:
            return datetime.today().date() - timedelta(days=1)
        else:
            # Dla pozostałych dni linia z datą ma format 'Friday, 26 December8h 31m'. Bierzemy to co jest po przecinku
            # i wyciągamy z tego datę
            if str_date.find(',') == -1:
                raise ValueError(f"Nieprawidłowe dane wejściowe - brakuje przecinka: '{str_date}'")
            str_to_find_date = str_date.split(',')[1].strip()

            day_str = str_to_find_date[0:str_to_find_date.find(' ')]
            if not day_str.isnumeric():
                raise ValueError(f"Nieprawidłowe dane wejściowe - '{day_str}' zawarte w ciągu '{str_date}' "
                                 f"nie jest dniem miesiąca")
            day = int(day_str)

            month = Report.__get_month(str_to_find_date)
            if month is None:
                raise ValueError(f"Nieprawidłowe dane wejściowe - w ciągu '{str_date}' nie znaleziono nazwy miesiąca")

            year = datetime.today().year
            return date(year, month, day)

    @classmethod
    def __get_month(cls, date_string) -> int | None:
        """ Funkcja ustala numer miesiąca

        Funkcja poszukuje w podanym tekście nazwy miesiąca, a następnie w zależności od wyniku wyszukiwania ustala numer
        miesiąca i go zwraca. W przypadku, gdy nie uda się znaleźć nazwy miesiąca funkcja zwraca None

        :param date_string: Tekst, w którym szukana jest nazwa miesiąca
        :type date_string: str
        :return: Numer miesiąca lub None
        :rtype: int | None
        """
        if 'January' in date_string:
            return 1
        elif 'February' in date_string:
            return 2
        elif 'March' in date_string:
            return 3
        elif 'April' in date_string:
            return 4
        elif 'May' in date_string:
            return 5
        elif 'June' in date_string:
            return 6
        elif 'July' in date_string:
            return 7
        elif 'August' in date_string:
            return 8
        elif 'September' in date_string:
            return 9
        elif 'October' in date_string:
            return 10
        elif 'November' in date_string:
            return 11
        elif 'December' in date_string:
            return 12
        else:
            return None

    @classmethod
    def __get_activity_time(cls, time_string: str) -> (int, int):
        """ Funkcja ustala czas trwania aktywności.

        Funkcja w podanym tekście poszukuje godzin i minut, które składają się na czas trwania aktywności. Godziny są
        identyfikowane poprzez literę 'h', natomiast minuty poprzez literę 'm'. Funkcja zwraca ilość godzin i minut.
        Domyślnie liczba godzin oraz minut ustawiana jest na 0.

        :param time_string: Tekst, w którym poszukiwany jest czas
        :type time_string: str
        :return: Liczba godzin oraz minut
        :rtype: (int, int)
        """
        hours, minutes = 0, 0
        if 'h' in time_string:
            hours = time_string[0:time_string.find('h')]
            if 'm' in time_string:
                minutes = time_string[time_string.find('h') + 1:time_string.find('m')]
        elif 'm' in time_string:
            minutes = time_string[0:time_string.find('m')]

        return int(hours), int(minutes)
