import json, os
from unicodedata import name
from discord.ext import commands
import discord
from discord.ext.commands import has_permissions
from discord.utils import get
from random import  randint 

class Crear_Respuesta():
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.respuesta = discord.Embed(
            title = self.title,
            description= self.content,
            colour= int("DC75FF",16)
            )
    @property
    def enviar(self):
        return self.respuesta

def main():
    if os.path.exists('config.json'):
        with open('config.json') as f:
            config_data = json.load(f)
    else:
        template = {'prefix': '!', 'token': "", 'palabrasbaneadas': []}
        with open('config.json', 'w') as f:
            json.dump(template, f)

    prefix = config_data["prefix"]
    token = config_data["token"]
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix = prefix, intents = intents,description= "Bot MKZC")
    #eventos
    @bot.event
    async def on_ready():
        print(f"sesion iniciada :)")
        await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"MKZC"))
    # Comandos
    @bot.command(name="saludar", help= "El bot te saludara")
    async def saludar(ctx):
        await ctx.reply(f'Kfue {ctx.author}, ¿Cómo es?')
    @bot.command(name="diablo", help= "El diablo")
    async def diablo(ctx):
        await ctx.reply(f'El diablo loco')
        await ctx.reply(f'https://media.tenor.com/46fm1uchOogAAAAd/evil-homer-homer.gif')

    @bot.command(name='sumar', help="Sumar dos números")
    async def sumar(ctx, num1: int, num2: int):
        suma = num1+num2
        respuesta = Crear_Respuesta('El resultado de la suma es:', suma)
        await ctx.reply(embed = respuesta.enviar)

    @bot.command(name='multi', help="Multiplicar dos números")
    async def multi(ctx, num1: int, num2: int):
        multi = num1*num2
        respuesta = Crear_Respuesta('El resultado de la multiplicacion es:', multi)
        await ctx.reply(embed = respuesta.enviar)
    
    @bot.command(name='div', help="Dividir dos números")
    async def div(ctx, num1: int, num2: int):
        div = num1/num2
        sobra = num1%num2
        respuesta = Crear_Respuesta('El resultado de la divicion es:', div, "la sobra es: ", sobra)
        await ctx.reply(embed = respuesta.enviar)
    
    @bot.command(name="random", help="un numero randon entre x y z numeros")
    async def random(ctx, num1: int, num2: int):
        random = randint(num1, num2)
        respuesta = Crear_Respuesta("El numero random es: ", random)
        await ctx.reply(embed = respuesta.enviar)

    bot.run(token)

if __name__ == '__main__':
    main()