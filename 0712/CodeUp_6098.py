b = [ list(map(int, input().split())) for i in range(10)]
done = 0

i, j = 1, 1
while i < 10:
    while j < 10:
        # 0�� ��� : �� ����
        if not b[i][j]:
            b[i][j] = 9
        # 1�� ��� : ��
        elif b[i][j] == 1:
            # ���� �Ʒ��� ���̸� �� �̻� �� �� ����
            if b[i + 1][j - 1] == 1:
                done = 1
                break
            # ���� �Ʒ��� ���� �ƴϸ� �ε����� �������ش�.
            else:
                i += 1
                j -= 2
        # 2�� ��� : ����
        else:
            b[i][j] = 9
            done = 1
            break
        j += 1

    # ���� �ݺ����� Ż���Ͽ� done �̶�� ��ŷ ������ Ȱ��ȭ�Ǹ� ���� ���´�.
    if done == 1:
        break

    i += 1

for i in range(10):
    for j in range(10):
        print(b[i][j], end=' ')
    print()