import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.Arrays;
import java.lang.Math;
import java.util.HashMap;
import java.util.ArrayList;


class Day1{

    public static ArrayList<Integer> getInput(String file_path) throws FileNotFoundException{
        File inFile = new File(file_path);
        ArrayList<Integer> inp = new ArrayList<Integer>();
        Scanner sc = new Scanner(inFile);
        while (sc.hasNextLine()){
            String line = sc.nextLine();
            String nums[] = line.split("   ");
            inp.add(Integer.valueOf(nums[0]));
            inp.add(Integer.valueOf(nums[1]));
        }
        sc.close();
        return inp;
    }

    public static void loadLists(int[] list1, int[] list2, ArrayList<Integer> inp){
        for(int i = 0; i < inp.size(); i=i+2){
            int lIdx = (int)i/2;
            list1[lIdx] = inp.get(i);
            list2[lIdx] = inp.get(i+1);
        }
    }

    public static void printList(int[] list){
        System.out.print('[');
        for(int i = 0; i < list.length; i++){
            System.out.print(list[i]);
            if(i != list.length - 1) System.out.print(",");
        }
        System.out.print("]\n");
    }

    public static void part1(int[] list1, int[] list2){
        int sum = 0;
        for(int i = 0; i < list1.length; i++){
            sum += Math.abs(list1[i] - list2[i]);
        }
        System.out.println(sum);
    }

    public static void part2(int[] list1, int[] list2){
        HashMap<Integer, Integer> map = new HashMap<Integer,Integer>();
        for(int i = 0; i < list2.length; i++){
            if(map.containsKey(list2[i])){
                int freq = map.get(list2[i]);
                map.replace(list2[i], freq, freq+1); 
            }else{
                map.put(list2[i], 1);
            }
        }
        // map.forEach((k, v) -> {System.out.println(Integer.toString(k) + ":" + Integer.toString(v));});
        int sum = 0;
        for (int i = 0; i < list1.length; i++){
            sum += list1[i] * map.getOrDefault(list1[i], 0);
        }
        System.out.println(sum);
    }

    public static void main(String[] args) {
        String file_path = "/Users/aaryaprakash/Desktop/Code/AOC2024/brute_force/inputs/examples/day1.txt";
        ArrayList<Integer> inp = null;
        try{
            inp = getInput(file_path);
        }catch (Exception e){
            if ( e instanceof FileNotFoundException ){
                System.err.println("Fatal: Invalid file path");
                System.exit(1);
            }
            System.err.println("Fatal: Unknown Error");
            System.exit(2);
        }
        if(inp == null){
            System.err.println("Fatal: Unknown Error");
            System.exit(3);
        }
        int list1[] = new int[inp.size()/2];
        int list2[] = new int[inp.size()/2];
        System.out.println(inp);
        loadLists(list1, list2, inp);
        printList(list1);
        printList(list2);
        Arrays.sort(list1);
        Arrays.sort(list2);
        part1(list1, list2);
        part2(list1, list2);
    }
}