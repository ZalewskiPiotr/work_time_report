Format źródła danych
====================
Dane wejściowe znajdują się w pliku tekstowym w formacie:

Today7h 33m
Realizacja zadań z poczty i Teams
Stopwatch
1h	08:13 - 09:13
Weryfikacja czasu pracy W1, W7
Stopwatch
1h 43m	09:13 - 10:57
Weryfikacja nowych zadań w Jirze: W1, W3, W7
Stopwatch
4m	10:57 - 11:02
Weryfikacja nowych zadań w Jirze: W1, W3, W7
Stopwatch
2m	11:03 - 11:05
Zadania organizacyjne - spotkania, rozmowy, planowanie zadań
Stopwatch
7m	11:05 - 11:13
Rozwój Wydziału Wytwarzania - rada starszych
Stopwatch
4h 35m	11:13 - 15:48
Yesterday6h 21m
Realizacja zadań z poczty i Teams
Stopwatch
40m	09:30 - 10:11
Rozwój Wydziału Wytwarzania - rada starszych
Stopwatch
1h 44m	10:11 - 11:56
Zadania organizacyjne - spotkania, rozmowy, planowanie zadań
Stopwatch
50m	11:56 - 12:46
Realizacja zadań z poczty i Teams
Stopwatch
3h 5m	12:46 - 15:52
Friday, 26 November5h 48m
Analiza pracy w nowej jirze z serwisem - mail od Doroty
Stopwatch
48m	08:03 - 08:52
Zlecenie przygotować dla Rafała
Stopwatch
10m	08:59 - 09:09
Weryfikacja czasu pracy W1, W3, W4, W7
Stopwatch
40m	09:10 - 09:50
Rozwój Wydziału Wytwarzania - rada starszych
Stopwatch
6m	09:50 - 09:57
Rozwój Wydziału Wytwarzania - rada starszych
Stopwatch
3h 20m	09:58 - 13:18
MAil od Gawła ze zgłoszeniami
Stopwatch
9m	13:38 - 13:48
Zrobić RETRO z protokołami
Stopwatch
32m	14:43 - 15:15

Klasy w programie
=================
class report
    Klasa zawiera informacje o całym raporcie

class reportDay
    Klasa zawiera informacje o jednym dniu w raporcie: data, lista pozycji z danego dnia (aktywności o tych samych
    nazwach są złączone w jedną pozycję), suma godzin, suma minut

class reportPosition
    Klasa zawiera informacje o jednej czynności w raporcie

Przepływ programu
=================
- odczyt danych z pliku wejściowego do pamięci - dokładne odwzorowanie danych z pliku wejściowego
- przejście po danych wejściowych w pamięci i przygotowanie danych raportu. Dane do raportu przechowywane w pomięci
- utworzenie raportu poprzez zapis do pliku txt danych z pamięci