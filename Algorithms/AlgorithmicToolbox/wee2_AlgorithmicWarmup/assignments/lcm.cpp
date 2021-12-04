#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;



int main(){
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i=0; i < n; ++i){
        cin >> numbers[i];
    }
    long long result = MaxPairwiseProductFast(numbers);
    cout << result << '\n';
    return 0;
}