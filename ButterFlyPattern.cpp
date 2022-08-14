

/*  Final Pattern , Height = 7

*    *
**  **
******
******
**  **
*    *

*/ 

#include <iostream>
using namespace std ;
int main() {
    // Write C++ code here
   int n;
   cout << "Enter height of the butterfly :\t"
    cin >> n;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        for (int j = 1; j <= 2*(n-i); j++) {
            cout << " ";
        }
        for (int k = 1; k <= i; k++) {
            cout << "*";
        }
        cout << endl;
    }
    for (int i = n; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        for (int j = 1; j <= 2 * (n - i); j++) {
            cout << " ";
        }
        for (int k = 1; k <= i; k++) {
            cout << "*";
        }
        cout << endl;
    }

    return 0;
}
