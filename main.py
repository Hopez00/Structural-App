import flet as ft
import traceback

def main(page: ft.Page):
    try:
        # --- PASTE YOUR ACTUAL APP CODE HERE ---
        page.add(ft.Text("Structural App Loaded Successfully!"))

    except Exception as e:
        # This forces the exact Python error to display on your screen
        page.add(
            ft.Text("App Startup Crash:", color="red", size=18, weight="bold"),
            ft.Text(traceback.format_exc(), color="red")
        )
        page.update()

ft.app(target=main)
