# Object-Oriented Programming Basics

## 1. Why OOP ?

+ Khắc phục các vấn đề:
  - *class*: Có thể coi như 1 bản vẽ hay 1 khuôn mẫu để tạo ra các objecsts. Nó đóng gói 2 đặc trưng:
    - Static properties
    - Dynamic operations
  - Ngoài ra, nó chỉ định sự tương tác với các class khác & tăng khả năng tái sử dụng.
  - **OOP = Data structures + Algorithms**

## 2. OOP in Java

### 2.1 Class & Instances
+ *Class*: như 1 bản vẽ mô tả các đối tượng bằng các thuộc tính tĩnh & hoạt động chính của nó.

+ *Instance*: có thể coi như 1 thực thể cụ thể từ class

### 2.2 A Class is 3-Compartment Box Encapsulating Data & Operations

+ Một class có thể được mô phỏng bằng 3 khối thành phần:
  - **Name**: định danh class
  - **Static Attributes**: (thuộc tính tĩnh) được thể hiện thông qua các biến.
  - **Dynamic Behaviors**: (hành vi động) được thể hiện thông qua các hàm.

### 2.3 Class Definition in Java

+ Cú pháp:
```
[AccessControlModifier] class ClassName{

    // class body contains members (variables & methods)
}
```

### 2.4 Creating Instances of a Class

+ Để tạo ra 1 *instance* của một class:
  - **Declare**: Khai báo một định danh cho 1 instance từ 1 class cụ thể.
  - **Construct**: khởi tạo một instance bằng việc sử dụng *new*.
  - Nếu 1 instance được khai báo nhưng k đc khởi tạo sẽ được khởi tạo giá trị mặc định *null*.

### 2.5 Dot (.) operator

+ Các biến & hàm thuộc class thường được gọi là biến thành phần & hàm thành phần. Để tham chiếu tới một thành phần của class:
  - Bước 1: Xác định instance (~ thực thể) cần dùng.
  - Bước 2: Sử dụng toán tử (.) để tham chiếu tới các thành phần của tham chiếu bước 1.

+ Cú pháp:
```
anInstance.a_variable;
//      or
anInstance.a_method();
```

### 2.6 Member variables
+ Một biến thành phần cần có tên (*identifier*) và kiểu dữ liệu (*type*). Có thể gán biến đó 1 giá trị cụ thể.

+ Cú pháp:
```
[AccessControlModifier] type variableName [= initialValue];
// or
[AccessControlModifier] type variableName_1 [= initialValue_1] [,  variableName_2 [= initialValue_2]];
```

+ Variable Naming Convention: các **biến** nên là **danh từ**.


### 2.7 Member Methods
+ Một hàm:
  - Nhận các tham số đầu vào.
  - Thực hiện các lệnh được định nghĩa trong thân hàm.
  - Trả về kết quả hoặc không nếu là hàm kiểu void.

+ Cú pháp:
```
[AccessControlModifier] returnType methodName ([parameterList]){
    // method body or implementation
}
```

+ Method Naming Convention: tên **hàm** nên là **động từ + danh từ** (thể hiện rõ **1 chức năng** của hàm).

### 2.8 Putting them Together: An OOP Example

### 2.9 Constructors

+ *constructor*: một hàm cùng tên với class. Được sử dụng để **construct** & **initialize** các biến thành viên của class.
  - sử dụng toán tử *new* để gọi tới một hàm *constructor*

+ Một hàm khởi tạo khác với các hàm khác ở các khía cạnh:
  - Tên hàm khởi tạo trùng với tên của class.
  - Hàm khởi tạo không có kiểu dữ liệu trả về.
  - Các hàm tạo sẽ k được kế thừa.

### 2.10 Revisit Method Overloading

+ Hàm

## 3. More Examples on Classes