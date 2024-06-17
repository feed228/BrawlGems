import flet as ft
import time


def main(page: ft.Page):
    page.title = "BrawlGems"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    img = ft.Image(
        src=f".\images\heroes\default\shelly\shelly_default.png",
        width=400,
        height=400,
        fit=ft.ImageFit.CONTAIN,
        scale=ft.transform.Scale(1),
        rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
        animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        animate_rotation=ft.animation.Animation(300, ft.AnimationCurve.EASE),
    )
   
    txt_number = ft.Text(
        value="0", text_align=ft.TextAlign.CENTER, width=800)

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        img.scale = 0.95
        img.rotate.angle = 0.20
        page.update()
        time.sleep(0.2)
        img.rotate.angle = 0
        img.scale = 1
        page.update()
  
    page.add(
        ft.Column(
            spacing=50,
            controls = [
               ft.Row([ft.IconButton(content = img, on_click=plus_click)],alignment=ft.MainAxisAlignment.CENTER),
               ft.Row([txt_number],alignment=ft.MainAxisAlignment.CENTER)
               ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )



ft.app(target=main)
