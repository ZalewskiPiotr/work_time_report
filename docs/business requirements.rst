Wymagania biznesowe
--------------------
- odczyt informacji o czasie pracy ze źródła danych
- przygotowanie raportu z czasem pracy
    - każdy dzień jest podliczony osobno w raporcie
    - jeżeli w ciągu jednego dnia było kilka takich samych pozycji to zostaną one zsumowane i złączone w jedną pozycję
    - suma wszystkich pozycji za jeden dzień w raporcie musi wynosić 8h. Jeżeli jest inna to należy ją dostosować do 8h według poniższego algorytmu:
        - jeżeli jest mniej niż 8h to dodajemy czas do pozycji, w której jest najmniej czasu
        - jeżeli jest więcej niż 8h to odejmujemy czas z pozycji, w której jest najwięcej czasu
- zapis raportu do pliku tekstowego.
Format raportu:
    data w formacie DD-MM-YYYY - np. 23-11-2021
    nazwa wykonywanej czynności; czas w formacie xh xm - np. Wprowadzanie danych do bazy; 2h 34m