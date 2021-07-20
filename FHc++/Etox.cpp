//  Student ID:20288575
//  Yukio Rivera
//
//  Etox.cpp
//  2a-Lab-01
//
#include <iostream>
#include <sstream>
#include <cmath> // needed for sqrt
#include <cstdlib> // for exit()
using namespace std;

//Function Declarations 
double etox_5_terms(double x) {
    double sm = 0;
    //cout << pow(x,2)/(2*1) + pow(x,3)/(3*2*1) + pow(x,4)/(4*3*2*1) << endl;
    sm = 1 + x + pow(x,2)/(2*1) + pow(x,3)/(3*2*1) + pow(x,4)/(4*3*2*1);
    return sm;
}

//Main Function 
int main(int argc, char **argv) {
string user_input;
double x;
cout <<"Enter a value for x: ";
getline(cin, user_input);
istringstream(user_input) >>x;
cout << etox_5_terms(x) << endl;

return 0;
}
