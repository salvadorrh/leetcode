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
