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

# https://swbeginner.tistory.com/entry/SWEA-%EC%BD%94%EB%94%A9-Base64-Decoder-PYTHON-1928
# 몰랐는데 이진수로 표현된 문자열을 내장함수 int() 의 첫 번째 인자로 주고, 두 번째 인자로 진수를 뜻하는 2를 넣으면 잘 작동한다.
# 알았으면 비트 연산자로 푸는 방법은 쓰지 않았을 것...
# T = int(input())
 
# # 표 1
# decode = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
#           'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
#           '0','1','2','3','4','5','6','7','8','9','+','/'
#           ]
 
# for tc in range(1,1+T):
 
#     # 입력받는 글자(인코딩 된 상태)
#     word = list(input())
 
#     # 글자의 길이
#     length = len(word)
 
#     # word의 글자 -> 표1에 따라 숫자로 변환 -> 이진수로 변환 -> 하나의 res로 만들기
#     res = ''
 
#     for q in range(length):
 
#         # word -> 표1에 따라 숫자로 변환
#         num = decode.index(word[q])
 
#         # num -> 이진수로 변환
#         # int형태로 더하면 단순 숫자의 합이 나오므로 str로 변환하고 앞의 0b 제거
#         bin_num = str(bin(num)[2:])
 
#         # bin_num의 길이가 6보다 작으면 앞에 0 붙여주기
#         # 1을 이진수로 바꾸면 1로 나옴(필요한 값은 000001임)
#         while len(bin_num) < 6:
#             bin_num = '0' + bin_num
 
#         res += bin_num
    
#     # 문제에서 구하고자 하는 원래 문장
#     r = ''
 
#     # 글자의 길이 * 6에서 8비트씩 자름
#     for w in range(length*6//8):
 
#         # 8비트씩 자르기
#         # 자른 값을 10진수로 변환
#         e = int(res[w*8:w*8+8],2)
 
#         # 아스키코드의 값을 r에 추가
#         r += chr(e)
 
#     print('#{} {}'.format(tc,r))