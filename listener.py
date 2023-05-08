import threading
import socket
import traceback

import logger

porta = 5555
host = ""

# Cria um objeto socket para IPv4 e TCP
listener_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Inicializa socket na porta e endereço especificados
listener_socket.bind((host, porta))

print("Ouvindo na porta {}...".format(porta))


def listen():
    try:
        while True:
                data = listener_socket.recv(2048)
                if not data:
                    break
                logger.loga_info(data.decode())
    except:
        traceback.print_exc()
        listener_socket.close()


thread = threading.Thread(target=listen)
thread.start()
