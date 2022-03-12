import static java.lang.System.out;

//class PreincrementDemo{
//    public static void main(String args[]){
//        int numberOfBunnies = 10;
//        //
//        ++numberOfBunnies;
//        out.println(numberOfBunnies);
//        int tmp = numberOfBunnies++;
//        out.println(tmp);
//        out.println(numberOfBunnies);
//    }
//}


class UseAssignmentOperators{
    public static void main(String args[]){
        int numberOfBunnies = 10;
        System.out.println(numberOfBunnies -= 7);
        System.out.println(numberOfBunnies =  20);
    }
}