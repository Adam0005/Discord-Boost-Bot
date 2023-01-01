import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.command()
async def boost(ctx):
  # check if the user has the "Boost Server" permission
  if ctx.author.guild_permissions.boost_server:
    # check if the user has already boosted the server
    if ctx.guild.premium_subscription_count > 0:
      await ctx.send("You've already boosted the server. Thanks for your support!")
    else:
      # boost the server
      await ctx.guild.premium_subscribe()
      await ctx.send("Thanks for boosting the server! You now have access to additional features and perks.")
  else:
    await ctx.send("Sorry, you don't have permission to boost the server. Only users with the "Boost Server" permission can use this command.")

bot.run('your-bot-token-here') 
