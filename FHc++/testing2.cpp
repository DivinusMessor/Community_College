#include <iostream>
#include<string>
using namespace std;
// Testing on how to do the vowels

string make_a_name(int len){
    string temp = "hi";
    char vowels[] = {'a', 'e', 'i', 'o', 'u'};
    char constants[] = {'b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'};
    for (int i=0; i<10; i++){
        cout << constants[i];
    }
    return temp;
}

int main(){
    cout << make_a_name(5);
}