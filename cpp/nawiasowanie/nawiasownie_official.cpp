#include <iostream>
#include <string>

using namespace std;

int main(){

    int a;   
    int b;
    cin >> a >> b;

    string brackets;
    cin >> brackets;


    int maxcurve = 0; // max bracket value
    int maxcurveplace = 0; // it's place in the string
    int ph = 0; // placeholder value
    int changes = 0;


        for (int i = 0; i < brackets.length()+1; i++) {
            if (brackets[i] == '('){
                ph++; // if open bracket then add to placeholder value
                if (ph > maxcurve) { // if ph is bigger than max then save new max and it's place index 
                    maxcurve = ph;
                    maxcurveplace = i;
                }
            }else if (ph != 0 and brackets[i] == ')') { // if close bracket then substract from ph
                ph--;
            }
        }
        
        for (int i = maxcurve; i > b; i -= 2, maxcurveplace -= 2) {
            brackets[maxcurveplace] == '(' ? brackets[maxcurveplace] = ')' : brackets[maxcurveplace] = '(';
            brackets[maxcurveplace] == ')' ? brackets[maxcurveplace+1] = '(' : brackets[maxcurveplace+1] = ')';

            changes += 2;
        
        }


    cout << changes << '\n' ;


    return 0;
}