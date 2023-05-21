import threading
import socket
import traceback
import time
import logger

# Porta
porta = 5000
host = ""

# Cria um objeto socket para IPv4 e UDP
listener_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Inicializa socket na porta e endereço especificados
listener_socket.bind(("", porta))

print("Ouvindo na porta {}...".format(porta))



def listen():
    try:
        while True:
            hora = time.time()
            data = listener_socket.recv(1024)
            if not data:
                break
            logger.loga_info(f"{data.decode()}-{(int(hora)-10800)}")
    except:
        traceback.print_exc()
        listener_socket.close()


thread = threading.Thread(target=listen)
thread.start()
