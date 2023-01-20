# flask-server
Суть работы состоит в том, чтобы обеспечить управление некоторым устройством по сети (например, через Интернет) с помощью современного стека технологий
и средств проектирования и разработки ПО.

Задание: обеспечить поддержку REST API сетевым сервисом, разработанным в
рамках [работы №1](https://github.com/Oddi17/socket-server) , с помощью flask или FastAPI.
В дополнение ко всем требованиям, изложенным в задании к  работе №1, сервис должен поддерживать управление «устройством» с помощью REST API (кроме
уведомлений). Проверка работы API должна быть возможна с помощью любого клиентского приложения, поддерживающего передачу HTTP-запросов (например, curl).

# Запуск

-Check for the existence of the cond.txt in your directory.This file should be named cond.txt and contain the parameters of your device

-Set the address and port in command line when running the scripts server.py and client.py when you starting (first address then port, for example - 0.0.0.0 7082) or just default values will be used - "0.0.0.0":12345

-Start file server.py #python3 server.py or ./server.py

-After you can use the command to work with server and device-file 
by using curl: (curl -i "0.0.0.0":12345/show) to show parameters in device-file and (curl -i "0.0.0.0":12345/set -d+"name of parameters"="value" 

-(name must be only: Angle_back, Angle_ankle, Angle_hip and value must be int in within the limits (Angle_back:0 to 50; Angle_hip:-15 to 15; Angle_ankle: 0 to 30)
