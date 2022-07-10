package HitRate;
import java.io.*;
import org.json.*;


public class HitRate {
    private int das_gate;
    private int das_num;
    private int line_num;
    private int order_num;

    public static JSONObject obj;
    /*      utils           */
    public static String readJsonFile(String jsonPath, String key){
        String questionsArray = "";
        try (FileWriter file = new FileWriter(jsonPath)) {
            obj = new JSONObject( fileToString(jsonPath) );
            questionsArray = obj.getString(key);
        } catch (IOException | JSONException e) {
            e.printStackTrace();
        }
        return questionsArray;

    }

    private static String fileToString(String fileName){
        String str = "";
        try {
            InputStream is = new FileInputStream(fileName);
            BufferedReader buf = new BufferedReader(new InputStreamReader(is));

            String line = buf.readLine();
            StringBuilder sb = new StringBuilder();

            while (line != null) {
                sb.append(line).append("\n");
                line = buf.readLine();
            }

            String fileAsString = sb.toString();

            return fileAsString;

        } catch(Exception e){
            System.out.println("Error");
        }

        return str;
    }

    static void main(){
        String output = readJsonFile("./output_optimize.json", "picking");
        System.out.println(output);
    }
}
