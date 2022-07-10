package OOP;

import java.util.Scanner;

public class PhienBanHang {

    SanPham ds[];

    public void nhapTin(){
        for (int i = 0; i < ds.length; i++){
            ds[i].nhapTin();
        }
    }

    public void hienThi(){
        for (int i = 0; i < ds.length; i++){
            ds[i].hienThi();
        }
    }

    public void sapXep(){
        for (int i = 0; i < ds.length - 1; i++){
            for (int j = i + 1; j < ds.length; j++){
                if (ds[j].numbItems < ds[i].numbItems){
                    int numb_tmp = ds[j].numbItems;
                    ds[j].numbItems = ds[i].numbItems;
                    ds[i].numbItems = numb_tmp;
                }
            }
        }
    }

    public static void main(String args[]){
        Scanner scan = new Scanner(System.in);
        //
        PhienBanHang phienBanHang = new PhienBanHang();
        System.out.println("So luong san pham ban duoc: ");
        int numb_sell = Integer.valueOf(scan.nextLine());
        //
        phienBanHang.ds = new SanPham[numb_sell];
        for (int i=0; i < numb_sell; i++){
            phienBanHang.ds[i] = new SanPham();
        }
        //
        System.out.println("--- Nhap vao cac san pham da ban duoc: ");
        phienBanHang.nhapTin();
        System.out.println("--- Cac san pham da ban duoc truoc khi sap xep: ");
        phienBanHang.hienThi();
        System.out.println("--- Sap xep theo thu tu giam dan: ");
        phienBanHang.sapXep();
    }
}
