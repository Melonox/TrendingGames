

import java.io.*;
import java.util.*;

public class Chomp extends AbstractStrategyGame { //0 = not chomp
    private int[][] board;
    private boolean isXTurn;

    // Constructs a new Chomp game.
    public Chomp() {
        this.board = new int[4][5];
        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[i].length; j++) {
                board[i][j] += 3; ///3 layers
            }
        }
        this.isXTurn = true;
    }

    // Constructs a new Chomp game with any size of chocolate.
    // Parameters: 
    // - int row: the amount of rows of chocolate you want in a chocolate bar
    // - int col: the amount of columns of chocolate you want in a chocolate bar
    // Throws illegalArgumentException if you input sizes that can't be possible for the bar
    public Chomp(int row, int col) {
        if (row < 1 || col < 1) {
            throw new IllegalArgumentException("Incorrect board size declaration");
        }
        this.board = new int[row][col];
        for(int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[i].length; j++) {
                board[i][j] += 3; ///3 layers
            }
        }
        this.isXTurn = true;
    } 

    // Returns a String containing instructions on how to play the game.
    public String instructions() {
        String result = "";
        result+="This is Chomp. There is a chocolate bar of a certain size and 3 layers. \n";
        result+="Each players take turns to choose one block of chocoloate and \"eats it\" \n";
        result+="(remove from the board). All of the following chocolate blocks below and \n";
        result+="to the right of the chocolate block chosen are eaten (but not the layers). \n";
        result+="Right now, the chocolate bar has 3 layers, and eating a block will reveal \n";
        result+="the next layers. The top left chocolate block of the bottom layer (0,0) is \n";
        result+="poisoned and thus whichever player eats that block loses. Have fun! \n";
        result+="P.S rows and columns start at 0 when counting which blocks to eat";
        return result;
    }

    // Returns a String representation of the current board.
    public String toString() {
        String result = "";
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                result += board[i][j] + " ";
            }
            result += "\n";
        }
        return result;
    }

    // Returns the player who won (either player 1 or player 2)
    // Returns -1 if game isn't over and there are no ties in this game
    public int getWinner() {
        if(board[0][0] == 0) {
            return (isXTurn ? 1 : 2);
        }
        return -1;
    }

    // Returns the player's turn
    // 1 if player 1 2 if player 2, -1 if the game is over
    public int getNextPlayer() {
        if (isGameOver()) {
            return -1;
        }
        return isXTurn ? 1 : 2;
    }

    // Given which block the user chooses to eat, chomp every chocolate on the same layer
    // to the right and below the selected block.
    // throws exceptions when accessing a chocolate block that isn't on the board or if there
    // are no chocolates left to be eat on where the player wants to eat/ chomp.
    // Board bounds are whatever the user set as the rows and cols 
    // (default is 0-3 for rows and 0-4 for columns).
    public void makeMove(Scanner input) {
        System.out.print("Row? ");
        int row = input.nextInt();
        System.out.print("Column? ");
        int col = input.nextInt();

        if (row < 0 || row >= board.length || col < 0 || col >= board[0].length) {
                throw new IllegalArgumentException("Invalid board position: " + row + "," + col);
        }
        if (board[row][col] == 0) {
            throw new IllegalArgumentException("No Chocolate: " + row + "," + col);
        }
        chomping(row, col);        
        isXTurn = !isXTurn;
    }

    // private helper method for chomping down the chocolate bar
    // only chomps the same layer of chocolate.
    // Parameters: 
    // - int row: the row of chocolate you want to eat/chomp
    // - int col: the columns of chocolate you want to eat/chomp
    private void chomping(int row, int col) {
        int layer = board[row][col];
        for(int i = row; i < board.length; i++) {
            for(int j = col; j < board[i].length; j++) {
                if ( (layer == board[i][j]) && !(board[i][j] == 0)) {
                    board[i][j]--;
                }
            }
        }
    }

}