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
    num_upgrade: int
    name_hero: str
    type_hero: str

    def init(self, name_hero: str, type_hero: str) -> None:
        self.name_hero = name_hero
        self.type_hero = type_hero
        self.num_upgrade = 0

        self.image_ava = ft.Image(
            src=f"images\heroes\{type_hero}\{name_hero}\{name_hero}_ava.png",
            fit=ft.ImageFit.CONTAIN,
            animate_scale=ft.Animation(
                duration=600, curve=ft.AnimationCurve.EASE),
            width=WIDTH_AVA,
            height=HEIGHT_AVA
        )
        self.image_default = ft.Image(
            src=f"images\heroes\{type_hero}\{name_hero}\{name_hero}_default.png",
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
                src=f"images\heroes\{self.type_hero}\{self.name_hero}\{self.name_hero}_upgrade_{self.num_upgrade}.png",
                fit=ft.ImageFit.CONTAIN,
                animate_scale=ft.Animation(
                    duration=600, curve=ft.AnimationCurve.EASE),
                width=WIDTH_HERO,
                height=HEIGHT_HERO
            )

    def set_image_hero(self, name: str, num_upgrade: int, type: str):
        self.num_upgrade = num_upgrade
        self.image_default = ft.Image(
            src=f"images\heroes\{self.type_hero}\{self.name_hero}\{self.name_hero}_upgrade_{self.num_upgrade}.png",
            fit=ft.ImageFit.CONTAIN,
            animate_scale=ft.Animation(
                duration=600, curve=ft.AnimationCurve.EASE),
            width=WIDTH_HERO,
            height=HEIGHT_HERO
        )
