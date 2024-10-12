class Solution {
    public int[] plusOne(int[] digits) {
        digits[digits.length - 1] += 1;

        for (int i = digits.length - 1; i >= 0; i--){
            if (digits[i] == 10 && i != 0){
                digits[i] = 0;
                digits[i-1] += 1;
            }

            if (digits[0] == 10){
                int[] newDigits = new int[digits.length + 1];
                newDigits[0] = 1;
                return newDigits;            
            }
        }

        return digits;        
    }
}