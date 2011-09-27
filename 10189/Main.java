import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    int fieldNum = 1;
    String ln = sc.nextLine();
    while (true) {      
      // input: read dimensions
      String[] dimStr = ln.split(" ");
      int n = Integer.parseInt(dimStr[0]);
      int m = Integer.parseInt(dimStr[1]);
      
      // initialize empty minesweeper grid (+ padding)
      int[][] grid = new int[n+2][m+2];
      
      // add up mine hints and set mine locations in the grid
      for (int i = 0; i < n; i++) {
        String gridLine = sc.nextLine();
        for (int j = 0; j < m; j++) {
          if (gridLine.charAt(j) == '*') {
            for (int gi = -1; gi <= 1; gi++)
              for (int gj = -1; gj <= 1; gj++)
                if (grid[i+gi+1][j+gj+1] != -1)
                  grid[i+gi+1][j+gj+1]++;
            
            grid[i+1][j+1] = -1;
          }
        }
      }
      
      // Output
      System.out.printf("Field #%d:\n", fieldNum);
      for (int i = 1; i < n+1; i++) {
        for (int j = 1; j < m+1; j++) {
          if (grid[i][j] == -1)
            System.out.print('*');
          else
            System.out.print(grid[i][j]);
        }
        System.out.println();
      }
      fieldNum++;
      
      // check for end
      try {
        ln = sc.nextLine();
        if (ln.equals("0 0") || ln.equals(""))
          break;
      } catch (Exception e) {
        break;
      }
      
      // separate output with blank line
      System.out.println();
    }
  }
}