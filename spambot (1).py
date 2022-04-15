from discord.ext import commands
TOKEN = "TOKEN HERE"

bot = commands.Bot(command_prefix="<3-") 
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == 'hello':
        await message.channel.send(f'Hi {message.author}')
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')

    await bot.process_commands(message)

spam = True


@bot.command()
async def stop(ctx):
    global spam
    spam = False
    await ctx.send('spam stopped')
# Start each command with the @bot.command decorater
@bot.command()
async def square(ctx, arg): 
  # EDIT: Set spam to True again so you can restart the loop
    global spam
    spam = True
    x=0

    while (spam ==True) and (x< 100):
        # If "spam" is set to False, stop looping
        if not spam:
            break
  
        await ctx.send(arg)
        x=x+1

    #await spam(arg) # ctx.send sends text in chat



bot.run(TOKEN)

