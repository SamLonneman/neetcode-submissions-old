class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int bestProfit = 0;
        int cheapestBuyPrice = prices[0];
        for (int sellPrice : prices)
        {
            bestProfit = max(bestProfit, sellPrice - cheapestBuyPrice);
            cheapestBuyPrice = min(cheapestBuyPrice, sellPrice);
        }
        return bestProfit;
    }
};
