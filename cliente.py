import socket
from sys import exit
from crc import crc

# Antes de tudo, interagir com o usuário
valid_inputs = ['S', 'N']
u_input = input('Forçar erro na mensagem? (S/N) ')
if u_input not in valid_inputs:
    exit("Entrada inválida.")

s = socket.socket()
s.connect(('127.0.0.1', 6661))

# mensagem a ser enviada: 3 bytes = 24 bits
# para o gerador serão usados 8 bits, totalizando 32 bits
# contudo, na realidade, serão usados apenas 30 bits (descontando 0s a esquerda)
msg = "KEK"
gen = 0b11010101 # CRC-8 (0xD5) -- fonte: https://en.wikipedia.org/wiki/Cyclic_redundancy_check

# string para binário
# Fonte: https://stackoverflow.com/questions/18815820/how-to-convert-string-to-binary
msg_b = int(''.join(format(ord(c), 'b').zfill(8) for c in msg), 2)

msg_crc = crc(msg_b, gen)[0]

# Forçando erro: flipando alguns bits
if(u_input == 'S'):
    # um número absolutamente aleatório que escolhi para "bagunçar a mensagem"
    msg_crc ^= 0x25A2A6E5

s.sendto(msg_crc.to_bytes(4, "big", signed = False), ('127.0.0.1', 6661))

s.close()