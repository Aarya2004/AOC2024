import java.util.ArrayList;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

class Day2{

    public static ArrayList<ArrayList<Integer>> getInput(String filePath) throws FileNotFoundException{
        File inFile = new File(filePath);
        ArrayList<ArrayList<Integer>> inp = new ArrayList<ArrayList<Integer>>();
        Scanner sc = new Scanner(inFile);
        while (sc.hasNextLine()){
            String line = sc.nextLine();
            String nums[] = line.split(" ");
            ArrayList<Integer> lineNums = new ArrayList<Integer>();
            for(int i = 0; i < nums.length; i++){
                lineNums.add(Integer.valueOf(nums[i]));
            }
            inp.add(lineNums);
        }
        sc.close();
        return inp;
    }
    public static void main(String[] args) {
        String filePath = "../inputs/examples/day2.txt";
        ArrayList<ArrayList<Integer>> inp = null;
        try{
            inp = getInput(filePath);
        }catch (Exception e){
            if ( e instanceof FileNotFoundException ){
                System.err.println("Fatal: Invalid file path");
                System.exit(1);
            }
            System.err.println("Fatal: Unknown Error: " + String.valueOf(e));
            System.exit(2);
        }
        if(inp == null){
            System.err.println("Fatal: Unknown Error:");
            System.exit(3);
        }
        System.out.println(inp);
    }
}