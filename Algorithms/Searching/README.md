# Searching

Searching is the process of finding an item with specified properties from a collection of items. The items may be stored as records in a database, simple data elements in arrays, text in files, nodes in trees, vertices and edges in graph, or they may be elements of some other search spaces.

## [Linear Search]

Linear Search is the simplest of all search algorithms. It just checks the required data point with all the elements in the array.

> Linear Search has a complexity of O(n).

## [Binary Search]

Binary Search requires the input array to be sorted. Binary Search in every iteration finds the middle element of the array and compares it with the data to be searched, if the middle element is smaller than data, it will skip the first half of the array and only check the second half in the next iteration. Again in the second iteration it will find the middle element of the updated array and repeat the process until we find the element or array has no element. In the second case the data is not in the array.

> Binary Search has a complexity of O(logn).

## [Interpolation Search]

Interpolation Search like Binary Search, always chooses the middle of the remaining search space, discarding one half or the other, again depending on the comparison between the key value found at the estimated position and the value sought.

> Interpolation Search has a complexity of O(logn).

## [Bloom Filter]

Bloom Filter is a very light data structure which could test whether a given value is in the array or not. It was invented by Burton Howard Bloom in 1970. The price paid for the efficiency is that the output given tells us either the data is **definetly not** in the set or **may be** present in the set.

> Bloom Filter has a complexity of O(k) where k is the no. of hash functions used.

## Comparison of Sorting Algorithms

|Name|Worst Case|Average Case|
|---|--|---|
|**Linear Search**| O(n) | O(n) |
|**Binary Search**|O(logn)|O(logn)|
|**Interpolation Search**|O(n)|O(log(logn))|

[Linear Search]: linear_search.py
[Binary Search]: binary_search.py
[Interpolation Search]: interpolation_search.py
