// In C++: write a function that takes a string as input and returns a new string that is equal to the 
// input but where &, < and > are replaced by &amp;, &lt; and &gt;

#include <iostream>
#include <string>

using namespace std;

string replace_char(string str) {
    string newStr = "";
    for (char c : str) {
        if (c == '&') {
            newStr += "&amp;";
        } else if (c == '<') {
            newStr += "&lt;";
        } else if (c == '>') {
            newStr += "&gt;";
        } else {
            newStr += c;
        }
    }
    return newStr;
}

int main() {
    string str;
    
    cout << "Enter your string: " << endl;
    getline(cin, str);
    
    str = replace_char(str);
    
    if (str == "") {
        cout << "Error" << endl;
    } else {
        cout << "Output string: " << endl;
        cout << str << endl;
    }
    
    return 0;
}