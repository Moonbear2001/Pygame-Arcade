# pygame_template

Pygame template for beginning a pygame project. It's purpose is to eliminate rewriting the same code over and over again and give a model for building common game features such as a loading screen, saving data, managing game assets like fonts, music, and images.

Features included include:
- Game class
  - implements delta time and frame rate independence
  - reading key presses from wasd keys
  - simple movement
- SaveLoadManager
  - serializes and saves data to be reloaded
- Folder layout
  - fonts, images, sounds, save_data, states folder pre-created

