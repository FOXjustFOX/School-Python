#include <cstddef>
#include <iostream> // thanks to this we are able to get user input and much more
#include <string> // we can use strings
#include "cmath" // math 

using namespace std; // standard ... without it, cout would be "std::cout"


//function declaration's
void prinrname(); 
void math();
void if_statment();
void switch_case();
void while_loop();
void for_loop();
void list();
void strings();
void pointer();
void swapnum();

// functions can have declarations inside the (brackets), devided with commas
// and a default argument value (string default_ex = "your_mom")
// functions can return something BUT!
/*the void key word indicates that a function should not return a value,
so if we want to use 'return' instead of 'void'
use the 'type' of the return value:

int myFunction(int x){
    return 5 * x
}

*/
// you can pass references to variables to the functions, to change theirs values
// you can pass whole lists to functions



// main function
int main(){ 
    prinrname(); 
    math();
    if_statment();
    switch_case();
    while_loop();
    for_loop();
    list();
    strings();
    pointer();
    return 0; // end the function
}


// Function definison's
void prinrname(){
    string name; // init of a string value
    cout << "enter your name: "; // user input
    getline (cin, name); /* almost the same as cin but with getline 
                        you can save the whole line in a var*/
    cout << "your name is: " << name << "\n"; // print some text with new line 

}

void math(){
    cout << sqrt(64) << "\n"; // math things
    cout << round(2.6) << "\n";
    cout << ceil(2.34567) << "\n";

}

void if_statment(){
    int time = 20;
    if (time > 18){
        cout << "evening! \n";
    } else {
        cout << "not evening! \n";
    }
                       // statment   if true         else
    string what_time = (time > 18) ? "evening \n" : "not evening \n"; // short hand i else

    cout << what_time;


}

void switch_case(){
    cout << "enter a number: ";
    int day;
    cin >> day; // 
    switch (day){ // switch function (case = (day))
        case 1: 
            cout << "monday \n";
            break;
        case 2:// comparing statment to each case
            cout << "tuesday \n";
            break;
        case 3:
            cout << "wednesday \n";
            break;
        case 4:
            cout << "thursday \n";
            break;
        case 5:
            cout << "friday \n";
            break;
        case 6:
            cout << "saturday \n";
            break;
        case 7:
            cout << "sunday \n";
            break;

        default: // if there's not case match then:
            cout << "not a weekday number! \n";
    }

}

void while_loop(){
    int i = 0;
    while (i < 5){ // normal while loop
        cout << i << '\n';
        i++; // add 1 to 'i' var
    }

    i = 6;

    do { // do/while loop will run once or more if the statment is true
        cout << i << '\n';
        i++;
    }
    while (i < 5); // the statment


}

void for_loop(){
    // in a for loop you can use 'break' and 'continue'
    for (int i = 0; i < 5; i++){ // for a variable
    /*
    st_1 = executed one time before the exe. of the block
    st_2 = defines the condition for exe. of the block
    st_3 = is executed every time after the block has been executed 
    */
        cout << i << '\n';
    }

    string mynumbers[3] = {"hello", "muef", "hasfdsd"};
    for (string i : mynumbers){ // for string(i) in list (variable : list_name)
        cout << i << '\n';
    }

    for (int i = 0; i < 10; i++){
        if (i == 4){
            continue; // break one iteration if st. is met and continues with the next interation of the loop 
        }
        cout << i << '\n';
    }


}

void list(){
    //var type  name of the list[num of items it should store (it's automatic)]
    int mylist[/*fixed or automatic size*/] = {1,2,3};
    //           curly brackets
    
    // to get the size of the array:
    // divide the sze of the array(in bytes) by the size of byte
    int size = sizeof(mylist) / sizeof(int);
    cout << '\n' << size << '\n';
    
    // multidimentional array
    char letters[2][2][2] = {
        {
            {'a','b'},
            {'c','d'}
        },
        {
            {'e','f'},
            {'g','h'}
        }
    };

    for (int i = 0; i < 2; i++){
        for (int j = 0; j < 2; j++){       // iterating through the whole array
            for (int k = 0; k < 2; k++){
                cout << letters[i][j][k] << '\n';
            }
        }
    }


}

void strings(){
    string food = "pizza";
    string meal = food; // saves the food value of food 
    string &meal2 = food; // is the value of food (reference)

    food = "lasagne"; // when changing the food value

    cout << meal << '\n' << meal2 << '\n'; // meal = pizza but meal2 = lasagne


}

void pointer(){
    //you can assign a variable memory adress to another variable, to later use it
    string food = "pizza";
    //  star
    string* ptr = &food;

    //    variable        pointer    value of the pointer's variable 
    cout << food << '\n' << ptr << '\n' << *ptr << '\n';
    //     pizza           0x......        pizza

    //star ptr
     *ptr = "hamburger";

    cout << food << '\n' << ptr << '\n' << *ptr << '\n';
}

// using the reference to the arguments variables
// to change them for teh whole file 
void swapnum(int &num1, int &num2){
    int z  = num1;
    num1  = num2;
    num2 = z;
}




