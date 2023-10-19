import csv


def command1(reader: csv.DictReader) -> None:
    """
    Принимает объект типа csv.DictReader, печатает иерархию команд,
    т.е. департамент и все команды, которые входят в него
    """
    deps = {}  # type: dict[str, set]
    for row in reader:
        if row['Департамент'] in deps:
            if row['Отдел'] not in deps[row['Департамент']]:
                deps[row['Департамент']].add(row['Отдел'])
        else:
            deps[row['Департамент']] = set()
            deps[row['Департамент']].add(row['Отдел'])
    for dep in deps:
        print(dep, ':\t', deps[dep])
    return


def summary(reader: csv.DictReader) -> dict[str, dict]:
    """
    Принимает объект типа csv.DictReader,
    возвращает словарь словарей вида
    {'Название_департамента': {'Численность': число,
                                'мин': число,
                                'макс': число,
                                'сумма зп': число
                                }, ...}
    """
    deps_prop = {}  # type: dict[str, dict]
    for row in reader:
        if row['Департамент'] not in deps_prop:
            deps_prop[row['Департамент']] = {}
            deps_prop[row['Департамент']]['Численность'] = 1
            deps_prop[row['Департамент']]['мин'] = int(row['Оклад'])
            deps_prop[row['Департамент']]['макс'] = int(row['Оклад'])
            deps_prop[row['Департамент']]['сумма зп'] = int(row['Оклад'])
        else:
            deps_prop[row['Департамент']]['Численность'] += 1
            if int(row['Оклад']) < deps_prop[row['Департамент']]['мин']:
                deps_prop[row['Департамент']]['мин'] = int(row['Оклад'])
            if int(row['Оклад']) > deps_prop[row['Департамент']]['макс']:
                deps_prop[row['Департамент']]['макс'] = int(row['Оклад'])
            deps_prop[row['Департамент']]['сумма зп'] += int(row['Оклад'])
    return deps_prop


def command2(deps_prop: dict) -> None:
    """
    Принимает словарь,
    печатает сводный отчёт по департаментам:
    название, численность, "вилка" зарплат в виде мин – макс, средняя зарплата
    """
    for dep_name in deps_prop:
        this_avg = round(float(deps_prop[dep_name]['сумма зп'])
                         / deps_prop[dep_name]['Численность'], 2)
        print(f"Название: {dep_name},\
        Численность: {deps_prop[dep_name]['Численность']},\
        Вилка зарплат: \
        {deps_prop[dep_name]['мин']} - {deps_prop[dep_name]['макс']},\
        Средняя зарплата:{this_avg}")
    return


def command3(deps_prop: dict) -> None:
    """
    Принимает словарь,
    записывает в csv-файл сводный отчёт по департаментам:
    название, численность, "вилка" зарплат в виде мин – макс, средняя зарплата
    """
    with open('summary.csv', 'w', newline='') as csvfile:
        flds = ['Название', 'Численность', 'Вилка зарплат', 'Средняя зарплата']
        writer = csv.DictWriter(csvfile, fieldnames=flds)
        writer.writeheader()
        for dep_name in deps_prop:
            writer.writerow({'Название': dep_name,
                             'Численность': deps_prop[dep_name]['Численность'],
                             'Вилка зарплат': f"{deps_prop[dep_name]['мин']}\
                             -{deps_prop[dep_name]['макс']}",
                             'Средняя зарплата':
                             round(float(deps_prop[dep_name]['сумма зп'])
                                   / deps_prop[dep_name]['Численность'], 2)})
    return


if __name__ == '__main__':
    print('Меню:')
    print('1. Вывести иерархию команд')
    print('2. Вывести сводный отчет по департаментам')
    print('3. Сохранить сводный отчет в csv-файл')
    choice = input('Выберите пункт меню: ')
    with open('Corp_Summary.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        if choice == '1':
            command1(reader)
        elif choice == '2':
            command2(summary(reader))
        elif choice == '3':
            command3(summary(reader))
        else:
            print('Некорректный ввод')
