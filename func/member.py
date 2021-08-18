
############################################
#                                          #
#   OMI-Chan ::: Function Set: (Members)   #
#                                          #
############################################

# IMPORT GLOBALS & OTHER FUNCTIONS
from functions import *

##################################################################################
#
#  REGISTER ::: Create a new member profile for a given user
#
#  Returns --> (int) registered member count
#
async def register(ctx):
    
    member = ctx.message.author

    # IGNORE IF ALREADY REGISTERED
    if R.hexists(RKEY_USERS, member.id): 
        await speak(ctx, embed_color="red", delete_after="15", embed_desc=LANG.register_err_already.format(LANG.emoji["warn"], ctx.message.author.id))
        await react(ctx, "warn")
        return

    # REGISTER THE MEMBER
    time_now = await now()
    R.hset(RKEY_USERS, member.id, time_now)
    R.hincrby(RKEY_USER.format(member.id), "count_commands", 1)

    # TODO: ASSIGN MEMBER ROLE

    # TODO: AUDIT LOG

    # RETURN MEMBER COUNT
    count = R.hlen(RKEY_USERS)
    return count