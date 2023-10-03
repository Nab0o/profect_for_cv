# project_for_cv
regression ui autotests on python.
This project was made for CV with example of code. This code can run only on machine with access to local testing server (ift) on specific commercial project.
all urls and names of project were removed to keep nda.

Добрый день, данный проект выложен как дополнение к резюме. В нем можно ознакомиться с некоторыми примерами кода на python.
Данный проект помогал мне проводить регрессионное тестирование части реального коммерческого проекта.
Он представляет собой небольшой регрессионный прогон, всего 32 тест-кейса.

Данный прогон возможно осуществить только если есть доступ к ift cерверу коммерческого проекта.
Ввиду того что проект коммерческий - все url, а также отсылки позволяющие точно установить название коммерческого проекта, были удалены или изменены. Все оставшиеся (надеюсь не пропустил) совпадения случайны :]

Ниже представлены результаты прохождения всего прогона, для запуска использовалась команда:
py -m pytest --alluredir=tests/allure_results -v --tb=line -m smoke
для выгрузки отчета:
allure serve C:\Users\{username}\project_cv\tests\allure_results
Результаты:
![allure report 1](https://github.com/Nab0o/profect_for_cv/blob/master/allure%20report%201.jpg "allure report 1")
![allure report 2](https://github.com/Nab0o/profect_for_cv/blob/master/allure%20report%202.jpg "allure report 2")
