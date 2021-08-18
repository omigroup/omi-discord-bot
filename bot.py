
# BONNNNNNNG!!!
print("\n\n\n\n\n\n\n\n")
print("########################################")
print("#                                      #")
print("#   OMI-Chan ::: The OMI Discord Bot   #")
print("#                                      #")
print("########################################")
print("\n")

# IMPORT FUNCTIONS
from functions import *

# ON READY...
@BOT.event
async def on_ready():
    if CONSOLE: await debug(LANG.ready_logged.format(discord.__version__, BOT.user.name, BOT.user.id))
    presence = LANG.local_presence if LOCAL else LANG.ready_presence
    await BOT.change_presence(activity=discord.Game(name=presence))
    
    if CONSOLE: await debug(LANG.ready_listen)
    return True 

# ON DISCONNECT...
@BOT.event
async def on_disconnect():
    if CONSOLE: await debug(" >>> DISCONNECTED...")
    return True 

# ON GUILD JOIN (INVITED)...
@BOT.event
async def on_guild_join(guild):
    '''
    TO DO:
    ------
    - Check if on the "retired" guilds list
        - Create a task to periodically wipe this list out (every 6 months)
        - Resurrect previous settings if applicable
    - Notify guild owner of bot presence
    '''
    return True

# ON GUILD REMOVE (KICKED)...
@BOT.event
async def on_guild_remove(guild):
    '''
    TO DO:
    ------
    - Check if on the installed guilds list
        - Retire guild
    - Notify guild owner of bot leaving
    '''
    return True

# ON MESSAGE...
@BOT.event
async def on_message(message):

    # IGNORE CRAZY SELF & OTHER "ROBOTS"
    # - This keeps things from spiraling into a dangerous
    # - loop and also keeps other bots from seizing control.
    if message == None: return False # <-- Also ignore messages without any text. For now...
    if message.author == BOT.user: return False
    if message.author.bot: return False

    # >>> DEBUG >>> Show messages and timestamp in console only when necessary
    if CONSOLE and DEBUG: 
        timestamp = await utc2dt(time.time())
        print("[{2}] ::: #{3} ::: <{0}> ::: {1}".format(message.author.name, message.content, timestamp, message.channel.name))

    # CHECK FOR FLAGS
    # - Use flags to let the bot know the status of things
    # - such as if a user has a command already pending or
    # - if a command made publicly requires certain aspects
    # - to be completed in private messages, like a temp
    # - auth token to allow just that thread.
    flags = R.hget(RKEY_FLAGS, message.author.id)
    flags = [] if flags == None else [f for f in flags.split(",") if f not in (""," ")]
    
    #########################################
    # Inconsequential local debug statement
    if len(flags) > 0: 
        if LOCAL: print(" >>> DEBUG >>> flags = {}".format(flags))
    #########################################

    # GET MESSAGE CONTEXT
    # - This is sent all the way down the async chain to 
    # - keep each user's command context from overlapping.
    ctx = await BOT.get_context(message)

    # NON-PREFIXED COMMAND ALIASES
    # - Here is a list of words or phrases that can be said to 
    # - trigger the help command. Copy this technique as needed
    # - for any other non-prefixed command aliases.
    if message.content.lower() in ["help"]:
        return await ctx.invoke(BOT.get_command("help"))

    # ALLOW CERTAIN COMMANDS IN PRIVATE DMS
    # - The commands listed in globals > DM_SAFE_CMDS are allowed
    # - to be delivered in private messages, safely outside of the
    # - piercing gaze of the public. *shudder*
    dm_safe_cmds = tuple([PREFIX+c for c in DM_SAFE_CMDS])
    if message.content.startswith(dm_safe_cmds):
        return await BOT.process_commands(message)

    # IGNORE ALL OTHER UNFLAGGED PRIVATE MESSAGES
    # - Any messages/commands delivered in DMs that are not listed
    # - above or flagged in some way are instantly ignored here.
    if isinstance(message.channel, discord.abc.PrivateChannel) and len(flags) == 0:
        return False
    
    # ONLY PROCEED IF BOT IS INSTALLED...
    if R.hexists(RKEY_GUILDS, message.guild.id):

        # Sometimes context just isn't valid. Well then bye, Felicia!
        if not ctx.valid: return False
        
        # Now then... if the message is longer than only the prefix...
        if len(message.content) > len(PREFIX):

            # And actually starts with the prefix...
            if message.content.startswith(PREFIX): 
            
                # Initially react with the little thinky hourglass
                await react(ctx, "think")

                # Process the given command and return
                time_start = await now()
                await BOT.process_commands(message)
                time_end = await now()
                time_lapsed = time_end - time_start
                await speak(ctx, content="``` >>> PING >>> {} seconds```".format(time_lapsed), delete_after=10)
                return


############################################
#
#  __MAIN__ ::: Boots and runs the bot
#
#  FORMAT --> python bot.py
#
if __name__ == "__main__":
    
    # Load each of the individual command "cogs"
    if CONSOLE: print(" >>> BOOTUP >>> Loading Command Cogs...")
    for cog in CMDS:
        try: 
            if CONSOLE: print(" >>> BOOTUP >>> Loaded --> \"{0}\"".format(cog))
            BOT.load_extension(cog)
        except Exception as err:
            print(" >>> ERROR >>> Failed to load cog: {0}".format(cog))
            print(" >>> REASON >>> {0}".format(err))
            traceback.print_exc()

    # Get the API Token from a seperate non-versioned local file
    if CONSOLE: print(" >>> BOOTUP >>> Reading in API TOKEN...")
    if LOCAL: token = open("token_local", "r") # <-- ((( that means add this to .gitignore )))
    else: token = open("token_live", "r")      # <-- ((( that means add this to .gitignore )))

    # Run it already!!!
    BOT.run(token.read(), bot=True, reconnect=True)
#########################################EOF