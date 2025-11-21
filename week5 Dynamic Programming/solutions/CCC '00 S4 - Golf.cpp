#include <iostream>
#include <cstring>

using namespace std;

int main() {
    int x, n;

    cin >> x >> n;

    int l[n + 1];

    for (int i = 1; i <= n; i++) {
        cin >> l[i];
    }

    int f[n + 1][x + 1];
    memset(f, 0x3f, sizeof(f));
    f[0][0] = 0;

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= x; j++) {
            f[i][j] = f[i - 1][j];
            if (j >= l[i]) f[i][j] = min(f[i][j], f[i][j - l[i]] + 1);
        }
    }

    if (f[n][x] == 0x3f3f3f3f) {
        cout << "Roberta acknowledges defeat." << endl;
    } else {
        cout << "Roberta wins in " << f[n][x]<< " strokes." << endl;
    }

    return 0;
}
