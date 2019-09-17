# Sorting

Sorting is an algorithm to arrange the elements of a list in a certain order. Sorting is one of the important categories of algorithms in computer science and a lot of research has gone into this categroy. Sorting can significantly reduce the complexity of a problem, and is often used for database algorithms and searches.

## [Bubble Sort]

Bubble Sort is the simplest sorting algorithm. It works by iterating over the input array from the first element to the last, comparing each pair of elements and swapping them if needed. Bubble sort continues its iterations until no more swaps are needed. The algorithm gets its name from the way smaller elements "bubble" to the top of the list.

> Bubble Sort takes O(n^2) (even in best case) and a space complexity of O(1).

## [Selection Sort]

Selection Sort is an in-place sorting algorithm. Selection sort works well for small files. It is used for sorting the files with very large values and small keys. This is because selection us made based on keys and swaps are made only when required.

> Selection Sort has an worst case complextity of O(n^2) and a space complexity of O(1).

## [Insertion Sort]

Insertion Sort is a simple and efficient comparison sort. In this algorithm, each iteration removes an element from the input data and inserts it into the correct position in the list being sorted. The choice of the element being removed from the input is random and this process is repeated until all the input elements have gone through.

> Insertion Sort has a worst case complexity of O(n^2) and a space complexity of O(1).

## [Shell Sort]

Shell Sort is a modification of insertion sort. In insertion sort we used to check every element to find the position of the removed element. Shell sort is also known as n-gap insertion sort. The basic idea of shell sort is to exchange every nth element in the array if necessary.

> Shell sort has a worst case complexity of O(nlog^2n). It has a space complexity of O(1).

## [Merge Sort]

Merge Sort is an example of Divide and Conquer strategy. In merge sort the array are first divided and the sorted while merging them. It is a recursive algorithm which will divide the array until only one element is left and then start merging those peices, to get final sorted array.

> Merge Sort has a worst case complexity of O(nlogn). It has a space complexity of O(1).

## [Quick Sort]

Quick Sort is an example of Divide and Conquer algorithmic technique. It is also called partition exchange sort. It uses recursive calls for sorting the elements, and it is one of the famous algorithms among comparison based sorting algorithms.

> Quick sort has a worst case complexity of O(n^2) when the array given is already sorted. Except that it gives time complexity of O(nlogn). It has a space complexity of O(1).

## [Heap Sort]

Heap Sort is a comparion-based sorting algorithm and is a part of the selection sort family. Altough slower than quick sort, but it has a better worst case complexity of O(nlogn) than quick sort. It is an in-place algorithm but it is not a stable sorting algorithm.

> Heap sort has a worst case complexity of O(nlogn). It has a space complexity of O(1).

## [Counting Sort]

Counting sort is not a comparison based sorting algorithm and gives O(n) complexity for sorting. To achieve O(n) complexity, it assumes that each of the element in the array is an integer in the range of 1 to K, for some integer K. The basic idea of counting sort is to determine, for each input element X, the number of element less than X. This information can be used to place it directly into its correct position.

> Counting Sort has a worst case complexity of O(n). It has a space complexity of O(n).

## [Bucket Sort]

Like counting sort, bucket sort also puts restrictions on the data to improve the performance. Bucket sort is the generalization of counting sort. It counts the occurance of each data in the input array and print it accordingly. It is indeed faster than counting sort as it does not have to calculate the elements occuring before a data point.

> Bucket Sort has a worst case complexity of O(n). It has a space complexity of O(n).

## [Radix Sort]

Similar to counting sort and bucket sort, radix sort also assumes some kind of information about the input elements. Suppose that the input values to be sorted are from base d. That means all numbers are d-digit numbers. In radix sort, the first the array is sorted based on the least significant bit using any other sorting technique, afterthat we move onto the second least significant bit and repeat the process untill the most significant bit.

> Radix Sort has a worst case complexity of O(n). It has a space complexity of O(n) (if we use secondary sorting technique as counting or bucket).

## Comparison of Sorting Algorithms

|Name|Average Case|Best Case|Auxilary Memory|Is Stable|Notes|
|---|--|---|--|---|--|
|**Bubble**| O(n 2) | O(n 2) | O(1) |Yes|Small Code|
|**Selection**|O(n 2)|O(n 2)|O(1)|No|Requires least number of swaps|
|**Insertion**|O(n 2)|O(n 2)|O(1)|Yes|Average case is also O(n + d), where d is the number of inversion|
|**Shell**|-|O(nlog 2n)|O(1)|No| It is also called n-gap insertion sort|
|**Merge**|O(nlogn)|O(nlogn)|O(1)|Yes|It works on Divide & Conquer strategy|
|**Quick**|O(nlogn)|O(nlogn)|O(1)|No|It works on Divide & Conquer strategy|
|**Heap**|O(nlogn)|O(nlogn)|O(1)|No|It is best for finding n maximum nos. or someting like this|
|**Counting**|O(n)|O(n)|O(n)|-|Best for arrays whose elements are in a fixed range|
|**Bucket**|O(n)|O(n)|O(n)|-|Best for arrays whose elements are in a fixed range|
|**Radix**|O(n)|O(n)|O(n)|-|Works best for small no. of elements|

[Bubble Sort]: \bubble_sort.py
[Selection Sort]: \selection_sort.py
[Insertion Sort]: \insertion_sort.py
[Shell Sort]: \shell_sort.py
[Merge Sort]: \merge_sort.py
[Quick Sort]: \quick_sort.py
[Heap Sort]: \heap_sort.py
[Counting Sort]: \counting_sort.py
[Bucket Sort]: \bucket_sort.py
[Radix Sort]: \radix_sort.py
