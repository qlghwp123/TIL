#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main(void)
{
    string A, B;

    cin >> A >> B;

    string big(A.size() > B.size()? A : B);
    string small(A.size() > B.size()? B : A);

    // 두 수 길이가 다를 수 있기 때문에 
    // 작은 것을 기준으로 한다.
    int len = small.size();

    string result("");
    int carry = 0;
    for(int i = 0; i < len; i++)
    {
        char one = big[big.size() - 1 - i];
        char two = small[small.size() - 1 - i];

        // 일단 두 수의 '문자' 값이 아닌 '숫자' 값을 구한다.
        // '0' 이 48이므로 48 * 2 만큼 빼준다.
        // 이 때, 다음 수를 처리할 경우 carry 발생할 수 있으므로 초기값은 0인 
        // carry 를 더해준다.
        int temp = (int) (one + two) - 96 + carry;

        // 캐리가 발생했을 경우
        // 캐리를 1로 갱신하고 temp의 일의 자리만 남겨둔다.
        if(temp > 9)
        {
            carry = 1;
            temp %= 10;
        }
        else
            carry = 0;

        // int 값이므로 +48 을 해주어 char 로 형변환해준다.
        // string(크기, char 값) 으로 하면 string 으로 char, char[] 을 string으로
        // 초기화한다.
        result.append(string(1, (char)(temp + 48)));
    }

    // cout << "자릿수 처리 전 : " << result << " 캐리 : " << carry << endl;

    // 자릿수가 다를 때 처리를 해야함. 
    if(big.size() != small.size())
    {
        // 자릿수가 다르고 캐리가 존재할 경우
        if(carry)
        {
            // 남은 자릿수만큼 반복
            for(int i = 0; i < big.size() - small.size(); i++)
            {
                // 두 수의 자릿수 차 - 1 부터 시작 해야한다.
                char one = big[big.size() - small.size() - 1 - i];

                // 아래의 코드는 자릿수가 같은 부분과 동일하다.
                int temp = (one - 48) + carry;

                if(temp > 9)
                {
                    carry = 1;
                    temp %= 10;
                }
                else
                    carry = 0;

                result.append(string(1, (char)(temp + 48)));
            }

            // 자릿수가 다른 부분을 다 처리했는데 마지막 부분에서
            // 캐리가 발생할 경우 1을 추가해준다.
            // ex) 999(공통부분) 라서 공통 부분에 carry 가 발생하여
            //     마지막에 1을 추가 해야하는경우
            if(carry)
                result.append(string(1, '1'));

        }
        // 자릿수가 다르고 캐리가 없는 경우
        else
        {
            // 캐리가 없으면 남은 값을 그냥 append 해준다.
            for(int i = 0; i < big.size() - small.size(); i++)
            {    
                char temp = big[big.size() - small.size() - 1 - i];
                result.append(string(1, temp));
            }

            // cout << "자릿수 처리 후 : " << result << endl;
        }
    }
    else
        if(carry)
            result.append(to_string(carry));

    reverse(result.begin(), result.end());

    cout << result << endl;

    return 0;
}