import java.util.Scanner;

public class N_8958 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n =sc.nextInt();
		String[] ox = new String[5];
		
		for(int i=0;i<n;i++) {
			ox[i]= sc.next();
		}
		sc.close();
		
		for(int i=0;i<n;i++) {
			int cnt=0;
			int count=0;
			for(int j=0;j<ox[i].length();j++) {
				if(ox[i].charAt(j)=='O') {
					cnt +=1;
					count +=cnt;
				}else if (ox[i].charAt(j)=='X') {
					cnt = 0;
					count+=cnt;
				}
			}
			System.out.println(count);
		}
		
		
	}

}


