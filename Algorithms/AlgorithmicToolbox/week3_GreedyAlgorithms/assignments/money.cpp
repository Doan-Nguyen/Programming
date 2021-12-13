#include <iostream>

using namespace std;

int money(int m){
    int number_money = 0;
    return 0;
}

int numbDigits(int n){
    int count = 0;
    while(n != 0){
        n = n/10;
        count += 1;
    }
    return count;
}

int main(){
    int n, count;
    cin >> n;
    count = numbDigits(n);
    cout << count;
    return 0;
}
