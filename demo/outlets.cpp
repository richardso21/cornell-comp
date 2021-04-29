#include <iostream>
using namespace std;

int main(void)
{
    int N;
    cin >> N;
    int c = 0;
    int e = 0;
    int a;
    for (int i = 0; i < N; i++)
    {
        cin >> a;
        if (a == 0)
            e++;
        c += a;
    }
    cout << c - (N - e - 1) << '\n';
}