import java.util.Scanner;

public class N_1110 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		int check = N;
		int count = 0;
		
		while(true) {
			int temp = (N / 10) + (N % 10);
			int new_N = (N % 10)*10 + (temp % 10);
			count += 1;
			N = new_N;
			if (new_N == check) break;
			
		}
		System.out.print(count);
			
	}
}
