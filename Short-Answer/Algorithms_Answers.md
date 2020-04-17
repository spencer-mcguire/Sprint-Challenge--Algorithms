#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) because it is linear.

b) O(n^2) becuase the operations are the square of the input size as such with nested loops.

c) O(n) because it recursively moves towards the base case.

## Exercise II

Write a function that takes in `n` as stories and outputs `f` as the floor where eggs begin to break

I need to check at which point in n stories do eggs begin to break then return f as the floor.

- Write a for loop to loop through n-stories
- as it loops drop an egg
- if the egg breaks return f as the floor where eggs begin to break
- else keep dropping eggs as the stories increase

This would be O(n) becuase the time complexity would be linear as the input increases.

# TO MINIMIZE NUMBER OF EGGS DROPPED

Start by // n to find the middle floor

Drop an egg - if comes back broken f // 2 to half the floors again and start over - if comes back not broken go the other way. find floor between middle floor and top floor, drop again

Stop when there is only one floor left as this is now the only floor it can be dropped from.

Time complexity would be O(log n ) because this is a bianary seach that increases number of operations in a log fashion of n.
