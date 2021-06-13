import discord, pyautogui

# from discord.ext import commands, tasks
# from discord.utils import get
# from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext
# from discord import Permissions

TOKEN = 'ODUzMDQ0OTgyNTA3NjM0NzA4.YMPqDA.VYS4KBKXLyoWNL202ixYdua04eU'

client = discord.Client()

add_prof_ship_info_f_name_cords = None
add_prof_bill_info_f_name_cords = None
add_prof_payment_details_f_name_cords = None


def minimize_pycharm_dark_mode():
    """Minimize the pycharm IDE"""

    cords = (pyautogui.locateOnScreen('min_pycharm.png'))
    pyautogui.click(cords)


def get_add_profile_first_names_cords():
    """Getting coordinates for First name on Add Profile screen"""
    cords = list(pyautogui.locateAllOnScreen('first_name.png', confidence=0.90))
    # print(cords)
    return cords


def get_add_profile_last_names_cords():
    """Getting coordinates for Last name on Add Profile screen"""
    cords = list(pyautogui.locateAllOnScreen('last_name.png', confidence=0.85))
    # print(cords)
    return cords


def get_add_profile_profile_name_cords():
    """Getting coordinates for Profile name on Add Profile screen"""
    return pyautogui.locateOnScreen('profile_name.png', confidence=0.6)
    # return pyautogui.locateOnScreen('profile_name.png')


def get_add_profile_email_cords():
    """Getting coordinates for Email on Add Profile screen"""
    return pyautogui.locateOnScreen('email.png', confidence=0.7)
    # return pyautogui.locateOnScreen('email.png')


def get_add_profile_phone_num_cords():
    """Getting coordinates for Phone number on Add Profile screen"""
    return pyautogui.locateOnScreen('phone_number.png', confidence=0.7)
    # return pyautogui.locateOnScreen('phone_number.png')


def input_profile_add_profile(msg):
    # Inserting profile name
    if msg[2]:
        profile_name_cords = get_add_profile_profile_name_cords()
        pyautogui.click(profile_name_cords)
        # pyautogui.typewrite(msg[2])

    # Inserting email
    if msg[3]:
        email_cords = get_add_profile_email_cords()
        pyautogui.click(email_cords)
        # pyautogui.typewrite(msg[3])

    # Inserting phone number
    if msg[4]:
        phone_num_cords = get_add_profile_phone_num_cords()
        pyautogui.click(phone_num_cords)
        # pyautogui.typewrite(msg[4])


def input_payment_add_profile(msg):
    # Inserting first name
    if msg[2]:
        first_name_payment_cords = get_add_profile_first_names_cords()[2]
        pyautogui.click(first_name_payment_cords)
        # pyautogui.typewrite(msg[2])

    # Inserting last name
    if msg[3]:
        last_name_payment_cords = get_add_profile_last_names_cords()[3]
        pyautogui.click(last_name_payment_cords)
        # pyautogui.typewrite(msg[3])


# get_add_profile_first_names()
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    msg = message.content.split()

    # Check if we are on the Add Profile  page
    if message.content.startswith('!add_profile'):
        # Check if want to interact with profile panel
        if 'in_profile' in message.content.lower():
            input_profile_add_profile(msg)

        # Check if want to interact with payment panel
        elif 'in_payment' in message.content.lower():
            input_payment_add_profile(msg)

    # await message.channel.send(message.content)
    elif message.content == 'raise-exception':
        raise discord.DiscordException


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(TOKEN)
