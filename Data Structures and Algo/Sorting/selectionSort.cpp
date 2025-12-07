/**
 * The code implements the selection sort algorithm in C++ to sort an array in ascending order.
 * 
 * @param arr The `arr` parameter is an integer array that stores the elements to be sorted using the
 * selection sort algorithm. In the `main` function, an array `arr` is initialized with values {4, 1,
 * 5, 2, 3} which will be sorted using the `
 * @param n The variable `n` in this code represents the number of elements in the array that you want
 * to sort. In this specific example, `n` is set to 5, indicating that the array `arr` contains 5
 * elements that need to be sorted using the selection sort algorithm.
 */
#include <iostream>
using namespace std;

void selectionSort(int arr[], int n ){
    for(int i=0; i<n-1; i++){
        int smallestIdx = i; //unsorted part starting
        for (int j=i+1; j<n; j++){
            if (arr[j]<arr[smallestIdx]){
                smallestIdx = j;
            }
        }   
        swap(arr[i],arr[smallestIdx]);
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

    selectionSort(arr,n);
    printArray(arr,n);
    return 0;
}