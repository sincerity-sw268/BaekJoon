import java.util.Scanner;

public class N_3052 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		int total = 0;
		float avg =0;
		for (int i=0;i<n;i++) {
			arr[i]=sc.nextInt();
			total +=arr[i];
		}
		int max = arr[0];
		for(int i=0;i<n;i++) {
			if (max<arr[i])
				max=arr[i];
		}
		for(int i=0;i<n;i++) {
			avg = total *100 /max /n;

		}

		System.out.print(avg);
	}
	
}



