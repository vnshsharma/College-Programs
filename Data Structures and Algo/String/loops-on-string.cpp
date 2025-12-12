#include<iostream>
#include<string>
using namespace std;

int main(){
    string str = "hello human.";

    // for (int i=0; i<str.length(); i++){
    //     cout<<str[i]<<" ";
    // }

    for (char ch : str){
        cout<<ch<<" ";
    }

    cout<<endl;
    return 0;
}