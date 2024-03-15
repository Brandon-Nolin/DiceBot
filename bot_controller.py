"""
Simple discord bot that will perform dice rolls.
"""
import dice_roller
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#Get bot token and developers id from .env.
load_dotenv()
TOKEN = os.getenv('TOKEN')
DEV_ID = os.getenv('DEV_ID')

#Define what events (intents) discord will send to the bot and how users can input commands.
intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="/", intents=intents)


@client.event
async def on_ready():
    print("Bot now running...")


"""
Syncs commands so they appear in the discord app UI.
"""
@client.command(name="sync")
async def synccmd(ctx):
    if str(ctx.message.author.id) == DEV_ID:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(
            f"Syncd {len(fmt)} commands"
        )
    else:
        pass
    return


"""
Command to handle rolls. Will determine which type of dice needs to be rolled and applies any modifiers before 
sending the result as a message.
"""
@client.tree.command(name="roll", description="Rolls a specified type and number of dice and adds/subtracts a modifier.")
async def roll(interaction: discord.Interaction, die: str, mod: int):
    if "d100" in die:
        print("d100")
        num_rolls = int(die.split("d")[0])

        if num_rolls == 1:
            roll = dice_roller.roll_d100()
            if mod > 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " + " + str(mod) + ".")
            elif mod < 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " - " + str(mod)[1:] + ".")
            else:
                await interaction.response.send_message("You rolled a " + str(roll) + ".")
        else:
            total = 0

            chat_message = "You rolled a ("

            for roll in range(0, num_rolls):
                current_roll = dice_roller.roll_d100()
                total += current_roll
                if roll != num_rolls - 1:
                    chat_message = chat_message + (str(current_roll) + " + ")
                else:
                    chat_message = chat_message + (str(current_roll))
            if mod > 0:
                chat_message = chat_message + (" + " + str(mod) + ").")
            elif mod < 0:
                chat_message = chat_message + (" - " + str(mod)[1:] + ").")
            else:
                chat_message = chat_message + (").")

            total = total + mod
            index = chat_message.find("(")
            chat_message = chat_message[:index] + \
                str(total) + " " + chat_message[index:]
            await interaction.response.send_message(chat_message)
    elif "d3" in die:
        print("d3")
        num_rolls = int(die.split("d")[0])

        if num_rolls == 1:
            roll = dice_roller.roll_d3()
            if mod > 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " + " + str(mod) + ".")
            elif mod < 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " - " + str(mod)[1:] + ".")
            else:
                await interaction.response.send_message("You rolled a " + str(roll) + ".")
        else:
            total = 0

            chat_message = "You rolled a ("

            for roll in range(0, num_rolls):
                current_roll = dice_roller.roll_d3()
                total += current_roll
                if roll != num_rolls - 1:
                    chat_message = chat_message + (str(current_roll) + " + ")
                else:
                    chat_message = chat_message + (str(current_roll))
            if mod > 0:
                chat_message = chat_message + (" + " + str(mod) + ").")
            elif mod < 0:
                chat_message = chat_message + (" - " + str(mod)[1:] + ").")
            else:
                chat_message = chat_message + (").")

            total = total + mod
            index = chat_message.find("(")
            chat_message = chat_message[:index] + \
                str(total) + " " + chat_message[index:]
            await interaction.response.send_message(chat_message)
    elif "d10" in die:
        num_rolls = int(die.split("d")[0])

        if num_rolls == 1:
            roll = dice_roller.roll_d10()
            if mod > 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " + " + str(mod) + ".")
            elif mod < 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " - " + str(mod)[1:] + ".")
            else:
                await interaction.response.send_message("You rolled a " + str(roll) + ".")
        else:
            total = 0

            chat_message = "You rolled a ("

            for roll in range(0, num_rolls):
                current_roll = dice_roller.roll_d10()
                total += current_roll
                if roll != num_rolls - 1:
                    chat_message = chat_message + (str(current_roll) + " + ")
                else:
                    chat_message = chat_message + (str(current_roll))
            if mod > 0:
                chat_message = chat_message + (" + " + str(mod) + ").")
            elif mod < 0:
                chat_message = chat_message + (" - " + str(mod)[1:] + ").")
            else:
                chat_message = chat_message + (").")

            total = total + mod
            index = chat_message.find("(")
            chat_message = chat_message[:index] + \
                str(total) + " " + chat_message[index:]
            await interaction.response.send_message(chat_message)
    elif "d12" in die:
        num_rolls = int(die.split("d")[0])

        if num_rolls == 1:
            roll = dice_roller.roll_d12()
            if mod > 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " + " + str(mod) + ".")
            elif mod < 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " - " + str(mod)[1:] + ".")
            else:
                await interaction.response.send_message("You rolled a " + str(roll) + ".")
        else:
            total = 0

            chat_message = "You rolled a ("

            for roll in range(0, num_rolls):
                current_roll = dice_roller.roll_d12()
                total += current_roll
                if roll != num_rolls - 1:
                    chat_message = chat_message + (str(current_roll) + " + ")
                else:
                    chat_message = chat_message + (str(current_roll))
            if mod > 0:
                chat_message = chat_message + (" + " + str(mod) + ").")
            elif mod < 0:
                chat_message = chat_message + (" - " + str(mod)[1:] + ").")
            else:
                chat_message = chat_message + (").")

            total = total + mod
            index = chat_message.find("(")
            chat_message = chat_message[:index] + \
                str(total) + " " + chat_message[index:]
            await interaction.response.send_message(chat_message)
    elif "d4" in die:
        num_rolls = int(die.split("d")[0])

        if num_rolls == 1:
            roll = dice_roller.roll_d4()
            if mod > 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " + " + str(mod) + ".")
            elif mod < 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " - " + str(mod)[1:] + ".")
            else:
                await interaction.response.send_message("You rolled a " + str(roll) + ".")
        else:
            total = 0

            chat_message = "You rolled a ("

            for roll in range(0, num_rolls):
                current_roll = dice_roller.roll_d4()
                total += current_roll
                if roll != num_rolls - 1:
                    chat_message = chat_message + (str(current_roll) + " + ")
                else:
                    chat_message = chat_message + (str(current_roll))
            if mod > 0:
                chat_message = chat_message + (" + " + str(mod) + ").")
            elif mod < 0:
                chat_message = chat_message + (" - " + str(mod)[1:] + ").")
            else:
                chat_message = chat_message + (").")

            total = total + mod
            index = chat_message.find("(")
            chat_message = chat_message[:index] + \
                str(total) + " " + chat_message[index:]
            await interaction.response.send_message(chat_message)
    elif "d6" in die:
        num_rolls = int(die.split("d")[0])

        if num_rolls == 1:
            roll = dice_roller.roll_d6()
            if mod > 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " + " + str(mod) + ".")
            elif mod < 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " - " + str(mod)[1:] + ".")
            else:
                await interaction.response.send_message("You rolled a " + str(roll) + ".")
        else:
            total = 0

            chat_message = "You rolled a ("

            for roll in range(0, num_rolls):
                current_roll = dice_roller.roll_d6()
                total += current_roll
                if roll != num_rolls - 1:
                    chat_message = chat_message + (str(current_roll) + " + ")
                else:
                    chat_message = chat_message + (str(current_roll))
            if mod > 0:
                chat_message = chat_message + (" + " + str(mod) + ").")
            elif mod < 0:
                chat_message = chat_message + (" - " + str(mod)[1:] + ").")
            else:
                chat_message = chat_message + (").")

            total = total + mod
            index = chat_message.find("(")
            chat_message = chat_message[:index] + \
                str(total) + " " + chat_message[index:]
            await interaction.response.send_message(chat_message)
    elif "d8" in die:
        num_rolls = int(die.split("d")[0])

        if num_rolls == 1:
            roll = dice_roller.roll_d8()
            if mod > 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " + " + str(mod) + ".")
            elif mod < 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " - " + str(mod)[1:] + ".")
            else:
                await interaction.response.send_message("You rolled a " + str(roll) + ".")
        else:
            total = 0

            chat_message = "You rolled a ("

            for roll in range(0, num_rolls):
                current_roll = dice_roller.roll_d8()
                total += current_roll
                if roll != num_rolls - 1:
                    chat_message = chat_message + (str(current_roll) + " + ")
                else:
                    chat_message = chat_message + (str(current_roll))
            if mod > 0:
                chat_message = chat_message + (" + " + str(mod) + ").")
            elif mod < 0:
                chat_message = chat_message + (" - " + str(mod)[1:] + ").")
            else:
                chat_message = chat_message + (").")

            total = total + mod
            index = chat_message.find("(")
            chat_message = chat_message[:index] + \
                str(total) + " " + chat_message[index:]
            await interaction.response.send_message(chat_message)
    elif "d20" in die:
        num_rolls = int(die.split("d")[0])

        if num_rolls == 1:
            roll = dice_roller.roll_d20()
            if mod > 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " + " + str(mod) + ".")
            elif mod < 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " - " + str(mod)[1:] + ".")
            else:
                await interaction.response.send_message("You rolled a " + str(roll) + ".")
        else:
            total = 0

            chat_message = "You rolled a ("

            for roll in range(0, num_rolls):
                current_roll = dice_roller.roll_d20()
                total += current_roll
                if roll != num_rolls - 1:
                    chat_message = chat_message + (str(current_roll) + " + ")
                else:
                    chat_message = chat_message + (str(current_roll))
            if mod > 0:
                chat_message = chat_message + (" + " + str(mod) + ").")
            elif mod < 0:
                chat_message = chat_message + (" - " + str(mod)[1:] + ").")
            else:
                chat_message = chat_message + (").")

            total = total + mod
            index = chat_message.find("(")
            chat_message = chat_message[:index] + \
                str(total) + " " + chat_message[index:]
            await interaction.response.send_message(chat_message)
    elif "d2" in die:
        num_rolls = int(die.split("d")[0])

        if num_rolls == 1:
            roll = dice_roller.roll_d2()
            if mod > 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " + " + str(mod) + ".")
            elif mod < 0:
                await interaction.response.send_message("You rolled a " + str(roll) + " - " + str(mod)[1:] + ".")
            else:
                await interaction.response.send_message("You rolled a " + str(roll) + ".")
        else:
            total = 0

            chat_message = "You rolled a ("

            for roll in range(0, num_rolls):
                current_roll = dice_roller.roll_d2()
                total += current_roll
                if roll != num_rolls - 1:
                    chat_message = chat_message + (str(current_roll) + " + ")
                else:
                    chat_message = chat_message + (str(current_roll))
            if mod > 0:
                chat_message = chat_message + (" + " + str(mod) + ").")
            elif mod < 0:
                chat_message = chat_message + (" - " + str(mod)[1:] + ").")
            else:
                chat_message = chat_message + (").")

            total = total + mod
            index = chat_message.find("(")
            chat_message = chat_message[:index] + \
                str(total) + " " + chat_message[index:]
            await interaction.response.send_message(chat_message)


client.run(TOKEN)
