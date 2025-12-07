/**
 * The code implements the bubble sort algorithm in C++ to sort an array of integers in ascending
 * order.
 * 
 * @param arr arr is an array of integers that stores the elements to be sorted using the bubble sort
 * algorithm. In the provided code snippet, the array arr contains the elements {4, 1, 5, 2, 3}.
 * @param n The variable `n` in this code represents the number of elements in the array that you want
 * to sort. In this specific example, `n` is set to 5, indicating that the array `arr` contains 5
 * elements that need to be sorted using the bubble sort algorithm.
 * 
 * @return If the `bubbleSort` function completes sorting the array without any swaps, it will return
 * without making any changes to the array.
 */
#include <iostream>
using namespace std;

void bubbleSort(int arr[], int n){   //O(n^2)
    for (int i=0; i<n-1; i++){
        bool isSwap = false;
        for (int j=0; j<n-i-1; j++){
            if (arr[j]>arr[j+1]){
                swap(arr[j],arr[j+1]);
                isSwap = true;
            }
        }
        if (!isSwap){
            return;
        }
    }
}

void printArray(int arr[], int n){
    for (int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}

int main(){
    int n = 5;
    int arr[] = {4,1,5,2,3};

    bubbleSort(arr,n);
    printArray(arr,n);
    return 0;
}