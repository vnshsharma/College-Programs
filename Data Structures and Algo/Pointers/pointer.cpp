/**
 * The program declares two variables, `a` and `price`, and prints out the memory addresses of these
 * variables using pointers.
 * 
 * @return The program will output the memory address of the variables `a` and `price` through the
 * pointers `ptr` and `ptr2` respectively. The output will be in hexadecimal format.
 */
#include<iostream>
using namespace std;
int main(){
    int a = 10;
    int* ptr = &a;


    float price = 100.2f;
    float* ptr2 = &price;

    cout<<ptr<<endl;
    cout<<&a<<endl;

    cout<<ptr2<<endl;
    return 0;   
}