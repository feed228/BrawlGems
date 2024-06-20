import flet as ft
import json

with open('assets/config/defaults_hero_entity.json') as json_file:
    dufaults = json.load(json_file)
    global WIDTH_AVA
    global HEIGHT_AVA
    global WIDTH_HERO
    global HEIGHT_HERO
    global MAX_LEVEL

    WIDTH_AVA = dufaults["size_ava"]["width"]
    HEIGHT_AVA = dufaults["size_ava"]["height"]
    WIDTH_HERO = dufaults["size_hero"]["width"]
    HEIGHT_HERO = dufaults["size_hero"]["height"]
    MAX_LEVEL = dufaults["max_level"]


class HeroEntity(object):
    image_ava: ft.Image
    image_hero: ft.Image
    taps: list[int]
    costs: list[int]

    num_upgrade: int
    name: str
    type_hero: str

    def __init__(self, type_hero: str, hero_stats: dict) -> None:
        self.type_hero = type_hero
        self.name = hero_stats.get("name")
        self.costs = hero_stats.get("costs")
        self.taps = hero_stats.get("taps")

        self.num_upgrade = 0

        self.image_ava = ft.Image(
            src=f"images\heroes\{type_hero}\{self.name}\{self.name}_ava.png",
            fit=ft.ImageFit.CONTAIN,
            animate_scale=ft.Animation(
                duration=600, curve=ft.AnimationCurve.EASE),
            width=WIDTH_AVA,
            height=HEIGHT_AVA
        )
        self.image_default = ft.Image(
            src=f"images\heroes\{type_hero}\{self.name}\{self.name}_default.png",
            fit=ft.ImageFit.CONTAIN,
            animate_scale=ft.Animation(
                duration=600, curve=ft.AnimationCurve.EASE),
            width=WIDTH_HERO,
            height=HEIGHT_HERO
        )

    def upgrade_hero(self):
        if (self.num_upgrade < MAX_LEVEL):
            self.num_upgrade += 1
            self.image_default = ft.Image(
                src=f"images\heroes\{self.type_hero}\{self.name}\{self.name}_upgrade_{self.num_upgrade}.png",
                fit=ft.ImageFit.CONTAIN,
                animate_scale=ft.Animation(
                    duration=600, curve=ft.AnimationCurve.EASE),
                width=WIDTH_HERO,
                height=HEIGHT_HERO
            )

    def set_image_hero(self, name: str, num_upgrade: int, type: str):
        self.num_upgrade = num_upgrade
        self.image_default = ft.Image(
            src=f"images\heroes\{self.type_hero}\{self.name}\{self.name}_upgrade_{self.num_upgrade}.png",
            fit=ft.ImageFit.CONTAIN,
            animate_scale=ft.Animation(
                duration=600, curve=ft.AnimationCurve.EASE),
            width=WIDTH_HERO,
            height=HEIGHT_HERO
        )

    def get_ava_hero(self):
        pass

    def get_image_hero(self):
        pass

    def get_tap_hero(self):
        pass

    def get_update_tap_hero(self):
        pass

    def get_cost_hero(self):
        pass

    def get_update_cost_hero(self):
        pass
