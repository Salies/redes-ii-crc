import socket
from crc import crc

gen = 0b11010101
s = socket.socket()
s.bind(('', 6661))
s.listen(1)

while True:
    conn, addr = s.accept()
    msg = conn.recv(4)
    msg = int.from_bytes(msg, "big") # voltando pra inteiro
    re = crc(msg, gen)[1] # resto
    # Resto é 0 -> não há erro -> pode decodificar (tratar a mensagem)
    if(re == 0):
        # Retira os len(gen) - 1 bits menos significativos do número
        # no caso, coloco 7.
        # Depois disso, converto para uma string de binários.
        # msg_t = mensagem tratada
        msg_t = '{0:b}'.format((msg >> 7) & (0x7FFFFF)).zfill(24)
        # Agora, quebro a mensagem para pegar os três caracteres diferentes
        # Depois, converto o binário dos caracteres para char, junto-os de volta, e exibo
        # mensagem.
        # msg_s = msg split
        msg_s = ''.join([chr(int(msg_t[i:i+8], 2)) for i in range(0, len(msg_t), 8)])
        print('Mensagem recebida com sucesso:', msg_s)
    else:
        print("Falha no recebimento da mensagem. Resto: ", str(re) + ".")
    # mata o servidor quando receber a mensagem
    if(msg):
        conn.close()
        break