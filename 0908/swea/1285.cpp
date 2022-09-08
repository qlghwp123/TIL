// import sys

// input = sys.stdin.readline

// T = int(input())

// for tc in range(1, T + 1):
//     N = int(input())

//     l = list(map(lambda x: abs(int(x)), input().split()))
//     l.sort()

//     val = l[0]
//     cnt = l.count(l[0])

//     print(f"#{tc}", val, cnt)

#include <bits/stdc++.h>

using namespace std;

int main(void)
{
    int T, N;

    cin >> T;

    for (int i = 1; i <= T; i++)
    {
        cin >> N;

        vector<int> v;

        for (int j = 0; j < N; j++)
        {
            int temp;

            cin >> temp;

            v.push_back(temp > 0 ? temp : -temp);
        }

        sort(v.begin(), v.end());

        int val = v[0];
        int cnt = count(v.begin(), v.end(), val);

        cout << "#" << i << " " << val << " " << cnt << '\n';
    }
    return 0;
}