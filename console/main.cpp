#include <bits/stdc++.h>

using namespace std;

inline void dijkstra(const vector<vector<pair<int, int>>>& g, 
                     const int n, const int src, const int dest,
                     int& dist, vector<pair<pair<int, int>, int>>& path) {
    set<pair<int, int>> q;
    vector<int> d(n, -1);
    vector<pair<int, int>> p(n);
    d[src] = 0;
    p[src] = make_pair(src, 0);
    q.insert(make_pair(d[src], src));
    while (!q.empty()) {
        int v = q.begin()->second;
        q.erase(q.begin());
        for (auto i : g[v]) {
            int u = i.first;
            int w = i.second;
            if (d[u] == -1 || d[u] > d[v] + w) {
                q.erase(make_pair(d[u], u));
                d[u] = d[v] + w;
                p[u] = make_pair(v, w);
                q.insert(make_pair(d[u], u));
            }
        }
    }
    dist = d[dest];
    if (dist != -1) {
        for (int v = dest; v != src; v = p[v].first) {
            path.emplace_back(make_pair(make_pair(p[v].first, v), p[v].second));
        }
        reverse(path.begin(), path.end());
    }
}

int main() {
    printf("number of test cases: ");
    int tests; scanf("%d", &tests);
    for (int test = 1; test <= tests; test++) {
        printf("number of vertices: ");
        int n; scanf("%d", &n);
        
        printf("number of edges: ");
        int m; scanf("%d", &m);
        
        printf("is graph directed? (yes/no) : ");
        char s[5]; scanf("%s", &s);
        bool dir = s[0] == 'y';
        
        puts("list of edges, in source destination weight format");
        vector<vector<pair<int, int>>> g(n, vector<pair<int, int>>(0));
        for (int i = 0; i < m; i++) {
            int x, y, c; scanf("%d%d%d", &x, &y, &c); --x; --y;
            g[x].emplace_back(make_pair(y, c));
            if (!dir) {
                g[y].emplace_back(make_pair(x, c));
            }
        }

        printf("source (starting vertex) and destination (ending vertex): ");
        int src, dest; scanf("%d%d", &src, &dest); --src; --dest;
        vector<pair<pair<int, int>, int>> path;
        int dist;
        dijkstra(g, n, src, dest, dist, path);
        if (dist == -1) {
            printf("there is no any path from %d to %d\n", src + 1, dest + 1);
        } else {
            printf("shortest path from %d to %d has a total weight %d and " 
                   "consists of %d edges.\n", src + 1, dest + 1, dist, path.size());
            for (auto i : path) {
                printf("%d %d %d\n", i.first.first + 1, i.first.second + 1, i.second);
            }
        }
    }
    return 0;
}