#include <iostream>
#include<string>
using namespace std;
// Testing on how to do the vowels

string make_a_name(int len){
    string temp = "hi";
    string vowels = "aeiou";
    string constants = "bcdfghjklmnpqrstvwxyz";
    int rand_num = rand();
    cout << rand_num << endl;
    return temp;
}

int main(){
    cout << make_a_name(5);
} 