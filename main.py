import discord
from discord.ext import commands
# A variável intents armazena as permissões do bot
intents = discord.Intents.default()
# Ativar a permissão para ler o conteúdo das mensagens
intents.message_content = True
# Criar um bot e passar as permissões
bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

@bot.command()
async def ajuda(ctx):
    """Mostra a lista de comandos disponíveis."""
    texto_ajuda = (
        "**🤖 Lista de Comandos do Bot:**\n\n"
        "`$ajuda` - Mostra esta mensagem de ajuda.\n"
        "`$joined @usuario` - Diz quando o membro entrou no servidor.\n"
        "`$soma <num1> <num2>` - Soma dois números.\n"
        "`$sub <num1> <num2>` - Subtrai o segundo número do primeiro.\n"
        "`$mult <num1> <num2>` - Multiplica dois números.\n"
        "`$div <num1> <num2>` - Divide o primeiro número pelo segundo.\n\n"
        "*Você também pode interagir comigo no chat usando `$hello` ou `$bye`!*"
    )
    await ctx.send(texto_ajuda)

@bot.command()
async def soma(ctx, num1: float, num2: float):
    """Soma dois números."""
    resultado = num1 + num2
    await ctx.send(f'🔢 O resultado de {num1} + {num2} é: **{resultado}**')

@bot.command()
async def sub(ctx, num1: float, num2: float):
    """Subtrai dois números."""
    resultado = num1 - num2
    await ctx.send(f'🔢 O resultado de {num1} - {num2} é: **{resultado}**')

@bot.command()
async def mult(ctx, num1: float, num2: float):
    """Multiplica dois números."""
    resultado = num1 * num2
    await ctx.send(f'🔢 O resultado de {num1} * {num2} é: **{resultado}**')

@bot.command()
async def div(ctx, num1: float, num2: float):
    """Divide dois números (com validação para divisão por zero)."""
    if num2 == 0:
        await ctx.send('❌ Erro: Não é possível dividir por zero!')
    else:
        resultado = num1 / num2
        await ctx.send(f'🔢 O resultado de {num1} / {num2} é: **{resultado}**')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Diz quando um membro entrou no servidor."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')   

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        
    if message.content.startswith('$hello'):
        await message.channel.send("Hello!")
        return
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
        return

    await bot.process_commands(message)

bot.run("")
