# 535-project2
It's a small world

Group members:

Kunal Chhatrapati Student ID: 885792390

Vallari Rajurkar Student ID: 885734566

Gouri Sabale  Student ID: 885189761

Summary: 

The report's primary focus is the Small World/Shortest Connection problem. Finding the shortest connection between two casts is the objective of this project. One must determine whether there is a common link between two casts to determine the shortest connection between them. The shortest link is one if there is a common string between the first two casts. If two casts don't have common strings, search for another cast in the list. If the other cast has exactly one common string in the first cast and one string common in the second cast, then the shortest connection is 2. Otherwise, the shortest connection is greater than two, or there is no connection.

Problem Statement:

In this problem, we are given two casts for two movies, and we have to find out what is the shortest connection between the two casts.
Given an input should be a positive integer n>2.
A list of n casts from which the first two sets are more significant, CAST[0]  and CAST[1]. If two casts CAST[0] and CAST[1] have at least one string in common, then the shortest connection is 1.
If the two casts CAST[0] and CAST[1] don’t have any string in common, then look for another cast in the list of n casts; lets called it tempCast, such that CAST[0] and tempCast have a string in common, and CAST[1] and tempCast have a string common, then the shortest connection is 2.
Else the shortest connection is greater than two or there is no connection.
