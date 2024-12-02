#include <cstdio>
#include <chrono>   
using namespace std;

char* ALG = "#.#..##...###..#.#....#######.###..#.#.##.####.###.####.#..###..##..#..##.######...####..#.#...##...##.#####.#....##.###.##..#####....####..###..#.#......##....#####..#.###...###..##.#..#.#....##...#.#.#..#.###..###..#..#...##..##.###...###.......##.##..##.#.##.....####..##..#..##..#.##.##...##.#.##..###.#..##.#.##..######....#.##.#.........#..#.#.#..###..#.#...#....#.#.#..###.........####.#.###.#.####...#..#..#...#####.##..........#.##.#.#.###....#.#.#.#.#.....##...#.#...###...##...##.#..######..###.###.#.";
int DATA_WIDTH=100;
int DATA_HEIGHT=100;
char* RAW_DATA = ""\
".##.#...#.#.##.##.#.#.#.##..#.#..###..##..##...#....#..###..#...#...######.###..#..#.#####.###...#.#"\
".#.###..#..#...#...#..#.#.##...##......##......#.#.#####....#..##.#.#..#..##.#..###.##..#..#.###.#.#"\
"#.#.....####.###.#.##.#...##..####..#...#.#...##.#.#.#.#.##.###.###.#.#.###..######......###.#.#.##."\
"#..#####.###........#..#..#...##.#.##.#..#.....####.#...#..#.#.###..#..###.......#.#......#.##.#.#.#"\
"###..#...#..#.##..#####.#.#..#...#.##..###.#..#.#....#..##.#...#.#.##..###.....###.##.###.#...###..#"\
"....##...####...#.##.#.#..##.####..#.#.#.......#.########.#...#..#.##..#.####.#...####...##.#..#...#"\
"..#.#.##.##..###.##.#.####.#.#######...#.####.###.###.....#.#..##.....#...###.#.#.#.########..##.#.."\
".#####.#.#.##.#.#.###.#.####..##.##.##.#.....#.###.##.#..########..#...#...####.###.#..###.#.#.####."\
"#...##.#.##.#....#.###.#.#.#.#..###.##.##.#..#####...##.###...#...#.###.##............###..#..###..#"\
"..#.####....##..#.##..##...#..#....#.###.##.#.#..########.##...##.#..####..#...#.#.####..#.....#.#.#"\
"...###..#.#..#...###.#.......#...##..##.##.#####....###.#######..##.#.####.#.##.#.##.#.#.#.....##.#."\
"#..#.#.##.#...#.###.#..#.#...#.##.##.....##...#.#....###..####..######.##..######..#..#.##...######."\
"#####.######........#.###....###..##.#.###.###.#...###.##.....#.........####.###..###...####.##....."\
"##.###..#..#.#.##.#.....#.##...###.#..#####.#..##...#.......###...#.##.##.#####...#...#.....#.##..##"\
".#####.......#..##.....#####.#.#.#.##.#..##......#..#....###.####..##...##..##.####.#.#.....#.#.#..."\
".##.#...##..#.#####.#...#..#.###..#.#.####...#...#.#..####.#.......###.##.##.#.###.....#####.##....#"\
"#..####..##.#.#.#.#.#####.###..######..#....#####....#...##...#...####..##.#....#.#..#.##..#.##.##.#"\
"......##..#..#...#..#.#.###.#.##.#.###..##.##.###.#....#######.....###.###.###.##.#.#.###..#.###...."\
"#.#.###.##.##..#.###..###.##....#.#.###.##.#...#...#..#.#.#...#.##..#....#.##.######.#.#....#####.#."\
"###.#.#.#...#.##....#.##..#.#....#..#.#........#.#####..#.#.......###.##...####..#..##.#....##.#...#"\
"#..####..###.#.#..##.....##..#.#..#######.##..###.##..#.#..###...###.#######..#..####.#.######.#.###"\
"#....#####.##.#.#..#....#.#.#.#..####.....#..###.####.######...#..#######.##...##.#.###..#....#####."\
"#.#..#.#..#.....#..#.#...#..###..##...##..####.....##.#.#.##.#.#.#.##.###.###.###.#..........####..#"\
"##..#########.###.#.......####.#...##..##.##.#.##.#.####..#..#...##..#......#...##...#.#..#.##....#."\
"#...#....#..#.####.##..#.##.#..#.#..##....#..#..##.#.#....##.####.##.#.#.#..#.#.#..###.#.#.#.###.###"\
".#.#.###.#...#...##.####..#...#######...###..#...#...##.##...#..#.#..#.###..#.###.....##.##.#..####."\
"..###...##.##..##.#..#.####.#..#.#.#.#.#.#.##...####.###.#....#..###..#.#....##..##.######...#.#...."\
"....####.#.#.###.####.###.##..#..#.##.#.######..######.###..#..#.####.###.#.#.#...##.#.##.##.####..."\
"#.....#######..###.#.....####..#...#.....#....#.#...##.##..##.#.###...##....##..#.#.##.#..##....####"\
"#.#.###..##.#.....#.##.##.##.##.###..####.#...##...##...##..####.##.#......###...##.#####.###...##.#"\
"#.###.#..###....##.....#....##...##.#..#..##..#.##.##.....#..##.....#....###.##...##.#..####....###."\
"##.##..##.###...###..##.#..#..###....###.##.#..#.#.##....#..#.#####..##...#.##........###...#.#.####"\
".##.##..####...######.##......#...###.##..#...##..#..#.#...#...#.#....#.#...#.####.....##.#.#...##.#"\
"#.#.##...#..#..#.###.###.#...#.###.#.##..#.###.##.#...###.....#.#.#..#.##.#.#.##....#.#..###...#...."\
".#.#...#..##..##.#...#..###.##.#..##...#..#..#....#..#.#...#..##.#.#.#########..#.##...##...#.##.##."\
"..##.#..#.#.#..#..#.#..#.#.####.#....#..##.#.#.#..#..##...#.##.......#..###..#####..#####..#..#..##."\
".#..##.......#.....#..####..#.....###.####..##.##.#.####..#..#.#.....####..###.####.####.###..#.##.#"\
"...###....#..##..####...##..#...#.##.#.##..###.#.#..##..##.#....#.......#....#.#...#...#.#.#..##..##"\
"#.##.#..##.#.#...###.#.###..#####.##.###.#.#......#..#.#.....##...#..##..###.......#...#..#...##...#"\
".###.#..####.###..#.#.##..#.#..##..#####.#.##.#.#...#...##.##.#....###....##..#.#...###..##..#..#.##"\
"###..###.##.#...###.#..#....######....#.#.##.#.#.#..##.#..........#..#######....#..##...##..#..#.###"\
"..#..###.#.#.....#####.##.###.##.#.#...........#.#..##.####...#.....##.#...##.#..##...##.##..##...##"\
"##...#.####..#.####.####..#.##.#..##..#.#...##.#..##.###..####..#.###..####...####.##.......#.##.###"\
"#.##...###.#.##.######.##.#..#######....#...#....##.#.###.####...#.###....####...#.#.#..#..#.....#.."\
"#.####..#.#..###.#..#.#.#..#.#...#.####..#.#..##.#...#....#..##..####..##.##.............#.###.#..##"\
"..##..#..#.#.#.##.##.#.#....#..#...#.##.##..#.....##.####.....##.###.....##.########....#..###...##."\
"###..##...#.#####.#...#####..#####...##.#.##...###.....##..#..##.#...###...######.###.#..##...#...##"\
"..#.##....##.#.....####..#..#....#...###.....##..###.#.###...####......#.##.#######..#..#..####..#.#"\
"##.##.###.#......##..#.###.#...########...#...#..####..##..####.#....#.###.#.#.#..#####.#..#..#..#.."\
"#....##...##.#.........##.#.####.#.####.##.#...#...##...#..##..##..#....#.####.##.#.#.#####....#...#"\
".###..#..#.#####..####.....##..##..##.#...########..##..###..#...##..#.##..#.##..##..###.#.#......#."\
"####.##.###.##..##...#..###.#.###..#.##..#.###.#.#.#.#..##.##..#.....##.##....####.#...#.##......###"\
"....#########...#.#...##....###.#...#####....###.#.....##.#..........##.####..##..#.#.#......#..#..."\
"##.#.#..###.##...##.#.#....#.###.####.#.#.##.#..##...####.#..##..#..####.##.##....####.####...#.###."\
"...#...#......#.#.##.##.#.....#.#####...###.#...#.#..#...#.##....#..###.....#.#.#.##..#....#.#####.."\
"..#.#...#...#..##.##..#..#.#..#.#.##.#..##..##.###.#....#....##...#.#.##..##...#.....#.###.###.##..#"\
"#..###..#....###...##.#.###...#...####.###.####..#...#.##.#..#.##....#..##.....#.##....#.###..#.##.#"\
"....##.#.#.##.#.#..#..###.#####...##.#..#.#.###...#..#..##.##.###..##..####..####...##.#..#.....#..#"\
".###.#.#.#.#.###.###.#.###.#.####....#.##.#.##.#.##......##.....##..#.##.#...#.#....#.#######..##..."\
"..#....#...##.#.#..#.#####...#..#####..#..################.###..##.#.##...#.#..##.##...#.####...#.##"\
"....#..#.#..#..####..##.#...####..#.#......##..##.###.####.##..###.#.##.#.#..#..#.#...#..###.###...#"\
"##.#.###.#......#..#.#..#####.#####.....#..#.###..##...#.####.......####.#.##..#......#.###..#.#..##"\
"#.#.#.####.###...##....#..#..#....##.##..##......####.##.#......###.#..###.#..####.....#..#...#....#"\
"####.##.....#.##..##......#...##.#.##...##...#.#..##.#.###.#..##.#######.#####....#.#.#####...#.#.##"\
"#####.......#.#.###.#.#.#.#.###.##.#..##.......##.#....#.#.#####.#.#...#.#.###..#..##..#...###..#..."\
"...##....#...#.###......##.##..#........#####..#..##...#######.###.####.#..##..#..###.#.#.#...#.####"\
"#######...####.##.###...##.####..####.#.##.###..#.#######.....###..#.#...#.####.####.##.....#####..."\
"...#....#.#...##.#.#..#...###...##.#.#.#..#.####.#....#.##.#.#...#.###......#..###.###.#####.####..#"\
".#.##.#########.#..#.#.#..#.#.#..##..####.##...##....#.#.##.#.#.###..#.#...#.#..###.##.###..##.....#"\
"##.#..#.###.#..####.....#......#..##.#.##.##.###...#.#..###.#.#.#..#..#.###.....###..########...#..."\
"#.#....#.##.#.#.#....###.#....###.#....#...###.#.#..#....##....#####.#.#.######.##.#.##....#.##.##.#"\
"###..#.#.##.....##.#.#....####.#..##....##.#..###.....###..#.#.####..#..#.#.#.###..###.####.#.#..#.."\
"##.####.#..#...#######.#...##.####...#..#...##.#....##..##...#..##....###.#.##..#..#.#.......##.####"\
"...####.#..##.##....#.#...#.###########.#.#..##...#.####.###.....###.....####.##.###.#####.######..#"\
".##..##.###....##.#..##..##..##.#...######.##.##..###.#..#.###.#.####.#..##.#..##..##.#####.#.####.."\
"#..##.....####..##.#.##.###.....####.#..##...###.####.###.##.#..####..###.#########.##..##....##..#."\
".#.###...#.##.#.#.#.#....#..##..##.##...##..#.######.#..#....##...##..###.....#.......##.....#.#...."\
"........#...#.##.#.....#..#.#####..#........#..###..........##...#.#.#.#.........##...#..#....#..#.#"\
"..........#...#####...#.####.###...##..#.##.#.#..#........#.####.#.#.....####..#######....##.#....##"\
"....#####.####.####..#.#...#.#....#.#.#######.#.####..#####.#.###.####..#.#.##.###..##.#.####.####.."\
"..####..#..###.#.##...#####...#.###.##.#.#....##..#.##.#####.##....#.#####..#...#.#....#.####.....#."\
"#...##..#...#...####...#.###...###.#..###.#.#...######..####..#.#.#.###.####.##.#.####.#....#..#.#.#"\
"###.##.#.....##.#.#.##..##..####...##..####...###..#.####.##...###.###.###.##..###.....###.#......##"\
".#..###.#..#..#..####.#.##.#.#.#.#.#...#.#.#......##.#.#..###.#....#.#..##.########.###..#..##.##..."\
"..#.#..###.##.##.#....#.#..###.##.....##...##...##..#..#.###.#.#.#.#.#.....##.#..##.#.#.#..#..#.#.#."\
"#.....##.##.....##....#.#.#.##.##..##..#.#..##.##......#.##..#.##.###..#..#..#.##...#.#.#...#.#.##.."\
"###.####...##.#...##..#..#.####..##..#.#.###.###.#.##..#####.#...#..##.####..####..#.#..#..###..#..#"\
"#.##.#...##....###.##..######...#.#.#####.#.##..#.###.####.##.#..##.#.#.#......#........####.#..#..#"\
"#.###.#...#####.######.##...####.#.#.#......##.##..#....#..#.###..####.#..#.#.#....#...##...#.####.."\
"..##...#..##......###.###.#..##.#.##.##..#######.#.....##..#....#.#.#.#####..#.#....##.##.#.#.##.#.."\
"#.##...#.#.##....##...##...##..#..##..##...#.#.##########..#####..##.####..#..#.#.......##.....#####"\
"###...##.##...#.#..#.##.#.##.#.#..#####.#....#...#...###.#.#.#.....##.#....##..#.#..#.#...#.#...#..#"\
".#.##..#####...###.#..#####..##....##.###.#..##....###..#.........#....#..##...##.##...##.######.#.."\
"##.##.#.###..#.##..#####..#.##.#...#...##..#......#.#..####.#.###.#.###...#.###..#.##.##....#..##.#."\
"...........##....##...####......#...#.#.#..##.#.#..#####..#...###......#####.#.##.###.#######.#.###."\
"...####.########.###..####..#.#.#.######.#..#.#####.####.######..##..##..######.#....##..#.##.##.#.."\
"#.#..#..##..#..###.#...#..##..##.#..####......#.....#.#..#...#.##.....##....##..#..#.###....##......"\
".###.####...#.#...#.#.###..#..#####.#..#...##.###.#.##.#.##...##....##..#.#.#..#.#..#........###...."\
"#.#..###.##.....#.##.#..##.##.###......#..####...#####.......####.#..##..####...#..##.##..#.##...###"\
"####.##.#...#.##...####...######.#.#.#.##.##.#...##..#.#..#.#.#.#.#.#.....##..##....#.#..###..#.###.";

int main(int argc, char *argv) {
    auto start = std::chrono::high_resolution_clock::now(); 
    
    int NN = 50;
    int BORDER = 2 * NN;
    int WIDTH = DATA_WIDTH+2*BORDER;
    int HEIGHT = DATA_HEIGHT+2*BORDER;
    char* data = (char*) malloc(WIDTH * HEIGHT * sizeof(char));
    char* new_data =  (char*) malloc(WIDTH * HEIGHT * sizeof(char));
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            data[i * WIDTH + j] = '.';
        }
    }
    for (int i = 0; i < DATA_HEIGHT; i++) {
        for (int j = 0; j < DATA_WIDTH; j++) {
            data[(BORDER + i) * WIDTH + BORDER + j] = RAW_DATA[i*DATA_WIDTH + j];
        }
    }
    
    for (int n = 0; n < NN; n++) {
        if (n == 2) {
            int total = 0;
            for (int i = NN; i < HEIGHT-NN; i++) {
                for (int j = NN; j < WIDTH-NN; j++) {
                    if (data[i*WIDTH + j] == '#') total += 1;
                }
            }
            
            printf("20-a: %d\n", total);
        }
        
        for (int i = 0; i < HEIGHT; i++) {
            new_data[i * WIDTH + 0] = '.';
            new_data[i * WIDTH + WIDTH-1] = '.';
        }
        for (int j = 0; j < HEIGHT; j++) {
            new_data[0 * WIDTH] = '.';
            new_data[(HEIGHT-1) * WIDTH] = '.';
        }
        for (int i = 1; i < HEIGHT-1; i++) {
            for (int j = 1; j < WIDTH-1; j++) {
                int index = 0;
                if (data[(i-1)*WIDTH + j-1] == '#') index += 1;
                index *= 2;
                if (data[(i-1)*WIDTH + j] == '#') index += 1;
                index *= 2;
                if (data[(i-1)*WIDTH + j+1] == '#') index += 1;
                index *= 2;
                if (data[(i)*WIDTH + j-1] == '#') index += 1;
                index *= 2;
                if (data[(i)*WIDTH + j] == '#') index += 1;
                index *= 2;
                if (data[(i)*WIDTH + j+1] == '#') index += 1;
                index *= 2;
                if (data[(i+1)*WIDTH + j-1] == '#') index += 1;
                index *= 2;
                if (data[(i+1)*WIDTH + j] == '#') index += 1;
                index *= 2;
                if (data[(i+1)*WIDTH + j+1] == '#') index += 1;
                new_data[i*WIDTH + j] = ALG[index];
            }
        }
        char* old_data = data;
        data = new_data;
        new_data = old_data;
    }
    
    int total = 0;
    for (int i = NN; i < HEIGHT-NN; i++) {
        for (int j = NN; j < WIDTH-NN; j++) {
            if (data[i*WIDTH + j] == '#') total += 1;
        }
    }
    
    printf("20-b: %d\n", total);
    
    free(data);
    free(new_data);
    
    auto stop = std::chrono::high_resolution_clock::now(); 
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start); 
    printf("Time %.3fms\n", duration.count() / 1000.0);
}