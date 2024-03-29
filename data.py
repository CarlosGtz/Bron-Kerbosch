#!/usr/bin/python
NEIGHBORS = [
    [], # I want to start index from 1 instead of 0
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
    [2, 3, 4],[1, 3, 4, 5],[1, 2, 4, 5],[1, 2, 3],[2, 3, 6, 7],[5, 7],[5, 6],[5, 6, 7],[1,2,4,6,7],[2,4,6,8],[1,3,5,7],
]
NODES = set(range(1, len(NEIGHBORS)))