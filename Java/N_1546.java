import java.util.Scanner;

public class N_1546 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[10];
		int[] count = new int[42];
		int cnt =0;
		for (int i =0; i< 10;i++) {
			arr[i] = sc.nextInt();
		}
		sc.close();
		for (int i =0; i< 10;i++) {
			count[arr[i]%42]++;
		}
		for (int i =0; i< count.length;i++) {
			if(count[i]!=0)
				cnt++;
		}
		System.out.print(cnt);
	}

}
