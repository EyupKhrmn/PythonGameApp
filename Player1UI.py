import tkinter as tk
import socket

def game(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return 'Berabere!'
    if (player1_choice == 'taş' and player2_choice == 'makas') or (player1_choice == 'kağıt' and player2_choice == 'taş') or (player1_choice == 'makas' and player2_choice == 'kağıt'):
        return 'Oyuncu 1 kazandı!'
    else:
        return 'Oyuncu 2 kazandı!'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

window = tk.Tk()
window.title("Taş Kağıt Makas Oyunu")

player_label = tk.Label(window, text="Oyuncu: Taş, Kağıt, Makas?")
player_label.pack()
player_entry = tk.Entry(window)
player_entry.pack()

def send_choice():
    player_choice = player_entry.get().lower()
    client.send(player_choice.encode())
    result = client.recv(1024).decode()
    result_label.config(text="Sonuç: " + result)

send_button = tk.Button(window, text="Gönder", command=send_choice)
send_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()