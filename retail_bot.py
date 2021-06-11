import pyautogui

# import discord, pyautogui
# from discord.ext import commands, tasks
# from discord.utils import get
# from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext
# from discord import Permissions

add_prof_ship_info_f_name_cords = None
add_prof_bill_info_f_name_cords = None
add_prof_payment_details_f_name_cords = None


def minimize_pycharm_dark_mode():
    """Minimize the pycharm IDE"""

    cords = (pyautogui.locateOnScreen('min_pycharm.png'))
    pyautogui.click(cords)


def get_add_profile_first_names():
    """Getting coordinates for First name on Add Profile screen"""

    global add_prof_ship_info_f_name_cords
    global add_prof_bill_info_f_name_cords
    global add_prof_payment_details_f_name_cords

    cords = list(pyautogui.locateAllOnScreen('first_name.png', confidence=0.90))
    add_prof_ship_info_f_name_cords = cords[0]
    add_prof_bill_info_f_name_cords = cords[1]
    add_prof_payment_details_f_name_cords = cords[2]


minimize_pycharm_dark_mode()
get_add_profile_first_names()
