# Tổng hợp các notes về C++
## 1. C++ Overview
+ Definition: C++ is a statically typed, compiled, general-purpose, case-sensitive, free-form programming language that support procedural, object-oriented and generic programming.
    - Statically typed (định kiểu dữ liệu tĩnh): ngôn ngữ lập trình xác định các kiểu dữ liệu vào thời điểm dịch.
    - Biên dịch (complied): ngôn ngữ phải qua một bộ dịch (complier) trước khi trở thành chương trình mà hệ điều hành có thể đọc được.
    - General-purpose (đa chức năng)
    - Free-form (đa hình): 
    - Case-sensitive 
    - Procedual programming (lập trình thủ tục): chương trình xử lý các thủ tục từ trên xuống dưới.
    - Object oriented programming: object include data + method.
    - Generic programming: khả năng lập trình cho phép đặt các kiểu dữ liệu sẽ được xác định về sau trong thuật toán.

+ Standard libraries
    - The core language: all the building blocks including variables, data types & literal
    - The C++ Standard library (std): set of functions manipulating files, strings ...
    - The Standard Template Library (STL): set of method manipulating data structures (set, vector, map)...

## 2. C++ Basic
### 2.1 Overview 
+ C++ program can be defined as a collection of objects that communicate via invoking each other's methods.
    - Object: have states & behaviors.
    - Class: define the behaviors and states of objects
    - Methods
    - Instance variables

### 2.2 Compound data types
#### 2.2.1 Array
+ An array is a series of elements of the same type placed in contigous memory locations that can be individually rereferenced by adding an index to a unique identifier.
+ A typical declaration:
    ```
    type name [elements];
    ```
    - **Note**:
        - The elements field within [], representing the number of elements in the array, *must be* a constant expression. The array's size must be determined at compile time before the program runs.

    - In order to reduce the number of variables define, we use array.
    - Initialize an array:
        ```
        type_data array_name[n] = {elem_1, elem_2, ..., elem_n};
        ```
    - Initialize an array multiples-dimension:
        ```
        type_dat array_name[dimension_1][dimension_2];
        ```
    - Access into a cell by index:
        ```
        array_name[row_indx][col_indx];
        ```
