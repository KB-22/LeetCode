class Solution {
public:
    struct Event {
        double y, x1, x2;
        int type;
        bool operator<(const Event& other) const {
            return y < other.y;
        }
    };

    double separateSquares(vector<vector<int>>& squares) {
        vector<Event> events;

        for (auto &s : squares) {
            double x = s[0], y = s[1], L = s[2];
            events.push_back({y, x, x+L, +1});
            events.push_back({y+L, x, x+L, -1});
        }

        sort(events.begin(), events.end());

        map<double,int> sweep;

        auto getWidth = [&]() {
            double width = 0;
            int cnt = 0;
            double prev = 0;
            for (auto &[x, c] : sweep) {
                if (cnt > 0) width += x - prev;
                cnt += c;
                prev = x;
            }
            return width;
        };

        double totalArea = 0;
        double prevY = events[0].y;

        for (int i = 0; i < events.size(); ) {
            double y = events[i].y;
            double width = getWidth();
            totalArea += width * (y - prevY);

            while (i < events.size() && events[i].y == y) {
                sweep[events[i].x1] += events[i].type;
                sweep[events[i].x2] -= events[i].type;
                if (sweep[events[i].x1] == 0) sweep.erase(events[i].x1);
                if (sweep[events[i].x2] == 0) sweep.erase(events[i].x2);
                i++;
            }
            prevY = y;
        }

        double target = totalArea / 2;

        sweep.clear();
        prevY = events[0].y;
        double area = 0;

        for (int i = 0; i < events.size(); ) {
            double y = events[i].y;
            double width = getWidth();
            double slice = width * (y - prevY);

            if (area + slice >= target) {
                double need = target - area;
                return prevY + need / width;
            }

            area += slice;

            while (i < events.size() && events[i].y == y) {
                sweep[events[i].x1] += events[i].type;
                sweep[events[i].x2] -= events[i].type;
                if (sweep[events[i].x1] == 0) sweep.erase(events[i].x1);
                if (sweep[events[i].x2] == 0) sweep.erase(events[i].x2);
                i++;
            }
            prevY = y;
        }

        return prevY;
    }
};
