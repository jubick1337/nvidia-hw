import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 1337))
sock.listen(1)
conn, addr = sock.accept()

print("Соединение установлено:", addr)

response = b"ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\neardrum.cpu 16.3 1123864259\n\n"

while True:
    data = conn.recv(1024)
    if not data:
        break
    request = data.decode("utf-8")
    print(f"Получен запрос: {ascii(request)}")
    print(f'Отправлен ответ {ascii(response.decode("utf-8"))}')
    conn.send(response)

conn.close()
