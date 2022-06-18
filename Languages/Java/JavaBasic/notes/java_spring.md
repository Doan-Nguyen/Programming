# [Core1] Dependency Injection (DI) and IoC

+ Dependency Injection (sự truyền vào các phụ thuộc): là một phương pháp lập trình.
    - các class không nên phụ thuộc vào các kế thừa cấp thấp, mà nên phụ thuộc vào Abstraction (lớp trừu tượng)
    - Việc thể hiện chi tết của nó sẽ được Inject vào đối tượng lúc runtime.

+ Các cách để *Inject dependency* vào một đối tượng cụ thể:
    - **Constructor Injection**: truyền dependency ngay vào *Constructor*
    - **Setter Injection**: 
    - **Interface Injection**: 

+ Inversion of Control
    - Chúng ta thực hiện khai báo toàn bộ các *dependency* rồi truyền vào một *container* & giao cho *framework* quản lý.
    - Khi 1 class nào đó khởi tạo, *framework* sẽ tìm các *dependency* cần thiết rồi *inject - tiêm* vào đối tượng.

# [SP1] @Component & @Autowired

+ Trong java spring:
    - Container ~ ApplicationContextt
    - Dependency ~ Bean

## @Component
+ Là một *Annotation ~ chú thích* đánh dấu trên các *class* để Spring nhận biết đó là một *Bean*

+ Spring Boot: khi chay se do tim toan bo cac class cung cap hoac trong cac package thap hon. Tim cac class *@Component* & tao ra mot instance roi dua vao *ApplicationContext* de quan ly.

## @Autowired 

+ Spring Boot sẽ tự động *inject* một instance của *Outfit* vào thuộc tính này khi khởi tạo *Girl*
  - 


## Singleton

+ Các *Bean* được quản lý trong *ApplicationContext* đều là singleton:
  - Singleton: 




