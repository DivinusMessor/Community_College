//  Student ID:20288575
//  Yukio Rivera
//
//  Eliza.cpp 
//  2a.Lab-05-Eliza 
// 
// takshaka the serpent
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
string rotate_vowels(string strg){
    //https://stackoverflow.com/questions/21358215/how-to-compare-string-to-multiple-char-c
    // go to that website and see how its done to switch
    //char vowels[5] = {'a','e','i','o','u'}; 
    for ( int i=0; i<6; i++){
        if (strg[i] == 'a') {
            strg[i] = 'e';
        }
        else if (strg[i] == 'e') {
            strg[i] = 'i';
        }
        else if (strg[i] == 'i') {
            strg[i] = 'o';
        }
        else if (strg[i] == 'o') {
            strg[i] = 'u';
        }
        else if (strg[i] == 'u') {
            strg[i] = 'a';
        }
    } 
    return strg;
}
// Return a string in which all occurrences of s have been replaced by th 
// TODO - Your code for lispify goes here 
string lispify(string strg){
    for ( int i=0; i<6; i++){
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
void enter(){
    cout << "What?" << endl;
    for (;;){
        string answer;
        getline(cin, answer);
        if (answer.empty()){
            enter();
        }
        else if (answer.find('!') != std::string::npos){
            cout << "OMG! You don't say!!  " << answer << "!!!!!" << endl;
            enter();
        }
        else if ((answer == "what?") | (answer == "why?")){
            cout << "I'm sorry, I don't like questions that contain what or why." << endl;
            enter();
        }   
        else if (answer.find('s') != std::string::npos){
            cout << "Interethting. When did you thtop thtopping your thibilanth?" << endl;
            cout << lispify(answer) << "! Sheesh! Now what?"  << endl;
            enter();
        }
        else if ((answer == "bye") | (answer == "quit") | (answer == "Bye") | (answer == "Quit")){
            cout << "Ok Bye. Nice being a force of change in your life." << endl;
            break;
        }
        if (rand() % 10 >= 8){
            cout << "Huh? Why do you say: " << answer << "?" << endl;
        }
        
        else{
            cout << rotate_vowels(answer) << "?" << endl;
        }
        cout << "    " << answer << endl;
        cout << endl;
        cout << endl;
        
    }
}

// int main(){
//     //cout << rotate_vowels("hats");
//     //cout << lispify("sixSix");
//     //cout << lispify("sAXsACKssS");
//     //cout << rotate_vowels("that's really cool");
//     enter();
// }