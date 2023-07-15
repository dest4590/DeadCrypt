from threading import Thread
from client import makeauth
import base64, os
import logging

nologger = False

if not nologger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

replacer = {
    '0': 'D3AD',
    '1': 'C0RE'
}

reversed_replacer = {
    'D3AD': '0',
    'C0RE': '1' 
}

force_disable_server = True # true for disable server verification (simple secure of server emulation)

if not force_disable_server:
    if not makeauth():
        print('S3RV3R D1SABL3D.')
        quit()

class Encrypt:
    def __init__(self, text: str = 'print("Hello, World!")') -> None:
        self.text = text
    
    def encrypt(self):
        logger.info('Encrypting text...')
        return base64.a85encode(base64.b64encode(''.join(format(ord(char), '08b') for char in self.text).replace('0', replacer['0']).replace('1', replacer['1']).encode()))
    
    def makebinary(self, name: str):
        logger.info('Making binary...')
        if not os.path.isdir('binares'):
            os.mkdir('binares')
            
        with open('binares/' + name + '.bin', 'wb') as binary:
            logger.info('Writing binary')
            binary.write(self.encrypt())

class Decrypt:
    def __init__(self, text: str) -> None:
        self.text = text

    def decrypt(self):        
        logger.info('Decrypting text...')
        
        binary_string = base64.b64decode(base64.a85decode(self.text)).decode().replace('C0RE', reversed_replacer['C0RE']).replace('D3AD', reversed_replacer['D3AD'])
        text = ''

        for i in range(0, len(binary_string), 8):
            binary_char = binary_string[i:i+8]
            decimal_char = int(binary_char, 2)
            text += chr(decimal_char)
        return text
    
class Binary:
    def __init__(self, path: str):
        self.path = path

    def launch(self):
        logger.info('\nLaunching binary: ' + self.path)
        exec(Decrypt(open(self.path, 'r').read()).decrypt())

    def launchThread(self):
        logger.info('\nLaunching binary as thread: ' + self.path)
        Thread(target=self.launch).start()