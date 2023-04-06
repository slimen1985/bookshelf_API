1. Прописываем команду (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
2. Затем переходим в директорию пайчарма cd .\PycharmProjects
3. Создаем директорию mkdir bookshelf_API
4. Переходим в эту директорию cd .\bookshelf_API
5. Создаем виртуальное окружение python -m venv venv
6. Активируем эту среду venv\Scripts\activate
7. Вводим команду poetry init
8. Добавляем библиотеки poetry add fastapi[all], sqlalchemy, alembic pydantic psycopg2
9. poetry --version проверяем версию
10. Создаем нужные директории backend
11. Создаем файл .env (его добавляем в гит игнор)
12. alembic позволяет связать наше приложение с БД
13. Создаем базовый класс settings, от которого будем передавать настройки
14. В папке main.py создаем функцию start_application
15. Пропишем логгирование в config.py
16. Сердце приложения связано с БД. Прежде чем написать, нужно придумать структуру.
17. 1 таблица: Roles(id: int, role: str), 2 таблица: Users(id: int, username: str, email: str, pass:str, is_active:bool, role_id:int),
    3 таблица: Order(id: int, status: str, user_id: int, book_id:int, amount:int)
    4 таблица: Order_book(id:int, order_id:int, book_id:int)
    5 таблица: Books(id: int, title:str, descrip: str(text), amount:int, author_id:int)
4 таблица будет промежуточной, между 3 и 5 таблицей
    6 таблица: Authors(id:int, fname: str, lname: str) связана с таблицей 5
18. Создаем в папке db 2 файла и прописываем код.
установим библиотеку psycopg2 (poetry add psycopg2)
19. Исправили немного файл main для корректной работы логгирования.
Устанавливаем postgresql и в переменной среды в path добавляем путь для него
20. В директории db создаем base_class.py (базовый класс)
21. В директории models создаем файл user.py
22. В shemas создаем файл role.py и прописываем классы
23. Создаем в shemas файл user.py и также прописываем классы
24. Создаем в shemas файл order.py и также прописываем классы
25. Создаем в shemas order_book и также прописываем классы
26. Создаем в shemas book.py&author.py и также прописываем классы
27. В файле db/создаем файл base.py
28. Теперь собираем миграции: alembic init migration
29. В файле alembic.ini прописываем код.
30. Находим env.py в migration
31. затем делаем миграцию с помощью команды alembic revision --autogenerate -m "create db"
32. 
33. Затем пишем команду alembic upgrade head или номер ревизии  
34. Заходим в config.py прописываем данные
35. В бобре открываем редактор sql и пишем фикстуры
insert into "role" values(1, 'admin', '2023-03-26', '2023-03-26'), (2, 'user', '2023-03-26', '2023-03-26')
36. Создаем файл run_db, в нем пропишем скрипт для запуска
37. Создаем в db файл init_db и init_order чтобы запускать 2 скрипта
38. 