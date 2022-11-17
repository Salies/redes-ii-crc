import socket


#s = socket.socket().connect(('127.0.0.1', 6661))

msg = "URRO" # mensagem a ser enviada: 4 bytes = 32 bits

# string para binário
# Fonte: https://stackoverflow.com/questions/18815820/how-to-convert-string-to-binary
msg_b = ''.join(format(ord(c), 'b').zfill(8) for c in msg)

print(msg_b)