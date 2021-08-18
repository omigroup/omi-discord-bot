
######################################################
#                                                    #
#   OMI-Chan ::: Function Set: (Basics Utilities)    #
#                                                    #
######################################################

# IMPORT GLOBALS & OTHER FUNCTIONS
from functions import *

##################################################################################
#
#  SPEAK ::: General Bot Output Formatter
#
async def speak(
        ctx, *, 
        target = None, 
        content = None,
        embed = None,
        embed_color = "blue",
        embed_title = "", 
        title_url = "",
        embed_author = "",
        author_url = "",
        author_icon = "",
        embed_desc = None, 
        embed_fields = [], # [{"name": "Field Title", "value": "Field content goes here"}, {...}, {...}]
        embed_thumb = "", 
        embed_image = "",
        embed_footer = "",
        footer_icon = "",
        delete_after = None, 
    ):

    # ASSEMBLE EMBED
    if embed_desc != None:
        embed = discord.Embed(color=COLOR[embed_color], title=embed_title, url=title_url, description=embed_desc)
        if embed_author != "" : embed.set_author(name=embed_author, url=author_url, icon_url=author_icon)
        if embed_thumb  != "" : embed.set_thumbnail(url=embed_thumb)
        if embed_image  != "" : embed.set_image(url=embed_image)
        if embed_footer != "" : embed.set_footer(text=embed_footer, icon_url=footer_icon)
        if len(embed_fields) > 0:
            for field in embed_fields: 
                if "inline" not in field: field["inline"] = False
                embed.add_field(name=field["name"], value=field["value"], inline=field["inline"])

    # BOT OUTPUT
    if embed_desc == None and content == None: return
    try: 
        if target == None: target = ctx
        return await target.send(content=content, embed=embed, delete_after=delete_after)
    except Exception as e: 
        
        # Catch 403 Forbidden errors and send public notices about 'em. Dag nabbit!
        if str(e).startswith("403"):
            try: 
                return await speak(ctx, embed_color="red", delete_after="30", embed_desc=LANG.dm_err_permission.format(LANG.emoji["warn"], ctx.message.author.id, ctx.message.guild.name))
            
            # If even that doesn't work, send a DM to the dev... UGH!!! Fine. MOVVVE!!!
            except Exception as e:
                print(" >>> CRITICAL ERROR >>> {}".format(e)) 
                dev_user = BOT.get_user(DEVS[0])
                if dev_user is not None:
                    print(" >>> ALERTING DEV >>> {}".format(dev_user.display_name))
                    return await speak(ctx, target=dev_user, embed_color="red", embed_title="CRITICALLY BORKED :(", embed_desc=LANG.dm_err_critical.format(e, ctx.message.guild.name, ctx.message.channel.name, ctx.message.author.display_name, ctx.message.content))


##################################################################################
#
#  REACT ::: Bot reactions to commands using predefined glyphs
#
async def react(ctx, how="none"):
    if how != "think": await ctx.message.remove_reaction(LANG.glyph["think"], BOT.user)
    if how == "none": return
    return await ctx.message.add_reaction(LANG.glyph[how])


##################################################################################
#
#  LOGGING RELATED FUCTIONS
#
try: os.stat(LOG_DIR)
except: os.mkdir(LOG_DIR)
LHF = logging.FileHandler(LOG_DIR+"debug.log")
LHF.setLevel(logging.INFO)
LFT = logging.Formatter('%(asctime)-15s - %(message)s')
LHF.setFormatter(LFT)
LOG = logging.getLogger()
LOG.setLevel(logging.INFO)
LOG.addHandler(LHF)

# MAKE A DEBUG STATEMENT
async def debug(statement):
    if CONSOLE: print(statement)
    if DEBUG: LOG.info(statement)
    if LOG_CHAN:
        chan = BOT.get_channel(LOG_CHAN)
        await chan.send(content=statement)
    return None

# RUN A BASH COMMAND LINE
async def run(command):
    try:
        if command == None: 
            if CONSOLE: await debug(" !!! ERROR: run() - No command supplied\n")
            return False
        command = list(filter(None, command))
        if CONSOLE: await debug(" >>> DEBUG >>> run() -----> COMMAND: {}".format(command))
        process = subprocess.run(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)        
        results = process.stdout.strip()
        results = results.decode("utf-8")
        if CONSOLE: await debug(" >>> DEBUG >>> run() -----> RESULTS: {}".format(results))
        if results == None or len(results) == 0: return None
        if command[0] == "curl":
            results = results.replace("'", "\"")
            results = json.loads(results)
            results = results["result"]
        return results
    except Exception as e: return await debug(" !!! ERROR: run() - {}\n".format(e))


##################################################################################
#
#  TIME-RELATED FUNCTIONS
#
async def now(): return time.time()

# Convert a UTC timestamp into a readable datetime object
async def utc2dt(timestamp):
    dt = datetime.datetime.fromtimestamp((timestamp))   # <-- convert UTC timestamp to a datetime object
    return dt.strftime("%Y-%m-%d @ %H:%M:%S UTC")      # <-- return a formatted datetime string

# Turn any number of seconds into readable english like "12 hours"
async def macrotime(secs):
    if secs >= 31540000: return { "value":secs/60/60/24/7/4/12, "unit":"year"   }
    if secs >= 2628000:  return { "value":secs/60/60/24/7/4,    "unit":"month"  }
    if secs >= 604800:   return { "value":secs/60/60/24/7,      "unit":"week"   }
    if secs >= 86400:    return { "value":secs/60/60/24,        "unit":"day"    }
    if secs >= 3600:     return { "value":secs/60/60,           "unit":"hour"   }
    if secs >= 60:       return { "value":secs/60,              "unit":"minute" }
    if secs <  60:       return { "value":secs,                 "unit":"second" }


##################################################################################
#
#  ACCESS-RELATED FUNCTIONS
#
async def is_dev(uuid): return int(uuid) in DEVS
async def is_admin(member): return member.guild_permissions.administrator
async def is_mod(member): return int(R.hget(RKEY_GUILD, "role_mod")) in [int(r.id) for r in member.roles]