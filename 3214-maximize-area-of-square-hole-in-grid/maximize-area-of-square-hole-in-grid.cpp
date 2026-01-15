class Solution {
public:
    int getMaxGap(vector<int>& bars) {
        sort(bars.begin(), bars.end());
        int longest = 1, cur = 1;

        for (int i = 1; i < bars.size(); i++) {
            if (bars[i] == bars[i - 1] + 1) {
                cur++;
            } else {
                longest = max(longest, cur);
                cur = 1;
            }
        }
        longest = max(longest, cur);

        // removing k bars creates gap of k+1
        return longest + 1;
    }

    int maximizeSquareHoleArea(int n, int m, vector<int>& hBars, vector<int>& vBars) {
        int maxH = getMaxGap(hBars);
        int maxV = getMaxGap(vBars);

        int side = min(maxH, maxV);
        return side * side;
    }
};
