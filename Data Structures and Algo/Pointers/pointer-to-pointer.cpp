/**
 * The function declares an integer variable, creates a pointer to it, and then creates a pointer to
 * the pointer.
 * 
 * @return The program is returning the memory address of the pointer `ptr` and the memory address of
 * the pointer `parPtr`.
 */
#include <iostream>
using namespace std;
int main(){
    int a = 100;
    
    int* ptr = &a;
    int** parPtr = &ptr;

    cout<<parPtr<<endl;
    cout<<&ptr<<endl;

    return 0;
}