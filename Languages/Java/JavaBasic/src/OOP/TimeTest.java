package OOP;

public class TimeTest {
    public static void main(String[] args){
        Time t1 = new Time(1, 2, 3);
        System.out.println(t1.toString());
        //
        t1.setTime(58, 59,23);
        System.out.println(t1.nextSecond());
        System.out.println(t1.nextSecond().nextSecond());
        System.out.println(t1.nextSecond().nextSecond().nextSecond());
    }
}
