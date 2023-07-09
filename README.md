python version: 3.11

deploy locally:

1) clone repo
```commandline
git clone https://github.com/phantom-profile/activities_manage_service.git
```

2) activate venv and install requirements
```commandline
# for Windows. If "python" command not found try "py" command
установка венва:
py -m venv venv

активация венва:
Set-ExecutionPolicy RemoteSigned -Scope Process
venv\Scripts\Activate.ps1
```

```commandline
# for Unix
python -m venv .
source venv/bin/activate
python -m pip install -r requirements.txt
```

```commandline
установка зависимостей
py -m pip install -r requirements.txt
```
### Использование IPython
_Все это делается в рамках venv!!_
1) создание и настройка конфига
```commandline
ipython profile create
open ~/.ipython/profile_default/ipython_config.py
```
2) добавление авторелоуда в конфиг
```python
c.InteractiveShellApp.extensions = ['autoreload']
c.InteractiveShellApp.exec_lines = ['%autoreload 2']
```
3) запуск консоли
```commandline
python manage.py shell_plus --ipython
```

### Django
```commandline
# Запуск сервера
py manage.py runserver
```
```commandline
# Работа с моделями
Изменение модели (models.py)
Запуск команды python manage.py makemigrations для создания миграций этих изменений
Выполнение команды python manage.py migrate для применения этих изменений в базе данных
```
### Основные понятия веб разработки:

**клиент** - в общем смысле, машина, которая делает запросы

**сервер** - машина, которая на запросы отвечает

_основной протокол, по которому происходит передача данных - http(s) дальше речь будет о нем_

**тип запроса** - Инструкция для сервера, какое действие с данными клиент запрашивает. 5 основных типов запроса:
```
GET - получение данных без изменения
POST - создание новых данных
PATCH - частичное изменение существующих данных
PUT - полное изменение существующих данных
DELETE - удаление данных
```

**Эндпоинт** - URL на который отправляется запрос определенного типа. показывает серверу, какую  функцию надо задействовать для обработки.
Например `GET http://localhost/users/1` - получение данных о юзере с id = 1

**запрос (request)** - обращение к серверу по протоколу для выполнения определенной задачи. 
На каждый запрос должен быть получен ответ в определенном формате.
Например `json, html, text, csv` и тд

**ответ (response)** - набор данных, которые возвращает сервер в ответ на запрос. 
У каждого ответа всегда есть формат и статус.

**формат** - тип данных, которые представлены в ответе

**статус** - 3-значный цифровой код, говорящий о состоянии ответа
```
1xx - служебная информация, в классическом вебе встречается редко
2xx - успешный ответ, значит, что запрос выполнен без ошибок
3xx - означает, что ошибок нет, но сервер от клиента ожидает доп инструкции. классика 301 - редирект на другую страницу.
4xx - запрос не выполнен из-за ошибки клиента. то есть сервер получил неверные инструкции. 404 - не найдено, 422 - необрабатываемая сущность
5xx - запрос не выполнен из-за ошибки сервера. то есть произошел сбой в работе сервера. 
```

### Классическое клиент-серверное взаимодействие 
_(пример - получение данных о юзере с id = 1:_
1) Клиент отправляет запрос серверу на эндпоинт `GET http://best_site.com/users/1`
2) Запрос перехватывает DNS сервер, который сопоставляет имя хоста best_site.com с ip адресом твоего сервера
3) Запрос перенаправляется на эндпоинт с реальным ip `GET http://192.188.22.33/users/1`
4) Сервер принимает запрос и сопоставляет путь с функцией, которая обрабатывает этот запрос, и передает ей управление
5) Функция отрабатывает, и сервер возвращает клиенту ответ, например:
```json
{
  "status": 200, 
  "format": "json", 
  "body": {
    "id": 1, 
    "user_name": "first user"
  }
}
```
6) клиент что-то делает с этими данными, и процесс запрос-ответ сессии завершается

### Веб приложение классически имеет 3 основных слоя:
1) слой данных - хранилище данных. Представлен базой данных (sql db, mongo db, redis и тд)
2) слой бизнес логики - обработка запросов. Представлен бэкенд кодом на разных ЯП (python ruby c# и тд)
3) слой отображения - отображение данных для юзера. Представлен фронтенд кодом (javascript html css) 

Существует множество бэкенд фреймворков, но многие из них строятся на классическом паттерне MVC (model, view, controller)
1) model (модель) - слой для работы с данными. представляет из себя класс, который отражает какую-то таблицу в базе. например
```python
from django.db.models import Model

class User(Model):
    id: int
    user_name: str
```
Строка в базе 
```
id, user_name
1, "best_user"
```
будет представлена через модель:
```
User(id=1, user_name="best_user")
```
2) controller (контроллер) - слой бизнес логики бэкенда. Это как раз функции-обработчики (см предыдущий раздел п. 4). 
Эти функции перехватывают данные от клиента, взаимодействуют с моделями, и возвращают данные клиенту. Пример:
```python
def show_one_user(params: dict):
    id = params['id']
    user = User.find(id=id)
    if not user:
        return Response(status=404, body={"error": "user not found"})
    return Response(status=200, body={"id": user.id, "user_name": user.user_name})
```
3) view (вью) - слой отображения данных. Например, готовые html страницы

В Django тот же принцип, только измененный нейминг
```
модель - model
контроллер - view
вью - template
```
