#include <ctime>
#include <fstream>
#include <ios>
#include <iostream>
#include <string>
#include "chrono"
#include "fstream"


using namespace std;


int main(){

    // int a = 10;   
    int b;

    // cin >> a >> b;

    string brackets;
    ifstream myfile;
    // myfile.open("text.txt", ios_base::app);
    // myfile >> brackets;

    cin >> b >> brackets;


    auto t0 = chrono::high_resolution_clock::now();

    int maxcurve = 0; // max bracket value
    int maxcurveplace = 0; // it's place in the string
    int ph = 0; // placeholder value
    int changes = 0;

    // cout << a << '\n' << b << '\n';
    // for (int z = 0; z < brackets.length()+1; z++, maxcurve = 0){
    do{
        maxcurve = 0;
        maxcurveplace = 0;
    

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
        cout << brackets << '\n';

        
    }while (maxcurve > b);



    

    auto t1 = chrono::high_resolution_clock::now();

    chrono::duration<double> elapsed = t1-t0;

    cout << maxcurve << ' ' << brackets << ' ' << changes << '\n';
    cout << elapsed.count() << '\n';

    return 0;
}