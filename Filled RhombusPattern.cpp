// Filled Rhombus pattern
/* Pattern formation for input 10 

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
   int n;
   cout<< "Enter the length of the Rhombus :\t"
    cin >> n;
    for (int i = 1; i <= n; i++) {
        for (int j = n; j >=i ; j-- ){
            cout<<" ";
        }
        for (int k = 1; k <= n; k++) {
            cout << "*";
        }
        cout << endl;
    }

    
}
