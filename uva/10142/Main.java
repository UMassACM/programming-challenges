import java.util.*;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    
    int cases = Integer.parseInt(sc.nextLine());
    sc.nextLine();
    
    for (int cas = 0; cas < cases; cas++) {
      int numCands = Integer.parseInt(sc.nextLine());
      String[] names = new String[numCands];
      
      // input: candidate names
      for (int cand = 0; cand < numCands; cand++) {
        names[cand] = sc.nextLine();
      }
      
      // input: votes
      ArrayList<LinkedList<Integer>> ballots = new ArrayList<LinkedList<Integer>>();
      while (true) {
        try {
          String voteLine = sc.nextLine();
          if (voteLine.equals(""))
            break;
          
          LinkedList<Integer> ballot = new LinkedList<Integer>();
          for (String vote : voteLine.split(" ")) {
            ballot.add(Integer.parseInt(vote));
          }
          ballots.add(ballot);
        } catch (Exception e) {
          break;
        }
      } 
      
      int win_votes = (int) Math.ceil(ballots.size() / 2.0);
      // System.out.println(win_votes); // debug
      
      int winner = -1;
      boolean elim[] = new boolean[numCands];
      for (int i = 0; i < numCands; i++)
        elim[i] = false;
      
      while (winner == -1) {
        int votes[] = new int[numCands];
        
        // add vote for candidate
        for (int i = 0; i < ballots.size(); i++) {
          int vote = ballots.get(i).peek()-1;
          if (!elim[vote])
            votes[vote]++;
        }
        
        // check for winner, losers
        int max_vote = Integer.MIN_VALUE;
        int min_vote = Integer.MAX_VALUE;
        for (int i = 0; i < numCands; i++) {
          if (votes[i] > max_vote) {
            max_vote = votes[i];
            
            if (votes[i] > win_votes)
              winner = i;
          } else if (votes[i] == max_vote) {
            winner = -1;
          }
          
          if (votes[i] < min_vote && !elim[i])
            min_vote = votes[i];
        }
        
        // System.out.println(winner); // debug
        // System.out.println(min_vote); // debug
        // System.out.println(max_vote); // debug
        
        // check for total tie
        if (min_vote == max_vote)
          break;
        
        // remove loser(s)
        for (int i = 0; i < numCands; i++) {
          if (votes[i] == min_vote) {
            elim[i] = true;
            
            for (LinkedList ballot : ballots)
              ballot.remove((Object) (i+1));
          }
        }
      }
      
      // output winner(s) for case
      if (winner != -1) {
        // select winner (if there is one)
        System.out.println(names[winner]);
      }
      else {
        // output remaining candidates (all tied)
        for (int i = 0; i < numCands; i++) {
          if (!elim[i])
            System.out.println(names[i]);
        }
      }
      
      // separate case output
      if (cas+1 < cases)
        System.out.println();
    }
  }
}