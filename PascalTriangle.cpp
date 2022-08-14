/* Pattern formation for input = 6

1
1 1 
1 2 1 
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1
*/

// Program for above pattern formation

#include <iostream>
using namespace std;
int fact(int num) {
    int fact_1 = 1;
    for (int i = 1; i <= num; i++) {
        fact_1 *= i;
    }
    int fact_2 = (num == 0) ? 1 : fact_1;
    return fact_2;
}
int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            cout << fact(i) / (fact(j) * fact(i - j)) << " ";
        }
        cout << endl;
    }
    return 0;
    
}
