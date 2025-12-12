#include <iostream>
#include <string>
using namespace std;

int main(){
    string str1 = "hello human, "; //dynamic in nature
    string str2 = "I am from Earth";

    string str3 = str1+str2; //concatenation
    cout<<str3<<endl;

    cout<<str3.length()<<endl;

    string str;
    getline(cin,str);

    cout<<"Output: "<<str<<endl;
    return 0;
}