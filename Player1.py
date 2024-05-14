import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

while True:
    player_choice = input("Taş, kağıt, makas? ")

    client.send(player_choice.encode())

    result = client.recv(1024).decode()
    print("Sonuç: " + result)