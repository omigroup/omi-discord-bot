
##############################################
#                                            #
#   OMI-Chan ::: Command Module: (Support)   #
#                                            #
##############################################

# IMPORT FUNCTIONS
from functions import *

'''
COMMANDS IN THIS MODULE
-----------------------
- ?help
'''

# BEGIN CLASS
class Support(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    ##################################################################################
    #
    #  (?) HELP ::: Provides users with instructions on how to use the bot as well as
    #               an example of taking a parameter to return a different result.
    #  
    #  FORMAT --> ?help
    #  FORMAT --> ?help single_keyword_topic
    #  FORMAT --> ?help "multi-word topics must be in quotes"
    #  (NOTE) The arguments are parsed by spaces automatically, hence the need for quotes
    #
    @commands.command(aliases=["rtfm","cmds","halp","wat"])
    async def help(self, ctx, *topic):
        
        topic_list = ""
        for key,desc in LANG.help_topics.items(): 
            topic_list += ":small_blue_diamond: `{0}help {1}` ::: *{2}*\n\n".format(PREFIX, key, desc)
        
        # Show help main menu
        if len(topic) == 0:
            await speak(ctx, embed_desc=LANG.help.format(topic_list))
            await react(ctx, "done")
            return 
        
        # look for specific topics
        if topic[0].lower() in ("omi","group","metaverse", "open metaverse initiative"):
            await speak(ctx, embed_desc=LANG.help_omi)
        elif topic[0].lower() in ("bot", "robot", "omi-chan","omichan","chan"):
            await speak(ctx, embed_desc=LANG.help_bot)
        
        # topic not found?
        else:
            await speak(ctx, embed_color="yellow", delete_after="30", embed_desc=LANG.help_err_topic404.format(LANG.emoji["warn"], ctx.message.author.id, topic[0], topic_list))
            await react(ctx, "warn")
            return 

        await react(ctx, "done")
        return



# ADD COMMANDS TO BOT
def setup(bot): BOT.add_cog(Support(bot))

#########################################
######################################EOF