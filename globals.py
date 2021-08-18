
#####################################
#                                   #
#   OMI-Chan ::: Global Variables   #
#                                   #
#####################################

# REQUIRED MODULES
import asyncio
import collections
import datetime
import discord
from   discord.ext import commands, tasks
import json
import lang.en as LANG
import logging
import os
import random
import redis
import requests
import subprocess
import sys
import time
import traceback

# LOCAL DEBUG SWITCH
####################
LOCAL = True      # <-- TRUE = Local Sandbox | FALSE = Live Running Bot
####################

# DEV CONTROLS
CONSOLE = True # Set to True to send output to console
DEBUG = True # Set to True to log output to debug.log
LOG_DIR = "./logs/" if LOCAL else "/var/log/omichan/" # Where to place debug.log
LOG_CHAN = False # Set to False to disable, Set to chan ID to log debug output to that channel

# REDIS CONNECTION
R = redis.Redis(host="127.0.0.1", port=6379, decode_responses=True)
if not R.ping(): 
    print(" >>> ERROR >>> Unable to connect to Redis @ 127.0.0.1:6379")
    exit()
RedisServerInfo = R.info()
print(" >>> BOOTUP >>> Connected to Redis Server v{}".format(RedisServerInfo["redis_version"]))

# REDIS KEY MAPPING
RKEY_GUILDS  = "OMI::Guilds"     # {guild_id:timestamp}     <-- Lists all installed guilds and their install timestamp
RKEY_RETIRED = "OMI::Retired"    # {guild_id:timestamp}     <-- Lists all retired guilds and their uninstall timestamp
RKEY_GUILD   = "OMI::Guild::{0}" # {key:value}              <-- Per-guild settings
RKEY_USERS   = "OMI::Users"      # {user_id:timestamp}      <-- Lists all registered users and their registration timestamp
RKEY_USER    = "OMI::User::{0}"  # {key:value}              <-- Per-member settings
RKEY_FLAGS   = "OMI::Flags"      # {user_id:flag,flag,flag} <-- Flags set to handle various function flow
RKEY_ROLES   = "OMI::Roles::{0}" # {role_key:role_id}       <-- Stores functional bot roles per guild with their unique IDs
RKEY_CHANS   = "OMI::Chans::{0}" # {chan_key:chan_id(s)}    <-- Stores functional channels per guild with their unique IDs
RKEY_TIMERS  = "OMI::Timers"     # {message_id:timestamp}   <-- Tracks internal messages and when they are to be deleted

# BOT INFORMATION
PREFIX = "?"
UUID = 464983705140854784 if LOCAL else 869826190662311936 # OMI-Chan
DEVS = [
	390246955282071564 # Cause
] 
INTENTS = discord.Intents.default()
INTENTS.members = True
INTENTS.presences = True
BOT = commands.Bot(command_prefix=PREFIX, description="OMI Discord Bot", case_insensitive=True, intents=INTENTS)
BOT.remove_command("help")
print(" >>> BOOTUP >>> Connected to Discord API")

# DEFINE COMMAND SETS
CMDS = [
    "cmds.admin",
    "cmds.developer",
    "cmds.fun",
    "cmds.member",
    "cmds.support",
]

# EMBED STRIPE COLORS
COLOR = {
	"black"   : 0x000000,
	"gray"    : 0x999999,
	"white"   : 0xffffff,
	"red"     : 0xff0000,
	"orange"  : 0xff9900,
	"yellow"  : 0xffcc4d,
	"green"   : 0x00ff00,
	"blue"    : 0x0099ff,
	"purple"  : 0x9933ee,
	"pink"    : 0xff88aa,
}

# DISCORD EMBED FOOTER
FOOTER_TEXT = ""
FOOTER_ICON = ""

# These commands can be given in private messages
DM_SAFE_CMDS = [
    "help",
    "debug",
    "methods",
    "poweroff",
	"install",
]

ROLENAME_ADMIN = "OMI Bot Admin"
ROLENAME_MEMBER = "OMI Member"

#########################################
######################################EOF