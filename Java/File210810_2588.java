import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		int a = input.nextInt();
		int b = input.nextInt();
		
		int first = b % 10;
		int second = b / 10 % 10;
		int third = b / 100 % 10;
		
		System.out.printf("%d\n%d\n%d\n%d", a*first, a*second, a*third, a*b);
		
		input.close();
	}
}