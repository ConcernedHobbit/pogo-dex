# Pokémon Go Dex Tracker
Pokémon Go is all about collecting different Pokémon (and nowadays battling as well).  
The aim of this project is to help track your progress in catching 'em all!

A trainer may sign up for the service and start tracking their caught Pokémon by going through an initial setup, made to be as easy as possible with the help of the in-game Pokédex. After setting up their Pokédex, the trainer may view stats about it (such as percentage caught of each generation, missing regional Pokémon etc.) and modify their Pokédex. Only Pokémon marked released in-game can be added to one's own Pokédex.

A trainer has a role, which is currently either user or admin, but can be expanded easily in the future. An admin may add or edit Pokémon or regions and mark Pokémon in the system as having been released in-game.

Features:
* Signup and login
* Adding Pokémon to your Pokédex
* Viewing Pokédex completeness statistics
  + Regionals
  + Legendaries
  + Generation completeness
* Viewing release statistics
  + Generation release progress
  + Legendary release progress
  + Regional percentage of released
  + etc.
* Admin functionality
  + Pokémon creation, updating, deletion (i.e. in case of erronous duplicates)
  + Region creation, updating, deletion (i.e. in case of region borders shifting)
  + General database info (# of overall catches, # of overall trainers etc.)

## Documentation
![Database diagram](https://github.com/ConcernedHobbit/pogo-dex/raw/master/documentation/db.png)  
[User stories](https://github.com/ConcernedHobbit/pogo-dex/master/documentation/stories.md)

## Heroku
[pogodex.herokuapp.com](http://pogodex.herokuapp.com)
