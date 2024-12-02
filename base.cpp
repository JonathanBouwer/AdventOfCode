#include <cstdio>
#include <chrono>   
using namespace std;

int main(int argc, char *argv) {
    auto start = std::chrono::high_resolution_clock::now(); 
    
    
    
    auto stop = std::chrono::high_resolution_clock::now(); 
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start); 
    printf("Time %.3fms\n", duration.count() / 1000.0);
}