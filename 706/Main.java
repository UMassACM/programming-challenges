import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    String[][] nums = new String[10][5];
    nums[0] = new String[]{"-","||"," ","||","-"};
    nums[1] = new String[]{" ", " |"," "," |", " "};
    nums[2] = new String[]{"-"," |","-","| ","-"};
    nums[3] = new String[]{"-"," |","-"," |","-"};
    nums[4] = new String[]{" ","||","-"," |"," "};
    nums[5] = new String[]{"-","| ","-", " |", "-"};
    nums[6] = new String[]{"-","| ","-","||","-"};
    nums[7] = new String[]{"-"," |"," "," |", " "};
    nums[8] = new String[]{"-","||","-","||","-"};
    nums[9] = new String[]{"-","||","-"," |","-"};

    while (true) {
      // Input
      int size = sc.nextInt();
      String num = Integer.toString(sc.nextInt());

      if (size == 0 && num.equals("0")) {// quit on double zero
        return;
    }
      // Distinguish horizontal/vertical rose by first char
      int first_char = num.charAt(0) - '0';

      // Output row by row
      for (int segm = 0; segm < 5; segm++) {
        if (nums[first_char][segm] == " " || nums[first_char][segm] == "-") {
          // horizontal segment
          for (int i = 0; i < num.length(); i++) {
            int digit = num.charAt(i) - '0';
            String disp = nums[digit][segm];

            if (disp == " ") {
              repeat(disp, size+2);
            }

            if (disp == "-") {
              System.out.print(" ");
              repeat(disp, size);
              System.out.print(" ");
            }

              if (i+1 < num.length())
                System.out.print(" "); // separate digits
          }
          System.out.println();
        } else {
          // vertical segment
          for (int height = 0; height < size; height++) {
            for (int i = 0; i < num.length(); i++) {
              int digit = num.charAt(i) - '0';
              String disp = nums[digit][segm];

              if (disp == "| ") {
                System.out.print("|");
                repeat(" ", size+1);
              }

              if (disp == " |") {
                repeat(" ", size+1);
                System.out.print("|");
              }

              if (disp == "||") {
                System.out.print("|");
                repeat(" ", size);
                System.out.print("|");
              }

              if (i+1 < num.length())
                System.out.print(" "); // separate digits
            }
            System.out.println();
          }
        }
      }
      System.out.println();
    }
  }

  public static void repeat(String chr, int num_times) {
    for (int i = 0; i < num_times; i++)
      System.out.print(chr);
  }
}