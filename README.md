# aaa_hw2
Есть csv-файл с отчётом о сотрудниках компании. В нём следующие данные:

ФИО полностью

Департамент

Команда внутри департамента

Занимаемая должность

Квартальная оценка – результат ревью

Текущая зарплата


Пример записи в отчёте:

Кузьмина Любовь Феликсовна

Разработка

Внутренний портал

Backend-инженер

4.5

89000

При старте программы выводится меню, которое состоит из 3-х пунктов:

Вывести в понятном виде иерархию команд, т.е. департамент и все команды, которые входят в него

Вывести сводный отчёт по департаментам: название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату

Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. При этом необязательно вызывать сначала команду из п.2

Пользователь выбирает пункт меню, вводя соответствующее число.

Условия:

Используем только встроенные модули (без pandas и т.д.)

Весь скрипт разбит на функции

Каждая функция содержит докстринги

Бонус: все параметры аннотированы типами
