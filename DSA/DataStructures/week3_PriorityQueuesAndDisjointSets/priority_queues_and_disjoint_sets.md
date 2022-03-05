# Priority Queues and Disjoint Sets

# Contents
- [Priority Queues and Disjoint Sets](#priority-queues-and-disjoint-sets)
- [Contents](#contents)
  - [1. Priority Queues: Introduction <a name="priority_queues_introduction"></a>](#1-priority-queues-introduction-)
  - [2. Priority Queues: Heaps <a name="priority_queues_heaps"></a>](#2-priority-queues-heaps-)
    - [Binary Trees](#binary-trees)
    - [Basic operations](#basic-operations)
    - [Complete binary trees](#complete-binary-trees)
    - [Pseudo code](#pseudo-code)
    - [Heap sort](#heap-sort)
    - [Final Remarks](#final-remarks)
  - [3. Priority Queues: Heap Sort <a name="priority_queues_heap_sort"></a>](#3-priority-queues-heap-sort-)
  - [4. Disjoint Sets: Naive Implementations <a name="disjoint_sets_naive_implementations"></a>](#4-disjoint-sets-naive-implementations-)
  - [5. Disjoint Sets: Efficient Implementations <a name="disjoint_sets_efficient_implementations"></a>](#5-disjoint-sets-efficient-implementations-)


## 1. Priority Queues: Introduction <a name="priority_queues_introduction"></a>

+ **Queue**: an abstract data type supporting the following main operations:
    - PushBack(e): adds an element to the back of queue
    - PopFront(): extracts an element from the front of queue

+ **Priority Queues** (Hàng đợi ưu tiên): a generalization (khái quát hóa) of a queue where each element is assigned a priority and elements come out in order by priority.

    - Example: scheduling jobs
        - process jobs one by one in order of decreasing priority
        - to add a job to the set of scheduled jobs: Insert(job)
        - to process a job with the highest priority: ExtractMax()

+ **Definition**: priority queue is an abstract data type supporting the follwing main operations:
    - Insert(p): adds a new element with priority *p*
    - ExtractMax(): extracts an element with maximum priority

+ Additional operations
    - remove(it): removes an element pointed by an iterator *it*
    - getMax(): returns an element with maximum priority (without changing the set of elements)
    - changePriority(it, p): changes the priority of an element pointed by *it* to *p*.

+ Problem: 
    - *Dijkstra's algorithm*: finding a shortest path in a graph.
    - *Prim's algorithm*: constructing a minimum spanning tree of a graph.
    - *Huffman's algorithm*: constructing an optimum prefix-free encoding of a string.
    - *Heap sort*: sorting a given sequence.

+ **Naive implementations**


+ **Summary**

![priority_queues_intro_summary](./figures/priority_queues_intro_summary.PNG)

## 2. Priority Queues: Heaps <a name="priority_queues_heaps"></a>

### Binary Trees
+ **Binary max-heap**: a binary tree where the value of each node is at least the values of it's children. (giá trị giảm dần từ root -> leaf)

    - Example:
    
    ![example_binary_max_heap](./figures/example_binary_max_heap.PNG)

### Basic operations

+ *GetMax*: return the root value

    ![ex_get_max_binary_max_heap](./figures/ex_get_max_binary_max_heap.PNG)

+ *Insert*:
    - attach a new node to any leaf
    - this maybe violate (break with) the heap property

    ![ex_insert_binary_max_heap](./figures/ex_insert_binary_max_heap.PNG)

    => Solution: let the new node sift up.

+ *SiftUp*: swap the problematic node with it's parent until the property is satisfied.
    
    ![ex_siftup](./figures/ex_siftup.PNG)

    - running time: O(tree height)

+ *ExtractMax* and *SiftDown*: 
    - Replace the root with any leaf -> maybe violate the heap property.
    => solution: *SiftDown* swap the problematic node with larger child until the heap property is satisfied.


    ![ex_extract_max](./figures/ex_extract_max.PNG)


### Complete binary trees

### Pseudo code

### Heap sort

### Final Remarks
## 3. Priority Queues: Heap Sort <a name="priority_queues_heap_sort"></a>

## 4. Disjoint Sets: Naive Implementations <a name="disjoint_sets_naive_implementations"></a>

## 5. Disjoint Sets: Efficient Implementations <a name="disjoint_sets_efficient_implementations"></a>