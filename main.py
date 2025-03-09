import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load token dari file .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Bikin si bot bisa make prefix or smth 
intents = discord.Intents.default()
intents.message_content = True  # Enable baca message
bot = commands.Bot(command_prefix="!", intents=intents)

# Info pada terminal jika bot sudah on
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Jawab pesan
@bot.event
async def on_message(message):
    # Biar si bot ngga ngejawab pesan sendiri
    # Jangan di hapus
    if message.author == bot.user:
        return

    # Jawaban
    if "hello" in message.content.lower():
        await message.reply("Hi there! 😊")

    if "hi" in message.content.lower():
        await message.reply("Hello mate!")

    # Jawaban tapi versi embed
    if message.content.lower() == "server info":
        # Dapetin info server
        guild = message.guild

        # Ngebuat embed
        embed = discord.Embed(
            title="	Server Information",
            description=f"Details for **{guild.name}**",
            color=discord.Color.blue()
        )

        # Field embed
        embed.add_field(name="Members", value=guild.member_count, inline=True)
        embed.add_field(name="Owner", value=guild.owner, inline=True)
        embed.add_field(name="Created On", value=guild.created_at.strftime("%B %d, %Y"), inline=False)

        # Logo
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        # Kirim embed
        await message.reply(embed=embed)

    await bot.process_commands(message)

# Command pake prefix contoh: !hola
async def help(ctx):
    await ctx.send("There's no help for you")

# Always on (replit)
bot.run(TOKEN)