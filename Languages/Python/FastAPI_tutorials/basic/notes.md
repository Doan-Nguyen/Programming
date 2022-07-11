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
      + Example: [request_body](https://github.com/Doan-Nguyen/Programming/blob/main/Languages/Python/FastAPI_tutorials/basic/src/c3_request_body_02.py)


+ **Form data & file uploads**
  + REST APIs thường sẽ làm việc với dạng file JSON nhưng đôi khi bạn cần xử lý dữ liệu dạng mã hóa (form-encode data) hoặc các upload files. Chúng thường được mã hóa bởi:
    + *application/x-www-form-urlencoded*
    + *multipart/form-data*: **Need more details**

  + *Form data*:
    + Dữ liệu được mã hóa thay vì để dạng JSON.
    + Example: 

  + *File uploads*:
    + FastAPI cung cấp *File()* thực hiện việc upload file.
      + Example: 
    + Nhược điểm: 
      + Với phương thức này, file tải lên sẽ lưu trữ hoàn toàn trong bộ nhớ. Khả năng xảy ra vấn đề khi gặp file có kích thước lớn.
      + Thao tác với đối tượng byte không phải lúc nào cũng thuận tiện cho xử lý.
      + **Solution**: FastAPI cung cấp lớp **UploadFile**.
        + Class này sẽ chỉ lưu trữ các file trong memory đến 1 ngưỡng. Nếu vượt qua, dữ liệu sẽ được lưu trữ ở một vị trí tạm thời trong ổ cứng.
        + Example: 

+ **Headers & cookies**
  + *headers*: là một trong những thành phần chính của HTTP requests bên cạnh URL, body.
    + Chúng gồm toàn bộ các loại metadata có thể được sử dụng trong quá trình xử lý requests.
    + Một cách sử dụng phổ biến của nó là xác thực (authentication) - *cookies*
    + FastAPI tự động chuyển header name dạng chữ thường (lowercase)
    + **More details**: 
      + HTTP requests:
      + cookies:
      + Example:       
    + ? Bạn có thể nhận cookies thông qua việc phân tích header. Với FastAPI cung cấp tham số hàm giúp tự động hóa việc này.
      + Example: 
      + Bằng cách này, ngay cả khi cookies không được yêu cầu, FastAPI vẫn sẽ tạo ra cookie & không tạo lỗi trạng thái 422.

+ **The request object**



#### Customizing the reponse
+ Ở các phần trước, chúng ta đã học cách trả về dạng *dictionary* hoặc pydantic object phục vụ cho FastAPi trả về 1 JSON respone. Phần này, ta sẽ tìm hiểu cách thức để tùy biến response thêm chút nữa như thay đổi status code, raising các lỗi xác nhận & thiết lập cho cookies.

+ **Path operation parameters**
  + Ở các phần trước, ta đã học để tạo ra một *endpoint* cần đặt một *decorator* ở đầu mỗi hàm đường dẫn hoạt động. Với mẫu thiết kế *decorator*, ta có thể tùy biến response.

  + HTTP status code: mã code server trả về sau mỗi lần gửi request. Tất cả các request đều được nhận được 1 status code tương ứng.
    + *status_code*: được coi như keyword đối số (argument) được truyền vào sau *path operation*. Thể hiện status code mong muốn được phản hồi, thậm chí ghi đè trạng thái được phản hồi (không khuyến khích). Tưởng tượng, bạn làm 1 hành động nhưng không trả lại gì (vd: xóa 1 bức ảnh). Khi đó, bạn mong muốn trạng thái trả về nên là "204 No content".
      + *Setting the status code dynamically*: ta sẽ tìm hiểu cách tùy biến status code bên trong *path operation* logic.
      + Example: 
      

    + *response model*: 
      + Với FastAPI, trường hợp thường xảy ra sẽ trả về một *pydantic model*. Nó tự động được chuyển thành dạng JSON. Đôi khi, bạn cần có sự thay đổi giữa input data, data được lưu trong DB & data show cho end-user.
      + Example: bạn cần có 1 DB bao gồm các blog posts. Chúng có vài thuộc tính: title, content, ngày tạo, số views. 
      + Example: 
      + Giả sử, bạn không muốn show số views. Sử dụng thêm: *response_model* sau *path operation*.
      + Example: 

+ The response parameter
  + Ngoài body & status code, đôi khi ta cần gửi headers hoặc set cookies (Response object) thông qua path operation function như các đối số của hàm.
  

  + **Setting headers**: 
    + *Response* cho phép truy xuất tới các đặc tính, bao gồm cả *headers*. Nó là một dictionary đơn giản với key - tên của header, value - giá trị tương đương với header.
    + Bạn không nhất thiết phải trả lại *Response object*, có thể trả lại JSON-encodable data & FastAPI sẽ thực hiện việc hình thành response thích hợp, bao gồm *headers*.

  + **Setting cookies**:
    + *cookies*: là file tạm được tự động tạo ra khi end-user truy cập web. Nó sẽ lưu những thông tin phục vụ cho những lần đăng nhập sau.
    + Ta có thể build cặp *Set-Cookie* & đặt nó như 1 *headers* dictionary thông qua việc sử dụng *set_cookie()*.
    + Example: 
      + *max_age*: sau khoảng thời gian (ms) này, brower sẽ xóa cookie
      + *set_cookie()*: hỗ trợ cho cả instance, path, domain, HTTP-only.

  + **Setting the status code dynamically**:
    + Ở mục *Path operation parameters*, chúng ta đã thử set mã trạng thái cho 1 response. Hạn chế của phương pháp này là nó sẽ thông báo như nhau cho các vấn đề xảy ra bên trong.
    + Giả sử, ta có 1 *endpoint* thực hiện update một đối tượng trong database hoặc sẽ tạo ra nó nếu như chưa tồn tại. Hướng tiếp cận đúng nên:
      + HTTP sẽ phản hồi *200 - OK* khi update thành công.
      + HTTP sẽ phản hồi *201 - Created* khi create thành công.
    + Giải pháp: sử dụng *status_code* trong *Response* object.
      + Example: c3_response_parameters_03.py

  + **Raising HTTP errors**
    + Khi gọi đến REST API một cách thường xuyên, đôi khi hệ thống sẽ gặp những vấn đề. Có thể là tham số truyền vào sai, các trọng tải không hợp lệ hoặc object không tồn tại ... Vì đó, việc phát hiện ra issues trọng & việc thông báo đến lập trình viên 1 cách rõ ràng là vô cùng quan. Hai thông tin này được sử dụng để trả về: 
      + status code: đưa ra gợi ý về bản chất lỗi.
      + payload: 

    + Để đưa ra các HTTP's issues, ta sẽ đưa ra các Python's exception (HTTPException). Từ các exceptions, ta có thể thiết lập *status code* & *error message*.
      + Example: 

  + **Building a custom response**
    + Trong hầu hết trường hợp, FastAPI sẽ đảm nhiệm việc xây dụng HTTP response bằng việc cung cấp cho nó một vài dữ liệu tuần tự. Một cách gián tiếp, FastAPI sử dụng **JSONResponse** - 1 sub-class của _Response_. Class này thực hiện:
      + Xử lý dữ liệu một cách tuần tự vào file JSON
      + Thêm cặp _Content-Type_ header.
    + Tuy nhiên, có một vài response classes cũng thực hiện các việc tương tự
      + HTMLResponse: trả về một HTTP response
      + PlainTextResponse: trả về một trường text
      + ...
    + Từ đó, ta có 2 cách để sử dụng chúng:
      + (1): thiết lập _response_class_ như một đối số truyền vào *path decorator*
      + (2): trả về trực tiếp một _response_
    
    + Sử dụng đối số _response_class_:
      + Đơn giản, ta chỉ trả về dữ liệu dạng tiêu chuẩn JSON responses. 
      + Example: 
    + Tạo một sự chuyển hướng
      + *RedirectResponse*: class thực hiện việc xây một HTTP hướng ~
    + Serving a file
    + Custom response

#### Structuring a bigger project with multiple routers
  + Với hệ thống lơn, ta nên sắp xếp cấu trúc source như sau: 
    + models\
      + 
    + routers\: thường dùng riêng cho loại đối tượng. Vd: posts, users ...
    + __init__.py
    + app.py
    + db.py


### 4. Managing Pydantic Data Models in FastAPI

#### Defining models & their field types with Pydantic

+ Standard field types

+ Optional fields & default values

+ Field validation

+ Validating emails addresses & URLs with Pydantic types

#### Creating model variations with class inheritance

#### Adding custom data validation with Pydantic

+ Applying validation at a field level

+ Applying validation at an object level 

+ Applying validation before Pydantic parsing

#### Working with Pydantic objects

+ Converting an object into a dictionary 

+ Creating an instance from a sub-class object

+ Updating an instance with a partial one

### 5. Dependency Injections in FastAPI

#### What is dependency injection ?

#### Creating & using a function dependency

#### Creating & using a parameterized dependency with a class

#### Using dependencies at a path, router & global level


## Section 2: Build & Deploy a Complete Web Backend with FastAPI

### 6. Databases and Asynchronous ORMs

### 7. Managing Authentication & Security in FastAPI

### 8. Defining WebSockets for Two-Way Interactive Communication in FastAPI

### 9. Testing an API Asynchronously with pytest and HTTPX

### 10. Deploying a FastAPI Project

## Section 3: Build a Data Science API with Python & FastAPI
