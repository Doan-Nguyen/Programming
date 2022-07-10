package OOP;

public class Time {
    private int hour;
    private int minute;
    private int second;
    //
    public Time(){}
    //
    public Time(int second, int minute, int hour){
        this.second = second;
        this.minute = minute;
        this.hour = hour;
    }

    public int getHour(){
        return this.hour;
    }

    public int getMinute(){
        return this.minute;
    }

    public int getSecond(){
        return this.second;
    }

    public void setTime(int new_second, int new_minute, int new_hour){
        this.second = new_second;
        this.minute = new_minute;
        this.hour = new_hour;
    }

    public Time nextSecond(){
        /*
        if second 60:
        if minute 60
        if hour 12
         */
        second ++;
        if (second >= 60){
            second = 0;
            minute ++;
            if (minute >= 60){
                minute = 0;
                hour ++;
                if (hour >= 23){
                    hour = 0;
                }
            }
        }
        //
        return this;
    }

    public String toString(){
        return String.format("%02d:%02d:%02d", hour, minute, second);
    }
}
