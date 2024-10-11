/**
 * @param {number[]} nums
 * @return {number}
 */
var pivotIndex = function(nums) {
    let totalSum = 0
    for(let i=0; i < nums.length; i++) {
        totalSum += nums[i]
    }

    let leftSum = 0
    for (let i=0; i < nums.length; i++) {
        // sum to the left == leftsum
        // sum to the right === totalSum - leftsum - nums[i]
        // check if leftsum == totalSum - leftsum - nums[i]
        if (leftSum * 2 == totalSum - nums[i])
            return i;
        leftSum += nums[i]
    }
    return -1
};