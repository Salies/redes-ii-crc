import socket
from crc import crc

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

#s.sendto(crc(msg_b, gen)[0].to_bytes(4, "big", signed = False), ('127.0.0.1', 6661))

# Forçando erro: flipando alguns bits
msg_crc ^= 0x25A2A6E5

s.sendto(msg_crc.to_bytes(4, "big", signed = False), ('127.0.0.1', 6661))

s.close()