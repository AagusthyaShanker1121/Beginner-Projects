/* Pattern formation for input = 10

**********
*********
********
*******
******
*****
****
***
**
*

*/


*/

// Program for above pattern formation

#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "enter value of n\t";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n-i; j++) {
            cout << "*";
        }
        cout << "\n";
    }
}
