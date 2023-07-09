import struct

NORMAL = "\033[0;0m"
NOIR_GRAS = "\033[1;30m"
ROUGE_GRAS = "\033[1;31m"
BLEU_GRAS = "\033[1;34m"
VERT_GRAS = "\033[1;32m"

def bin32(num):
    return [bin(c).replace('0b', '').rjust(8, '0') for c in struct.pack('!f', num)]

def float_bin32(num):
    bits = ''.join(bin32(num))
    return VERT_GRAS + bits[0] + ROUGE_GRAS + bits[1:9] + BLEU_GRAS + bits[9:] + NORMAL

def bin64(num):
    return [bin(c).replace('0b', '').rjust(8, '0') for c in struct.pack('!d', num)]

def float_bin64(num):
    bits = ''.join(bin64(num))
    return VERT_GRAS + bits[0] + ROUGE_GRAS + bits[1:12] + BLEU_GRAS + bits[12:] + NORMAL

def _octet_vers_entier(octet):
    entier = 0
    for k in range(8):
        entier = entier + int(octet[k]) * 2**(7-k)
    return entier

def _binaire_vers_mantisse(bits):
    mantisse = 1
    for k in range(23):
         mantisse = mantisse + int(bits[k]) * 2**(-1-k)
    return mantisse

def bin32_float(bits):
    signe = int(bits[0])
    exposant = _octet_vers_entier(bits[1:9]) - 127
    mantisse = _binaire_vers_mantisse(bits[9:])
    if signe == 0:
        flottant = mantisse * 2 ** exposant
    else:
        flottant = - mantisse * 2 ** exposant
    return flottant