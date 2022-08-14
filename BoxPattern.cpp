/* Pattern formation for input = 10

**********
**********
**********
**********
**********
**********
**********
**********
**********
**********

*/




// Program for above pattern formation

#include <iostream>
using namespace std;

int main() {
   int m, n;
   cout << "Enter the Rows and Columns for the star pattern.\t" ;
    cin >> m >> n;
    for (int i = 1; i <= m; ++i) {
        for (int j = 1; j <= n; j++) {
            cout << "*"<<" ";
        }
        cout << " "<<endl;
    }
    return 0 ;
}
