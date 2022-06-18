class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int lp=0, rp=1, res = 0;
        int n = prices.size();
        if (n<2){
            return 0;
        }
        while(rp<n){
            res = max(res, prices[rp]-prices[lp]);
            if(prices[lp]>prices[rp])
                lp++;
            else
                rp++;
        }
        return res;
    }
};