#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;

long long gcd(long long a, long long b){
    if (b==0){
        return a;
    }
    return gcd(b, a%b);
}

long long lcm(long long a, long long b){
    long long gcd_value = gcd(a, b);
    long long lcm_value = a*b/gcd_value;
    return lcm_value;
}


int main(){
    long long a, b;
    cin >> a >> b;
    long long result = lcm(a, b);
    cout << result << '\n';
    return 0;
}
