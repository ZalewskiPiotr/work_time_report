# Standard library import
from datetime import date

# Third party imports

# Local imports
import report_position


class ReportDay:
    """ Klasa reprezentuje jeden dzień w raporcie.

    Klasa zawiera informacje o czynnościach i czasie ich trwania. Jeżeli w ciągu dnia czynność się powtarzała, to jest
    ona łączona w jedną pozycję w raporcie, a czas jest sumarycznym czasem wszystkich czynności w danym dniu o tej samej
    nazwie.
    Klasa zawiera także informację o całkowitym czasie pracy w ciągu dnia.

    Atrybuty
    ---------
    day : date
        data w formacie isoformat: 'YYYY-MM-DD'
    hours_sum : int
        suma liczby godzin z danego dnia
    minutes_sum : int
        suma liczby minut z danego dnia
    position_list : list[]
        lista czynności z danego dnia. Jest to lista obiektów klasy ReportPosition

    Metody
    -------
    add_position(position: report_position.ReportPosition)
        Dodaje kolejną pozycję danych wejściowych z danego dnia
    __join_position(self, position_from_list: report_position.ReportPosition,
                        new_position: report_position.ReportPosition):
        Złączenie dwóch pozycji o takiej samej nazwie
    """

    def __init__(self, day: date):
        """
        :param day: data dla której zebrane są dane o czynnościach
        :type day: datetime
        """
        self._day = day
        self._hours_sum = 0
        self._minutes_sum = 0
        self._position_list: list[report_position.ReportPosition] = []

    @property
    def day(self) -> str:
        """
        :return: Data dla której zebrane są dane. Zwracana data ma format 'YYYY-MM-DD'
        :rtype: str
        """
        return self._day.isoformat()

    @property
    def position_list(self) -> list[report_position.ReportPosition]:
        """
        :return: Lista wszystkich czynności z danego dnia. Na liście znajdują się obiekty typu ReportPosition
        :rtype: list
        """
        return self._position_list

    @property
    def hours_sum(self) -> int:
        """
        :return: Sumaryczna liczba godzin z danego dnia
        :rtype: int
        """
        return self._hours_sum

    @property
    def minutes_sum(self) -> int:
        """
        :return: Sumaryczna liczba minut z danego dnia
        :rtype: int
        """
        return self._minutes_sum

    def add_position(self, position: report_position.ReportPosition):
        """ Dodanie kolejnej czynności w danym dniu.

        Metoda przy dodaniu pozycji do listy sprawdza ilość minut. Jeżeli suma minut jest większa niż 59 to zwiększana
        jest sumaryczna liczba godzin i odpowiednio zmniejszana liczba minut

        :param position: Pozycja z czynnością z danego dnia
        :type position: ReportPosition
        :return: None
        :rtype: ---
        """

        is_new_position = True
        # Jeżeli pozycja już istnieje na liście to łączymy ją z nową
        for position_from_list in self._position_list:
            if position_from_list.activity == position.activity:
                self.__join_position(position_from_list, position)
                is_new_position = False
                break

        # Jeżeli jest to nowa pozycja to ją dodajemy do listy i sumujemy czasy
        if is_new_position:
            self._position_list.append(position)
            self._hours_sum += position.hours
            self._minutes_sum += position.minutes
            if self._minutes_sum > 59:
                self._hours_sum += 1
                self._minutes_sum = self._minutes_sum - 60

    def __join_position(self, position_from_list: report_position.ReportPosition,
                        new_position: report_position.ReportPosition):
        """ Złączenie dwóch pozycji o takiej samej nazwie

        Funkcja łączy ze sobą dwie pozycje o takiej samem nazwie czynności. Dodawane są do siebie czasu obu pozycji

        :param position_from_list: Pozycja, która już istnieje na liście
        :type position_from_list: ReportPosition
        :param new_position: Nowa pozycja, która ma być dodana do isniejącej
        :type new_position: ReportPosition
        :return: None
        :rtype: ---
        """

        # Złączenie pozycji
        position_from_list.hours += new_position.hours
        position_from_list.minutes += new_position.minutes
        if position_from_list.minutes > 59:
            position_from_list.hours += 1
            position_from_list.minutes -= 60

        # Sumowanie czasów wszystkich pozycji
        self._hours_sum += new_position.hours
        self._minutes_sum += new_position.minutes
        if self._minutes_sum > 59:
            self._hours_sum += 1
            self._minutes_sum = self._minutes_sum - 60
