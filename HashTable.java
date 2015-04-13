
import java.io.IOException;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.*;
import java.math.*;

public class HashTable {
	
	public static double comparisons = 0;

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		String[] fileList = openFile("top_secret_agent_aliases_2015.txt");
		
		/*
		 * Quadratic Probing Trials
		 */
		
		//First trial, c1=c2=1
		String[] hashtable = new String[2477];
		for (int j=0; j < fileList.length; j++){
			quadInsert(hashtable, fileList[j], 1.0, 1.0);
		}
		double avCompare = comparisons/2000.0;
		System.out.println("Quadratic Probing c1=c2=1:");
		System.out.println("list length = 2477 \nAverage num of comparisons = "+avCompare+"\n\n");
		
		//Second trial, c1=c2=0.5
		comparisons = 0;
		String[] hashtable2 = new String[2477];
		for (int j=0; j < fileList.length; j++){
			quadInsert(hashtable2, fileList[j], 0.5, 0.5);
		}
		
		double avCompare2 = comparisons/2000.0;
		System.out.println("Quadratic Probing c1=c2=0.5:");
		System.out.println("list length = 2477 \nAverage num of comparisons = "+avCompare2+"\n\n");

		//Third trial, c1=0, c2=1
		comparisons = 0;
		String[] hashtable3 = new String[2477];
		for (int j=0; j < fileList.length; j++){
			quadInsert(hashtable3, fileList[j], 0, 1);
		}
				
		double avCompare3 = comparisons/2000.0;
		System.out.println("Quadratic Probing c1=0, c2=1:");
		System.out.println("list length = 2477 \nAverage num of comparisons = "+avCompare3+"\n\n");
		
		
		 /* 
		  * Double Hashing Trials
		 */
		
		//First trial, second hash function is the mid-square method
		comparisons = 0;
		String[] hashtable4 = new String[2477];
		for (int j=0; j < fileList.length; j++){
			int hk2 = midSquareMethod(stringtoInt(fileList[j]));
			doubleInsert(hashtable4, fileList[j], hk2);
		}
				
		double avCompare4 = comparisons/2000.0;
		System.out.println("Double Hashing h'(k)=stringtoInt, h''(k)=midSquare method:");
		System.out.println("list length = 2477 \nAverage num of comparisons = "+avCompare4+"\n\n");
		
		//Second trial, second hash function is the multiplication
		comparisons = 0;
		String[] hashtable5 = new String[2477];
		for (int j=0; j < fileList.length; j++){
			int hk2 = (int)multMethod(stringtoInt(fileList[j]), hashtable5);
			doubleInsert(hashtable5, fileList[j], hk2);
		}
						
		double avCompare5 = comparisons/2000.0;
		System.out.println("Double Hashing h'(k)=stringtoInt, h''(k)=multiplication method:");
		System.out.println("list length = 2477 \nAverage num of comparisons = "+avCompare5+"\n\n");
		
		//Third trial, second hash function is the even & odd method
		comparisons = 0;
		String[] hashtable6 = new String[2478]; //to keep m even so m and hk2 will be relatively prime
		for (int j=0; j < fileList.length; j++){
			int hk2 = evenOdd(stringtoInt(fileList[j]));
			doubleInsert(hashtable6, fileList[j], hk2);
		}
								
		double avCompare6 = comparisons/2000.0;
		System.out.println("Double Hashing h'(k)=stringtoInt, h''(k)=even & odd method:");
		System.out.println("list length = 2478 \nAverage num of comparisons = "+avCompare6+"\n\n");
		
		
	}
	
	/*
	 * mid-square method described in class
	 */
	public static int midSquareMethod(int hk){
		String square = Integer.toString(hk*hk);
		String hk1 = Integer.toString(hk);
		int len = hk1.length();
		int end = square.length() - (int)(len/2.0);
		int sub = Integer.parseInt(square.substring((int)(len/2.0), end)); //splice number and then convert it back to an int
		if (sub < 2500){ //if number is too small, change it so there is a wider spread of distribution
			sub += 2503; //prime #
		}
		return sub;
	}
	
	/*
	 * multiplication method described in class with v = 0.618
	 */
	public static double multMethod(int hk, String[] hashtable){
		double v = 0.618;
		double x = (hk*v) - Math.floor(hk*v);
		double a = Math.floor(x*hashtable.length);
		if (a < 2500){ //if number is too small, change it so there is a wider spread of distribution
			a += 2503; // prime #
		}
		return a;
	}
	
	/*
	 * the length of the list must be even, and then h''(k) must be odd
	 * therefore the numbers will be evenly prime and the hashing should
	 * be evenly distributed
	 */
	public static int evenOdd(int hk){
		if (hk % 2 == 0){
			hk = (hk+1);
		}
		return hk;
	}
	
	
	/*
	 * openFile puts all the lines in the file into a String array
	 * readLines gets the number of lines of the file
	 */
	public static String[] openFile(String path) throws IOException{
		FileReader fr = new FileReader(path);
		BufferedReader textReader = new BufferedReader(fr);
		int numLines = readLines(path);
		String[] textData = new String[numLines];
		for (int i = 0; i < numLines; i++){
			textData[i] = textReader.readLine();
		}
		textReader.close();
		return textData;
	}
	
	public static int readLines(String path) throws IOException {
		FileReader file_to_read = new FileReader(path);
		BufferedReader bf = new BufferedReader(file_to_read);
		
		String aLine;
		int numLines = 0;
		while ((aLine = bf.readLine()) != null){
			numLines ++;
		}
		bf.close();
		return numLines;
	}
	
	/*
	 * insert method for quadratic probing
	 */
	public static void quadInsert(String[] hashtable, String key, double c1, double c2){
		double j = 0.0;
		int numKey = stringtoInt(key);
		int hk = numKey % (hashtable.length);
		while (j < hashtable.length){
			if (hashtable[hk] == null){
				hashtable[hk] = key;
				comparisons++;
				break;
			}else{
				comparisons++;
				j++;
				hk = (int)((numKey + (c1*j)+(c2*j*j)) % hashtable.length);
			}
		}
	}
	
	/*
	 * insert method for double hashing
	 */
	public static void doubleInsert(String[] hashtable, String key, int hk2){
		int j = 0;
		int numKey = stringtoInt(key);
		int hk = numKey % hashtable.length;
		while (j < hashtable.length){
			if (hashtable[hk] == null){
				hashtable[hk] = key;
				comparisons++;
				break;
			}else{
				comparisons++;
				j++;
				hk = (numKey + (hk2*j)) % hashtable.length;
			}
		}
	}
	
	
	/*
	 * Creates a number from the String key so the hash function can start at
	 * a value based on the characters
	 * 
	 * Always the h'(k) for the hash functions
	 */
	public static int stringtoInt(String key){
		int total = 0;
		char[] alpha = {'a', 'b', 'c', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
		int[] nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26};
		for (int i = 0; i < key.length(); i++){
		    char c = key.charAt(i);
		    for (int j = 0; j < alpha.length; j++){
		    	if (alpha[j] == c){
		    		total += 2*total + nums[j]; //make total larger so there is a wider distribution for the hashtable
		    		break;
		    	}
		    }
		}
		return total;
	}
}
