import java.lang.*;
import java.util.*;

class New2
{
	public static void main(String arg[])
	{
		 try 
		 { 
		 	Scanner sobj = new Scanner(System.in);
		 	System.out.println("Enter string"); 
		 	String str = sobj.nextLine(); 
		 	MyString mobj = new MyString();
		 	String out = mobj.DuplicateWord(str); 
		 	System.out.println("Modified string is : "+out);
		 } 
		 catch(Exception obj) 
		 {
		 	System.out.println(obj);
		 }  
	}
}

class MyString 
{ 
	String DuplicateWord(String str) throws Exception 
	{
	 	char arr[] = str.toCharArray();
	 	char brr[] = new char[arr.length];
	 	int j=0;
	 	int i=0;
	 	while(i<arr.length-1)
	 	{
	 		int flag=0;
	 		while(i<arr.length-1 && arr[i]==arr[i+1])
	 		{
	 			i++;
	 			flag=1;
	 		}
	 		if(flag==1)
	 		{
	 			brr[j]='$';
	 		}
	 		else
	 		{
	 			brr[j]=arr[i];
	 		}
	 		j++;
	 		i++;
	 	}
	 	if(arr[arr.length-1]!=arr[arr.length-2])
	 	{
	 		brr[j]=arr[arr.length-1];
	 	}
	 	
	 	String temp = new String(brr);
	 	
	 	return temp.substring(0,j+1);
	}
}
	 	
	 	
	 	
