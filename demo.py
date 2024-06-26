

from assets.tools.HeroEntity import HeroEntity
import time
import pygame
import flet as ft
hero_shelly = {"name": "shelly",
               "taps": [1, 2, 3, 4],
               "costs": [0, 5000, 10000, 20000],
               "max_click": [1000, 1500, 2000, 3000]}


# Инициализация Pygame
pygame.mixer.init()


def main(page: ft.Page):
    page.title = "Sound Play Example"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {"MarkerFelt": "front/MarkerFelt.ttf"}
    page.theme = ft.Theme(font_family="MarkerFelt")
    page.bgcolor = "#E8DAB2"
    hero = HeroEntity(type_hero="default", hero_stats=hero_shelly)

    audio = pygame.mixer.Sound("assets/audio/click_audio.mp3")

    def upgrade_hero(event):
        price = "asdasd"
        page.update()

    def on_tap_down(event: ft.ContainerTapEvent):
        global tap_position
        tap_position = (event.local_x, event.local_y)

    def score_up(event: ft.ContainerTapEvent):
        score.data += 1
        score.value = str(score.data)
        hero.image_hero.scale = 0.95

        score_counter.opacity = 50
        score_counter.value = "+1"
        score_counter.right = 0
        score_counter.left = tap_position[0]
        score_counter.top = tap_position[1]
        score_counter.bottom = 0

        audio.play()

        progress_bar.value += (1/100)

        if score.data % 100 == 0:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="+100",
                    size=20,
                    color="#8B0000",
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor="#25223a"
            )
            page.snack_bar.open = True
            progress_bar.value = 0

        page.update()
        time.sleep(0.1)

        hero.image_hero.scale = 1
        score_counter.opacity = 0
        page.update()

    score = ft.Text(value="0", size=50, data=0,
                    font_family="MarkerFelt", color="#DD6E42")
    score_counter = ft.Text(size=30, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.DECELERATE),
                            font_family="MarkerFelt", color="#43DE8E")
    image = ft.Image(
        src="images\heroes\default\shelly\shelly_default.png",
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE),
        width=600,
        height=600
    )
    price = f"Улучшить героя за 113123"

    progress_bar = ft.ProgressBar(
        value=0,
        width=page.width - 200,
        bar_height=20,
        color="#FFA07A",
        bgcolor="#FF6347"
    )

    page.add(
        score,
        ft.Container(content=ft.Stack(controls=[
                     hero.image_hero, score_counter]), on_click=score_up, on_tap_down=on_tap_down, margin=ft.Margin(0, 0, 0, 30),),
        ft.Container(content=progress_bar, border_radius=ft.BorderRadius(10, 10, 10, 10)
                     ),
        ft.Container(ft.TextButton(
            text=f"Улучшить героя за {price}", scale=2, on_click=upgrade_hero))
    )


if __name__ == "__main__":
    ft.app(target=main)
    # ft.app(target=main, view=ft.WEB_BROWSER)
