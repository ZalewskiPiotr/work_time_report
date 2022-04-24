# Standard library import
# Third party imports
# Local imports


class ReportPosition:
    """
    Klasa reprezentuje jedną pozycję raportu

    Atrybuty:
    ---------
    - activity : str
        Nazwa czynności
    hours : int
        Liczba godzin przez jakie dana czynność była wykonywana
    minutes : int
        Liczba minut przez jakie dana czynność była wykonywana
    """

    def __init__(self, activity: str, hours: int, minutes: int):
        """
        :param activity: Nazwa czynności
        :type activity: str
        :param hours: Liczba godzin przez jakie dana czynność była wykonywana
        :type hours: int
        :param minutes: Liczba minut przez jakie dana czynność była wykonywana
        :type minutes: int
        :raise ValueError 'Activity name is empty': Nie podano nazwy czynności
        :raise ValueError 'Invalid hours': Podane godziny nie są liczbą
        :raise ValueError 'Invalid minutes': Podane minuty nie są liczbą
        """
        if len(activity.strip()) == 0:
            raise ValueError(f"Activity name is empty")

        if not str(hours).isdigit():
            raise ValueError(f"Invalid hours {hours}")

        if not str(minutes).isdigit():
            raise ValueError(f"Invalid minutes {minutes}")

        if minutes < 0 or minutes > 59:
            raise ValueError(f"Minutes must be between 0-59")

        self._activity = activity
        self._hours = hours
        self._minutes = minutes

    @property
    def activity(self) -> str:
        """
        :return: Nazwa czynności
        :rtype: int
        """
        return self._activity

    @property
    def hours(self) -> int:
        """
        :return: Liczba godzin dla danej czynności
        :rtype: int
        """
        return self._hours

    @hours.setter
    def hours(self, value):
        """ Ustawia liczbę godzin dla danej czynności """
        self._hours = value

    @property
    def minutes(self) -> int:
        """
        :return: Liczba minut dla danej czynności
        :rtype: int
        """
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        """ Ustawia liczbę minut dla danej czynności """
        self._minutes = value
