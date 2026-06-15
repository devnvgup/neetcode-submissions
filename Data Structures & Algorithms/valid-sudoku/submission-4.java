class Solution {
    public boolean isValidSudoku(char[][] board) {
        
        
       // each rơw unique 1 -> 9
        // each col unique 1 -> 9
        // 3 x 3 => unique 1 -> 9
        // return true
        // check row
        List<Character> tmp1 = new ArrayList<>();
        List<Character> tmp2 = new ArrayList<>();
        List<Character> tmp3 = new ArrayList<>();
        for (int i = 0; i < board.length; i++) {
            List<Character> arrTmp = new ArrayList<>();
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == '.') continue;
                if (arrTmp.contains(board[i][j])) {
                    return false;
                }
                arrTmp.add(board[i][j]);
                if (j <= 2 && j >= 0) {
                    if (tmp1.contains(board[i][j])) {
                        return false;
                    }
                    tmp1.add(board[i][j]);
                } else if (j <= 5 && j > 2) {
                    if (tmp2.contains(board[i][j])) {
                        return false;
                    }
                    tmp2.add(board[i][j]);
                } else {
                    if (tmp3.contains(board[i][j])) {
                        return false;
                    }
                    tmp3.add(board[i][j]);
                }
            }
            if (i == 2 || i == 5 || i == 8) {
                tmp1.clear();
                tmp2.clear();
                tmp3.clear();
            }
        }
        // check col
        for (int i = 0; i < board[0].length; i++) {
            List<Character> arrTmp = new ArrayList<>();
            for (int j = 0; j < board.length; j++) {
                if (board[j][i] == '.') continue;
                if (arrTmp.contains(board[j][i])) {
                    return false;
                }
                arrTmp.add(board[j][i]);
            }
        }
        // check 3 x 3

        return true;  
        
    }
}
