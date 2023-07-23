import discord
from discord.ext import commands
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import json
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
bot.remove_command('help')


current_activity = None
activity_file = 'activity.json'

def load_activity():
    try:
        with open(activity_file, 'r') as file:
            activity_data = json.load(file)
            return activity_data
    except FileNotFoundError:
        return None
activity_data = load_activity()
if activity_data:
    last_activity = discord.Game(name=activity_data['activity'])


@bot.event
async def on_ready():
    global current_activity
    await bot.change_presence(activity=current_activity)
    print(f'Logged in as {bot.user.name}')

    activity_data = load_activity()
    if activity_data:
        current_activity = discord.Game(name=activity_data['activity'])

@bot.command()
async def encrypt(ctx, plaintext):
    public_key_path = 'C:/Users/Kaias/Downloads/testing code/python/public_key.pem'
    with open(public_key_path, 'rb') as f:
        public_key = RSA.import_key(f.read())
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher.encrypt(plaintext.encode('utf-8'))
    encoded_data = base64.b64encode(encrypted_data).decode('utf-8')
    await ctx.send(f'Encrypted data: {encoded_data}')

@bot.command()
async def decrypt(ctx, encrypted_data):
    private_key_path = 'C:/Users/Kaias/Downloads/testing code/python/private_key.pem'
    with open(private_key_path, 'rb') as f:
        private_key = RSA.import_key(f.read())
        cipher = PKCS1_OAEP.new(private_key)
        decrypted_data = cipher.decrypt(base64.b64decode(encrypted_data))
    await ctx.send(f'Decrypted data: {decrypted_data.decode("utf-8")}')

@bot.command()
@commands.is_owner()  # Restrict the command to the bot owner
async def admin(ctx, command_name=None, *, description=None):
    if command_name is None:
        await ctx.send("Please provide a command name.")
        return

    if description is None:
        await ctx.send("Please provide a description.")
        return

    command = bot.get_command(command_name)
    if command:
        command.help = description
        command_descriptions[command_name] = description
        await ctx.send(f"Description for command '{command_name}' has been updated.")
    else:
        await ctx.send(f"Command '{command_name}' not found.")

@bot.command()
@commands.is_owner()  # Restrict the command to the bot owner
async def save_config(ctx):
    save_command_descriptions(command_descriptions)
    save_activity()
    await ctx.send("Bot configuration has been saved.")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

    # Log the error
    print(f'Error: {error}')
    await ctx.send('An error occurred with the command.')

@bot.command(name='help')
async def bot_help(ctx):
    embed = discord.Embed(title="Bot Commands", description="List of available commands:")

    for command_name, description in command_descriptions["regular"].items():
        embed.add_field(name=f"{bot.command_prefix}{command_name}", value=description, inline=False)

    embed.add_field(name=f"{bot.command_prefix}save_config", value="Manually save the bot configuration.", inline=False)

    await ctx.send(embed=embed)

@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("Shutting down the bot...")
    save_activity()
    await bot.close()

@bot.command()
@commands.is_owner()
async def clear(ctx):
    global clear_in_progress
    clear_in_progress = True 

    async for message in ctx.channel.history(limit=None):
        if not clear_in_progress:
            break
        
        try:
            await message.delete()
        except discord.errors.Forbidden:
            await asyncio.sleep(0.3)
            await message.delete()
            await asyncio.sleep(3) 
        await asyncio.sleep(0.00000005)

    await ctx.send("Channel cleared.")
    clear_in_progress = False 
    
@bot.command()
async def desc(ctx, *, activity: str):
    global current_activity

    if activity.lower() == "last":
        with open("activity.json", "r") as file:
            activity_data = json.load(file)
            if "last_activity" in activity_data:
                last_activity = activity_data["last_activity"]
                current_activity = discord.Game(name=last_activity)
                await bot.change_presence(activity=current_activity)
                await ctx.send(f"Bot activity has been updated to the last activity: {current_activity.name}")
            else:
                await ctx.send("There is no last activity stored.")
    else:
        current_activity = discord.Game(name=activity)
        await bot.change_presence(activity=current_activity)
        await ctx.send(f"Bot activity has been updated. New activity: {current_activity.name}")

        # Store the current activity as the last activity #
        activity_data = {"last_activity": activity}
        with open("activity.json", "w") as file:
            json.dump(activity_data, file)

@bot.command()
@commands.is_owner()
async def stop(ctx):
    global clear_in_progress
    if clear_in_progress:
        clear_in_progress = False
        await ctx.send("Clear operation stopped.")
    else:
        await ctx.send("No clear operation is in progress.")

@bot.command(name='help2')
@commands.is_owner()
async def owner_help(ctx):
    embed = discord.Embed(title="Owner Commands", description="List of available owner commands:")

    for command_name, description in command_descriptions["owner"].items():
        embed.add_field(name=f"{bot.command_prefix}{command_name}", value=description, inline=False)
    
    await ctx.send(embed=embed)

def load_command_descriptions():
    try:
        with open("command_descriptions.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"regular": {}, "owner": {}}
    except json.JSONDecodeError:
        return {"regular": {}, "owner": {}}

def load_activity():
    try:
        with open(activity_file, 'r') as file:
            activity_data = json.load(file)
            return activity_data
    except FileNotFoundError:
        return None

def save_command_descriptions(command_descriptions):
    with open("command_descriptions.json", "w") as file:
        json.dump(command_descriptions, file)

def save_activity():
    activity_data = {
        'activity': current_activity.name if current_activity else None
    }
    with open(activity_file, 'w') as file:
        json.dump(activity_data, file)

command_descriptions = load_command_descriptions()
clear_in_progress = False 

bot.run('TOKEN')
