import discord
from discord import SelectOption, app_commands
from discord.ext import commands, tasks
import random
from PIL import Image, ImageDraw, ImageFont, ImageOps
import io
from datetime import time
import os
from dotenv import load_dotenv

load_dotenv(".env")

TOKEN: str = os.getenv("TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user})')
    print('------')
    
    mudar_status.start()
    mandar_mensagem.start()
    await bot.change_presence(status=discord.Status.idle)
    canal = bot.get_channel(1437203672340758681)
    await canal.send('ESTOU ONLINE SEUS MERDA')

@bot.tree.command(name="pinto", description="Responde com pinto!")
async def pinto(interaction: discord.Interaction):
    await interaction.response.send_message("pinto!")
@bot.tree.command(name="soma", description="soma dois numeros!")
async def soma(interaction: discord.Interaction,numero1:int,numero2:int):
    numero_somado = numero1 + numero2
    await interaction.response.send_message(f"A soma é: {numero_somado}")
    
@bot.tree.command(name="ship", description="faca um ship!")
@app_commands.describe(
    pessoa1="Primeira pessoa para o ship",
    pessoa2="Segunda pessoa para o ship"
)
async def ship(interaction: discord.Interaction,pessoa1:discord.User,pessoa2:discord.User):
    porcentagem = random.randint(0,100)
    metade1 = pessoa1.name[:len(pessoa1.name)//2]
    metade2 = pessoa2.name[len(pessoa2.name)//2:]
    nomeship = metade1 + metade2

    imagem1 = await pessoa1.avatar.read()
    avatar1 = Image.open(io.BytesIO(imagem1))
    avatar1 = avatar1.resize((250, 250))

    imagem2 = await pessoa2.avatar.read()
    avatar2 = Image.open(io.BytesIO(imagem2))
    avatar2 = avatar2.resize((250, 250))

    fundo = Image.new('RGB', (500,300), (56, 56, 56))
    fundo.paste(avatar1, (0, 0))
    fundo.paste(avatar2, (250, 0))
    

    fundodraw = ImageDraw.Draw(fundo)
    fundodraw.rectangle(((0, 250), (500*(porcentagem/100), 300)), fill="red")

    fonte = ImageFont.truetype("Inter_18pt-Bold.ttf", 32)
    fundodraw.text((230, 255), f"{porcentagem}%", font=fonte)
    
    buffer = io.BytesIO()
    fundo.save(buffer, format="PNG")
    buffer.seek(0)

    await interaction.response.send_message(f"**Sera que temos um novo casal aq?**\n`{pessoa1.name}` + `{pessoa2.name}` = `{nomeship}`\n eles tem **{porcentagem}%** de dar certo", file=discord.File(fp=buffer, filename="ship.png"))

 
@bot.tree.command(name="d20", description="VC SABE OQ CARALHOS Ë UM D20 NE? é um dado de 20 lados😁")
async def d20(interaction: discord.Interaction):
    dado = random.randint(1,20)
    if dado < 5:
     await interaction.response.send_message(f"que merda deu {dado}")  
    elif dado == 20:
      await interaction.response.send_message(f"CARALHO DEU {dado}")
    else:
      await interaction.response.send_message(f"o numero do dado é {dado}")


@bot.tree.command(name="gay", description="GAY")
@app_commands.describe(
    pessoa1="pessoa gay",
)
async def ship(interaction: discord.Interaction,pessoa1:discord.User):
    imagem1 = await pessoa1.avatar.read()
    avatar1 = Image.open(io.BytesIO(imagem1))
    avatar1 = avatar1.resize((250, 250))

    fundo = Image.new('RGB', (500,300), (56, 56, 56))
    fundo.paste(avatar1, (0, 0))

    fonte = ImageFont.truetype("Inter_18pt-Bold.ttf", 32)
    fundo.text((250, 0), f"GAY", font=fonte)

    buffer = io.BytesIO()
    fundo.save(buffer, format="PNG")
    buffer.seek(0)
    
    await interaction.response.send_message(file=discord.File(fp=buffer, filename="GAY.png"))


    
@tasks.loop(seconds=60)

async def mudar_status():
    lista_status = ["eu like man", "we like casting spells", "tenho muitas enxadas"]
    novo_status = random.choice(lista_status)
    await bot.change_presence(activity=discord.Game(name=novo_status))

@tasks.loop(time=time(hour=18, minute=50, second=0))
async def mandar_mensagem():
    lista_mensagens = ["@everyone vamo entra em call", "eu gosto de homens masculos", "algm quer ouvir uma piada? @everyone"]
    mensagem = random.choice(lista_mensagens)
    canal = bot.get_channel(1437203672340758681)
    await canal.send(mensagem)

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if after.channel.id == 1233597795009826944:
            lista_mensagens = [f"{member.mention} entrou da call", f"{member.mention} finalmente entrou na call", f"{member.mention} OIIIIIIIIIIIIIIIIIIIIIIIIII"]
            mensagem = random.choice(lista_mensagens)
            canal = bot.get_channel(1437203672340758681)
            await canal.send(mensagem)

   
    elif before.channel is not None and after.channel is None:
        if before.channel.id == 1233597795009826944:   
            lista_mensagens = [f"{member.mention} saiu da call", f"{member.mention} Porque voce saiu da call??😭😭😭😭😭"]
            mensagem = random.choice(lista_mensagens)
            canal = bot.get_channel(1437203672340758681)
            await canal.send(mensagem)

@bot.command()
async def gay(ctx:commands.Context):
    imagem1 = await ctx.author.avatar.read()
    avatar1 = Image.open(io.BytesIO(imagem1))
    avatar1 = avatar1.resize((250, 250))

    fundo = Image.new('RGB', (500,300), (56, 56, 56))
    fundo.paste(avatar1, (0, 0))

    fonte = ImageFont.truetype("Inter_18pt-Bold.ttf", 32)
    fundo.text((250, 0), f"GAY", font=fonte)

    buffer = io.BytesIO()
    fundo.save(buffer, format="PNG")
    buffer.seek(0)
    
    await ctx.reply(file=discord.File(fp=buffer, filename="GAY.png"))

@bot.command()
async def homo(ctx):
    url_imagem = "https://i.pinimg.com/736x/d3/7d/af/d37daf9c19268da35cd1e51b39add302.jpg"
    await ctx.reply(url_imagem)




bot.run(TOKEN)