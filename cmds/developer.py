
################################################
#                                              #
#   OMI-Chan ::: Command Module: (Developer)   #
#                                              #
################################################

# IMPORT FUNCTIONS
from functions import *

'''
COMMANDS IN THIS MODULE
-----------------------
- ?off
'''

# BEGIN CLASS
class Developer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ##################################################################################
    #
    #  (?) OFF ::: Cleanly shuts the bot down.
    #  
    #  FORMAT --> ?off
    #
    @commands.command()
    async def off(self, ctx):

        # CHECK ACCESS
        if not await is_dev(ctx.message.author.id): return await react(ctx, "stop")
        try: await ctx.message.delete() # <-- DELETE MESSAGE
        except: pass

        # BOT OUTPUT
        await speak(ctx, embed_color="gray", embed_desc="{0} Shutting down...".format(LANG.emoji["sleep"]), delete_after=15)
        await react(ctx, "sleep")
        
        # GO INVISIBLE
        await BOT.change_presence(status=discord.Status.invisible)

        if CONSOLE:
            await debug("\n=========================================================================")
            await debug(" >>> POWER >>> Bot connection closed.")
            await debug("=========================================================================\n\n")

        # KILL CONNECTION
        await BOT.close()
        return

# ADD COMMANDS TO BOT
def setup(bot): BOT.add_cog(Developer(bot))

#########################################
######################################EOF