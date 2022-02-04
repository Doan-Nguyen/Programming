#include <iostream>
#include <vector>
#include <cassert>

using std::cin;
using std::cout;
using namespace std;

int fibonacci_naive(int n){
    if (n <= 1){
        return n;
    }
    return fibonacci_naive(n -1) + fibonacci_naive(n - 2);
}

int fibonacci_fast(int n){
    vector<int> vec_nums = {0, 1};
    if (n <= 1){
        return n;
    }
    for (int i=2; i <= n; i++){
        // cout << vec_nums.end()[-1] << " - " <<  vec_nums.end()[-2] << '\n';
        int next_num = vec_nums.end()[-1] + vec_nums.end()[-2];
        // cout << "append: " << next_num << '\n';
        vec_nums.push_back(next_num);
    }
    return vec_nums.end()[-1];
}

void test_solution() {
    assert(fibonacci_fast(3) == 2);
    assert(fibonacci_fast(10) == 55);
    for (int n = 0; n < 20; ++n)
        assert(fibonacci_fast(n) == fibonacci_naive(n));
}


int main(){
    int n;
    cin >> n;
    // std::cout << fibonacci_naive(n) << '\n';
    // test_solution();
    std::cout << fibonacci_fast(n) << '\n';
    return 0;
}
