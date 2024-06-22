from assets.package.BrawlHeroes import BrawlHeroes
from assets.tools.HeroEntity import HeroEntity


hero = HeroEntity("default", {"name": "Golovach", "costs": [
                  10000, 15000, 20000, 25000], "taps": [2, 4, 5, 6]})

print("name ", hero.name)
print("cost ", hero.get_cost_hero())
print("tap ", hero.get_tap_hero())
print("upgrade cost ", hero.get_upgrade_cost_hero())
print("update tap ", hero.get_upgrade_tap_hero())


# bh = BrawlHeroes()
# bh.crate_dict_heroes()
# for hero_type in bh.dict_heroes.keys():
#     for hero in bh.dict_heroes.get(hero_type):
#         print(hero.name)
