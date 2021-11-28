#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;

long long MaxPairwiseProduct(const vector<int>& numbers){
    long long result = 0;
    int n = numbers.size();
    for (int i = 0; i < n; ++i){
        for (int j = i + 1; j < n; ++j){
            if (((long long)numbers[i])*numbers[j] > result){
                result = ((long long)numbers[i])*numbers[j];
            }
        }
    }
    return result;
}


long long MaxPairwiseProductFast(const vector<int>& numbers){
    long long result = 0;
    int n = numbers.size();
    // find the index which is max value
    int max_index = -1;
    for (int i = 0; i < n; ++i){
        if((numbers[i] > numbers[max_index])){ 
            max_index = i;
        }
    }
    // 
    int max_index2 = -1;
    for (int j = 0; j < n; ++j){
        if (j != max_index && numbers[j] > numbers[max_index2]){ 
            max_index2 = j;
        }
    }
    return ((long long)numbers[max_index])*numbers[max_index2];
}

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