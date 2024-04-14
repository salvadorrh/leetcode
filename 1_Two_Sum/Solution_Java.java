/* 
Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

My Notes:
Note that this is an easy problem, one of the first LeetCode problems I've done using something more advanced like a HashMap. To have advantage of the O(1) access time
and not loop through all the numbers every time when searching for the target sum.
*/

class Solution_Java {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> Rojo = new HashMap<>();
        int arr[] = new int[2];
        
        for(int i = 0; i < nums.length; i++){
            if(Rojo.containsKey(target-nums[i])){
                arr[0] = Rojo.get(target-nums[i]);
                arr[1] = i;
                return arr;
            }
            Rojo.put(nums[i], i);
        }
        
        return arr;
    }
}
