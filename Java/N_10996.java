import java.util.Scanner;

public class N_10996 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int even = (n/2);
		int odd = n-(n/2);
		for (int i = 1; i <= n; i++) {
			for(int j = 1; j<= odd;j++) {
				System.out.print("*");
				System.out.print(" ");
				
			}
			System.out.println();
			for(int j = 1; j<= even;j++) {
				System.out.print(" ");
				System.out.print("*");
			}
			System.out.println();
		}
			
	}
}
