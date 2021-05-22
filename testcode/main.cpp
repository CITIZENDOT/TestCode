#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n, i, m;
    long int j;
    scanf("%d", &n);
    long int temp;
    vector<long int> scores;
    for (i = 0; i < n; i++)
    {
        scanf("%ld", &temp);
        if (count(scores.begin(), scores.end(), temp) == 0)
            scores.push_back(temp);
    }
    sort(scores.begin(), scores.end());
    int k = scores.size();
    scanf("%d", &m);
    long int alice[m];
    vector<int> ranks;
    vector<long int>::iterator it;
    for (i = 0; i < m; i++)
    {
        scanf("%ld", &temp);
        if (temp < scores[0])
            ranks.push_back(k + 1);
        else if (temp > scores[k - 1])
            ranks.push_back(1);
        else
        {
            it = lower_bound(scores.begin(), scores.end(), temp);
            j = it - scores.begin();
            if (scores[j] == temp)
                ranks.push_back(k - j);
            else
                ranks.push_back(k + 1 - j);
        }
    }
    for (i = 0; i < m; i++)
        cout << ranks[i] << "\n";
}
