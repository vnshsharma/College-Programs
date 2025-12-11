/**
 * The function `changeA` modifies the value of an integer variable passed by reference using pointers.
 * 
 * @param b b is a reference parameter of type int in the function changeA. It is passed by reference
 * using pointers, allowing the function to modify the value of the variable passed to it.
 */
#include <iostream>
#include <vector>
using namespace std;

void changeA(int &b){ // pass by reference using pointers
    b = 20;
}

int main(){
    int a = 10;

    changeA(a);
    cout<<"inside main function: "<<a<<endl; //20
    return 0;
}