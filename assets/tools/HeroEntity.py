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
    image_hero: ft.Image
    name_hero:str
    num_upgrade:int
    type_hero:str


    def __init__(self,name_hero:str,type_hero:str
                 ) -> None:
        self.image_ava = ft.Image(
            src=f"images\heroes\{type_hero}\{name_hero}\{name_hero}_default.png",
            fit=ft.ImageFit.CONTAIN,
            animate_scale=ft.Animation(
                duration=600, curve=ft.AnimationCurve.EASE),
            width=WIDTH_AVA,
            height=HEIGHT_AVA
        )
        self.image_default = ft.Image(
            src=path_to_default,
            fit=ft.ImageFit.CONTAIN,
            animate_scale=ft.Animation(
                duration=600, curve=ft.AnimationCurve.EASE),
            width=WIDTH_HERO,
            height=HEIGHT_HERO
        )
        
        
        def set_image_hero(self, name:str,num_upgrade:int,type:str):
            
            self.image_default = ft.Image(
            src="assets\images\heroes\{type}\{name}\{name}_upgrade_{num_upgrade}.png",
            fit=ft.ImageFit.CONTAIN,
            animate_scale=ft.Animation(
                duration=600, curve=ft.AnimationCurve.EASE),
            width=WIDTH_HERO,
            height=HEIGHT_HERO
        )
