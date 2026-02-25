class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> hashmap;
        int index = 0;
        std::vector<int> res;

        while (index < nums.size()) {
            if (hashmap.find(target - nums[index]) != hashmap.end()) {
                res.push_back(hashmap[target - nums[index]]);
                res.push_back(index);
                return res;
            }
            hashmap[nums[index]] = index;
            index ++;
        }
        
        return res;
    }
};
