import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);

    // number of events
    int len = scan.nextInt();

    // event order
    int[] order = new int[len];
    for (int o = 0; o < len; o++) {
      int eventOrder = scan.nextInt() - 1;
      order[o] = eventOrder;
      // System.out.println(o + " " + eventOrder); // debug
    }
    // System.out.println(); // debug

    // keep scanning until we run out of input,
    // failing quietly on exception
    try {
      while (true) {
        int[] maxes = new int[len]; // max length starting at index
        int[] events = new int[len];

        // read events list, init lengths
        for (int e = 0; e < len; e++) {
          int eventOrder = scan.nextInt() - 1;
          events[eventOrder] = e;
          maxes[e] = 1;
          // System.out.print(events[e] + " "); // debug
        }
        // System.out.println(); // debug

        int max, this_max;
        max = 0;
        for (int i = 0; i < len; i++) {
          this_max = 0;
          for (int j = 0; j < i; j++) {
            if (order[events[i]] > order[events[j]]) {
              // System.out.println(events[i] + " " + order[events[i]] + " " + events[j] + " " + order[events[j]]);
              if (maxes[j] > this_max) {
                this_max = maxes[j];
              }
            }
            // System.out.println(events[i] + " " + events[j]); // debug
          }
          maxes[i] = this_max + 1;
        }

        // find max
        for (int k = 0; k < len; k++) {
          if (maxes[k] > max) {
            max = maxes[k];
          }
        }

        System.out.println(max);
      }
    } catch (Exception e) { }
  }
}
