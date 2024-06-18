from assets.tools.HeroEntity import HeroEntity
import json

with open('assets/config/heroes_types.json') as json_file:
    global HEROES_TYPES
    HEROES_TYPES = json.load(json_file)

with open('assets/config/heroes_names.json') as json_file:
    global HEROES_NAMES
    HEROES_NAMES = json.load(json_file)


class BrawlHeroes(object):
    dict_heroes: dict = dict()

    def __init__(self) -> None:
        self.dict_heroes = HEROES_TYPES
        self.dict_heroes_name = HEROES_NAMES

    def add_hero(self, name_hero: str, type_hero: str):
        self.dict_heroes[type_hero] = HeroEntity(path_to_ava=f"images\heroes\{type_hero}\{name_hero}\{name_hero}_ava.png",
                                                 path_to_default=f"images\heroes\{type_hero}\{name_hero}\{name_hero}_default.png",
                                                 path_upgrade_1=f"images\heroes\{type_hero}\{name_hero}\{name_hero}_upgrade_1.png",
                                                 path_upgrade_2=f"images\heroes\{type_hero}\{name_hero}\{name_hero}_upgrade_2.png",
                                                 path_upgrade_3=f"images\heroes\{type_hero}\{name_hero}\{name_hero}_upgrade_3.png",
                                                 )

    def crate_dict_heroes(self):
        for type_hero in self.dict_heroes_name.keys():
            for name_hero in self.dict_heroes_name[type_hero]:
                print(name_hero)
                self.add_hero(name_hero=name_hero, type_hero=type_hero)

    def get_main_hero(self):
        pass
