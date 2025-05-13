import flet as ft
from flet import BorderSide

def main(page: ft.Page):
    page.title = "FARMI-UJAT"
    page.appbar = ft.AppBar(
        title=ft.Text("FARMI-UJAT", size=40),
        center_title=True
    )
    btn_interacciones = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[ 
                    ft.Icon("medication", size=40, color="black"),
                    ft.Text("Interacciones Medicamentosas")
                ]
            ),
            padding=10
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=BorderSide(1, "orange")
        ),
        bgcolor="orange",
        color="black",
        width=200
    )
    btn_alta = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("add_circle", size=40, color="black"),
                    ft.Text("Alta De Medicamentos")
                ]
            ),
            padding=10
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=BorderSide(1, "blue")
        ),
        bgcolor="blue",
        color="white",
        width=200
    )
    btn_lista = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("list", size=40, color="black"),
                    ft.Text("Lista De Medicamentos")
                ]
            ),
            padding=10
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            side=BorderSide(1, "green")
        ),
        bgcolor="green",
        color="white",
        width=200
    )
    page.add(ft.Divider(color="black"))
    page.add(
        ft.Row(
            controls=[btn_interacciones, btn_alta, btn_lista],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)
