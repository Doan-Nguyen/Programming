package OOP;

public class Point {
    private int x, y;
    //
    public Point(){};

    public Point(int x, int y){
        this.x = x;
        this.y = y;
    }

    public int getX(){ return this.x;}

    public void setX(int new_x){ this.x = new_x;}

    public int getY(){ return this.y;}

    public void setY(int new_y){ this.y = new_y;}

    public String toString(){
        return  String.format("(%d, %d)", this.x, this.y);
    }

    public void setXY(int new_x, int new_y){
        this.x = new_x;
        this.y = new_y;
    }

    public double distance(int x, int y){

    }


}
