//  Student ID:20288575
//  Yukio Rivera
//
//  Limerick.cpp
//  2a-Lab-01
//
#include <iostream>
#include <sstream> // Need this for istringstreambelow
#include <cmath>   // needed for sqrt
#include <cstdlib> // for exit()

using namespace std;
double eval_limerick(int dozen, int gross, int score){
    // TODO - Your code here
    //Score = 20, gross = 144
    double ans = ((dozen + gross + score + 3 * sqrt(4)) / 7) + 5 * 11; 
    return ans;
}
// I'm using command line arguments below to let me ntest your program with
// various values from a batch file. You don't have to know the details for
// CS2A, but you're welcome to - Discuss in the forums any aspect of this
// program you don't understand.
int main(int argc, char ** argv)
{
    int dozen, gross, score;

    if (argc < 4) {
        cerr <<"Usage: limerick dozen-val gross-valscore-val\n";
        exit(1);
    }
    istringstream(argv[1]) >>dozen;
    istringstream(argv[2]) >>gross;
    istringstream(argv[3]) >>score;
    
    // Invoke the eval_limerick function correctlyand print the result
    // with a single newline at the end of the line.
    // TODO - Your code here (just invoke your functionwith the above
    // values for its params. Don't worry about argc,etc. for now)
    cout << eval_limerick (dozen, gross, score) << endl;

    return 0;
}