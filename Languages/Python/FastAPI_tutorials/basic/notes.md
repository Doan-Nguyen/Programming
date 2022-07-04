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

+ API endpoint: là điểm thực hiện kết nối các chương trình phần mềm với nhau. Cách thực hoạt động của API gửi yêu cầu thông tin từ web tới máy chủ web & nhận phản hồi trở lại.
    + Với việc khởi tạo FastAPI object, nó đảm nhiệm vai trò kết nối tất cả các tuyến API.
    + *path operation function*: 
    + *decorator*: 

+     

#### Handling request parameters

+ Path parameters

+ Query parameters

+ The request body

+ Form data & file uploads 

+ Headers & cookies 

+ The request object

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
