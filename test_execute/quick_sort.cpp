#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    vector<int> a;
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        int tmp;
        cin >> tmp;
        a.push_back(tmp);
    }
    sort(a.begin(), a.end());
    for (auto i:a) {
        cout << i << " ";
    }
    return 0;
}