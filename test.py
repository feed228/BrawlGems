from assets.package.BrawlHeroes import BrawlHeroes


bh = BrawlHeroes()
bh.crate_dict_heroes()
for hero_type in bh.dict_heroes.keys():
    for hero in bh.dict_heroes.get(hero_type):
        print(hero.name)
