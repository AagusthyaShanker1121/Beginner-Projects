// Zig-Zag pattern
/* Pattern formation for input 60 

  *   *   *   *   *   *   *   *   *   *   *   *   *   *   * 
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*   *   *   *   *   *   *   *   *   *   *   *   *   *   *   


*/




// Program for above pattern formation

#include <iostream>
using namespace std;

int main() {
   int n;
   cout << "Enter the length of zig zag pattern :\t" ;
    cin >> n;
    for (int i = 1; i <= 3; i++)
    {
        for (int j = 1; j <= n; j++) {
            if ((i + j) % 4 == 0 || (i == 2 && j % 4 == 0)) {
                cout << "*";
            }
            else {
                cout << " ";
            }
        }
        cout << endl;
   }

    
}
