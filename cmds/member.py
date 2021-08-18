
#############################################
#                                           #
#   OMI-Chan ::: Command Module: (Member)   #
#                                           #
#############################################

# IMPORT FUNCTIONS
from functions import *

'''
COMMANDS IN THIS MODULE
-----------------------
- ?register
'''

# BEGIN CLASS
class Member(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ##################################################################################
    #
    #  (?) REGIStER ::: Register an account with the bot
    #  
    #  FORMAT --> ?register
    #
    @commands.command()
    async def register(self, ctx):
        
        # REGISTER MEMBER
        count = await register(ctx)
        
        # BOT OUTPUT
        await speak(ctx, embed_color="green", embed_desc=LANG.register.format(ctx.message.author.id, count))
        await react(ctx, "done")
        return


# ADD COMMANDS TO BOT
def setup(bot): BOT.add_cog(Member(bot))

#########################################
######################################EOF