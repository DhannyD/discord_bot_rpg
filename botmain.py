import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

class RPGView(discord.ui.View):
    @discord.ui.button(label="Explorar", style=discord.ButtonStyle.primary, custom_id="explorar_button")
    async def explorar(self, interaction: discord.Interaction, button: discord.ui.Button):
        eventos = [
            ("Te encuentras con un grupo de bandidos.", "https://example.com/bandidos.png"),
            ("Descubres un cofre lleno de oro.", "https://example.com/cofre.png"),
            ("Un dragón aparece y ruge en la distancia.", "https://example.com/dragon.png"),
        ]
        import random
        evento, imagen = random.choice(eventos)
        embed = discord.Embed(title="Evento RPG", description=evento, color=discord.Color.gold())
        embed.set_image(url=imagen)
        await interaction.response.send_message(embed=embed, ephemeral=True)

    @discord.ui.button(label="Salir", style=discord.ButtonStyle.danger, custom_id="salir_button")
    async def salir(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Gracias por jugar. tus muertos!", ephemeral=True)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def start(ctx):
    view = RPGView()
    await ctx.send("yepa ya estoy por aqui. que tu quiere ase manito?", view=view)

bot.run('eltokenvaaquivale?')
