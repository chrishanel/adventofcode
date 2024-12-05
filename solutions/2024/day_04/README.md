# Day 4 (2024)

`TITLE` ([prompt](https://adventofcode.com/2024/day/4))

Use this space for notes on the day's solution and to document what you've learned!

## Part 1

Oh my god this problem is the reason why this event can sometimes feel maddening.

I'm looking at this as a word search puzzle, so naturally i wanna have a grid. That means a 2D array. That means using numpy, right?

So i jump through a ton of hoops and spend a lot of time researching using numpy, getting the grid set up, and then creating the function to iterate through it and locate the 'XMAS' instances. And it takes like 10 minutes to run.

And then I look online and someone's done the same thing with 6 lines and it runs instantly, and I have zero motivation to try and refactor when it basically means starting over.

The code included in today's solution file is the 6 line thing instead of the O(n) abomination that I started with.

Total time spent: About 2 hours.

## Part 2

