# Space Invaders

This is a simple Space Invaders game implemented in Python using the Pygame library.  
In this game, your objective is to control a spaceship and shoot down enemy spaceships while avoiding their attacks.  
Below is a detailed explanation of the code:

## Game Features

- The game window has a size of 800x600 pixels.
- The game is titled "Space Invaders" with a custom icon.
- It has background music that plays continuously.
- The player controls a spaceship with arrow keys.
- The player can shoot bullets using the spacebar key.
- There are enemy spaceships on the screen.
- The player scores points by shooting down enemies.
- The game ends when the player's spaceship is hit by an enemy.

## Code Explanation

1. **Initializing Pygame:**
   - Pygame is initialized using `pygame.init()`.

2. **Creating the Screen:**
   - The game window is created with a size of 800x600 pixels.
   - The game's title and icon are set.

3. **Loading Background Music:**
   - Background music is loaded and played continuously using Pygame's mixer.

4. **Initializing Game Objects:**
   - The player's spaceship is created and initialized.
   - A list of enemy spaceships (controlled by the `Enemy` class) is created, and they are initialized.
   - A bullet is created and initialized.
   - A scoreboard to display the player's score is created.

5. **Game Loop:**
   - The main game loop runs until the player quits the game (`running` becomes `False`).
   - The game screen is filled with a black background, and the background image is drawn.

6. **Event Handling:**
   - Pygame events are processed to handle quitting the game (`pygame.QUIT` event).
   - Player's spaceship and bullets are controlled using events.

7. **Player Movement:**
   - The player's spaceship's position is updated based on user input, and boundary checks are applied to keep it within the screen.

8. **Enemy Movement and Collision Detection:**
   - Each enemy spaceship's position is updated, and they move horizontally.
   - If a bullet hits an enemy, it is reset, and the enemy is respawned. The player's score is increased.
   - The Collision between the Enemy and the bullet is detected using the Cartesian distance formula.

9. **Player-Enemy Collision Detection:**
   - If the player's spaceship is hit by an enemy, all enemies are moved off-screen, and the player's spaceship is moved off-screen to end the game.
   - The Collision between the Enemy and the Player is detected using the Cartesian distance formula.

10. **Bullet Control:**
    - The bullet's position is controlled, and it can be fired using the Spacebar key. It moves upwards, and if it reaches the top of the screen, it's reset.

11. **Updating and Display:**
    - The player's spaceship, enemies, and scoreboard are updated.
    - The game screen is updated to display all changes.

12. **Game Over:**
    - If the player's spaceship is hit, the `Game Over !!` message is displayed.

## Controls

- Use the Arrow keys to move the player's spaceship.
- Use the Spacebar key to fire bullets.