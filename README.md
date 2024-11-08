# 🕹️ Pygame Arcade

Welcome to the **Pygame Arcade** – a versatile, expandable collection for organizing and showcasing a Pygame portfolio. I created this project as a way to show off all my pygame projects in one central project.

All the art is of my own making.

# ✏️ Design choices
This template uses a scene-based organizational system partly inspired by some work I did in the Godot game engine.

The game is composed of scenes. A scene is an object with the ability to handle events, update, and render. Scenes can nest within one another, and when a scene renders it passes its surface up its parent scene. The parent scene is then responsible for using its child's positioning rect to blit the child onto its own surface.

A scene then also functions as a node in a graph. The top-level scene updates and renders its children, which in turn do the same, etc.

### Managers

This project uses 'managers' to handle certain game elements. Managers are singletons that can be used anywhere in the code provide a certain service. The managers in this project are:

- **EventManager**
An event bus that publishes events to subscribers. Subscribers pass an event handler to the manager to be called when that event occurs. This subscription based model prevents Scenes from receiving any events that do not interest them.

- **SceneManager**
Manages loading and switching to new scenes. Includes a scene stack that allows returning to scenes that were just left.

- **SaveLoadManager**
Manages saving and loading of data to json files. Settings, game data, and other such information can be easily saved and loaded using this manager.

- **AudioManager**
Manages music and sounds effects. Can do things like queue a playlist and adjust the volume of music and sound effects.

- **TransitionManager**
Allows for the addition of transitions while changing scenes.

### Summary

The combination of a tree-like Scene system with a series of global singleton managers that abstract away complicated code is a powerful addition on top of Pygame's simple layer on top of SDL 2. It solves questions like:
- How do I create a complex scene?
- How do I pass around events?
- How do I determine the order in which to render objects?

By providing a simple and intuitive framework.

---

## 🚀 Getting Started

Clone the repository, download python, run `main.py`, and explore the arcade.

