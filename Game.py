import socket
import threading

def game(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return 'Berabere!'
    if (player1_choice == 'taş' and player2_choice == 'makas') or (player1_choice == 'kağıt' and player2_choice == 'taş') or (player1_choice == 'makas' and player2_choice == 'kağıt'):
        return 'Oyuncu 1 kazandı!'
    else:
        return 'Oyuncu 2 kazandı!'

choices = {}

def player_thread(conn, player):
    while True:
        choice = conn.recv(1024).decode()
        if not choice:
            break
        choices[player] = choice
        if len(choices) == 2:
            result = game(choices['player1'], choices['player2'])
            for conn in connections:
                conn.send(result.encode())
            choices.clear()
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(2)

print('Sunucu başlatıldı ve oyuncular bekleniyor...')

connections = []

while True:
    conn, address = server.accept()
    player = 'player1' if len(connections) == 0 else 'player2'
    print(f'{address} adresinden {player} bağlandı.')
    connections.append(conn)
    threading.Thread(target=player_thread, args=(conn, player)).start()

server.close()