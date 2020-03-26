import java.util.Scanner;

public class N_1065 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n =sc.nextInt();
		int cnt=0;
		String m;
		for (int i=1;i<n+1;i++) {
			if (i <=99)
				cnt+=1;
			else {
				int num1 = i/100;
				int num2 = (i/10)%10;
				int num3 = (i)%10;
				
				if (num1-num2==num2-num3)
					cnt+=1;
						
			}
		}
		System.out.print(cnt);
	}

}
