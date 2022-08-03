## What is this?

This is the "Eat-them-all" game!

## Why do we need it?

This game is used to demonstrate different search algorithms in "AI crash course: Search" lecture.

## How to install all dependencies?

Run `make install` in your terminal (MacOS and Ubuntu based distros supported):

    ```
    $ make install
    ```

## How to play the game?

Run `make run` in bash console:

    ```
    $ make run
    ```

There are 2 ways to play this game:

- use keyboard
- write computer program (agent) that will play this game

By default, the game will start in keyboard mode. Keyboard controls:

- arrows keys to move the pacman
- 'R' to restart the level
- 'N' to skip the level
- 'Q' to quit the game

To run your agent, add the argument `agent` to the game start command like this:

```
$ make run agent=random_walk_agent 
```

To start the game with your agent, put your agent to the ./agents folder and run the game with the name of class of your agent!

### Game goal

Target of the game is to get maximum score in the end! All scores of completed levels will be summed up for the finish score.

### Game rules

Pacman will move into pressed key direction. Each step of pacman will decrease the score by 1 unit. Each bump into the wall will not only stop pacman but also decrease the score by 3 units. Each small dot eaten by pacman will increase score by 10 units. Each finished level will add 20 units to the final score.

## Who is the author?

Evgenii Tsatsorin - eugtsa@gmail.com - evgenii.tsatsorin@behavox.com