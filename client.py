import threading
import time
import socket
import traceback

porta = 5555
host = "127.0.0.1"

# Cria um objeto socket para IPv4 e TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Conecta socket ao IP e porta especificados
client_socket.connect((host, porta))

seq = 0


def send():
    try:
        global seq
        while True:
            seq += 1
            message = "// Identificador: {} // Sequencia {}".format(threading.current_thread().ident, seq)
            client_socket.sendall(message.encode())
            print(f"Mensagem enviada: {message}")
            time.sleep(0.5)
    except:
        traceback.print_exc()
        client_socket.close()


thread = threading.Thread(target=send)
thread.start()
