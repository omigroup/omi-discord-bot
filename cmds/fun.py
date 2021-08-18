
#############################################
#                                           #
#   OMI-Chan ::: Command Module: (Basics)   #
#                                           #
#############################################

# IMPORT FUNCTIONS
from functions import *

'''
COMMANDS IN THIS MODULE
-----------------------
- ?hello
- ?slap
- ?joke
- ?pun
'''

# BEGIN CLASS
class Fun(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
       
    ##################################################################################
    #
    #  (?) HELLO USER ::: Gotta start somewhere, right?
    #  
    #  FORMAT --> ?hello
    #
    @commands.command(aliases=["hi","hey","allo"])
    async def hello(self, ctx):
        hello = [
            "{0}!",
            "{0}!!",
            "{0}!!!",
            "Hi {0}!",
            "Hey {0}!",
            "Hiya {0}!",
            "Hello {0}!",
            "Oh hey {0}!",
            "Whaddup {0}!",
            "Good day {0}!",
            "Greetings {0}!",
            "Hello there {0}!",
            "What? Oh it's {0}!",
            "Oh hello there {0}!",
            "Why hello there {0}!",
            "And hello to you {0}!",
            "=(^_^)= ohayogozaimasu {0}-channnn! What? Too much?",
        ]
        await speak(ctx, content=str(random.choice(hello)).format(ctx.message.author.display_name))
        await react(ctx, "done")
        return 

    ##################################################################################
    #
    #  (?) SLAP ::: Just a simple example of tagging a user in a command
    #  
    #  FORMAT --> ?slap @User
    #
    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        await speak(ctx, embed_desc=LANG.slap.format(ctx.message.author.id, member.id))
        await react(ctx, "done")
        return 

    @slap.error
    async def slap_error(self, ctx, error):          
        if isinstance(error, commands.errors.MissingRequiredArgument):
            formatting = "{0}slap @User".format(PREFIX)
            await speak(ctx, embed_color="red", delete_after="15", embed_desc=LANG.err_format.format(LANG.emoji["warn"], formatting))
            await react(ctx, "warn")
            return 

    ##################################################################################
    #
    #  (?) JOKE ::: Tell a random joke
    #  
    #  FORMAT --> ?joke
    #
    @commands.command()
    async def joke(self, ctx):
        await speak(ctx, content=str(random.choice(LANG.jokes)).format(ctx.message.author.display_name))
        await react(ctx, "rofl")
        return 

    ##################################################################################
    #
    #  (?) PUN ::: Tell a random pun
    #  
    #  FORMAT --> ?pun
    #
    @commands.command()
    async def pun(self, ctx):
        await speak(ctx, content=str(random.choice(LANG.puns)).format(ctx.message.author.display_name))
        await react(ctx, "rofl")
        return 
        






















# ADD COMMANDS TO BOT
def setup(bot): BOT.add_cog(Fun(bot))

#########################################
######################################EOF