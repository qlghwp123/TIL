#include <iostream>

using namespace std;

int distance(int x1, int y1, int x2, int y2)
{
    return (int)((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

bool detect(int x, int y, int cx, int cy, int r)
{
    /*
    if (cx - r < x && x < cx + r)
        if (cy - r < y && y < cy + r)
            return true;
        else
            return false;
    else
        return false;
    */
    if (distance(x, y, cx, cy) < r * r)
        return true;
    else
        return false;
}

int main(void)
{
    int x1, y1, x2, y2;
    int t;
    int n;
    int cx, cy, r;
    int result;
    bool f1, f2;

    cin >> t;

    for (int i = 0; i < t; i++)
    {
        result = 0;
        cin >> x1 >> y1 >> x2 >> y2;
        cin >> n;
        for (int j = 0; j < n; j++)
        {
            cin >> cx >> cy >> r;
            f1 = detect(x1, y1, cx, cy, r);
            f2 = detect(x2, y2, cx, cy, r);

            if ((!f1 && f2) || (f1 && !f2))
                result++;
        }
        cout << result << endl;
    }

    return 0;
}