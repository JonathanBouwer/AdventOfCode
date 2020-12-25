#include <cstdio>
#include <chrono>   
using namespace std;

struct mypair {
    int first;
    int second;
};

int main(int argc, char *argv) {
    auto start = std::chrono::high_resolution_clock::now(); 
    int k = 7;
    int a[7] = {5,1,9,18,13,8,0};
    int n = 30000000;
    mypair *vals = (mypair *) malloc(n*sizeof(mypair));
    memset(vals, -1, n*sizeof(mypair));
    
    for (int i = 0; i < k; i++) {
        vals[a[i]] = mypair{-1, i + 1};
    }

    int cur = a[k - 1];
    for (int i = k; i < n; i++) {
        vals[cur].first = vals[cur].second;
        vals[cur].second = i;
        cur = vals[cur].first == -1 ? 0 : i - vals[cur].first;
    }

    printf("%d\n", cur);
    free(vals);
    auto stop = std::chrono::high_resolution_clock::now(); 
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start); 
    printf("Time %fms\n", duration.count() / 1000.0);
}