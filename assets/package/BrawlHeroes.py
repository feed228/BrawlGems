from assets.tools.HeroEntity import HeroEntity
import json

with open('assets/config/heroes_types.json') as json_file:
    global HEROES_TYPES
    HEROES_TYPES = json.load(json_file)

with open('assets/config/heroes_stats.json') as json_file:
    global HEROES_STATS
    HEROES_STATS = json.load(json_file)


class BrawlHeroes(object):
    dict_heroes: dict = dict()

    def __init__(self) -> None:
        self.dict_heroes = HEROES_TYPES
        self.dict_heroes_stats = HEROES_STATS

    def add_hero(self, type_hero: str, hero_stats: dict):
        self.dict_heroes[type_hero].append(HeroEntity(
            type_hero=type_hero, hero_stats=hero_stats))

    def crate_dict_heroes(self):
        for type_hero in self.dict_heroes_stats.keys():
            for hero_stats in self.dict_heroes_stats[type_hero]:
                self.add_hero(type_hero=type_hero, hero_stats=hero_stats)

    def get_main_hero(self):
        pass
