class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        std::vector<int> final_price;
        int length = prices.size();
        for (int i = 0; i < length - 1; i++) {
            for (int j = i + 1; j < length; j++) {
                if (prices[j] <= prices[i]) {
                    prices[i] -= prices[j];
                    break;
                }
            }
        }
        
        return prices;
    }
};
