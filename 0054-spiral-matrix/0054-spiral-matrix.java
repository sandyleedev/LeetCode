class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int x = matrix.length;
        int y = matrix[0].length;
        
        ArrayList<Integer> result = new ArrayList<>();
        
        if (y == 1){
            for (int i = 0; i < x; i++){
                result.add(matrix[i][0]);
            }
            return result;
        }
        
        int a = 0, b = 0, roundIndex = 0;
        
        for(int i = 0; i < x * y; i++){
            result.add(matrix[a][b]);
            
            if (a == roundIndex + 1 && b == roundIndex){
                roundIndex++;
            }
            
            // in each round,
            // 1. right : a, b++
            // 2. down : a++, b
            // 3. left : a--, b
            // 4. up : a, b--
            
            // right
            if (a == roundIndex && b < y - (roundIndex + 1)){
                b++;
            }
            // left
            else if (a == x - (roundIndex + 1) && b > roundIndex){
                b--;
            }
            // up
            else if (b == roundIndex && a > (roundIndex + 1)){
                a--;
            }
            // down
            else if (b >= y - (roundIndex + 1) && a <= x - (roundIndex + 1)){
                a++;
            }
        }
        
        return result;
    }
}