//  Student ID:20288575
//  Yukio Rivera
//
//  Branching_Functions.cpp
//  2a-Lab-03
//
#include <iostream>

// Forward declarations of functions that will be used in this file
// before their definitions are encountered by the compiler
double mean_of_3(int n1, int n2, int n3);
int max_of_5(int n1, int n2, int n3, int n4, int n5);
int min_of_5(int n1, int n2, int n3, int n4, int n5);
bool sides_make_triangle(int a, int b, int c);
bool angles_make_triangle(int A, int B, int C);
bool is_a_leap_year(int year);

// This function returns the mean the three numbers passed
// in as parameters. Note that the mean may not be a round
// number. So you must use the double datatype for it.
double mean_of_3(int n1, int n2, int n3){
    // TO do
    double avg = 0;
    avg = (n1 + n2 + n3)/3.0;
    return avg;
}

// This function returns the maximum of the 5 given numbers
int max_of_5(int n1, int n2, int n3, int n4, int n5){
    //to do
    int arr [5] = {n1, n2, n3, n4, n5};
    int asr = arr[0];
    for (int i=0; i<5; i++){
        if (arr[i] > asr){
            asr = arr[i];
        }
    }
    return asr;
}

// This function returns the minimum of the 5 given numbers
int min_of_5(int n1, int n2, int n3, int n4, int n5){
    // to do
    int arr [5] = {n1, n2, n3, n4, n5};
    int asr = arr[0];
    for (int i=0; i<5; i++){
        if (arr[i] < asr){
            asr = arr[i];
        }
    }
    return asr;
}

// Given three lengths, this function should return whether they can be the
// sides of some triangle. The heuristic you code should check if the
// sum of the two smallest sides is greater than or equal to the third side.
// Treat extreme cases as valid trianges. E.g. a+b == c means valid triangle.
// The challenge is to do it without using arrays
bool sides_make_triangle(int a, int b, int c){
    if ((a <= c) and (b <= c)){
        return a + b >= c;
    }
    if ((a <= b) and (c <= b)){
        return a + c >= b;
    }
    if ((b <= a) and (c <= a)){
        return b + c >= a;
    }
    return 0;
}


// Given three angles as integer degrees, this function should return whether
// they can be internal angles of some triangle. Treat extreme cases as
// valid triangles. E.g. (0, 0, 180) is a valid triangle
bool angles_make_triangle(int A, int B, int C) {    
    if (A + B + C == 180){
        return true;
    }
    return false;
}

// Return true if the year yyyy is a leap year and false if not.
bool is_a_leap_year(int yyyy){
    //do
    if (yyyy == 100){
        return false;
    }
    else if (yyyy%4 == 0){
        return true;
    }
    return false;
}


// int main(){
//     //std::cout << sides_make_triangle(4458,8026,7006) << std::endl;
//     //std::cout << sides_make_triangle(1,3,5) << std::endl;
//     //std::cout << sides_make_triangle(19615,13871,3365) << std::endl;
//     //std::cout << sides_make_triangle(6421,17583,16) << std::endl;
//     std::cout << is_a_leap_year(100) << std::endl;
//     std::cout << is_a_leap_year(104) << std::endl;
//     return 0;
// }