#include <iostream>
#include<string>
using namespace std;
// Testing on how to do the vowels

string lispify(string strg){
    for ( int i=0; i<strg.length(); i++){
        if (strg[i] == 's'){
            strg.replace(i, 1, "th");
        } 
        else if (strg[i] == 'S'){
            strg.replace(i, 1, "Th");
        }
    }
    return strg;
}


int main(){
    cout << lispify("a handthome buthh leaned at a red mat!");
}