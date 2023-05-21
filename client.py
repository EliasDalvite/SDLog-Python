import threading
import time
import socket
import traceback

# Porta e IP do listener q vou mandar
porta = 5000
host = "localhost"

# Cria um objeto socket para IPv4 e UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Conecta socket ao IP e porta especificados
client_socket.connect((host, porta))


def send():
    try:
        seq = 0
        while True:
            seq += 1
            message = f"{threading.current_thread().ident}-{seq}"
            client_socket.sendall(message.encode())
            print(f"Mensagem enviada: {message}")
            time.sleep(0.5)
    except:
        traceback.print_exc()
        client_socket.close()


thread1 = threading.Thread(target=send)
thread1.start()
time.sleep(5)
thread2 = threading.Thread(target=send)
thread2.start()
time.sleep(5)
thread3 = threading.Thread(target=send)
thread3.start()

