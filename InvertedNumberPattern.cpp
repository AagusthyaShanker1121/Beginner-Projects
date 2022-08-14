

/* Pattern Formation 
12345678910
123456789
12345678
1234567
123456
12345
1234
123
12
1
*/

/* Program for above such pattern*/ 

#include <iostream>
using namespace std ;
int main() {
    int n;
    cout << "Enter the any nuumber :\t" ;
    cin >> n;
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= n + 1 - i; j++) {
            cout << j;
        }
        cout << endl;
    }

}
