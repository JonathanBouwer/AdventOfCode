#include <cstdio>
#include <chrono>

int range = 32;
int halfRange = 16;
int range2 = range * range;
int range3 = range2 * range;
int range4 = range3 * range;

int minx=0, maxx=0, miny=0, maxy=0, minz=0, maxz=0, minw=0, maxw=0; 

int getBoardIndex(int x, int y, int z, int w) {
    return (x + halfRange) * range3 + (y + halfRange) * range2 + (z + halfRange) * range + (w + halfRange);
}

void setBoard(int x, int y, int z, int w, int *board) {
    board[getBoardIndex(x, y, z, w)] = 1;
    minx = minx < x ? minx : x;
    maxx = maxx > x ? maxx : x;
    miny = miny < y ? miny : y;
    maxy = maxy > y ? maxy : y;
    minz = minz < z ? minz : z;
    maxz = maxz > z ? maxz : z;
    minw = minw < w ? minw : w;
    maxw = maxw > w ? maxw : w;
}

int main(int argc, char *argv) {
    auto start = std::chrono::high_resolution_clock::now();
    int *board = (int *) malloc(range4*sizeof(int));
    int *newboard = (int *) malloc(range4*sizeof(int));
    memset(board, 0, range4*sizeof(int));
    memset(newboard, 0, range4*sizeof(int));
    int width = 8, height = 8;
    char *a = "####.#.."\
              ".......#"\
              "#..#####"\
              ".....##."\
              "##...###"\
              "#..#.#.#"\
              ".##...#."\
              "#...##..";
        
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            if (a[i * width + j] == '#'){
                setBoard(j, i, 0, 0, board);
            } 
        }
    }

    for (int i = 0; i < 6; i++) {
        int startw = minw - 1;
        int startz = minz - 1;
        int starty = miny - 1;
        int startx = minx - 1;
        int endw = maxw + 2;
        int endz = maxz + 2;
        int endy = maxy + 2;
        int endx = maxx + 2;
        for (int w = startw; w < endw; w++) {
            for (int z = startz; z < endz; z++) {
                for (int y = starty; y < endy; y++) {
                    for (int x = startx; x < endx; x++) {
                        int sum = 0;
                        for (int zi = z - 1; zi < z + 2; zi++) {
                            for (int yi = y - 1; yi < y + 2; yi++) {
                                for (int xi = x - 1; xi < x + 2; xi++) {
                                    int index = getBoardIndex(xi, yi, zi, w);
                                    sum += board[index+1] + board[index] +  board[index-1];
                                }
                            }
                        }
                        int boardVal = board[getBoardIndex(x, y, z, w)];
                        sum -= boardVal;
                        if (sum == 3) {
                            setBoard(x, y, z, w, newboard);
                        } else if (sum == 2 && boardVal == 1) {
                            setBoard(x, y, z, w, newboard);
                        }
                    }
                }
            }
        }
        
        int *oldboard = board;
        board = newboard;
        newboard = oldboard;
        memset(newboard, 0, range4*sizeof(int));
    }
    
    int total = 0;
    for (int i = 0; i < range4; i++) {
        total += board[i];
    }

    printf("%d\n", total);
    free(board);
    free(newboard);
    auto stop = std::chrono::high_resolution_clock::now(); 
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start); 
    printf("Time %fms\n", duration.count() / 1000.0);
}