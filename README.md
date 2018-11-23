# Cars_classifier
Классификация российских спецавтомобилей по классам "Скорая помощь", машины МЧС, пожарные, полицейские и мусоровозы. Также присутствует класс "прочие"

# Requirements
```
Docker version 18.09.0`
```

# Run server locally
Чтобы запустить сервер на Flask локально, нужно прописать в консоли следующую команду:
```
 export FLASK_APP=routes.py
```
Затем для запуска такого сервера используется команда
```
 flask run
```
ВАЖНО: для того, чтобы подтянуть все зависимости в проекте лежит файл requirements.txt. Чтобы не было конфликтов версий библиотек, необходимо создать виртуальное окружение. В python для этого можно использовать venv в python или virtualenvwrapper. https://python-scripts.com/virtualenv Затем, чтобы установить необходимые зависимости нужно выполнить следующую команду в созданном виртуальном окружении
```
pip install -r requirements.txt
```
# Run server with Docker
Для того, чтобы запустить сервис с помощью Docker нужно сначала собрать Docker image:
```
cd car-classifier
docker build -t car-classifier:latest .
```
Затем чтобы запустить образ, нужно применить следующую команду:
```
docker run --name car-classifier -d -p 80:5000 --rm car-classifier
```
После запуска сервис будет доступен по адресу 0.0.0.0:80

# Usage
https://carsclassifierapi01.docs.apiary.io
