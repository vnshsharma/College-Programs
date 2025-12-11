/**
 * The C++ program initializes a pointer to a pointer and prints its value, which is NULL.
 * 
 * @return The code is returning the memory address of the pointer variable `ptr`. Since `ptr` is
 * initialized to `NULL`, the output will be `0` or a similar representation of a null pointer in the
 * system.
 */
#include <iostream>
using namespace std;
int main(){
    int** ptr = NULL;

    cout<< ptr <<endl;
    return 0;
}