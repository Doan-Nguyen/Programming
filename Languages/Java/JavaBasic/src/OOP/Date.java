package OOP;

public class Date {
    private int year;
    private int month;
    private int day;
    //
    public Date(int input_year, int input_month, int input_day) {
        this.year = input_year;
        this.month = input_month;
        this.day = input_day;
    }

    public int getYear(){
        return this.year;
    }

    public int getMonth(){
        return this.month;
    }

    public int getDay(){
        return this.day;
    }

    public void setYear(int new_year){
        this.year = new_year;
    }

    public void setMonth(int new_month){
        this.month = new_month;
    }

    public void setDay(int new_day){
        this.day = new_day;
    }

    public String toString(){
        String output_str = this.month + "/" + this.day + "/" + this.year;
        return output_str;
    }

    public void setDate(int set_day, int set_month, int set_year){
        this.day = set_day;
        this.month = set_month;
        this.year = set_year;
    }
}

