//ID
// YUkio rivera

#include <iostream>
using namespace std;

//Enumeration
enum EyeColor {Brown, Blue, Green, Gray, other};
float sum(float a, float b);

int main()
{
    cout << "Variable example----------------------------" << endl;
    int age = 25;
    age = 26;
    cout << age << endl;
    float weight = 65.5;
    double balance = 1234567.8;
    char gender = 'f';
    string username = "CodeBeauty";
    string colors[10] = {"red", "green", "pink", "blue", "black"};
    cout << colors[0] << endl;
    
    bool isTodaySunny = true;
    bool isWeekend = true;
    // if (isTodaySunny) {
    //     cout << "Go outside" << endl;
    // }
    
    // else {
    //     cout << "Stay inside" << endl;
    // }
    
    //You can also do if else in trenary format
    isTodaySunny ? cout << "Go outside" << endl : cout << "Stay inside" << endl;
    isWeekend && isTodaySunny ? cout << "Good day" << endl : cout << "bad day" << endl;

    cout << "Swich case Example------------------------" << endl;
    EyeColor eyeColor = Brown;
    

    switch (eyeColor){
        case Brown: cout << "80% of people have Brown eyes.";
        case Blue: cout << "10% of people have Brown eyes.";
        case Green: cout << "2% of people have Brown eyes.";
        case Gray: cout << "1% of people have Brown eyes.";
        case other: cout << "7% of people have Brown eyes.";
        default:cout << "Not valid eye color";
    }
    cout << "While Loop example----------------------" << endl;
    int counter = 1;
    while (counter <= 10){
        cout << to_string(counter) + ",";
        counter ++;
    cout << endl;
    }

    cout << "Do while loop example--------------------" << endl;
    int doWhilecounter = 1;
    do {
        cout << to_string(doWhilecounter) + ",";
        doWhilecounter ++;
    cout << endl;
    }  while(doWhilecounter <= 10);

    cout << "For loop example ----------------" << endl;
    string animals[5] = {"cat", "dog", "cow", "goat", "bee"};
    for (int i = 0; i < 5; i++){
        cout << animals[i] << endl;
    }

    cout << "Functions example----------------------------" << endl;
    cout << "Function that returns a value" << endl;

}