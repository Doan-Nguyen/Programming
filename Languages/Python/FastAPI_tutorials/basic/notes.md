# Building Data Science Applications with FastAPI

## Section 1: Introduction to Python & FastAPI

### 1. Python Development Environment Setup

+ Technical requirements

+ Installing a Python distribution using pyenv

+ Creating a Python virtual environment

  - command lines:
    ```
    python3.7 -m venv fastapi_env
    source ./fastapi_env/bin/activate
    ```

+ Installing Python packages with pip
  - command lines:
    ```
    pip install --upgrade pip
    pip install fastapi uvicorn[standard]
    ```

+ Installing the HTTPie command-line utility
  - command lines:
    ```
    pip install --upgrade pip wheel
    pip install httpie
    ```

### 2. Python Programming Specificities

+ Basics of Python programming
  + Check whether two variables are the same
    ```
    >>> a is b
    ```

+ List comprehensions & generators

+ Classes & objects

+ Type hinting & type checking with *mypy*
  + type annotations (version 3.5+):
  ```
    def greeting(name: str) -> str:
  ```

  + Using *mypy* to perform a type check:
    ```
    pip install mypy
    ```

+ Asynchronous I/O
  + Khi có nhiều request, Flask hoặc Django sử dụng cơ chế Web Server Gateway Interface (WSGI) để tạo ra một vài *worker*. Nếu có 1 request lớn được gửi đến, một worker chưa trả lời xong. Các workers khác sẽ đảm nhiệm vai trò trả lời các requests khác được gửi lên.
  + Với Asynchronous I/O, một process sẽ không bị *block* khi đang bận xử lý một request dài. Nó vẫn có thể trả lời các requests khác.
  + So sánh Web Server Gateway Interface (WSGI) & Asynchronous Server Gateway Interface:
    + Giống:
      + Chúng đều có thể coi như cầu nối giữa _Web Server_ & _Web Application_
      + Xử lý các requests gửi từ client tới API
    + Khác:
      + Với WSGI, các requests được xử lý một cách tuần tự. Xong request này sẽ được chuyển sang request khác.

      [Cơ chế xử lý của WSGI](https://d226lax1qjow5r.cloudfront.net/blog/blogposts/how-pythons-wsgi-vs-asgi-is-like-baking-a-cake/screen-shot-2021-11-16-at-2.10.14-pm.png)
      + ASGI được cái tiến so với WSGI. Các request không phải đợi được xử lý xong mới chuyển sang xử lý request khác.

      [Cơ chế xử lý của ASGI](https://d226lax1qjow5r.cloudfront.net/blog/blogposts/how-pythons-wsgi-vs-asgi-is-like-baking-a-cake/screen-shot-2021-11-16-at-2.10.24-pm.png)

  + FastAPI dựa trên cơ chế ASGI để cải thiện hiệu suất. Bằng cách đặt *async* keyword trước function sử dụng:
     ```
     async def main():
     ```
  +

### 3. Developing a RESTful API with FastAPI

+ Target:
  + Creating the first endpoint & running it locally
  + Handling request parameters
  + Customizing the respone
  + Structuring a bigger project with multiple routers

#### Creating the first endpoint & running it locally

+ API endpoint: là điểm thực hiện kết nối các chương trình phần mềm với nhau. Cách thuc hoạt động của API gửi yêu cầu thông tin từ web tới máy chủ web & nhận phản hồi trở lại.
  + Sau khi khởi tạo FastAPI object, nó đảm nhiệm vai trò kết nối tất cả các tuyến API.
  + *path operation function*:
  + *decorator*: là một mẫu thiết kế sẽ linh động trong việc thay đổi tính chất của đối tượng khi chương trình vẫn đang chạy.
    + Chúng ta sẽ sử dụng *decorator* khi chạy ứng dụng trong FastAPI với keyword "--reload"


#### Handling request parameters

+ Mục tiêu chính của REST API là cung cấp phương pháp có hệ thống trong việc tương tác với dữ liệu.
  + FastAPI cho phép người dùng định nghĩa toàn bộ tham số một cách rõ ràng thông qua khả năng tự động nhận chúng từ các _request_ & áp dụng việc xác nhận dựa trên gợi ý.

+ **Path parameters**

  + Người dùng cuối sẽ tương tác với đường dẫn API.
  + Mỗi đường dẫn API sẽ là định danh duy nhất mà người dùng tác động.
  + FastAPI sử dụng *type hint* nhằm tăng tính nhận dạng của các parameters đầu vào.

  + Limiting allowed values ~ giới hạn các giá trị cho phép
    + Trong python, class *Enum* dùng để liệt kê các giá trị hợp lệ cho một loại dữ liệu cụ thể.
    + Ví dụ: Enum class dưới đây sẽ liệt kê các kiểu người dùng cho hệ thống:
    ```
    from enum import Enum
    from fastapi import FastAPI 
    
    class UserType(str: Enum):
      STANDARD = 'standard'
      ADMIN = 'admin'
    ```
    
  + Advanced validation ~ xác thực nâng cao
    + Chúng ta có thể thực hiện thêm một bước nhằm nâng cao các quy tắc xác thực. Cụ thể ở đây là kiểu dũ liệu strings & numbers. Giả sử, type hint (~ cú pháp tiêu chuẩn để chú thích kiểu dữ liệu đầu vào & đầu ra.)
    
+ **Query parameters**
  + Là phương pháp giúp thêm các tham số động cho 1 URL. Các tham số này có thể dùng để phân trang, một bộ lọc hoặc việc lựa chọn các trường cần thiết.
  + Chúng được sử dụng với cú pháp như tham số đường dẫn *path parameters*. Ngoài ra, chúng được coi như các thành phần bổ sung, phụ trợ.

+ **The request body**
  + *body*: là đường dẫn của HTTP request. Nó có thể bao gồm: 
    + raw data
    + documents
    + files 
    + biểu mẫu 
  + Request body thường được mã hóa (encoded) dạng file JSON & dùng để tạo ra đối tượng có cấu trúc đưa vào database.
    + Kiểu đơn giản nhất, việc nhận data từ body hoàn toàn giống như với query parameters.
    + Việc định nghĩa mỗi tham số với *type hint* bởi hàm *Body* sẽ không cần thiết lập giá trị mặc định.
    + Nhưng cách thức này vẫn tồn tại nhiều hạn chế:
      + Dài dòng khi gặp những models lớn.
      + Khả năng tái sử dụng CTDL kém.
    + **Solution**: pydantic model
      + Example: 
      

+ **Form data & file uploads**

+ **Headers & cookies**

+ **The request object**

#### Customizing the reponse

+ Path operation parameters

+ The reponse parameters

+ Raising HTTP errors

+ Building a custom response


### Managing Pydantic Data Models in FastAPI

#### Defining models & their field types with Pydantic

+ Standard field types

+ Optional fields & default values

+ Field validation

+ Validating emails addresses & URLs with Pydantic types

#### Creating model variations with class inheritance

#### Adding custom data validation with Pydantic

+ Applying validation at a field level


### 4. Managing Pydantic Data Models in FastAPI

### 5. Dependency Injections in FastAPI

## Section 2: Build & Deploy a Complete Web Backend with FastAPI

### 6. Databases and Asynchronous ORMs

### 7. Databases and Asynchronous ORMs

### 8. Defining WebSockets for Two-Way Interactive Communication in FastAPI


### 9. Testing an API Asynchronously with pytest and HTTPX

### 10. Deploying a FastAPI Project

## Section 3: Build a Data Science API with Python & FastAPI
