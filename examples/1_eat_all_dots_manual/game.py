from helpers.level_loader import LevelLoader
from domain.rules import Rules
from domain.world import World
from domain.agents.keyboard_agent import KeyboardAgent
from helpers.world_renderer_simple import WorldRenderSimple
from helpers.key_press import press_any_key


def main():
    ll = LevelLoader()

    total_score = 0

    for level_name in ll.list_levels():
        map,dots = ll.load_level(level_name)
        current_world = World(Rules(), map, dots, map.start_pos, total_score)
        wrs = WorldRenderSimple(current_world.map.size_x,current_world.map.size_y)
        
        agent = KeyboardAgent()

        wrs.render_world(current_world)

        # draw initital world
        while not current_world.is_finished():
            action = agent.get_action(current_world)
            current_world = current_world.apply_action(action)
            wrs.render_world(current_world)
            # draw world + score
        wrs.render_world(current_world)
        total_score+=current_world.score
        press_any_key()

if __name__ == "__main__":
    main()