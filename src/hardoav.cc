// main file
// author: grepcook

#include <iostream>

#include <boost/program_options.hpp>

using namespace std;
using namespace boost::program_options;
void on_age(int age)
{
  std::cout << "On age: " << age << '\n';
}

int main(int argc, const char *argv[]) {
    try {

    }
    catch (const error &ex) {
        std::cerr << ex.what() << std::endl;
        return 1;
    }
    return 0
}

