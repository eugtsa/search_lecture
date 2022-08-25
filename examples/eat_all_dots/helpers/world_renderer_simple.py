from domain.map import Map
from domain.world import World
from domain.point import Point
import pygame

pygame.init()

SCALE = 50
SPRITES = {
    "pac": "./images/pac.png",
    "wall": "./images/wall.png",
    "fin_pos": "./images/fin_pos.png",
}
GAME_FONT = pygame.freetype.Font("./fonts/kongtext.ttf", SCALE / 2)


class WorldRenderSimple:
    BLACK = (0, 0, 0)
    WHITE = (200, 200, 200)
    YELLOW = (255, 174, 66)

    def __init__(self, size_x, size_y,agent_name) -> None:
        global SCREEN, CLOCK
        # pygame.init()
        SCREEN = pygame.display.set_mode((size_x * SCALE, (size_y + 1) * SCALE))
        pygame.display.set_caption(agent_name)
        CLOCK = pygame.time.Clock()
        SCREEN.fill(self.BLACK)

        self._load_all_sprites()

    def _load_all_sprites(self):
        for k, v in SPRITES.items():
            self.__dict__["_" + k] = self._load_sprite(v)

    def _load_sprite(self, sprite_file):
        sprite = pygame.image.load(sprite_file)
        return pygame.transform.scale(sprite, (SCALE, SCALE))

    def render_world(self, world: World):
        SCREEN.fill(self.BLACK)
        for w in world.map.walls:
            self._draw_wall(w)

        for d in world.dots:
            self._draw_dot(d)

       # self._draw_finish_pos(world.map.finish_pos)
        self._draw_score(world._cur_score, world.map, world.tick_num)
        self._draw_pac_man(world.cur_pos)
        if world.is_finished():
            self._draw_finish(world._cur_score, world.map)
        pygame.display.update()

    def _draw_finish_pos(self, fin_pos):
        self._draw_sprite(fin_pos, self._fin_pos)

    def _draw_sprite(self, point, sprite):
        rect = sprite.get_rect()
        rect = rect.move((point.x * SCALE, point.y * SCALE))
        SCREEN.blit(sprite, rect)

    def _draw_finish(self, score, map):
        GAME_FONT.render_to(
            SCREEN,
            ((map.size_x + 0.5) * SCALE - 5 * SCALE, map.size_y * SCALE / 2 - SCALE),
            "FIN!",
            self.WHITE,
        )

    def _draw_pac_man(self, pac_pos: Point):
        self._draw_sprite(pac_pos, self._pac)

    def _draw_wall(self, pac_pos: Point):
        self._draw_sprite(pac_pos, self._wall)

    def _draw_score(self, score, map: Map, tick_num: int):
        GAME_FONT.render_to(
            SCREEN, (0, map.size_y * SCALE), "SCORE:{}".format(score), self.WHITE
        )
        GAME_FONT.render_to(
            SCREEN,
            (0, (map.size_y + 0.5) * SCALE),
            "TICK:{}".format(tick_num),
            self.WHITE,
        )

    def _draw_dot(self, dot_pos):
        pygame.draw.circle(
            SCREEN,
            self.YELLOW,
            (SCALE * dot_pos.x + SCALE / 2, SCALE * dot_pos.y + SCALE / 2),
            SCALE / 4,
        )
