def hexadd(hexa, hexb):
    return hex(int(hexa, 16) + int(hexb, 16))


def hexsub(hexa, hexb):
    return hex(int(hexa, 16) - int(hexb, 16))


def fillnull(hexvalue, length=4):
    
    if int(hexvalue, 16) >= 0:
        while len(hexvalue) < length + 2:
            hexvalue = hexvalue[:2] + "0" + hexvalue[2:]
    else:
        while len(hexvalue) < length + 3:
            hexvalue = hexvalue[:3] + "0" + hexvalue[3:]

    return hexvalue
