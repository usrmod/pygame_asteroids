# Asteroids Game - README

A classic Asteroids arcade game implementation built with Python and Pygame. Navigate your spaceship through an asteroid field, shoot asteroids to break them into smaller pieces, and survive as long as possible!

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [Game Mechanics](#game-mechanics)
- [Configuration](#configuration)
- [Code Architecture](#code-architecture)
- [Development](#development)
- [Troubleshooting](#troubleshooting)

## Features

- **Classic Arcade Gameplay**: Authentic Asteroids experience with smooth controls
- **Progressive Difficulty**: Asteroids spawn continuously at random edges
- **Dynamic Asteroid Splitting**: Large asteroids break into smaller fragments when hit
- **Cooldown-Based Shooting**: Prevents spam with configurable shoot cooldown
- **Collision Detection**: Precise circle-based collision system
- **60 FPS Performance**: Smooth gameplay with delta-time updates
- **Object-Oriented Design**: Clean, modular code structure

## Prerequisites

### System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Linux (Fedora), Windows, or macOS
- **Display**: 1280x720 minimum resolution

### Python Dependencies

pygame>=2.0.0

text

## Installation

### On Fedora Linux

**Step 1:** Install Python (if not already installed)

sudo dnf install python3 python3-pip

text

**Step 2:** Clone or download the project

mkdir ~/asteroids-game
cd ~/asteroids-game

text

**Step 3:** Install Pygame

pip3 install pygame

text

or

pip3 install --user pygame

text

**Step 4:** Verify installation

python3 -c "import pygame; print(pygame.version.ver)"

text

## How to Play

### Starting the Game

cd ~/asteroids-game
python3 main.py

text

### Controls

| Key | Action |
|-----|--------|
| **W** | Move forward |
| **C** | Move backward |
| **A** | Rotate counter-clockwise |
| **S** | Rotate clockwise |
| **SPACE** | Shoot |

### Objective

- **Survive**: Avoid colliding with asteroids
- **Score**: Destroy as many asteroids as possible
- **Strategy**: Large asteroids split into smaller ones - plan your shots!

### Game Over

The game ends when your spaceship collides with an asteroid. The terminal will display "Game over!"

## Project Structure

asteroids-game/
├── main.py # Game entry point and main loop
├── player.py # Player spaceship class
├── asteroid.py # Asteroid class with split mechanics
├── asteroidfield.py # Asteroid spawning system
├── shot.py # Player projectile class
├── circleshape.py # Base class for circular objects
└── constants.py # Game configuration constants

text

## Game Mechanics

### Asteroid System

**Spawning:**
- Asteroids spawn from random screen edges every 0.8 seconds
- Initial velocity between 40-100 pixels/second
- Random directional variance of ±30 degrees

**Splitting:**
- When hit, asteroids split into two smaller fragments
- Split angle: random between 20-50 degrees
- Fragment velocity: 1.2x original velocity
- Minimum size asteroids disappear when destroyed

**Size Categories:**

Large: radius = 60 (3 × ASTEROID_MIN_RADIUS)
Medium: radius = 40 (2 × ASTEROID_MIN_RADIUS)
Small: radius = 20 (1 × ASTEROID_MIN_RADIUS)

text

### Player Mechanics

**Movement:**
- Forward speed: 200 pixels/second
- Rotation speed: 300 degrees/second
- No friction or momentum damping

**Shooting:**
- Projectile speed: 500 pixels/second
- Cooldown: 0.3 seconds between shots
- Unlimited ammunition

**Collision:**
- Player radius: 20 pixels
- Game ends on any asteroid collision

### Collision Detection

Uses circle-based collision with distance formula:

collision = distance <= radius1 + radius2

text

Where `distance` is the Euclidean distance between object centers

## Configuration

### Customizing Game Settings

Edit `constants.py` to adjust gameplay:

Screen settings

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
Asteroid settings

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8 # seconds
Player settings

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
Shooting settings

SHOT_RADIUS = 5
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3

text

## Code Architecture

### Class Hierarchy

pygame.sprite.Sprite
↓
CircleShape (base class)
├── Player
├── Asteroid
└── Shot

pygame.sprite.Sprite
↓
AsteroidField (spawner)

text

### Key Components

#### CircleShape (circleshape.py)

Base class for all circular game objects:

class CircleShape(pygame.sprite.Sprite):
def init(self, x, y, radius):
self.position = pygame.Vector2(x, y)
self.velocity = pygame.Vector2(0, 0)
self.radius = radius

text
def colli(self, other):
    distance = self.position.distance_to(other.position)
    return distance <= self.radius + other.radius

text

**Features:**
- Position and velocity tracking
- Collision detection method
- Sprite group integration

#### Player (player.py)

Spaceship controlled by the player:

class Player(CircleShape):
def init(self, x, y):
super().init(x, y, PLAYER_RADIUS)
self.rotation = 0
self.timer = 0 # Shoot cooldown

text

**Methods:**
- `triangle()`: Generates spaceship triangle vertices
- `draw()`: Renders the spaceship
- `rotate(dt)`: Handles rotation
- `move(dt)`: Handles movement
- `shoot()`: Creates projectiles
- `update(dt)`: Processes keyboard input

#### Asteroid (asteroid.py)

Destructible space rocks:

class Asteroid(CircleShape):
def split(self):
self.kill()
if self.radius <= ASTEROID_MIN_RADIUS:
return
# Create two smaller asteroids
rand_angle = random.uniform(20, 50)
new_radius = self.radius - ASTEROID_MIN_RADIUS
# Spawn fragments with rotated velocities

text

**Features:**
- Recursive splitting mechanics
- Random fragment trajectories
- Size-based behavior

#### AsteroidField (asteroidfield.py)

Manages asteroid spawning:

class AsteroidField(pygame.sprite.Sprite):
edges = [
# Four screen edges with velocity directions
[pygame.Vector2(1, 0), lambda y: ...], # Left
[pygame.Vector2(-1, 0), lambda y: ...], # Right
[pygame.Vector2(0, 1), lambda x: ...], # Top
[pygame.Vector2(0, -1), lambda x: ...] # Bottom
]

text

**Spawning Logic:**
1. Wait for spawn timer to expire
2. Select random edge
3. Generate random speed and angle
4. Create asteroid just outside screen boundary

#### Shot (shot.py)

Player projectiles:

class Shot(CircleShape):
def init(self, x, y):
super().init(x, y, SHOT_RADIUS)

text

**Behavior:**
- Moves in straight line
- Destroyed on asteroid collision
- No lifetime limit

### Main Game Loop (main.py)

def main():
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

text
# Create sprite groups
drawable = pygame.sprite.Group()
updatable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

# Set up containers for auto-grouping
Player.containers = (updatable, drawable)
Asteroid.containers = (asteroids, updatable, drawable)
Shot.containers = (shots, updatable, drawable)

# Initialize objects
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField()

# Game loop
fps_clock = pygame.time.Clock()
dt = 0

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    
    # Update all objects
    updatable.update(dt)
    
    # Check collisions
    for asteroid in asteroids:
        if asteroid.colli(player):
            sys.exit("Game over!")
        for shot in shots:
            if shot.colli(asteroid):
                asteroid.split()
                shot.kill()
    
    # Render
    screen.fill("black")
    for sprite in drawable:
        sprite.draw(screen)
    pygame.display.flip()
    
    # Frame timing (60 FPS)
    dt = fps_clock.tick(60) / 1000.0

if name == "main":
main()

text

## Development

### Running the Game

python3 main.py

text

### Debugging Mode

Add debug prints to track game state:

In main.py, add to game loop:

print(f"Asteroids: {len(asteroids)}, Shots: {len(shots)}")

text

### Modifying Difficulty

**Make game easier:**

In constants.py

ASTEROID_SPAWN_RATE = 1.5 # Slower spawning
PLAYER_SPEED = 300 # Faster movement

text

**Make game harder:**

ASTEROID_SPAWN_RATE = 0.5 # Faster spawning
PLAYER_SHOOT_COOLDOWN = 0.5 # Slower shooting

text

## Troubleshooting

### Game won't start

**Issue:** `ImportError: No module named 'pygame'`

pip3 install --user pygame

text

**Issue:** `ModuleNotFoundError: No module named 'player'`

Ensure all game files are in the same directory

### Performance issues

**Issue:** Low FPS or stuttering

In main.py, reduce FPS:

dt = fps_clock.tick(30) / 1000.0 # 30 FPS instead of 60

text

### Gameplay issues

**Issue:** Asteroids spawn too fast

In constants.py

ASTEROID_SPAWN_RATE = 1.5 # Increase spawn interval

text

**Issue:** Can't shoot fast enough

In constants.py

PLAYER_SHOOT_COOLDOWN = 0.1 # Reduce cooldown

text

## License

This project is open source and available for educational purposes.

## Credits

Built with:
- **Python 3**: Programming language
- **Pygame**: Game development library
- Classic Asteroids arcade game inspiration

---

**Enjoy the game! 🚀**
