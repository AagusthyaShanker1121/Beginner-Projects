/* Pattern formation for input = 20

         1011
        9101112
       8910111213
      7891011121314
     6789101112131415
    5678910111213141516
   4567891011121314151617
  3456789101112131415161718
 2345678910111213141516171819
1234567891011121314151617181920

*/ 

// pattern for above pattern 

#include <iostream>

using namespace std;

int main()
{
     int n;
     cout << "Enter any number :\t"
    cin >> n;
    for (int i = 1; i <= n; i++) {
        int j;
        for ( j = 1; j <= n - i; j++) {
            cout << " ";
        }
        for (; j <=i; j++) {
            cout << j;
        }
        cout << endl;
    }


    return 0;
}
