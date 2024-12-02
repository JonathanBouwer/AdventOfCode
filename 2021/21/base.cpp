#include <cstdio>
#include <chrono>   
using namespace std;

struct Game {
    int p1;
    int p2;
    int p1Score;
    int p2Score;
    int turn;
    long long p1Mult;
    long long p2Mult;
};

struct Score {
    int move;
    long long mult;
};

int GOAL_SCORE = 21;

int main(int argc, char *argv) {
    auto start = std::chrono::high_resolution_clock::now(); 
    
    Game* games = (Game*) malloc(128 * sizeof(Game));
    Score* scores = (Score*) malloc(7 * sizeof(Game));
    scores[0] = {3,1LL};
    scores[1] = {4,3LL};
    scores[2] = {5,6LL};
    scores[3] = {6,7LL};
    scores[4] = {7,6LL};
    scores[5] = {8,3LL};
    scores[6] = {9,1LL};
    int currentGame = 1;
    games[0] = {8,6,0,0,1,1LL,1LL};
    long long p1Wins = 0;
    long long p2Wins = 0;
    while (currentGame > 0) {
        currentGame--;
        Game game = games[currentGame];
        if (game.turn == 1) {
            for (int s = 0; s < 7; s++) {
                Score score = scores[s];
                int newPos = (game.p1 + score.move) % 10;
                if (newPos == 0) {
                    newPos = 10;
                }
                int newScore = game.p1Score + newPos;
                if (newScore >= GOAL_SCORE) {
                    p1Wins += score.mult * game.p1Mult;
                } else {
                    games[currentGame] = {
                        newPos,
                        game.p2,
                        newScore,
                        game.p2Score,
                        2,
                        score.mult * game.p1Mult,
                        score.mult * game.p2Mult
                    };
                    currentGame++;
                }
            } 
        } else {
            for (int s = 0; s < 7; s++) {
                Score score = scores[s];
                int newPos = (game.p2 + score.move) % 10;
                if (newPos == 0) {
                    newPos = 10;
                }
                int newScore = game.p2Score + newPos;
                if (newScore >= GOAL_SCORE) {
                    p2Wins += score.mult * game.p2Mult;
                } else {
                    games[currentGame] = {
                        game.p1,
                        newPos,
                        game.p1Score,
                        newScore,
                        1, 
                        score.mult * game.p1Mult, 
                        score.mult * game.p2Mult
                    };
                    currentGame++;
                }
            }
        }
    }
    if (p1Wins > p2Wins) {
        printf("%lld\n", p1Wins);
    } else {
        printf("%lld\n", p2Wins);
    }
    
    free(scores);
    free(games);
    
    auto stop = std::chrono::high_resolution_clock::now(); 
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start); 
    printf("Time %.3fms\n", duration.count() / 1000.0);
}