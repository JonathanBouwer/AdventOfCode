#include <cstdio>
#include <chrono>
using namespace std;

int main(int argc, char *argv) {
    auto start = std::chrono::high_resolution_clock::now();
    int instructions[] = {2,4,1,5,7,5,1,6,0,3,4,6,5,5,3,0};
    int inst_len = 16;
    
    // For some reason all results end on 4632 in octal = 2458 decimal
    long long a_incr = 4096;
    long long a_start = 136904920099226LL - 30000000LL*4096; // (2LL << (3*(inst_len - 1))) + 04632;
    long long a_end = (2LL << (3*inst_len));
    for (long long reg_a_potential = a_start; reg_a_potential < a_end; reg_a_potential += a_incr) {
        if (reg_a_potential % (a_incr * 1000000) == 04632) {
            printf("\r%.2f%%", ((reg_a_potential - a_start)*100.0)/(2LL << 46));
        }
        // For some reason all potential results have one of the following values in the next chunk
        int hex_suffix = (reg_a_potential / 4096) % 4096;
        if (hex_suffix != 0x216 && 
            hex_suffix != 0x2d6 && 
            hex_suffix != 0x312 && 
            hex_suffix != 0x316 && 
            hex_suffix != 0x322 && 
            hex_suffix != 0x33a)
            continue;
        long long reg_a = reg_a_potential;
        long long reg_b = 0;
        long long reg_c = 0;
        int out_pos = 0;
        for (;reg_a > 0; reg_a /= 8) {
            reg_b = reg_a % 8;
            reg_b = reg_b ^ 5;
            reg_c = reg_a >> (reg_b);
            reg_b = reg_b ^ 6;
            reg_b = reg_b ^ reg_c;
            int val = reg_b % 8;
            if (val != instructions[out_pos]) {
                break;
            }
            out_pos += 1;
        }
        
        if (out_pos >= 16) {
            printf("\rRESULT       \n");
            printf("%lld\n", reg_a_potential);
            break;
        }
    }
    
    auto stop = std::chrono::high_resolution_clock::now(); 
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start); 
    printf("Time %.3fms\n", duration.count() / 1000.0);
}