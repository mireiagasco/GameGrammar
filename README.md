# Game Grammar Documentation
This game grammar is implemented as an assignment for the Formal Languages course at Universitat Rovira i Virigili (URV), 2024.
It uses ANTLR to define the grammar and check the correct formatting of the scripts, contained in the GameScripts folder.
The interpreter is coded in python and it obtains the information of the game script to generate a game like execution where the aim is to obtain the final_prize item.

## Execution Requirements
The python version used for this project is 3.8.10.
To properly execute this project it is required that ANTLR version 4.7.2 for python is installed. This can be done with the command:

``` pip install antlr4-python3-runtime==4.7.2 ```

Moreover, in case you want to regenerate the lexer, listener and parser for the grammar, you will need to execute the folowing command:

``` antlr4 -Dlanguage=Python3 GameGrammar.g4 ```

Once everything is set up, you can run the interpreter on any given ```.txt``` file that complies with the GameGrammar.g4 and interpreter rules.

## Grammar Description
Given that the aim of the grammar is to define a game with its room structure, items and actions, the grammar is based on the definition of those features.  We will now describe how each of them has to be defined.

### Room Definition
Rooms can have up to six attributes.  They must have a description, which is a string literal, and then they can have room connections on the four sides: norht, south, east and west. 
Those connections are optional, so a room can have from 0 to 4 of them.f  Additionally, the room can contain items, that have to be indicated in the items list.  The structure is as follows:

```
    room armory {
        description: "You enter the armory";
        south: ceremony_room;
        west: broken_staircase;
        east: exhibition_room;
        items: [shield]
    }
```


### Item Definition
The items also have a description, and then they can have a list of actions, indicating the actions that can be performed on them.
In case one of those actions requires an item to be performed, it will be indicated inside ```( )```.
Then, when an action that requires an item is performed, the ```secret_item``` of the item can be obtained, in case it exists.
Let's exemplify this with an example:

```
    item old_armour {
        description: "An old armour that has no emblem";
        actions: interact(emblem);
        secret_items: final_prize;
    }
```

In the previous example, when the ```interact``` action is performed on the ```old_armour``` object, if the player is in posession of the ```emblem```, the ```final_prize``` is obtained.



### Action Definition
The actions are the most simple feature to be defined, as they only need to be declared at the start of the game script.  For instance:

```
    action pickup {}
    action interact {}
    action open {}
```

The interpreter considers three important actions: ```pickup```, ```open``` and ```interact```.  The first one adds the item to the player's inventory, while open and interact both check if the player has the 
```required_item``` in its inventory and, if so, adds the ```secret_item```.



## Interpreter Description
It is important to note that the interpreter requires a ```start_room``` and a ```final_prize``` to be able to generate the game execution. 
The ```start_room``` is required because it will be the room where the player will be placed at the beggining of the game, and the ```final_prize``` is the item that makes the player win the game upon obtention.

## Execution Example
Here you can check the starting configuration generated with the ```game_script_v2.txt```, which can be found in the ```GameScripts``` folder:
```
/------------------------ Game map ---------------------------\
|---------|   |---------|   |---------|   |---------|   
|         |   |         |   |         |   |         |   
|    B             O             S             O    |   
|                                                   |   
|                                                   |   
|         |   |         |   |         |   |         |   
|---------|   |---   ---|   |---   ---|   |---------|   
                                                        
                                                        
                                                        
|---------|   |---   ---|   |---   ---|                 
|         |   |         |   |         |                 
|                                E    |                 
|                                     |                 
|                                     |                 
|         |   |         |   |         |                 
|---------|   |---   ---|   |---------|                 
                                                        
                                                        
                                                        
              |---   ---|                               
              |         |                               
              |         |                               
              |    X    |                               
              |         |                               
              |         |                               
              |---------|                               
                                                        
                                                        
                                                        
"You have an enormous old castle in front of you"


-------------- Pick an option -------------
1. Go north
2. End game
Enter your choice: 1
```
Then, if you select the first option to go to the next room:

```
/------------------------ Game map ---------------------------\
|---------|   |---------|   |---------|   |---------|   
|         |   |         |   |         |   |         |   
|    B             O             S             O    |   
|                                                   |   
|                                                   |   
|         |   |         |   |         |   |         |   
|---------|   |---   ---|   |---   ---|   |---------|   
                                                        
                                                        
                                                        
|---------|   |---   ---|   |---   ---|                 
|         |   |         |   |         |                 
|                                E    |                 
|                  X                  |                 
|                                     |                 
|         |   |         |   |         |                 
|---------|   |---   ---|   |---------|                 
                                                        
                                                        
                                                        
              |---   ---|                               
              |         |                               
              |         |                               
              |         |                               
              |         |                               
              |         |                               
              |---------|                               
                                                        
                                                        
                                                        
"You entered the main hall"


-------------- Pick an option -------------
1. Go north
2. Go south
3. Go east
4. Go west
5. End game
Enter your choice: 3
```
Then you go to the room on the right, to get the object there:

```
/------------------------ Game map ---------------------------\
|---------|   |---------|   |---------|   |---------|   
|         |   |         |   |         |   |         |   
|    B             O             S             O    |   
|                                                   |   
|                                                   |   
|         |   |         |   |         |   |         |   
|---------|   |---   ---|   |---   ---|   |---------|   
                                                        
                                                        
                                                        
|---------|   |---   ---|   |---   ---|                 
|         |   |         |   |         |                 
|                                E    |                 
|                                X    |                 
|                                     |                 
|         |   |         |   |         |                 
|---------|   |---   ---|   |---------|                 
                                                        
                                                        
                                                        
              |---   ---|                               
              |         |                               
              |         |                               
              |         |                               
              |         |                               
              |         |                               
              |---------|                               
                                                        
                                                        
                                                        
"You are in an enormous ceremony room"


-------------- Pick an option -------------
1. Go north
2. Go west
3. Inspect item: emblem
4. End game
Enter your choice: 

```
Now you can inspect the item:
```
-------------- Inspect Item: emblem -------------
Description: "An old emblem"
Choose an action:
1. Pick up
2. Go back
Enter your choice: 
```
And pick it up:
```
/------------------------ Game map ---------------------------\
|---------|   |---------|   |---------|   |---------|   
|         |   |         |   |         |   |         |   
|    B             O             S             O    |   
|                                                   |   
|                                                   |   
|         |   |         |   |         |   |         |   
|---------|   |---   ---|   |---   ---|   |---------|   
                                                        
                                                        
                                                        
|---------|   |---   ---|   |---   ---|                 
|         |   |         |   |         |                 
|                                     |                 
|                                X    |                 
|                                     |                 
|         |   |         |   |         |                 
|---------|   |---   ---|   |---------|                 
                                                        
                                                        
                                                        
              |---   ---|                               
              |         |                               
              |         |                               
              |         |                               
              |         |                               
              |         |                               
              |---------|                               
                                                        
                                                        
                                                        
"You are in an enormous ceremony room"


-------------- Pick an option -------------
1. Go north
2. Go west
3. Show item list
4. End game
Enter your choice: 3
```
The item disappears from the map and now you can check your inventory:
```
-------------- Pick an option -------------
1. Go north
2. Go west
3. Show item list
4. End game
Enter your choice: 3
Player items: emblem
```
Now you go north:
```
/------------------------ Game map ---------------------------\
|---------|   |---------|   |---------|   |---------|   
|         |   |         |   |         |   |         |   
|    B             O             S             O    |   
|                                X                  |   
|                                                   |   
|         |   |         |   |         |   |         |   
|---------|   |---   ---|   |---   ---|   |---------|   
                                                        
                                                        
                                                        
|---------|   |---   ---|   |---   ---|                 
|         |   |         |   |         |                 
|                                     |                 
|                                     |                 
|                                     |                 
|         |   |         |   |         |                 
|---------|   |---   ---|   |---------|                 
                                                        
                                                        
                                                        
              |---   ---|                               
              |         |                               
              |         |                               
              |         |                               
              |         |                               
              |         |                               
              |---------|                               
                                                        
                                                        
                                                        
"You enter the armory"


-------------- Pick an option -------------
1. Go south
2. Go east
3. Go west
4. Inspect item: shield
5. Show item list
6. End game
Enter your choice: 
```
And now to the right:
```
/------------------------ Game map ---------------------------\
|---------|   |---------|   |---------|   |---------|   
|         |   |         |   |         |   |         |   
|    B             O             S             O    |   
|                                              X    |   
|                                                   |   
|         |   |         |   |         |   |         |   
|---------|   |---   ---|   |---   ---|   |---------|   
                                                        
                                                        
                                                        
|---------|   |---   ---|   |---   ---|                 
|         |   |         |   |         |                 
|                                     |                 
|                                     |                 
|                                     |                 
|         |   |         |   |         |                 
|---------|   |---   ---|   |---------|                 
                                                        
                                                        
                                                        
              |---   ---|                               
              |         |                               
              |         |                               
              |         |                               
              |         |                               
              |         |                               
              |---------|                               
                                                        
                                                        
                                                        
"You enter a room with a big armor"


-------------- Pick an option -------------
1. Go west
2. Inspect item: old_armour
3. Show item list
4. End game
Enter your choice: 
```
Here you inspect the item:
```
-------------- Inspect Item: old_armour -------------
Description: "An old armour that has no emblem"
Choose an action:
1. Interact
2. Go back
Enter your choice: 
```
And interact with it:
```
You interacted with the old_armour and obtained ['final_prize'].


-------------------------
         YOU WON         
-------------------------

```
You are able to interact because you have the ```emblem```, therefore you obtain the ```final_prize``` and win the game.

## LaTeX


## Team Contribution
