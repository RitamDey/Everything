import java.util.Scanner;


class Prime {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();

		Prime obj = new Prime();

		for(int i=2; i<=num; ++i) {
			if(obj.isprime(i))
				System.out.print(i+" ");
		}

		System.out.println();
	}

	public boolean isprime(int n) {
		int sum = 0;
		for(int i=1; i<=n; ++i) {
			if(n%i == 0)
				sum += 1;
		}
		
		return sum == 2;
	}
}
