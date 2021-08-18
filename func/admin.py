
###################################################
#                                                 #
#   OMI-Chan ::: Function Set: (Administration)   #
#                                                 #
###################################################

# IMPORT GLOBALS & OTHER FUNCTIONS
from functions import *

##################################################################################
#
#  INSTALL ::: Adds the Guild to the Bot Registry
#
async def install(ctx):
    
    guild = ctx.message.guild
    
    # REGISTER THE GUILD
    time_now = await now()
    R.hset(RKEY_GUILDS, guild.id, time_now) # <-- register the install time
    R.hincrby(RKEY_GUILD.format(guild.id), "count_commands", 1) # <-- add 1 to the commands count

    # CREATE BOT MEMBER ROLE
    member_role = discord.utils.get(guild.roles, name=ROLENAME_MEMBER)
    if member_role == None: member_role = await guild.create_role(name=ROLENAME_MEMBER, permissions=discord.Permissions.none())
    R.hset(RKEY_ROLES.format(guild.id), "member", member_role.id)

    # CREATE BOT ADMIN ROLE
    member_role = discord.utils.get(guild.roles, name=ROLENAME_ADMIN)
    if member_role == None: member_role = await guild.create_role(name=ROLENAME_ADMIN, permissions=discord.Permissions.none())
    R.hset(RKEY_ROLES.format(guild.id), "admin", member_role.id)

    # ASSIGN DEFAULT NOTICE CHANNEL
    R.hset(RKEY_CHANS.format(guild.id), "notice", ctx.message.channel.id)

    # TODO: CREATE ADMIN CHANNELS
    # Audit Channel
    # Edit Channel
    # Log Channel

    return True