import time
import flet as ft

# class


def main(page: ft.Page):
    page.title = "BrawlGem"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {"MarkerFelt": "fonts/MarkerFelt.ttf"}
    page.theme = ft.Theme(font_family="MarkerFelt")

    def score_up(event: ft.ContainerTapEvent):
        score.data += 1
        score.value = str(score.data)
        image.scale = 0.95

        score_counter.opacity = 50
        score_counter.value = "+1"
        score_counter.right = 0
        score_counter.left = 1
        score_counter.top = 1
        score_counter.bottom = 0

        page.overlay.append(audio)

        progress_bar.value += (1/100)

        if score.data == 100:
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

        image.scale = 1
        score_counter.opacity = 0
        page.update()

    score = ft.Text(value="0", size=50, data=0)
    score_counter = ft.Text(
        size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN)
    )
    image = ft.Image(
        src="images\heroes\default\shelly\shelly_default.png",
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE),
        width=600,
        height=600
    )
    audio = ft.Audio(
        src="audio\click_audio.mp3", autoplay=True
    )

    progress_bar = ft.ProgressBar(
        value=0,
        width=page.width - 200,
        bar_height=20,
        color="#FFA07A",
        bgcolor="#FF6347"
    )

    page.add(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0, 0, 30),
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10)
        )

    )


if __name__ == "__main__":
    # ft.app(target=main)
    ft.app(target=main, view=ft.WEB_BROWSER)
