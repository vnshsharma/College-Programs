#include <iostream>
#include <cstring>
using namespace std;

/* In C and C++, `'\0'` represents the null character, which is a
character with all bits set to zero. It is used to denote the
end of a string in C-style strings. When a null character is
encountered in a character array, it signifies the end of the
string. In the code snippet provided, `'\0'` is used to
terminate the character array `str`, making it a valid C-style
string. */

int main(){
    char str[] = "hello human";
    cout<<"enter char array: ";
    
    // cin>>str;
    cin.getline(str,14);

    // for (char ch : str){
    //     cout<<ch<<" ";
    // }
    // cout<<endl;
    int len=0;
    for (int i=0; i<str[i] != '\0'; i++){
        len++;
    }
    cout<<"length of string: "<<len<<endl;
    
    // cout<<strlen(str)<<endl;
    return 0;
}