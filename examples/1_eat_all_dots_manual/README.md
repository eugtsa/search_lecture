## What is this?

This is the "Eat-them-all" game!

## Why do we need it?

This game is used to demonstrate different search algorithms in "AI crash course: Search" lecture.

## How to install all dependencies?

Run `make install` in your terminal (MacOS and Ubuntu based distros are supported):

```shell
make install
```

## How to play the game?

Run `make run` in bash console:

```shell
make run
```

There are 2 ways to play this game:

- use keyboard
- write computer program (agent) that will play this game

By default, the game will start in keyboard mode. Keyboard controls:

- arrow keys to move the pacman
- 'R' to restart the level
- 'N' to skip the level
- 'Q' to quit the game

Add the argument `agent` to the game start command to run your agent. For example:

```shell
make run agent=random_walk_agent 
```

To start the game with your own custom agent put your agent to the ./agents folder. Agent module should be named in underscore notation (my_custom_agent) and agent class in it should be named the same but in camel case notation (MyCustomAgent)

### Game goal

Target of the game is to get maximum score in the end! All scores of completed levels will be summed up for the finish score.

### Game rules

Each pacman step will decrease the score by 1 credit. Each bump into the wall will not only stop pacman but also decrease the score by 3 credits. Each small dot eaten by pacman will increase score by 10 credits. Each finished level will add 20 credits to the final score.

## Who is the author?

Evgenii Tsatsorin - eugtsa@gmail.com - evgenii.tsatsorin@behavox.com