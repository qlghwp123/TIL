for i in range(10):
    N = int(input())
    original = input().split()

    cmd_len = int(input())
    cmd = input().split()

    result = original[:]
    for j in range(len(cmd)):
        if cmd[j] == 'I':
            idx = int(cmd[j + 1])
            code_len = int(cmd[j + 2])

            # 삼항 연산자를 사용 할 수 있지만 가독성을 위해 사용 안함.
            if idx:
                result = result[:idx] + cmd[j + 3 : j + 3 + code_len] + result[idx:]
            else:
                result = cmd[j + 3 : j + 3 + code_len] + result
            # for k in range(code_len):
            #     result.insert(idx + k, cmd[j + 3 + k])

    print(f"#{i + 1}", *result[:10])