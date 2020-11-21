import java.lang.*;
import java.util.*;

class New
{
	public static void main(String arg[])
	{
		 try 
		 { 
		 	Scanner sobj = new Scanner(System.in);
		 	System.out.println("Enter string"); 
		 	String str = sobj.nextLine(); 
		 	MyString mobj = new MyString();
		 	mobj.DuplicateWord(str); 
		 } 
		 catch(Exception obj) 
		 {
		 	System.out.println(obj);
		 }  
	}
}

class MyString 
{ 
	void DuplicateWord(String str) throws Exception 
	{
	 	String arr[] = str.split(" "); 
	 	
	 	HashMap<String,Integer> WordCount = new HashMap<String,Integer>();
	 	
	 	for(String s : arr)
	 	{
	 		if(WordCount.containsKey(s.toLowerCase()))
	 		{
	 			WordCount.put(s.toLowerCase(),WordCount.get(s.toLowerCase())+1);
	 		}
	 		else
	 		{
				WordCount.put(s.toLowerCase(),1); 		
	 		}
	 	}
	 	System.out.println("Result is : ");
	 	System.out.println(WordCount);
	 	
	 	Set<String> words = WordCount.keySet();
	 	
	 	System.out.println("Duplicate words and count are");
	 	
	 	for(String word : words)
	 	{
	 		if(WordCount.get(word)>1)
	 		{
	 			System.out.println("String :"+word + " ,Count: "+WordCount.get(word));
	 		}
	 	}
	 }
}
	 	
	 	
	 	
