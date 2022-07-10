**Note**: Tài liệu này mình tham khảo từ https://loda.me/articles/sb0-series-lam-ch-spring-boot-zero-to-hero

# 1. Khái niệm tight-coupling (liên kết ràng buộc) & cách loosely coupled

## Contetn without images

+ *tight-coupling* ~ liên kết ràng buộc: ám chỉ việc liên kết các classes quá chặt chẽ. Khi cần thay đổi logic hay một class sẽ ảnh hưởng tới toàn bộ các classes khác.
+ *loosely-coupled*: cách làm giảm bớt sự phụ thuộc giữa các class.

### Example 1:
```
public class BubbleSortAlgorithm{

    public void sort(int[] array) {
        // TODO: Add your logic here
        System.out.println("Đã sắp xếp bằng thuật toán sx nổi bọt");
    }
}


public class VeryComplexService {
    private BubbleSortAlgorithm bubbleSortAlgorithm = new BubbleSortAlgorithm();
    public VeryComplexService(){
    }

    public void complexBusiness(int array[]){
        bubbleSortAlgorithm.sort(array);
        // TODO: more logic here
    }
}
```

    - Các vấn đề dễ nhận thấy:
        - Khi cần thay đổi thuật toán sắp xếp, ta cần phải thay đổi class *VeryComplexService*
        - Thuật toán sắp xếp chỉ tồn tại nếu *VeryComplexService* tồn tại.

### Example 2: 
```
public interface SortAlgorithm {
    /**
     * Sắp xếp mảng đầu vào
     * @param array
     */
    public void sort(int array[]);
}

public class BubbleSortAlgorithm implements SortAlgorithm{

    @Override
    public void sort(int[] array) {
        // TODO: Add your logic here
        System.out.println("Đã sắp xếp bằng thuật toán sx nổi bọt");
    }
}

public class QuicksortAlgorithm implements SortAlgorithm {
    @Override
    public void sort(int[] array) {
        // TODO: Add your logic here
        System.out.println("Đã sắp xếp bằng thuật sx nhanh");

    }
}

public class VeryComplexService {
    private SortAlgorithm sortAlgorithm;
    public VeryComplexService(SortAlgorithm sortAlgorithm){
        this.sortAlgorithm = sortAlgorithm;
    }

    public void complexBusiness(int array[]){
        sortAlgorithm.sort(array);
        // TODO: more logic here
    }
}
```
    - *VeryComplexService* chỉ quan tâm đến *SortAlgorithm*, còn việc *SortAlgorithm* sử dụng thuật toán như thế nào tủy ý. 

## Dependency Injection (DI) & IoC

### Dependency Injection
+ Nó là một design pattern, giúp nâng cao hiệu quả code.

    - Example:
    ```
    public class BunDau{
        private NuocCham mamTom;
  
        public BunDau(){
            
        }
    }
    ```
  
  - Một mẹt bún đậu sẽ đi kèm với nước chấm => nước chấm tồn tại mang ý nghĩa **dependency** của bún đậu.
    - Bún đậu sẽ luôn được ăn kèm với 1 loại nước chấm nhưng có khách thích ăn muối vắt chanh hoặc chỉ ăn bún đậu
    - Giả sử, nước chấm hết/gặp vấn đề (có bug) sẽ ảnh hưởng đến món bún đậu.

+ Nguyên tắc:
```
Các class không nên phụ thuộc vào các kế thừa cấp thấp, mà nên phụ thuộc vào lớp trừu tượng (abstraction).
```

+ Example 1:
```
// Một interface cho việc ăn mặc
public interface Outfit {
  public void wear();
}

// Một object cấp thấp, implement của Outfits
public class Bikini implements Outfit {
  public void wear() {
    System.out.println("Đã mặc Bikini");
  }
}

// Bây giờ Girl chỉ phụ thuộc vào Outfit. nếu muốn thay đổi đồ của cô gái, chúng ta chỉ cần cho Outfit một thể hiện mới.
public class Girl{
    private Outfit outfit;
    public Girl(){
      outfit = new Bikini();
    }
}
```

+ Example 2:
```

```
