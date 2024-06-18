import flet as ft
import time

money = 0


def main(page: ft.Page):
    page.title = "BrawlGems"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    img = ft.Image(
        src=f"images\heroes\default\shelly\shelly_default.png",
        width=400,
        height=400,
        fit=ft.ImageFit.CONTAIN,
        scale=ft.transform.Scale(1),
        rotate=ft.transform.Rotate(0, alignment=ft.alignment.center),
        animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        animate_rotation=ft.animation.Animation(300, ft.AnimationCurve.EASE),
    )
    img_coin = ft.Image(
        src=f"images\coins\Coins-2.png",
        width=50,
        height=50,
        fit=ft.ImageFit.CONTAIN,
    )
    img_shop = ft.Image(
        src=f"images\coins\Credits-2.png",
        width=50,
        height=50,
        fit=ft.ImageFit.CONTAIN,
    )
    img_test = ft.Image(
        src=f"images\heroes\default\shelly\shelly_ava.png",
        width=450,
        height=450,
        fit=ft.ImageFit.CONTAIN,
    )

    def set_window(list_elements):
        for i in list_elements:
            page.controls.append(i)
        page.update()

    def plus_click(e):
        global money
        money += 1
        txt_number.value = str(money)
        img.scale = 0.95
        img.rotate.angle = 0.20
        page.update()
        time.sleep(0.2)
        img.rotate.angle = 0
        img.scale = 1
        page.update()

    def open_shop_window(e):
        page.clean()
        set_window(shop_window_elements)

    def back_main_window(e):
        page.clean()
        set_window(main_window_elements)

    txt_number = ft.Text(value="0", text_align=ft.TextAlign.CENTER, width=200)
    main_window_elements = [ft.Column(
        spacing=0,
        controls=[
            ft.IconButton(content=img_shop, on_click=open_shop_window)
        ],
        alignment=ft.MainAxisAlignment.START,
    ),
        ft.Column(
            spacing=50,
            controls=[
                ft.Row([ft.IconButton(content=img, on_click=plus_click)],
                       alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([img_coin, txt_number],
                       alignment=ft.MainAxisAlignment.CENTER)
            ],
            alignment=ft.MainAxisAlignment.CENTER,
    )
    ]
    shop_window_elements = [ft.Column(
        spacing=0,
        controls=[
            ft.IconButton(icon="park_rounded", on_click=back_main_window),
            img_test,
            ft.Row([img_coin, txt_number],
                   alignment=ft.MainAxisAlignment.CENTER)

        ],
        alignment=ft.MainAxisAlignment.START,
    ),
    ]

    set_window(main_window_elements)


ft.app(target=main, view=ft.WEB_BROWSER)
