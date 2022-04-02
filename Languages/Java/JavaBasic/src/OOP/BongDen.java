package OOP;

public class BongDen {
    protected int soWatts;
    private boolean batTat=false;
    private String viTri;
    //
    public void batDen(){batTat=true;}
    public void tatDen(){batTat=false;}
    public boolean checkDenSang(){return batTat;}
    //
    public BongDen nhanDoi(BongDen bongDenCu){
        BongDen bongDenMoi = new BongDen();
        bongDenMoi.soWatts = bongDenCu.soWatts;
        bongDenMoi.batTat = bongDenCu.batTat;
        bongDenMoi.viTri = new String(bongDenCu.viTri);
        return bongDenMoi;
    }
}
