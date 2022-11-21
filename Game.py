import pygame
import time
from states.title import Title


class Game:

    def __init__(self):

        pygame.init()

        self.canvas_width = 480
        self.canvas_height = 270
        self.canvas = pygame.Surface((self.canvas_width, self.canvas_height))
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.state_stack = []
        self.running = True
        self.playing = True
        self.actions = {"left": False, "right": False, "up": False, "down": False, "action1": False, "action2": False,
                        "start": False}
        self.delta_time = 0
        self.prev_time = 0
        self.fps = 60

        self.colors = None
        self.colors_init()

        self.fonts = None
        self.font_init()

        self.example_img = None
        self.image_init()

        self.example_sound = None
        self.sound_init()

        self.title_state = None
        self.state_init()

        self.socket_init()

    def colors_init(self):
        self.colors = {"white": (255, 255, 255),
                       "black": (0, 0, 0),
                       "red": (255, 0, 0),
                       "green": (0, 255, 0),
                       "blue": (0, 0, 255)}

    def font_init(self):
        self.fonts = {
            "main_font": pygame.font.Font("fonts/Pokemon Solid.ttf", 20)
        }

    def image_init(self):
        self.example_img = pygame.image.load("images/pygame_logo.png").convert()

    def sound_init(self):
        self.example_sound = pygame.mixer.Sound("sounds/example_sound.mp3")

    def state_init(self):
        self.title_state = Title(self)
        self.state_stack.append(self.title_state)

    def socket_init(self):
        pass

    def render_text(self, surface, text, color, x, y):
        text_surface = self.fonts["main_font"].render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    def reset_actions(self):
        for action in self.actions:
            self.actions[action] = False

    def get_delta_time(self):
        now = time.time()
        self.delta_time = now - self.prev_time
        self.prev_time = now

    def event_loop(self):

        for event in pygame.event.get(): 

            if event.type == pygame.QUIT: 
                break   

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.moving = False         
                if event.key == pygame.K_d:
                    self.actions["right"] = True
                if event.key == pygame.K_a:
                    self.actions["left"] = True
                if event.key == pygame.K_w:
                    self.actions["up"] = True
                if event.key == pygame.K_s:
                    self.actions["down"] = True
                if event.key == pygame.K_q:
                    self.actions["action1"] = True
                if event.key == pygame.K_e:
                    self.actions["action2"] = True
                if event.key == pygame.K_r:
                    self.actions["ultimate"] = True

            if event.type == pygame.KEYUP:            
                if event.key == pygame.K_d:
                    self.actions["right"] = False
                if event.key == pygame.K_a:
                    self.actions["left"] = False
                if event.key == pygame.K_w:
                    self.actions["up"] = False
                if event.key == pygame.K_s:
                    self.actions["down"] = False
                if event.key == pygame.K_q:
                    self.actions["action1"] = False
                if event.key == pygame.K_e:
                    self.actions["action2"] = False
                if event.key == pygame.K_r:
                    self.actions["ultimate"] = False

    def update(self):
        self.state_stack[-1].update(self.delta_time, self.actions)

    def render(self):
        self.state_stack[-1].render()
        scaled_canvas = pygame.transform.scale(self.canvas, (self.screen_width, self.screen_height))
        self.screen.blit(scaled_canvas, (0, 0))
        pygame.display.flip()

    def game_loop(self):

        clock = pygame.time.Clock()

        self.prev_time = time.time()
        
        while self.playing:
            
            # --- Delta time logic --- #
            self.get_delta_time()

            # --- Event Loop --- #
            self.event_loop()

            # --- Game logic --- #
            self.update()

            # --- Drawing to screen --- #
            self.render()

            # --- Limit frame rate --- #
            clock.tick(self.fps)
        
        pygame.quit()
        exit()