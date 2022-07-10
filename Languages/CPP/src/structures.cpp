#include <iostream>
#include <string>
#include <sstream>
using namespace std;


struct movies_title
{
    string title;
    int year;
};
//
movies_title mine;
movies_title* us;
//
void printmovie(movies_title movie){
    cout << movie.title;
    cout << " (" << movie.year << ") \n";
}
// 
int main(){
    string mystr;
    //
    mine.title = "You are apple in my eyes";
    mine.year = 2010;
    // 
    us = &mine;
    cout << "Enter title: ";
    // getline (cin, us.title);
    getline (cin, us->title);
    cout << "Enter year: ";
    getline (cin, mystr);
    // stringstream(mystr) >> us.year;
    stringstream(mystr) >> us->year;
    // 
    cout << "My favorite move is: \n";
    printmovie(mine);
    cout << "Our favorite move is: " << us->title << "\n";
    return 0;
}


