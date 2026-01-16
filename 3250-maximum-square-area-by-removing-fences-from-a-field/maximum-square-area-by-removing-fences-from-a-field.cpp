class Solution {
public:
    int maximizeSquareArea(int m, int n, vector<int>& hFences, vector<int>& vFences) {
        const long long MOD = 1e9 + 7;

        // Step 1: add boundary fences
        hFences.push_back(1);
        hFences.push_back(m);
        vFences.push_back(1);
        vFences.push_back(n);

        // Step 2: sort fences
        sort(hFences.begin(), hFences.end());
        sort(vFences.begin(), vFences.end());

        // Step 3: store all possible gaps
        unordered_set<long long> horizontalGaps;

        for (int i = 0; i < hFences.size(); i++) {
            for (int j = i + 1; j < hFences.size(); j++) {
                horizontalGaps.insert(hFences[j] - hFences[i]);
            }
        }

        long long maxSide = 0;

        // Step 4: check vertical gaps
        for (int i = 0; i < vFences.size(); i++) {
            for (int j = i + 1; j < vFences.size(); j++) {
                long long gap = vFences[j] - vFences[i];
                if (horizontalGaps.count(gap)) {
                    maxSide = max(maxSide, gap);
                }
            }
        }

        // Step 5: result
        if (maxSide == 0) return -1;

        return (maxSide * maxSide) % MOD;
    }
};
