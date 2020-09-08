# Python Collaboration exercise

## Overview
Your goal is to make a single-player Tic-tac-toe game by applying the feature branch workflow!

## Detailed specs

0. The player will use 'O' and the computer will use 'X'. Ignore the ' . ' symbols inside boards below, they are just there to format the table in Markdown.

1. When the project is run through Terminal, it should first display a 3x3 empty board (shown below) and prompt a message ```Your move:``` for the user to input their first move.

<table>
  <tr>
    <td>.</td>
    <td>.</td>
    <td>.</td>
  </tr>
  <tr>
    <td>.</td>
    <td>.</td>
    <td>.</td>
  </tr>
  <tr>
    <td>.</td>
    <td>.</td>
    <td>.</td>
  </tr>
</table>

> Your move: 

2. The user will then input the coordinates of their first move, using the coordinate system shown below.

<table>
  <tr>
    <td>3</td>
    <td>.</td>
    <td>.</td>
    <td>.</td>
  </tr>
  <tr>
    <td>2</td>
    <td>.</td>
    <td>.</td>
    <td>.</td>
  </tr>
  <tr>
    <td>1</td>
    <td>.</td>
    <td>.</td>
    <td>.</td>
  </tr>
  <tr>
    <td>0</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
  </tr>
</table>

For example, if a player inputs (2, 2), then the board will look like the following:

<table>
  <tr>
    <td>.</td>
    <td>.</td>
    <td>.</td>
  </tr>
  <tr>
    <td>.</td>
    <td>O</td>
    <td>.</td>
  </tr>
  <tr>
    <td>.</td>
    <td>.</td>
    <td>.</td>
  </tr>
</table>

3. Your program should then output the current board, select a random spot on the board, and output the new board along with the message ```Your move: ```

For example, the computer selects (3, 2) and outputs

<table>
  <tr>
    <td>.</td>
    <td>.</td>
    <td>.</td>
  </tr>
  <tr>
    <td>.</td>
    <td>O</td>
    <td>X</td>
  </tr>
  <tr>
    <td>.</td>
    <td>.</td>
    <td>.</td>
  </tr>
</table>

> Your move:

4. Continue to take user input and generate computer output until there is a winner (three symbols connected together horizontally, vertically, or diagonally). When there is a winner, print the statement ```You Win!``` if the user wins, or ```You Lose``` if the computer wins.

For example,

<table>
  <tr>
    <td>O</td>
    <td>X</td>
    <td>X</td>
  </tr>
  <tr>
    <td>O</td>
    <td>O</td>
    <td>X</td>
  </tr>
  <tr>
    <td>.</td>
    <td>.</td>
    <td>O</td>
  </tr>
</table>

> You Win!


5. If all spaces in the board is filled, print the final board and output the following message ```It's a draw!```
 
For example,

<table>
  <tr>
    <td>O</td>
    <td>X</td>
    <td>O</td>
  </tr>
  <tr>
    <td>X</td>
    <td>O</td>
    <td>X</td>
  </tr>
  <tr>
    <td>O</td>
    <td>X</td>
    <td>O</td>
  </tr>
</table>

> It's a draw!

## Hints
You will definitely need the following methods:

1. Input Scanner - to scan the user input
2. Input Parser - to parse the user input and apply it to the game
3. Random Computer Algorithm - to randomly select a random move
4. Win/Lose/Draw Detector - to end the game and notify the user

The rest is up to you!
