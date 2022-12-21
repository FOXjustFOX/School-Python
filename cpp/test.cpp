#include <iostream>
#include "limits"

using namespace std;
using std::numeric_limits;
using std::boolalpha;

int main(){
    cout << boolalpha;
    cout << "is_signed: " << numeric_limits<int>::is_signed << endl;
    cout << "is_integer: " << numeric_limits<int>::is_integer << endl;
    cout << "is_exact: " << numeric_limits<int>::is_exact << endl;
    cout << "has_infinity: " << numeric_limits<int>::has_infinity << endl;
    cout << "has_quiet_NaN: " << numeric_limits<int>::has_quiet_NaN << endl;

    return 0;
}

Output:
