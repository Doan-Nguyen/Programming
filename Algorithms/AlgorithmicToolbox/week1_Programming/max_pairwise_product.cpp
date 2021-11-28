// AlgorithmsToolbox.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;

long long MaxPairwiseProduct(const vector<int>& numbers) {
    long long result = 0;
    int n = numbers.size();
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            if (((long long)numbers[i]) * numbers[j] > result) {
                result = ((long long)numbers[i]) * numbers[j];
            }
        }
    }
    return result;
}


long long MaxPairwiseProductFast(const vector<int>& numbers) {
    long long result = 0;
    int n = numbers.size();
    // find the index which is max value
    int max_index = -1;
    for (int i = 0; i < n; ++i) {
        if ((numbers[i] > numbers[max_index])) { // (max_index == -1) || 
            max_index = i;
        }
    }
    // 
    int max_index2 = -1;
    for (int j = 0; j < n; ++j) {
        if (j != max_index && numbers[j] > numbers[max_index2]) { // max_index2 == -1) || // (numbers[j] != numbers[max_index])
            max_index2 = j;
        }
    }
    return ((long long)(numbers[max_index])) * numbers[max_index2];
}

int main() {
    //int n;
    //cin >> n;
    //vector<int> numbers(n);
    //for (int i = 0; i < n; ++i) {
    //    cin >> numbers[i];
    //}
    long long result = MaxPairwiseProductFast(vector<int>(100000, 0));
    cout << result << '\n';
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
