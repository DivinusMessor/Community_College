#include <iostream>
#include<string>
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
        else if (answer.find('!') != std::string::npos){
            cout << "OMG! You don't say!!  " << answer << "!!!!!" << endl;
            enter();
        }
        else if (answer == "what?" | answer == "why?"){
            cout << "I'm sorry, I don't like questions that contain what or why." << endl;
            enter();
        }   
        else if (answer.find('s') != std::string::npos){
            cout << "Interethting. When did you thtop thtopping your thibilanth?" << endl;
            lispify(answer);
            enter();
        }
        cout << "    " << answer << endl;
        cout << endl;
        cout << endl;
        
    }
}

int main(){
    enter();
}