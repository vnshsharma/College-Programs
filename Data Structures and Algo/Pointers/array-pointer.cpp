/**
 * The code initializes an integer array, prints the memory address of the array, and then prints the
 * value at the first element of the array.
 * 
 * @return The code snippet is returning the memory address of the first element in the array `arr`
 * when `cout<< arr <<endl;` is executed. It is returning the value of the first element in the array
 * when `cout<< *arr <<endl;` is executed.
 */
#include <iostream>
using namespace std;

int main(){
    int arr[] = {1,2,3,4,5};

    cout<< arr <<endl;
    cout<< *arr <<endl; //pointer => 1
    return 0;
}