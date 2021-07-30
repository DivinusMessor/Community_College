#include <iostream>
#include <string>

using namespace std;
// Testing on how to do the vowels

string make_a_name(int len){
    string n_name = "";
    string temp = "hi";
    string vowels = "aeiou";
    string constants = "bcdfghjklmnpqrstvwxyz";
    int counter = 0;
    // Going to add a counter to swtich between the vowels and consts
    if (rand() % 2 != 0){
        for (int i = 0; i < constants.length(); i++){
            cout << ( rand() % (10 + 1 ) ) << endl;
        }
    }
    return temp;
}

int main(){
    cout << make_a_name(5);
} 