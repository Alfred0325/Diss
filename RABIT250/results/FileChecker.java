package results;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class FileChecker {

    public static void main(String[] args) {
        String searchStr = "InCorrect! The calculated parallel result is different from the Original result!";
        String filePath = args[0];
        Boolean flag = true;

        try (BufferedReader br = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (line.contains(searchStr)) {
                    flag = false;
                    System.out.println("Incorrect!! PLease check your results!");
                    return;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        if (flag){
            System.out.println("All correct!! Great!!");
        }
    }
}

