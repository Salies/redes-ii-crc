# Referência: https://en.wikipedia.org/wiki/Cyclic_redundancy_check

from math import log, ceil

# Função CRC usada para codificar e decodificar a mensagem
def crc(msg, gen):
    gensize = 8 # tamanho do gerador: no caso, aqui sempre vai ser 8
    dd = msg << (gensize - 1) # dividendo
    # bits menos signifcativos que não sofrerão com o XOR da divisão modulo-2
    lsb = ceil(log(dd + 1, 2)) - gensize
    while lsb >= 0 or dd >= gen:
        # XORs da divisão modulo-2
        # atualizando o divivendo
        re = (dd >> lsb) ^ gen # resto
        dd = (dd & ((1 << lsb) - 1)) | (re << lsb)
        lsb = ceil(log(dd + 1, 2)) - gensize
    # retorna a mensagem codiciada e o resto
    return (msg << (gensize - 1) | dd), re
