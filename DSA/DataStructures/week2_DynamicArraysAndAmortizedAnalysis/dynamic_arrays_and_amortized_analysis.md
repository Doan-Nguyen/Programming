# Dynamic Arrays and Amortized Analysis 

## Contents
1. [Dynamic arrays](#dynamic_arrays)
2. [Amortized Analysis](#amortized_analysis)

## 1. Dynamic arrays <a name="dynamic_arrays"></a>

+ Problem:
    - Dont know how many objects will store in array.

+ Solution:
    - Dynamic arrays (also known as *resizable arrays*)
    - **Idea**: store a pointer to a dynamically allocated array (mang phan bo dong) & replace it with newly-allocated array as needed.

+ Definition:   
    - Dynamic array: abstract data type with the following operations:
        - get(i): returns elements at location i
        - set(i, val): sets element i to val
        - push_back(val): adds val to the end of array
        - remove(i): removes element at position i
        - size(i): the number of elements

+ Implement:
    - Store:
        - arr: dynamically-allocated array
        - capacity: size of the dynamically-allocated array
        - size: number of elements currently in array
    - Example:
        - arr: [ , ] ~> size: 0, capacity: 2
        - push a, b => arr : [a, ] -> [a, b]
        - push c, d => arr_tmp : [ , , , ] ~> capacity: 4, size: 0
                    => arr_tmp : [a, b, , ] ~> capacity: 4, size: 2 => arr := arr_tmp
                    => arr : [a, b, c, ] ~> capacity: 4, size: 3
                    => arr : [a, b, c, d] ~> capacity: 4, size: 4

+ Common implementations
    - C++: vector
    - Python: list

+ Summary:
    - Unlike static arrays, dynamic arrays can be resized.
    - Appending a new element to a dynamic array is often constant time but can take O(n)
    - Some space is wasted - at most half.

## 2. Amortized (khau hao) Analysis <a name="amortized_analysis"></a>

+ Phân tích khấu hao: quan tâm đến thời gian trung bình của mỗi operation trong trường hợp không tốt.

+ Có 3 phương pháp phân tích khấu hao:
    - Aggregate analysis (phân tích tổng hợp): 
        - Xác định giới hạn trên T(n) của tổng chi phí chuỗi n-operations.
        - Chi phí trung bình của mỗi operation: T(n)/n.
        - Lấy chi phí trung bình ~ chi phí khấu hao của mỗi operations.
    - 

### 2.1 Aggregate method


### 2.2 Banker's method
+ Features:
    - Charge extra for each cheap operation
    - Save the extra charges as tokens in your data structure
    - Use the tokens to pay for expensive operations

+ Implements:
    - Dynamic array: n calls to PushBack
    - Idea: charge 3 for each insertion: 1 token is the raw cost for insertion. 
        - Resize needed: to pay for moving the elements, use the token that's present on each element that needs to move.
        - Place one token on the newly-inserted elements & one token (capacity/2) elements prior.

### 2.3 Physicist's method
+ Idea:
    - define a potential function (động năng) which maps states of the data structure to integers:
        - p(h_0) = 0 # h_0: time of the data structure h ~ initial
        - p(h_t) >= 0 
    - amortized cost for operation t: 
        - c_t + p(h_t) - p(h_(t-1))
    - Choose p() so that:
        - if c_t : small, the potential increases
        - if c_t : large, the potential decreases by the same scale

+ Implement:
    - The cost of *n* operations is: 
    $$
    \sum^{n}_{i=1} c_{i}
    $$
    - The sum of the amortized costs is:
    $$
    \sum_{i=1}^{n} (c_{i} + p(h_{i}) - p(h_{i - 1}))
    $$

Reference:
[Chap 17 Introduction algorithms]