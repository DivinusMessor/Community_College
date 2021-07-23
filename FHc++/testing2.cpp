#include <iostream>
using namespace std;
// Testing on how to do the vowels

void enter(){
    cout << "What?" << endl;
    for (;;){
        string answer;
        getline(cin, answer);
        if (answer.empty()){
            enter();
        }
        cout << "    " << answer << endl;
    }
}

int main(){
    enter();
}