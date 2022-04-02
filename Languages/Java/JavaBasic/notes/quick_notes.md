# Content

+ **Notes**:
    - Phần 1 . Hướng đối tượng trong Java, mình tóm tắt trong cuốn "Giáo trình lập trình Java - Đoàn Văn Ban & Đoàn Văn Trung"

- [Contents](#contents)
- [1. Hướng đối tượng trong Java](#1_huong_doi_tuong_trong_Java)
- 

# 1. Hướng đối tượng trong Java

+ Lập trình hướng đối tượng: phân tích bài toán thành tập các thực thể (class). Sau đó xây dựng các dữ liệu thành phần & các hàm thành phần thao tác trên dữ liệu đó & trao đổi với những đối tượng khác để thực hiện yêu cầu của bài toán.

## 1.1 Lớp các đối tượng

+ **Đối tượng**: 
  - Thực thể xác định trong thời gian hệ thống hướng đối tượng hoạt động thông qua định danh **O**bject **ID**entifier.

+ Tập các đặc trưng của đối tượng gồm:
  - Các dữ liệu thành phần hoặc các thuộc tính mô tả tính chất
  - Các phương thức hoặc các thao tác trên dữ liệu

### 1.1.1 Định nghĩa lớp

+ **Lớp**: khuôn mẫu cho các đối tượng có những đặc trưng giống nhau về
  - Dữ liệu thuộc tính (Attribute data field)
  - Phương thức xử lý (methods)
  - Mối quan hệ với các đối tượng của lớp khác.

+ Các đối tượng được tạo ra từ class ~ *thể hiện của lớp (class instance)*
+ Trong LTHĐT, các lớp ~ kiểu dữ liệu trừu tượng (Abstract data type)
+ Khi định nghĩa một lớp, cần xác định *thuộc tính & phương thức*:
```
[modifier] class ClassName [extends AnyClass] [implements InterfaceList] {
        //    Khai bao bien thanh phan du lieu hay cac thuoc tinh
    [dac tinh truy cap] DataType varName;
    
        // dinh nghi ham toan tu tao lap doi tuong
    [public ClassName([ArgList]){
        // dinh nghia ham tao dung    
    }]
        
        // Khai bao hoac dinh nghia cac ham, phuong thuc
    [dac tinh truy cap] ReturnType methodName(paramList){
        // khai bao cac bien cuc bo
    }
}
```
  - **[modifier]**: Xac dinh pham vi cua lop {public, abstract, final}
  - **[dac tinh truy cap]**: xác định phạm vi truy cập của biến {public, protected, private, static, final}
  - **DataType**: kieu du lieu {int, float, long ...}
  - **varName**: ten cua bien du lieu.
  - **ReturnName**: xac dinh kieu tra lai ket qua tinh toan.
  - **methodName**: ten cua phuong thuc

### 1.1.2 Biến thành phần dữ liệu của lớp
+ Cú pháp: 

```[dac tinh truy cap] DataType varName [ = valueInit];```

+ Các đặc tính truy cập:

| Đặc tính truy cập  | Phạm vi của biến |
| -----------------  | ------- |
|     public         | Được nhìn thấy & truy cập **từ mọi nơi** |
|     private         | Được nhìn thấy & truy cập **trong cùng một lớp** |
|     default         | Được nhìn thấy & truy cập **giữa các lớp trong một package**   |
|     static         | Tự động khởi tạo giá trị mặc định khi tạo đối tượng. Có thể gọi qua tên lớp (sử dụng chung cho tất cả các đối tượng của lớp) |
|     final         | Khi tạo lập giá trị thì sẽ khhong thể thay đổi được  |


+ **DataType**: có 2 kiểu khai báo dữ liệu:
  - Primitive Type: byte, short, char, int ...
  - Kiểu tham chiếu: class, String, Integer,  IOException, ...

### 1.1.3 Phương thức của lớp

+ **Method**: 
  - Một hành động của object
  - Một tác vụ thực của object để xử lý dữ liệu
  - Trao đổi thông tin với các đối tượng khác

+ Cú pháp:
```
[dac tinh truy cap] DataType methodName([paramList]){
  // khai bao cac bien cuc bo
  // cac lenh thuc thi 1 nhiem vu
}
```

+ Đặc tính truy cập:

| Đặc tính truy cập  | Phạm vi của phương thức |
| -----------------  | ------- |
|     public         | Được nhìn thấy & truy cập **từ mọi nơi**. Tất cả các gói hoặc lớp khác  |
|     protected         | Được nhìn thấy & truy cập **ở các lớp con trong cùng một gói** hoặc tại **các lớp kế thừa** |
|     default         | Được nhìn thấy & truy cập **giữa các lớp trong một package**   |
|     private         | Được nhìn thấy & truy cập **trong một lớp**   |
|     static         | Tự động khởi tạo giá trị mặc định khi tạo đối tượng. Có thể gọi qua tên lớp (sử dụng chung cho tất cả các đối tượng của lớp) |


+ Datatype: tương tự như biến nhưng có thêm kiểu *void* ~ không có dữ liệu trả về.

+ Các loại phương thức thường dùng:
  - **Constructor**: khởi tạo đối tượng
    - Sử dụng toán tử *new* để khởi tạo các biến thành viên của một lớp
    - Được dùng khhi cần tạo ra đối tượng của lớp đó.
  - Phương thức nhập liệu
  - Phương thức truy cập dữ liệu
  - Phương thức cập nhật dữ liệu
  - Phương thức xử lý tính toán

## 1.2 Phạm vi & thuộc tính kiểm soát truy cập các thành phần của lớp

### 1.2.1 Phạm vi của các thành phần trong chương trình Java
+ Phạm vi xác định các thành phần trong chương trình chia thành:
  - Phạm vi lớp của các thành phần
  - Pham vi khối của các biến cục bộ

+ Phạm vi lớp:
  - Để xác định những thành phần được truy cập bên trong của một lớp & ở các lớp khác.
  - Quyền truy cập được xác định bằng *modifier* {public, protected, default or private}
  - Bên trong định nghĩa của lớp, các biến đc tham chiếu tới chính lớp đó & đc truy nhập tới các thành phần của nó (k quan tâm tới *modifier*)
  
+ Vi du:
  ```
  public class BongDen {
      protected int soWatts;
      private boolean batTat=false;
      private String viTri;
      //
      public void batDen(){batTat=true;}
      public void tatDen(){batTat=false;}
      public boolean checkDenSang(){return batTat;}
      //
      public BongDen nhanDoi(BongDen bongDenCu){
          BongDen bongDenMoi = new BongDen();
          bongDenMoi.soWatts = bongDenCu.soWatts;
          bongDenMoi.batTat = bongDenCu.batTat;
          bongDenMoi.viTri = new String(bongDenCu.viTri);
          return bongDenMoi;
      }
  }
  ```
  
  - _bongDenCu_ : tham biến
  - _bongDenMoi_ : biến cục bộ
  - => đều có thể truy cập đến các biến thành phần


+ Phạm vi khối
  - Các khối được định nghĩa, thực hiện trong {}
  - Một biến được định nghĩa trong khối => phạm vi xác định chỉ bên trong khối.

### 1.2.2 Các thuộc tính kiểm soát truy nhập các thành phần của lớp

+ Ưu điểm của OOP là có thể tổ chức dữ liệu theo nguyên lý đóng gói & che giấu thông tin.
  - Các thuộc tính & thành phần của lớp có thể khai báo thêm _modified_ để kiểm soát quyền truy nhập 
  
## 1.3 Truyền tham số vào các lời gọi hàm

## 1.4 Các tham số của chương trình

## 1.5 Phương thức tạo lập đối tượng

## 1.6 Sự kết thúc của đối tượng

## 1.7 Hàm đệ quy

## 1.8 Quan hệ giữa các lớp

## 1.9 Đa xạ & nạp chồng

## 1.10 Java swing

# 2. Cấu trúc dữ liệu cơ bản

# 3. Collections

# 4. Java 8 code

