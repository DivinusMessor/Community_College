//  Student ID:20288575
//  Yukio Rivera
//
//  Looping_Functions.cpp
//

#include <iostream>
#include <sstream>
#include <string>
#include <cmath> // needed for sqrt
using namespace std;


double fact(int x){
    double fact_an = 1;
    for (int i= 1; i<=x; i++){
        fact_an *= i;
    }
    return fact_an;
}

double pwr(double x, int i){
    double rt = 1;
    int counter = 0;
    while (counter < i){
        rt = rt * x;
        counter += 1; 
    }
    return rt;
}

// int n is the secret number
// Give the user 6 chances to guess the secret number n (0-10). If they get it,
// say so and return true. Else say so and return false.
bool play_game(int n) {
    string guess;
    int g_int;
    int counter;
    cout << "Welcome to my number guessing game" << endl;
    while (counter < 6){ 
        cout << endl;
        cout << "Enter your guess: " << endl;
        getline(cin, guess);
        istringstream c_str(guess);
        c_str >> g_int;
        cout << "You entered: " << guess;
        counter ++;
        if (n == g_int){
            cout << endl;
            cout << "You found it in " << counter;
            cout << " guess(es)." << endl;
            return true;
        }
    }
    cout << "I'm sorry. You didn't find my number." << endl;
    cout << "It was ​" << n;
    return false;
}

// Calculate e^x using the series summation up to exactly the first
// n terms including the 0th term.
double etox(double x, size_t n) {    
    double top = 0;
    double bottom = 0;
    double sm = 0;
    for (unsigned int i = 0; i<n; i++){
        top = pwr(x, i);
        bottom = fact(i);
        sm = sm + (top/bottom);
    }
    return sm;
}

// Return the number of occurrences of char c in string s
size_t count_chars(string s, char c) {    
    // TODO - Your code here
    int count = 0;
    //cout << c << "Make sure i know" << endl;
    //cout << s[1] << "does it work?" << endl;
    for (unsigned int i = 0; i < s.size(); i++){
        //cout << s[i] << "what letter point" << endl;
        if (s[i] == c){
            count++;
        }
    }
    return count;
}

// Use Euclid's algorithm to calculate the GCD of the given numbers
size_t gcd(size_t a, size_t b) {    
    // TODO - Your code here
    int divisor, dividend, remainder;
    dividend = a;
    divisor = b;
    //quotient = divisor / dividend;
    remainder = divisor % dividend;

    if (remainder == 0){
        return dividend;
    }
    return gcd(remainder, dividend);
}

// Return a string of the form n1,n2,n3,... for the given AP.
string get_ap_terms(int a, int d, size_t n) {    
    // TODO - Your code here
    string s;
    int num = a;
    unsigned int counter = 0;
    while (counter < n){
        s += to_string(num) + ",";
        num += d;
        counter += 1;
    }
    if (!s.empty()) {
        s.pop_back();
    }
    return s;
}

// Return a string of the form n1,n2,n3,... for the given GP.
string get_gp_terms(double a, double r, size_t n) {    
    // TODO - Your code here
    string s;
    double num = a;
    double counter = 0;
    while (counter < n){
        s += to_string(num) + ",";
        num *= r;
        counter += 1;
    }
    if (!s.empty()) {
        s.pop_back();
    }
    return s;
}

double get_nth_fibonacci_number(size_t n) {    
    // TODO - Your code here
    int first = 0;
    int second = 1;
    int sm = 0;
    unsigned int counter = 0;
    if (n == 1){
        return 1;
    }
    while (counter < n-1){
        sm = first + second;
        first = second;
        second = sm;
        counter ++;
    }
    return sm;
}

// int main() {
//     cout << get_ap_terms(3,-1,12) << "checked" << endl;
//     cout << get_gp_terms(4, .5, 6) << endl;
//     cout << get_nth_fibonacci_number(1) << endl;
//     cout << get_nth_fibonacci_number(2) << endl;
//     cout << get_nth_fibonacci_number(3) << endl;
//     cout << get_nth_fibonacci_number(4) << endl;
//     cout << get_nth_fibonacci_number(5) << endl;
//     cout << get_nth_fibonacci_number(6) << endl;
//     cout << get_nth_fibonacci_number(7) << endl;
//     cout << get_nth_fibonacci_number(8) << endl;
// }