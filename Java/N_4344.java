import java.util.Scanner;

public class N_4344 {
 
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n =sc.nextInt();
		int[] arr = new int[1000];
		
		
		for(int i=0;i<n;i++) {
			int c= sc.nextInt();
			int sum=0;
			int avg,count=0;
			for(int j=0;j<c ;j++) {
				arr[j]= sc.nextInt();	
				sum+=arr[j];
				
			}
			avg = sum/c;

			for(int j=0;j<c ;j++) {
				if (arr[j]>avg)
					count ++;
			}
			
			System.out.printf("%.3f", 100.0 * count / c);
            System.out.println("%");
			
		}
		
		
	}

}



