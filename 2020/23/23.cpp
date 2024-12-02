#include <cstdio>
#include <chrono>

int main(int argc, char *argv) {
    auto start = std::chrono::high_resolution_clock::now();
    
    int input[]{9,6,3,2,7,5,4,8,1};
    
    int max_cup = 1000000;
    int *circle = (int *) malloc((max_cup + 1) * sizeof(int));
    circle[0] = -1;
    for(int i = 1; i < max_cup + 1; i++) {
        circle[i] = i+1;
    }
    
    for(int i = 0; i < 8; i++) {
        circle[input[i]] = input[i + 1];
    }
    
    circle[input[8]] = 10;
    circle[max_cup] = input[0];
    
    int currentCup = input[0];
    
    int remCup1, remCup2, remCup3;
    for(int i = 0; i < 10000000; i++) {
        remCup1 = circle[currentCup];
        remCup2 = circle[remCup1];
        remCup3 = circle[remCup2];
        
        circle[currentCup] = circle[remCup3];
        int destCup = currentCup - 1;
        while (1) {
            if (destCup <= 0) {
                destCup = max_cup;
            }
            if (destCup != remCup1 && destCup != remCup2 && destCup != remCup3) {
                break;
            }
            destCup -= 1;
        }
        
        int oldNext = circle[destCup];
        circle[destCup] = remCup1;
        circle[remCup3] = oldNext;
        
        currentCup = circle[currentCup];
    }
    
    printf("%lld\n", ((long long) circle[1]) * ((long long) circle[circle[1]]));
    
    free(circle);
    auto stop = std::chrono::high_resolution_clock::now(); 
    auto duration = std::chrono::duration_cast<std::chrono::nanoseconds>(stop - start); 
    printf("Time %.3fms\n", duration.count() / 1000000.0);
}
