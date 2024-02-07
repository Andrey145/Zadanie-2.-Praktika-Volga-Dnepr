def convert(number):
    if number[0:2] == "0o":
        number = int(number[2:], base=8)
    elif number[0:2] == "0x":
        number = int(number[2:], base=16)
    else:
        number = int(number, base=2)
    return number

def extract_by_mask(data, mask):
    data = str(bin(convert(data)))[2:]
    mask = str(bin(convert(mask)))[2:]

    while len(data) > len(mask):
        data = data[1:]
    while len(mask) > len(data):
        mask = mask[1:]

    for i in range(0, len(data)):
        if mask[i] == "0":
            data = data[:i] + "-" + data[i + 1:]

    for j in range(len(data)-1, -1, -1):
        try:
            while data[j] == "-":
                data = data[:j] + data[j + 1:]
        except:
            pass

    if data == "":
        return 0
    else:
        return bin(convert(data))

if __name__ == '__main__':
    data = input("data = ")
    mask = input("mask = ")
    result = extract_by_mask(data, mask)
    print(result)