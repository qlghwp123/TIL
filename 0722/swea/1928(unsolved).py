# from base64 import b64decode

l = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")
T = int(input())

for i in range(T):
    enc = input()
    index_list = []

    # result = b64decode(enc).decode("ascii")
    # print(f"#{i + 1}", result)
    result = ""
    for j in enc:
        index_list.append(l.index(j))

    byte_list = bytearray(index_list)

    for j in range(0, len(byte_list) - 1, 4):
        # 6비트므로 2비트 공간 확보를 함.
        first = byte_list[j] << 2
        # 2비트 추출 후 합침.
        first += (48 & byte_list[j + 1]) >> 4
        # 아스키 코드 값을 문자로 변환.
        result += chr(int(first))

        second = byte_list[j + 1] << 4
        second += (60 & byte_list[j + 2]) >> 2
        result += chr(int(second))

        third = byte_list[j + 2] << 4
        third += byte_list[j + 3]
        result += chr(int(third))

    print(result)


