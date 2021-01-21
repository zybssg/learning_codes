#include <iostream>
#include <string>
#include "pystring.h"

int main(){
    std::string str = "1212 21";
    std::vector< std::string >  result;
    std::string sep = " ";
    int maxsplit = 4;
    pystring::split(str, result, sep, maxsplit);
    std::cout << result[0] << std::endl;
}
