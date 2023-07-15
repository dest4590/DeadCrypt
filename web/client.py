import socket
import base64
import random

class requests:
    def get(url: str):
        return "You've Been Trolled"

token = 'https://bit.ly/43pswio'

requests.get(token)

HOST = 'IP_TO_SERVER'
PORT = 4444

decode = lambda text: base64.b85decode(base64.b85decode(base64.b64decode(text)))

def auth(message: str):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        client_socket.send(message.encode())
        return decode(client_socket.recv(1024).decode())

def makeauth():
    random_dots = random.randint(30, 50)
    try: 
        if auth(str(random_dots) + ':D3ADCR7PT' + ':'*random_dots + '@' + base64.b64encode(b'D3AD:C0RE:BEEN:HERE').decode()).decode() == 'D3A'.replace('X', 'GHKS') + ''.join('DCR'.split('GBB')) + '7PT_TRUE':
            return True
    except:
        return False