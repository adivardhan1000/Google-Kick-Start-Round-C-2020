# Google-Kick-Start-Round-C-2020
Starter attempts. Only sample test cases working.

## test1:
Problem

Avery has an array of N positive integers. The i-th integer of the array is Ai.

A contiguous subarray is an m-countdown if it is of length m and contains the integers m, m-1, m-2, ..., 2, 1 in that order. For example, [3, 2, 1] is a 3-countdown.

Can you help Avery count the number of K-countdowns in her array?
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the integers N and K. The second line contains N integers. The i-th integer is Ai.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of K-countdowns in her array.
Limits

Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
2 ≤ K ≤ N.
1 ≤ Ai ≤ 2 × 105, for all i.
Test set 1

2 ≤ N ≤ 1000.
Test set 2

2 ≤ N ≤ 2 × 105 for at most 10 test cases.
For the remaining cases, 2 ≤ N ≤ 1000.
Sample

Input
  	
Output
 

3
12 3
1 2 3 7 9 3 2 1 8 3 2 1
4 2
101 100 99 98
9 6
100 7 6 5 4 3 2 1 100

  

	

Case #1: 2
Case #2: 0
Case #3: 1

  

In sample case #1, there are two 3-countdowns as highlighted below.

    1 2 3 7 9 3 2 1 8 3 2 1
    1 2 3 7 9 3 2 1 8 3 2 1

In sample case #2, there are no 2-countdowns.

In sample case #3, there is one 6-countdown as highlighted below.

    100 7 6 5 4 3 2 1 100
    
## test2:

Problem

Apollo is playing a game involving polyominos. A polyomino is a shape made by joining together one or more squares edge to edge to form a single connected shape. The game involves combining N polyominos into a single rectangular shape without any holes. Each polyomino is labeled with a unique character from A to Z.

Apollo has finished the game and created a rectangular wall containing R rows and C columns. He took a picture and sent it to his friend Selene. Selene likes pictures of walls, but she likes them even more if they are stable walls. A wall is stable if it can be created by adding polyominos one at a time to the wall so that each polyomino is always supported. A polyomino is supported if each of its squares is either on the ground, or has another square below it.

Apollo would like to check if his wall is stable and if it is, prove that fact to Selene by telling her the order in which he added the polyominos.
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing the two integers R and C. Then, R lines follow, describing the wall from top to bottom. Each line contains a string of C uppercase characters from A to Z, describing that row of the wall.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is a string of N uppercase characters, describing the order in which he built them. If there is more than one such order, output any of them. If the wall is not stable, output -1 instead.
Limits

Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ R ≤ 30.
1 ≤ C ≤ 30.
No two polyominos will be labeled with the same letter.
The input is guaranteed to be valid according to the rules described in the statement.
Test set 1

1 ≤ N ≤ 5.
Test set 2

1 ≤ N ≤ 26.
Sample

Input
  	
Output
 

4
4 6
ZOAAMM
ZOAOMM
ZOOOOM
ZZZZOM
4 4
XXOO
XFFO
XFXO
XXXO
5 3
XXX
XPX
XXX
XJX
XXX
3 10
AAABBCCDDE
AABBCCDDEE
AABBCCDDEE

  

	

Case #1: ZOAM
Case #2: -1
Case #3: -1
Case #4: EDCBA

  

In sample case #1, note that ZOMA is another possible answer.

In sample case #2 and sample case #3, the wall is not stable, so the answer is -1.

In sample case #4, the only possible answer is EDCBA. 

## test 3:
Problem

Cristobal has an array of N (possibly negative) integers. The i-th integer in his array is Ai. A contiguous non-empty subarray of Cristobal's array is perfect if its total sum is a perfect square. A perfect square is a number that is the product of a non-negative integer with itself. For example, the first five perfect squares are 0, 1, 4, 9 and 16.

How many subarrays are perfect? Two subarrays are different if they start or end at different indices in the array, even if the subarrays contain the same values in the same order.
Input

The first line of the input gives the number of test cases, T. T test cases follow. The first line of each test case contains the integer N. The second line contains N integers describing Cristobal's array. The i-th integer is Ai.
Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the number of perfect subarrays.
Limits

Memory limit: 1GB.
1 ≤ T ≤ 100.
-100 ≤ Ai ≤ 100, for all i.
Test set 1

Time limit: 20 seconds.
1 ≤ N ≤ 1000.
Test set 2

Time limit: 30 seconds.
For up to 5 cases, 1 ≤ N ≤ 105.
For the remaining cases, 1 ≤ N ≤ 1000.
Sample

Input
  	
Output
 

3
3
2 2 6
5
30 30 9 1 30
4
4 0 0 16

  

	

Case #1: 1
Case #2: 3
Case #3: 9

  

In sample case #1, there is one perfect subarray: [2 2] whose sum is 22.

In sample case #2, there are three perfect subarrays:

    [9], whose total sum is 32.
    [1], whose total sum is 12.
    [30 30 9 1 30], whose total sum is 102.

In sample case #3, there are nine perfect subarrays:

    [4], whose total sum is 22.
    [4 0], whose total sum is 22.
    [4 0 0], whose total sum is 22.
    [0], whose total sum is 02.
    [0 0], whose total sum is 02.
    [0 0 16], whose total sum is 42.
    [0], whose total sum is 02.
    [0 16], whose total sum is 42.
    [16], whose total sum is 42.

Note: We do not recommend using interpreted/slower languages for the test set 2 of this problem. 

## test 4:
Problem

Carl has an array of N candies. The i-th element of the array (indexed starting from 1) is Ai representing sweetness value of the i-th candy. He would like to perform a series of Q operations. There are two types of operation:

    Update the sweetness value of a candy in the array.
    Query the sweetness score of a subarray.

The sweetness score of a subarray from index l to r is: Al × 1 - Al+1 × 2 + Al+2 × 3 - Al+3 × 4 + Al+4 × 5 ...

More formally, the sweetness score is the sum of (-1)i-lAi × (i - l + 1), for all i from l to r inclusive.

For example, the sweetness score of:

    [3, 1, 6] is 3 × 1 - 1 × 2 + 6 × 3 = 19
    [40, 30, 20, 10] is 40 × 1 - 30 × 2 + 20 × 3 - 10 × 4 = 0
    [2, 100] is 2 × 1 - 100 × 2 = -198

Carl is interested in finding out the total sum of sweetness scores of all queries. If there is no query operation, the sum is considered to be 0. Can you help Carl find the sum?
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case begins with a line containing N and Q. The second line contains N integers describing the array. The i-th integer is Ai. The j-th of the following Q lines describe the j-th operation. Each line begins with a single character describing the type of operation (U for update, Q for query).

    For an update operation, two integers Xj and Vj follow, indicating that the Xj-th element of the array is changed to Vj.
    For a query operation, two integers Lj and Rj follow, querying the sweetness score of the subarray from the Lj-th element to the Rj-th element (inclusive).

Output

For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is the total sum of sweetness scores of all the queries.
Limits

Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ Ai ≤ 100, for all i.
1 ≤ N ≤ 2 × 105 and 1 ≤ Q ≤ 105 for at most 6 test cases.
For the remaining cases, 1 ≤ N ≤ 300 and 1 ≤ Q ≤ 300.
If the j-th operation is an update operation, 1 ≤ Xj ≤ N and 1 ≤ Vj ≤ 100.
If the j-th operation is a query operation, 1 ≤ Lj ≤ Rj ≤ N.
Test set 1

There will be at most 5 update operations.
Test set 2

There are no special constraints.
Sample

Input
  	
Output
 

2
5 4
1 3 9 8 2
Q 2 4
Q 5 5
U 2 10
Q 1 2
3 3
4 5 5
U 1 2
U 1 7
Q 1 2

  

	

Case #1: -8
Case #2: -3

  

In sample case #1:

    The first query asks for the sweetness score of [3, 9, 8] which is 3 × 1 - 9 × 2 + 8 × 3 = 9.
    The second query asks for the sweetness score of [2] which is 2 × 1 = 2.
    The third query asks for the sweetness score of [1, 10] which is 1 × 1 - 10 × 2 = -19.

Thus, the final output should be 9 + 2 - 19 = -8.

In sample case #2:

    The first and only query asks for the sweetness score of [7, 5] which is 7 × 1 - 5 × 2 = -3.

Thus, the final output should be -3. 
