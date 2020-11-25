import java.lang.*;
import java.util.*;

class New3
{
	public static void main(String arg[])
	{
		 try 
		 { 
		 	Scanner sobj = new Scanner(System.in);
		 	System.out.println("Enter number of elements"); 
		 	int size = sobj.nextInt();
		 	int arr[]=new int[size];
		 	
		 	for(int i=0;i<size;i++)
		 	{
		 		arr[i]=sobj.nextInt();
		 	}
		 	
		 	MyArray mobj = new MyArray();
		 	int no = mobj.Equilibrium(arr); 
		 	System.out.println(no);
		 } 
		 catch(Exception obj) 
		 {
		 	System.out.println(obj);
		 }  
	}
}

class MyArray
{ 
	int Equilibrium(int Arr[]) throws Exception 
	{
	 	int totalsum=0;
	 	int partsum=0;
	 	int i=0;
	 	
	 	for(i=0;i<Arr.length;i++)
	 	{
	 		totalsum=totalsum+Arr[i];
	 	}
	 	for(i=0;i<Arr.length;i++)
	 	{
	 		totalsum=totalsum-Arr[i];
	 		if(totalsum==partsum)
	 		{
	 			return i;
	 		}
	 		partsum=partsum+Arr[i];
	 	}
	 	return -1;
	}
}
	 	
	 	
	 	
