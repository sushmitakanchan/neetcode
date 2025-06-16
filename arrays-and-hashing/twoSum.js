function twoSum(nums, target){
    for(let i=0; i<nums.length; i++){
        for(let j=i+1; j<nums.length; j++){
            if(nums[i]+nums[j]===target){
                return [i, j]
            }
        }
    }
    return [];

}

console.log(twoSum([5,5], 10));

// Time complexity: O(n2)
// Space complexity: O(1)
