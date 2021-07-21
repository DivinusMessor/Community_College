//  Student ID:20288575
//  Yukio Rivera
//
//  Eliza.cpp 
//  2a.Lab-05-Eliza 
// 
// 
#include <iostream> 
#include <sstream> 
#include <string>
#include <algorithm>
 
using namespace std; 
 
// Return a new string in which the letters (lowercase) a, e, i, o, and u 
// have been replaced by the next vowel in the sequence aeiou. Replace u by a. 
// 
// Note that the string is passed in by reference. So the caller may not 
// rely on the result being returned. 
// TODO - Your code for rotate_vowels goes here
int rotate_vowels(string strg){
    // cout << strg.length(); //This returns the length of the str
    // string vowels[strg.length()] = {};
    // for (int i=0; i<strg.length(); i++){
    //     temp = strg[i];
    //     if temp in 
    // }
    return 0;
} 
 
// Return a string in which all occurrences of s have been replaced by th 
// TODO - Your code for lispify goes here 
string lispify(string strg){
    for (int i=0; i<strg.length(); i++){
        if (strg[i] == 's'){
            strg.replace(i, 1, "th");;
        } 
        else if (strg[i] == 'S'){
            strg.replace(i, 1, "Th");
        }
    }
    return strg;
}
 
// Enter the user-interaction loop as described earlier 
void enter() { 
    // TODO - Your code here 
    ;
}

int main(){
    //cout << rotate_vowels("hats");
    cout << lispify("sixSix");
}