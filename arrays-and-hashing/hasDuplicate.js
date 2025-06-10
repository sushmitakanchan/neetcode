// Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

//Brute force 
// function hasDuplicate(nums){
//     for (let i=0; i< nums.length; i++ ){
//         for(let j = i+1; j<nums.length; j++){
//             if(nums[i]===nums[j]){
//                 return true;
//             }
//         }
//     }
//         return false;

// }

const result = hasDuplicate([1,2,3,5,4]);
console.log(result);
    
// Time Complexity: O(n²)
// Space Complexity: O(1)

// Sorting

// function hasDuplicate(nums){
//     nums.sort((a,b)=>a-b)
//     for(i=0; i< nums.length; i++){
//         if(nums[i] === nums[i-1]){
//             return true
//         }
//     }
//     return false;
// }

// Time Complexity: O(n log n)
// Space Complexity: O(1)

// Hash set Length

function hasDuplicate(nums){
    return new Set(nums).size < nums.length;
}

// Time Complexity: O(n)
// Space Complexity: O(n)
