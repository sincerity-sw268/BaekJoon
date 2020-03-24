import java.util.Scanner;

public class N_2577 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
		int b = sc.nextInt();
		int c = sc.nextInt();
		int num = a*b*c;
		String s_num = String.valueOf(num);

		int[] count = new int[10];
		for (int i =0; i< s_num.length();i++) {
			count[s_num.charAt(i)-'0']++;
		}
		for (int i = 0; i < count.length; ++i) {
			System.out.println(count[i]);
	        }

	}
}
