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
        first = (byte_list[j] << 2) & (127 - 3)
        # 110000 마스킹을 통해서 상위 2비트 추출 후 합침.
        first += (48 & byte_list[j + 1]) >> 4
        # 아스키 코드 값을 문자로 변환.
        result += chr(first)

        # 6비트므로 4비트 공간 확보를 함. 
        # 이 때, 1바이트 위로 올라갈 수 있어서 마스킹이 반드시 필요하다.
        second = (byte_list[j + 1] << 4) & (127 - 15)
        # 111100 마스킹을 통해서 상위 4개 비트를 추출 후 합침.
        second += ((63 - 3) & byte_list[j + 2]) >> 2
        # 아스키 코드 값을 문자로 변환.
        result += chr(second)

        # 2비트 추출을 위해 000011 마스킹 후 상위 2비트로 올림.
        third = (byte_list[j + 2] & 3) << 6
        # 네 번째 값을 더함.
        third += byte_list[j + 3]
        result += chr(third)

    print(f"#{i + 1}", result)

