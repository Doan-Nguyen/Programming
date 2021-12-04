#include <iostream>

using std::cin;
using std::cout;

int fibonacci(int n){
    if (n <= 1){
        return 1;
    }
    return fibonacci(n -1) + fibonacci(n - 2);
}

int main(){
    int n;
    cin >> n;
    int result = fibonacci(n);
    cout << result << '\n';
    return 0;
}