// DSA_Coursera.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>
#include <cassert>

using std::cin;
using std::cout;
using namespace std;


int LastDigitFibonacci(int n){
    vector<long long int> vec_nums = {0, 1};
    if (n <= 1){
        return n;
    }
    for (int i=2; i <= n; i++){
        long long int next_num = vec_nums.end()[-1]%10 + vec_nums.end()[-2]%10;
        // cout << "append: " << next_num << '\n';
        vec_nums.push_back(next_num%10);
    }
    return vec_nums.end()[-1];
}

int get_fibonacci_last_digit_naive(int n) {
    if (n <= 1)
        return n;

    int previous = 0;
    int current  = 1;

    for (int i = 0; i < n - 1; ++i) {
        int tmp_previous = previous;
        previous = current;
        current = tmp_previous + current;
    }

    return current % 10;
}


int main() {
    int n;
    cin >> n;
    int last_digit_number = LastDigitFibonacci(n);
    cout << last_digit_number << '\n';
    return 0;
}


// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
