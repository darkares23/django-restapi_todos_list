# Django Todo REST API

Aplication to view, edit, create adn delete todos for user previuosly registered in the admin.

### Prerequisites 📋

Must have django installed

Must have rest_framework installed


### Instalation 🔧

```
pip install -r requeriments.txt
```
## Starting 🚀



LOGIN URL
```
http://127.0.0.1:8000/login
```
super user: juan
passw : elena1234

user: testsimple
pass: elena1234

FRONTEND URL TODOLIST MANIPULATION
# After logged only for already created users
```
http://127.0.0.1:8000/
```

ADMIN URL
```
http://127.0.0.1:8000/admin/api/todo/
```

ENDPOINTS
```
http://127.0.0.1:8000/api/v1/todo_list
```
```
http://127.0.0.1:8000/api/v1/todo_create/
```
```
http://127.0.0.1:8000/api/v1/todo_update/<pk:id>
```
```
http://127.0.0.1:8000/api/v1/delete/<pk:id>
```
```
http://127.0.0.1:8000/api/v1/todo_list/
```
```
http://127.0.0.1:8000/api/v1/search/?search=<str>
```
```
http://127.0.0.1:8000/api/v1/search/?search=<str:str>
```
```
http://127.0.0.1:8000/api/v1/todo_list/?page=<int:int>'
```

## testing ⚙️

```
python3 manage.py test
```

## Author ✒️

* **Juan Sebastián Ocampo** -(https://github.com/darkares23)
