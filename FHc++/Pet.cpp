//  Pet.cpp 
//  2a-Lab-06-Pets 
// a calculating crow
 
#include <iostream> 
#include <sstream> 
#include <vector> 
 
#include "Pet.h" 
 
using namespace std; 
 
// This is a way to properly initialize (out-of-line) a static variable. 
size_t Pet::_population = 0; 
 
Pet::Pet(string name, long id, int num_limbs) { 
    // TODO - Your code here 
} 
 
Pet::~Pet() { 
    // TODO - Your code here 
} 
 
string Pet::get_name() const { return _name; } 
long Pet::get_id() const {  
    // TODO - Your code here 
} 
 
int Pet::get_num_limbs() const {  
    // TODO - Your code here 
} 
 
bool Pet::set_name(string name) { 
    // TODO - Your code here 
} 
 
bool Pet::set_id(long id) { 
    // TODO - Your code here 
} 
 
bool Pet::set_num_limbs(int num_limbs) { 
    // TODO - Your code here 
} 
 
string Pet::to_string() const { 
    // TODO - Your code here 
} 
 
// Fill in the supplied pets vector with n pets whose 
// properties are chosen randomly. 
// Don't mess with this method more than necessary. 
void Pet::get_n_pets(size_t n, std::vector<Pet>& pets, int name_len) { 
    // TODO - Resize pets as necessary 
    long prev_id = 0; 
    for (size_t i = 0; i < n; i++) { 
        long id = prev_id + 1 + rand() % 10; 
        pets[i].set_id(id); 
        pets[i].set_num_limbs(rand() % 9); // up to arachnids 
 
        // TODO - make and set a name of the requested length 
        // TODO - adjust prev_id as necessary
    } 
} 
 
string Pet::make_a_name(int len) { 
    // TODO - Your code here 
} 
 
// Optional EC points 
// Global helpers 
bool operator==(const Pet& pet1, const Pet& pet2) { 
    // TODO - Your code here 
} 
 
bool operator!=(const Pet& pet1, const Pet& pet2) { 
    // TODO - Your code here 
} 
 
ostream& operator<<(ostream& os, const Pet& pet) { 
    // TODO - Your code here 
} 