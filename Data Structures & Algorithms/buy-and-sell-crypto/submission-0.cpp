class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int best = 0;
        int cheapest = prices[0];
        for (int price : prices)
        {
            best = max(best, price - cheapest);
            cheapest = min(cheapest, price);
        }
        return best;
    }
};
