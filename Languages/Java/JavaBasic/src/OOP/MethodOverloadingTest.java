public class MethodOverloadingTest{
    public static int average(int n1, int n2){
        return (n1 + n2)/2;
    }

    public static double average(double n1, double n2){
        return (n1 + n2)/2;
    }

    public static void main(String[] args){
        System.out.println(average(1.0, 2.0));
    }
}	
