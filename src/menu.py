"""
This class handles creating and displaying menu's for the end user
"""
from tabulate import tabulate
from simple_term_menu import TerminalMenu

class Menu():

    def __init__(self, title, menu_items):
        self.main_menu_title = title
        self.main_menu_items = menu_items
        self.main_menu_cursor = "> "
        self.main_menu_cursor_style = ("fg_green", "bold")
        self.main_menu_style = ("bg_green", "fg_yellow", "bold")

    def menu(self):

        main_menu = TerminalMenu(
            menu_entries = self.main_menu_items,
            title = self.main_menu_title,
            menu_cursor = self.main_menu_cursor,
            menu_cursor_style = self.main_menu_cursor_style,
            menu_highlight_style = self.main_menu_style,
            cycle_cursor = True,
            clear_screen = True,
        )
        return main_menu