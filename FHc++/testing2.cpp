#include <iostream>
#include <string>
#include <ctime>

using namespace std;
// Testing on how to do the vowels

string make_a_name(int len){
    string n_name = "";
    string temp = "hi";
    string vowels = "aeiou";
    //21 constants
    string constants = "bcdfghjklmnpqrstvwxyz";
    int counter = 0;
    // Going to add a counter to swtich between the vowels and consts
    srand(time(NULL));
    int rand_num = rand() % 10 + 1;
    int rand_con = rand() % 21;
    cout << rand_num;
    cout << rand_con;
    if (rand_num % 2 == 0){
        for (int i = 0; i < constants.length(); i++){
            n_name[counter] = constants[rand()];
            counter ++;
            cout << n_name << endl;
        }
    }
    return temp;
}

int main(){
    cout << make_a_name(5);
} 