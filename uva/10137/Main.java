import java.util.*;

public class Main {
  public static void main(String[] argv) {
    Scanner scan = new Scanner(System.in);
    try {
      while (true) {
        // input: number of students
        int num_students = scan.nextInt();
        if (num_students == 0)
          break;
        
        // input: student payments (= number of students)
        // calculate: payment sum
        double[] payments = new double[num_students];
        double sum = 0;
        for (int i = 0; i < num_students; i++) {
          payments[i] = scan.nextDouble();
          sum += payments[i];
        }
        
        // calculate: average paid for finding difference among students
        // rounded to nearest cent
        double avg = sum / (double) num_students;
        avg = Math.round(avg * 100.0) / 100.0;
        
        // calculate difference from average for each student
        // round to nearest cent (least amount of money)
        // must round-up underpayments
        // must round-down overpayments
        double high = 0;
        double low = 0;
        for (int i = 0; i < num_students; i++) {
          double diff = payments[i] - avg;
          if (diff < 0)
            low -= diff;
          else
            high += diff;
        }
        
        // difference is at most one cent, but still need to pick
        // the closest to one cent
        double change;
        if (low > high)
          change = low;
        else
          change = high;
        
        // output w/ proper 2-decimal monetary formatting
        System.out.printf("$%.2f\n", change);
      }
    } catch (Exception e) {}
  }
}