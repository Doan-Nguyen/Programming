#include <iostream>
#include <array>

using namespace std;

void arr_multi_dimension(){
    float temp[31][24];
    float sum = 0.0, average_temp;
    //
    for (int day=0; day < 31; day++){
        sum += temp[day][11];
    }
    //
    average_temp = sum/31;
    cout << "Average temperature at noon: " << average_temp << endl;
}


int main(){
    // arr_multi_dimension();
    //          Static array
    int arr[15];
    int n = 0;

    return 0;
}