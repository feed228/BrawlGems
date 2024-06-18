import flet as ft
import json

with open('assets/config/defaults_hero_entity.json') as json_file:
    dufaults = json.load(json_file)
    global WIDTH_AVA
    global HEIGHT_AVA
    global WIDTH_HERO
    global HEIGHT_HERO

    WIDTH_AVA = dufaults["size_ava"]["width"]
    HEIGHT_AVA = dufaults["size_ava"]["height"]
    WIDTH_HERO = dufaults["size_hero"]["width"]
    HEIGHT_HERO = dufaults["size_hero"]["height"]


class HeroEntity(object):
    image_ava: ft.Image
    image_default: ft.Image
    list_images_updates: list[ft.Image] = []
    count_upgrade: int

    def __init__(self,
                 path_to_ava: str,
                 path_to_default: str,
                 path_upgrade_1: str,
                 path_upgrade_2: str,
                 path_upgrade_3: str) -> None:
        self.image_ava = ft.Image(
            src=path_to_ava,
            fit=ft.ImageFit.CONTAIN,
            animate_scale=ft.Animation(
                duration=600, curve=ft.AnimationCurve.EASE),
            width=WIDTH_AVA,
            height=HEIGHT_AVA
        )
        self.image_default = ft.Image(
            src=path_to_ava,
            fit=ft.ImageFit.CONTAIN,
            animate_scale=ft.Animation(
                duration=600, curve=ft.AnimationCurve.EASE),
            width=WIDTH_HERO,
            height=HEIGHT_HERO
        )
        self.list_images_updates.append(ft.Image(
            src=path_upgrade_1,
            fit=ft.ImageFit.CONTAIN,
            animate_scale=ft.Animation(
                duration=600, curve=ft.AnimationCurve.EASE),
            width=WIDTH_HERO,
            height=HEIGHT_HERO
        ))
        self.list_images_updates.append(ft.Image(
            src=path_upgrade_2,
            fit=ft.ImageFit.CONTAIN,
            animate_scale=ft.Animation(
                duration=600, curve=ft.AnimationCurve.EASE),
            width=WIDTH_HERO,
            height=HEIGHT_HERO
        ))
        self.list_images_updates.append(ft.Image(
            src=path_upgrade_3,
            fit=ft.ImageFit.CONTAIN,
            animate_scale=ft.Animation(
                duration=600, curve=ft.AnimationCurve.EASE),
            width=WIDTH_HERO,
            height=HEIGHT_HERO
        ))
