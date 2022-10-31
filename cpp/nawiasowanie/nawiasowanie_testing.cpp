#include <fstream>
#include <ios>
#include <iostream>
#include <string>
#include "fstream"
#include <cstring>

using namespace std;

int algorythm(int a, int b){
    // int a;   
    // // int b;
    // cin >> a >> b;

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
    return changes;
}


int main(){
    string pathin = "/testin/";//"/home/fox/Documents/ply/in/ply";
    string pathout = "/testout/";//"/home/fox/Documents/ply/out/ply";

    for (int i = 1; i< 2; i++) {
        ifstream myfilein;
        ifstream myfileout;

        //number of the test
        string sn = to_string(i);

        //value in
        string values; 
        int a,b;
        string brackets;

        //value out
        string valueout;
        int vout;

        //file in
        myfilein.open(pathin+sn+".in", ios_base::app);
        getline(myfilein, values);
        // getline(myfilein, brackets);
        
        a = values[0];
        b = values[2];

        cout << values;
        // << ' ' << a << " " << b << " " << brackets << endl;

        //file out
        myfileout.open(pathout+sn+".out", ios_base::app);
        getline(myfileout, valueout);
        // vout = stoi(valueout);

        cout << vout << endl;

        if (to_string(algorythm(a,b)) == valueout) {
            cout << "test " << i << " passed" << endl;
        }
    }

    return 0;

}