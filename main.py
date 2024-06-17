import flet as ft
import time


def main(page: ft.Page):
    page.title = "BrawlGems"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    img = ft.Image(
        src=f"D:\Yandex\BrawlGems\images\heroes\default\shelly\shelly_default.png",
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
        animate_scale= ft.Animation(duration=300,curve=ft.AnimationCurve.EASE)
    )
   
    txt_number = ft.TextField(
        value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        img.sacle = 0.95
        page.update()
        time.sleep(1)
        img.sacle = 1
        page.update()

    page.add(
        ft.Row(
            [
               ft.IconButton(content = img, on_click=plus_click,)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(spacing=0,controls=
            [
                txt_number
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
      )



ft.app(main)
