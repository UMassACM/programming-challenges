import java.util.*;

public class Main {
  public static void main(String[] args) {
    // read number of inputs
    Scanner sc = new Scanner(System.in);
    int numCases = sc.nextInt();
    // iterate over each input case
    for (int i = 0; i < numCases; i++) {
      int n = sc.nextInt(); // want number of digits in n!

      // the trick: the number of digits in n! is log10(n!)
      // since multiplication is addition in log space, we can
      // convert log10(n!) to log10(n) + log10(n-1) + ... + log10(1)
      // and finally take the floor of the log sum + 1,
      // since log(10) = 1 and not 2 (and we want the number of digits)
      double numDigits = 0;
      for (int j = n; j > 1; j--) {
        numDigits += Math.log10(j);
      }

      numDigits = Math.floor(numDigits) + 1;
      System.out.println((int) numDigits);
    }
  }
}
