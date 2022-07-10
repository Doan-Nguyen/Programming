package OOP;

public class Main {

    public static void main(String args[]){
        BanHang banHang = new BanHang();
        int n;
        Scanner scan = new Scanner(System.in);
        System.out.print("\t So san pham: n = ");
        n = scan.nextInt();
        banHang.ds = new SanPham[n];
        banHang.nhapTin();
        System.out.printf("\t %12s %10s %14s %14s", "Ten san pham", "So luong", "Gia ban", "Thanh tien");
        banHang.hienThi();
    }
}
