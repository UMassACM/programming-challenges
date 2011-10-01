import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    // generate movement indices
    ArrayList<Integer[]> bpawn = new ArrayList<Integer[]>();
    ArrayList<Integer[]> wpawn = new ArrayList<Integer[]>();
    ArrayList<Integer[]> rook = new ArrayList<Integer[]>();
    ArrayList<Integer[]> bishop = new ArrayList<Integer[]>();
    ArrayList<Integer[]> knight = new ArrayList<Integer[]>();

    wpawn.add(new Integer[]{-1,-1});
    wpawn.add(new Integer[]{1,-1});
    bpawn.add(new Integer[]{-1,1});
    bpawn.add(new Integer[]{1,1});

    knight.add(new Integer[]{2,1});
    knight.add(new Integer[]{2,-1});
    knight.add(new Integer[]{-2,1});
    knight.add(new Integer[]{-2,-1});
    knight.add(new Integer[]{1,2});
    knight.add(new Integer[]{1,-2});
    knight.add(new Integer[]{-1,2});
    knight.add(new Integer[]{-1,-2});

    for (int i = 1; i <= 7; i++)
      rook.add(new Integer[]{0,i});
    for (int i = 1; i <= 7; i++)
      rook.add(new Integer[]{0,-i});
    for (int i = 1; i <= 7; i++)
      rook.add(new Integer[]{i,0});
    for (int i = 1; i <= 7; i++)
      rook.add(new Integer[]{-i,0});

    for (int i = 1; i <= 7; i++)
      bishop.add(new Integer[]{i,i});
    for (int i = 1; i <= 7; i++)
      bishop.add(new Integer[]{-i,-i});
    for (int i = 1; i <= 7; i++)
      bishop.add(new Integer[]{i,-i});
    for (int i = 1; i <= 7; i++)
      bishop.add(new Integer[]{-i,i});

    ArrayList<Integer[]> queen = new ArrayList<Integer[]>(rook);
    queen.addAll(bishop);

    int gameNum = 1;
    while (true) {
      // read board
      char[][] board = new char[8][8];
      boolean empty = true;
      for (int i = 0; i < 8; i++) {
        String line = sc.nextLine();
        for (int j = 0; j < 8; j++) {
          board[i][j] = line.charAt(j);
          if (board[i][j] != '.')
            empty = false;
        }
      }

      // end with empty board
      if (empty) {
        break;
      }

      // check pieces and then check for checks
      String side = "no";
      for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
          char piece = board[i][j];
          if (piece == '.' || piece == 'K' || piece == 'k')
            continue;

          // set target king and side
          char target;
          String target_side;
          if (Character.isUpperCase(piece)) {
            target = 'k';
            target_side = "black";
          } else {
            target = 'K';
            target_side = "white";
          }
          /* debug
          System.out.println("\npiece:");
          System.out.println(piece + " " + i + " " + j);
          System.out.println(target);
          System.out.println(target_side);
          */
          // set move list
          ArrayList<Integer[]> moves = new ArrayList<Integer[]>();
          if (piece == 'P') {
            moves = wpawn;
          }
          if (piece == 'p') {
            moves = bpawn;
          }
          if (piece == 'N' || piece == 'n') {
            moves = knight;
          }
          if (piece == 'R' || piece == 'r') {
            moves = rook;
          }
          if (piece == 'B' || piece == 'b') {
            moves = bishop;
          }
          if (piece == 'Q' || piece == 'q') {
            moves = queen;
          }

          // check moves
          for (int move = 0; move < moves.size(); move++) {
            try {
              Integer[] coords = moves.get(move);
              int x = coords[0];
              int y = coords[1];

              char this_piece = board[i+y][j+x];
              /* debug
              System.out.print(this_piece);
              System.out.printf(" %d, %d\n", i+y, j+x);
              */
              if (this_piece == target) {
                side = target_side;
                break;
              }

              // check for piece in the way
              if (this_piece != '.' && this_piece != target) {
                // ignore pawns and knights
                if (piece == 'P' || piece == 'p' || piece == 'N' || piece == 'n') {
                  continue;
                } else {
                  // try another direction
                  move = ((move / 7)+1)*7 - 1;
                }
              }

            } catch (Exception e) { // went out of array bounds (simpler to try all than test)
                // ignore pawns and knights
                if (piece == 'P' || piece == 'p' || piece == 'N' || piece == 'n') {
                  continue;
                } else {
                  move = ((move / 7)+1)*7 - 1;
                }
            }
          }
          if (side != "no")
            break;
        }

        if (side != "no")
          break;
      }

      System.out.printf("Game #%d: %s king is in check.\n", gameNum, side);
      gameNum++;

      // consume newline
      sc.nextLine();
    }
  }

}