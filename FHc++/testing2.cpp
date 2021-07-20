#include <iostream>
using namespace std;

float sum(float a, float b);

int main(){
    cout << "Using functions------------------------------------------------" << endl;
    cout << sum(2.2, 5) << endl;
}

float sum(float a, float b){
    return a + b;
}
