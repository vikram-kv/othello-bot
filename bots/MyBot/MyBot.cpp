/*
 * @file botTemplate.cpp
 * @author Arun Tejasvi Chaganty <arunchaganty@gmail.com>
 * @date 2010-02-04
 * Template for users to create their own bots
 */

#include "Othello.h"
#include "OthelloBoard.h"
#include "OthelloPlayer.h"
#include <cmath>
#include <cstdlib>
#include <vector>
#define BOARD_SIZE 8
#define MAXPLAYER 1
#define MINPLAYER -1
#define MAXDEPTH 5
#define NINF -100000000
#define INF 100000000
using namespace std;
using namespace Desdemona;

class MyBot : public OthelloPlayer {
public:
    /**
     * Initialisation routines here
     * This could do anything from open up a cache of "best moves" to
     * spawning a background processing thread.
     */
    MyBot(Turn turn);

    /**
     * Play something
     */
    virtual Move play(const OthelloBoard &board);

private:
    double evaluateLeaf(OthelloBoard &board, int pType);
    double alphaBeta(OthelloBoard &board, int ptype, double alpha, double beta, int depth);
    Coin myColor;
    Coin oppColor;
    int player;
    Move bestMove;
    vector<vector<int>> weights; // weights for leaf node evaluation
};

MyBot::MyBot(Turn turn) : OthelloPlayer(turn), bestMove(-1, -1) {
    // weights for eval function
    weights.resize(8);
    weights[0] = {4, -3, 2, 2, 2, 2, -3, 4};
    weights[7] = {4, -3, 2, 2, 2, 2, -3, 4};

    weights[1] = {-3, -4, -1, -1, -1, -1, -4, -3};
    weights[6] = {-3, -4, -1, -1, -1, -1, -4, -3};

    weights[2] = {2, -1, 1, 0, 0, 1, -1, 2};
    weights[5] = {2, -1, 1, 0, 0, 1, -1, 2};

    weights[3] = {2, -1, 0, 1, 1, 0, -1, 2};
    weights[4] = {2, -1, 0, 1, 1, 0, -1, 2};

    myColor = turn;
    oppColor = other(turn);
}

double MyBot::alphaBeta(OthelloBoard &board, int ptype, double alpha, double beta, int depth) {

    Coin pColor = ptype == MAXPLAYER ? myColor : oppColor;

    if (depth == 0) {
        return evaluateLeaf(board, ptype);
    }

    list<Move> moves = board.getValidMoves(pColor);
    // handling skipped turns
    if (moves.size() == 0) {
        return alphaBeta(board, -ptype, alpha, beta, depth - 1);
    }

    double value;
    if (ptype == MAXPLAYER) {
        value = NINF;
        for (auto it = moves.begin(); it != moves.end(); ++it) {
            OthelloBoard bcopy = board;
            bcopy.makeMove(pColor, *it);
            double moveValue = alphaBeta(bcopy, -ptype, alpha, beta, depth - 1);
            if (moveValue > value && depth == MAXDEPTH) {
                value = moveValue;
                bestMove = *it;
            }

            alpha = max(moveValue, alpha);
            if ( beta <= alpha) {
                return beta;
            }
        }
        return alpha;
    } else {
        value = INF;
        for (auto it = moves.begin(); it != moves.end(); ++it) {
            OthelloBoard bcopy = board;
            bcopy.makeMove(pColor, *it);
            double moveValue = alphaBeta(bcopy, -ptype, alpha, beta, depth - 1);

            if (moveValue < value && depth == MAXDEPTH) {
                value = moveValue;
                bestMove = *it;
            }

            beta = min(moveValue, beta);
            if (beta <= alpha) {
                // return value;
                return alpha;
            }
        }
        return beta;
    }
}

double MyBot::evaluateLeaf(OthelloBoard &board, int ptype) {

    /* static weight heuristic to cells */
    double static_heuristic = 0;
    for (int i = 0; i < BOARD_SIZE; ++i) {
        for (int j = 0; j < BOARD_SIZE; ++j) {
            Coin col = board.get(i, j);
            if (col == myColor) {
                static_heuristic += weights[i][j];
            } else if (col == oppColor) {
                static_heuristic -= weights[i][j];
            }
        }
    }

    /* coin parity */
    double parity = 0;
    double diff = 100 * ((double)(board.getBlackCount() - board.getRedCount())) / ((double)(board.getBlackCount() + board.getRedCount()));
    if (myColor == BLACK)
        parity += diff;
    else
        parity -= diff;

    /* mobility */
    // actual mobility
    double mobility = 0.0;
    int myMobility = board.getValidMoves(myColor).size();
    int opMobility = board.getValidMoves(other(myColor)).size();
    if (myMobility + opMobility != 0) {
        double n = (double)myMobility;
        double m = (double)opMobility;
        mobility = (100.0 * (n - m)) / (n + m);
    }
    // potential mobility

    /* corners captured */
    int myTiles = 0, oppTiles = 0;
    board.get(0, 0) != EMPTY &&board.get(0, 0) == myColor ? myTiles++ : oppTiles++;
    board.get(0, 7) != EMPTY &&board.get(0, 7) == myColor ? myTiles++ : oppTiles++;
    board.get(7, 0) != EMPTY &&board.get(7, 0) == myColor ? myTiles++ : oppTiles++;
    board.get(7, 7) != EMPTY &&board.get(7, 7) == myColor ? myTiles++ : oppTiles++;
    double corner_heuristic = 0;
    if (myTiles + oppTiles > 0) {
        corner_heuristic = 25.0 * ((double)(myTiles - oppTiles));
    }

    /* stability */

    double score = 10 * parity + 801.1 * corner_heuristic + 79.1 * mobility + 10.0 * (static_heuristic);
    return score;
}

Move MyBot::play(const OthelloBoard &board) {
    OthelloBoard boardcopy = board;
    alphaBeta(boardcopy, MAXPLAYER, NINF, INF, MAXDEPTH);
    return bestMove;
}

// The following lines are _very_ important to create a bot module for Desdemona

extern "C" {
OthelloPlayer *createBot(Turn turn) {
    return new MyBot(turn);
}

void destroyBot(OthelloPlayer *bot) {
    delete bot;
}
}
