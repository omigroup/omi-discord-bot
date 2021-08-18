
############################################
#                                          #
#   OMI-Chan ::: Command Module: (Admin)   #
#                                          #
############################################

# IMPORT FUNCTIONS
from functions import *

'''
COMMANDS IN THIS MODULE
-----------------------
- ?install
'''

# BEGIN CLASS
class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ##################################################################################
    #
    #  (?) INSTALL ::: Install the initial bot requirements
    #  
    #  FORMAT --> ?install
    #
    @commands.command()
    async def install(self, ctx):
        
        # CHECK ACCESS
        if not await is_admin(ctx.message.author): return await react(ctx, "stop")
        try: await ctx.message.delete() # <-- DELETE MESSAGE
        except: pass

        # ALREADY INSTALLED?
        if R.hexists(RKEY_GUILDS, ctx.message.guild.id): 
            await speak(ctx, embed_color="red", delete_after="15", embed_desc=LANG.install_err_already.format(LANG.emoji["warn"], PREFIX))
            return False

        # INSTALL
        await install(ctx)
        
        # BOT OUTPUT
        await speak(ctx, embed_color="green", embed_desc=LANG.install.format(PREFIX))
        return True

# ADD COMMANDS TO BOT
def setup(bot): BOT.add_cog(Admin(bot))

#########################################
######################################EOF