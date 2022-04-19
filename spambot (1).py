from discord.ext import commands

import discord, datetime, time

def spamBot(TOKEN):
  
  
  bot = commands.Bot(command_prefix="<3-",help_command=None) 
  @bot.event
  async def on_ready():
      print(f'{bot.user} succesfully logged in!')
  
  @bot.event
  async def on_message(message):
      if message.author == bot.user:
          return

  
      await bot.process_commands(message)
  
  spam = True
  @bot.command()
  async def ping(ctx):
    await ctx.send('Pong! {0} Seconds!'.format(round(bot.latency, 1)))
  @bot.command()
  async def invite(ctx):
    await ctx.send('Invite me!!\nhttps://discord.com/api/oauth2/authorize?client_id=964469973051408387&permissions=8&scope=bot')
  
  @bot.command()
  async def stop(ctx):
      global spam
      spam = False
      await ctx.send('Spam stopped successfully,\nCheckout the website:\nhttps://blakemccullough.com/')
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
  
  #For getting how long the bot has been running for
  @bot.command(pass_context=True)
  async def uptime(ctx):

          current_time = time.time()
          difference = int(round(current_time - start_time))
          text = str(datetime.timedelta(seconds=difference))
          embed = discord.Embed(colour=0xc8dc6c)
          embed.add_field(name="Spam Bot Uptime", value=text)
          embed.set_footer(text="Made By Spoiled_Kitten#4911")
          try:
              await ctx.send(embed=embed)
          except discord.HTTPException:
              await ctx.send("Current uptime: " + text)

  #help command
  @bot.command(pass_context=True)
  async def help(ctx):
          embed = discord.Embed(colour=0xc8dc6c)
          embed.add_field(name="Start Spam", value="Use `<3-square` and the word/ping to send after and it shall start!")
          embed.add_field(name="Stop Spam", value="Use `<3-stop` to stop spam messages")
          embed.add_field(name="Ping bot", value="Use `<3-ping` to ping the bot")
          embed.add_field(name="Bot Uptime", value="Use `<3-uptime` to get the uptime of the bot")
          embed.add_field(name="Invite", value="Use `<3-invite` to get the invite link!")
          embed.set_footer(text="Made By Spoiled_Kitten#4911")
          try:
              await ctx.send(embed=embed)
          except discord.HTTPException:
              await ctx.send("An error occured\n:Awkward:\nPlease try again")
  start_time = time.time()
  bot.run(TOKEN)

if __name__ == "__main__":
  spamBotToken = "TOKEN HERE"
  spamBot(spamBotToken)
