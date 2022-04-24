def hexadd(hexa, hexb):
    return hex(int(hexa, 16) + int(hexb, 16))


def hexsub(hexa, hexb):
    return hex(int(hexa, 16) - int(hexb, 16))


def fillnull(hexvalue):

    if len(hexvalue) == 3 and int(hexvalue, 16) > 0:
        hexvalue = hexvalue[:2] + "000" + hexvalue[2:]
    elif len(hexvalue) == 4 and int(hexvalue, 16) > 0:
        hexvalue = hexvalue[:2] + "00" + hexvalue[2:]
    elif len(hexvalue) == 5 and int(hexvalue, 16) > 0:
        hexvalue = hexvalue[:2] + "0" + hexvalue[2:]
    elif len(hexvalue) == 4 and int(hexvalue, 16) < 0:
        hexvalue = hexvalue[:3] + "000" + hexvalue[3:]
    elif len(hexvalue) == 5 and int(hexvalue, 16) < 0:
        hexvalue = hexvalue[:3] + "00" + hexvalue[3:]
    elif len(hexvalue) == 6 and int(hexvalue, 16) < 0:
        hexvalue = hexvalue[:3] + "0" + hexvalue[3:]
    elif int(hexvalue, 16) == 0:
        hexvalue = "0x0000"

    return hexvalue