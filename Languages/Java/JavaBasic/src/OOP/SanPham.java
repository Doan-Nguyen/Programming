package OOP;

import java.util.Scanner;

public class SanPham {
    private String nameItem;
    public int numbItems;
    private float costVal;

    public SanPham(){}

    public void nhapTin(){
        Scanner scan = new Scanner(System.in);
        System.out.print("Nhap ten san pham: ");
        nameItem = scan.nextLine();
        System.out.print("So luong: ");
        numbItems = Integer.valueOf(scan.nextLine());
        System.out.print("Gia ban: ");
        costVal = Float.valueOf(scan.nextLine());
    }

    public void hienThi(){
        System.out.println("\t Item: " +  nameItem + " , number of item: " +  numbItems + " , cost of item:" + costVal + " , Total cost: " + totalCost());
    }

    public float totalCost(){
        return numbItems*costVal;
    }

//    public static void main(String args[]){
//        BanHang banHang = new BanHang();
//        int n;
//        Scanner scan = new Scanner(System.in);
//        System.out.println("So san pham n: ");
//        n = Integer.valueOf(scan.nextLine());
//        banHang.ds = new SanPham[n];
//        banHang.nhapTin();
//        banHang.hienThi();
//    }
}

class BanHang{
    SanPham ds[];

    public void nhapTin(){
        for (int i = 0; i < ds.length; i++){
            System.out.println("\t --- San pham thu: " + (i + 1));
            ds[i] = new SanPham();
            ds[i].nhapTin();
        }
    }

    public void hienThi(){
        for (int i = 0; i < ds.length; i ++){
            ds[i].hienThi();
        }
    }


}
