#Описание проекта:
Проект api_yatube - это API социальной сети yatube.

cd api_final_yatube
Cоздать и активировать виртуальное окружение:

python3 -m venv venv
source venv/bin/activate
Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip
pip install -r requirements.txt

Выполнить миграции:

python3 manage.py migrate
Запустить проект:

python3 manage.py runserver
Примеры запросов к API:
Получить список всех постов (GET):

http://127.0.0.1:8000/api/v1/posts/
Получить определенный пост (GET):

http://127.0.0.1:8000/api/v1/posts/1/
Получить коментарии определенного поста (GET):

http://127.0.0.1:8000/api/v1/posts/1/comments/
Получить список всех групп (GET):

http://127.0.0.1:8000/api/v1/groups/
Создать новый пост (POST):

(Требуется аутентификация)

http://127.0.0.1:8000/api/v1/posts/
