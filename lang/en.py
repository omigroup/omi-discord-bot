
#############################################
#                                           #
#   OMI-Chan ::: Language File: (English)   #
#                                           #
#############################################

# ON_READY()
ready_logged   = " >>> BOOTUP >>> Bot User connected via Discord.py v{0}\n\n --> BOT NAME: {1}\n --> BOT UUID: {2}\n" # <-- __version__, BOT.user.name, BOT.user.id
ready_listen   = " >>> READY >>> THE BOT IS ONLINE AND LISTENING...\n\n"
ready_presence = "in the METAverse!"
local_presence = "in the BETAverse!"

# ERRORS: PRIVATE MESSAGE
dm_err_public = ":warning: This command must be given in a public channel."
dm_err_permission = "{0} <@{1}> I just tried to send you a direct message and was denied permission. In order to function properly I need you to enable this in here.\n\n:white_check_mark: To remedy, select **Privacy Settings** from the {2} server menu and enable **Allow direct messages from server members.**" # <-- LANG.emoji["warn"], ctx.message.author, ctx.message.guild.name
dm_err_critical = ":warning: Ruh roh! Something borked. ```fix\n{0}```\n`Server`  :: {1}\n`Channel` :: {2}\n`Author`  :: {3}\n`Offending Message`\n{4}"

# ERRORS: GENERAL
err_format = "{0} **INVALID COMMAND FORMAT**\n\nPlease use the format:```fix\n{1}```"

# CONFIRMATION
confirm_expire = ":alarm_clock::warning: **TIME IS UP!**\n\n30 seconds have passed so this transaction is now expired. Please try again."
confirm_cancel = ":x: **CANCELLED!**\n\nYou did not indicate that you wanted to continue so this transaction has been cancelled. Please try again."

##################################################################################
# ?INSTALL
install = ":white_check_mark: **BOT INSTALLED**\n\nI have been successfully integrated into your server. You may kick me at any time to uninstall.\n\nType `{0}help` for more info and a list of commands." # <-- PREFIX
uninstall = ":robot: I have been removed from your server. You may re-invite me at any time to re-install!"
install_err_already = "{0} I am already setup and ready to use in here, but thank you anyway!.\n\nType `{1}help` for more info and a list of commands." # <-- LANG.emoji["warn"], PREFIX

##################################################################################
# ?REGISTER
register = """
:new: **PLAYER {1} HAS JOINED**

Welcome to the open metaverse, <@{0}>! From here on out, no matter where we see one another, I shall always remember you and listen to your commands.
""" # <-- ctx.message.author.id
register_err_already = "{0} You are already registered with me :wink:"

##################################################################################
# ?HELP
help = """
:information_source: **HELP** 

Hello I am OMI-Chan, a Discord bot here to make your life a little easier.

Type one of the following commands for more info:

{0}
"""

help_err_topic404 = """
{0} Sorry <@{1}>, I am not familiar with the topic `{2}`

{3}
""" # <-- LANG.emoji["warn"], ctx.message.author.id, topic[0], topic_list

help_topics = {
	"omi" : "Learn more about The OMI Group, it's amazing members, and its incredible mission.",
	"bot" : "Learn more about the Discord bot known as OMI-Chan, benevolent overlord of the metaverse.",
}

help_omi = """
```HELP TOPIC: "The OMI Group"```

This is where we can explain more about the group and its mission...

Links to OMI resources...
"""

help_bot = """
```HELP TOPIC: "The OMI-Chan Bot"```

This is where we can explain more about the bot and its functionality...

Links to OMI resources...
"""

##################################################################################
# ?SLAP
slap = "<@{0}> slaps <@{1}> around a bit with a large trout :fish:"

##################################################################################
# EMOJI & GLYPHS
emoji = {
	"done"    : ":white_check_mark:",
	"fail"    : ":no_entry:",
	"fire"    : ":fire:",
	"love"    : ":heart:",
	"rofl"    : ":rofl:",
	"shit"    : ":poop:",
	"sleep"   : ":zzz:",
	"speak"   : ":speech_left:",
	"star"    : ":star:",
	"stop"    : ":octagonal_sign:",
	"think"   : ":hourglass_flowing_sand:",
	"thumbup" : ":thumbsup:",
	"warn"    : ":warning:",
	"what"    : ":grey_question:",
}
glyph = {
	"done"    : "\U00002705",
    "fail"    : "\U000026d4",
    "fire"    : "\U0001f525",
    "love"    : "\U0001f49b",
    "rofl"    : "\U0001f923",
    "shit"    : "\U0001f4a9",
	"sleep"   : "\U0001f4a4",
    "speak"   : "\U0001f4ac",
    "star"    : "\U00002b50",
    "stop"    : "\U0001f6d1",
	"think"   : "\U000023f3",
    "thumbup" : "\U0001f44d",
    "warn"    : "\U000026a0",
    "what"    : "\U00002754",
}

##################################################################################
# ?PUN
puns = [
	"Yesterday I accidentally swallowed some food coloring. The doctor says I'm OK, but I feel like I've dyed just a little inside.!",
	"I heard a joke the other day about a giant squid. I can't remember it clearly but it was really Kraken me up!",
	"Long fairy tales have a tendency to dragon.",
	"I think about making pancakes every morning but I always end up waffling.",
	"I used to be addicted to the Hokey Pokey, but I turned myself around.",
	"My friend's bakery burned down last night. Now his business is toast.",
	"Rick Astley will let you borrow any movie in his Pixar collection, but he will never give you Up.",
	"I got some new shoes from my drug dealer. I don't know what he laced them with but I've been tripping all day...",
	"Forrest Gump's email password is `1forrest1`",
	"My grandfather has the heart of a lion! Also a lifetime ban from the zoo.",
	"I lost my mood ring this morning and I just don't know how to feel about it.",
	"I don't trust stairs! They're always up to something...",
	"I ate at the new restaurant on the moon! The food was amazing but there was really no atmosphere.",
	"I wasn't originally going to get a brain transplant, but then I changed my mind!",
	"I tried to bid on a silent auction but it wasn't aloud!",
	"If you've ever tried to eat a clock you know it's very time consuming!",
	"I would give you a Chemistry pun but I don't think I'd get a reaction.",
	"Did you hear about the man whose entire left half was cut off? Don't worry, he's all right now!",
	"I stayed up all night searching for the missing sun, then it dawned on me.",
	"I wondered why the baseball was growing larger... then it hit me.",
	"When notes get in treble, bass-ically they get put behind bars. The alto-nate punishment is to push them off a clef and hope they land flat on sharp objects.",
	"I actually used to be a banker, but I lost interest.",
	"I am reading a book about anti-gravity. It's impossible to put down.",
	"Nope. Unintended.",
	"The shovel was a ground breaking invention, but the broom really swept everyone away.",
	"A scarecrow says, \"This job isn't for everyone, but hay, it's in my jeans.\"",
	"A Buddhist walks up to a hot dog stand and says \"Make me one with everything.\"",
	"I did a theatrical performance on puns. It was a play on words.",
	"I bet the person who created the door knocker won a Nobel prize.",
	"Towels can’t tell dirty jokes. Their sense of humor is far too dry.",
	"I heard about the cheese factory that exploded in France... There was nothing but des brie everywhere.",
	"If you don't know any sign language you should learn some. It’s pretty handy.",
	"A cross-eyed teacher could never control his pupils.",
	"I've always wanted to learn to extreme juggle, but I just don't have the balls.",
	"I used to be afraid of hurdles, but I got over it.",
	"A broken pencil is pointless.",
	"If you are cold just go stand in the corner where it's always 90 degrees!",
	"I once knew a soldier who survived both mustard gas and pepper spray! He was quite a seasoned veteran.",
	"I'd give you a pun about sausage but it's just the wurst.",
	"I have never trusted atoms. They literally make up everything!",
	"I watched a lion lose a race the other day... yeah the other guy was a total cheetah.",
	"My senile old neighbor dug a hole in my backyard and then filled it with water. I guess he meant well.",
	"A cabbage and celery walk into a bar but the cabbage gets served first because he was a head.",
	"I'm a big fan of whiteboards. I find them quite re-markable.",
	"I asked my French friend if she likes to play video games. She said, \"Wii.\"",
	"Yesterday, a clown held the door open for me. It was such a nice jester!",
	"I was going to make myself a belt made out of watches, but then I realized it would be a waist of time.",
	"You can't run through a camp ground, you can only ran. Because it's past tents.",
	"I wrote a song about a tortilla... well it's actually more of a wrap.",
	"I can cut a piece of wood in half just by looking at it! It's true! I saw it with my own eyes.",
	"Never let anyone tell you that you don't matter. You occupy space and have mass, you totally matter!",
	"Supposedly there's a bipartisan push in the Senate to legalize marijuana for arthritic therapy. In other words, there's joint support for joint support for joint support!",
	"If a Norwegian robot ever analyses a bird... it Scandinavian!",
	"I put a picture of myself in my own locket so I can be truly independent!",
	"Ugh!! The other day I went deep sea fishing with my DJ friends but they all kept dropping the bass!",
	"The other day I attended a very emotional wedding. Even the cake was in tiers!",
	"It's impossible to explain a pun to a kleptomaniac because they always take things literally.",
	"I was going to tell you a pizza joke but I decided it's just too cheesy!",
	"I heard the pet store was having a bird contest... no perches necessary!",
	"The furniture store keeps calling and leaving voice mails but all I really wanted was one night stand...",
	"Technically the library is the tallest building in your city because it has the most stories.",
	"I love the BBC’s programmes about space and time…I hope they continuum.",
	"A friend threw some magnesium chloride at me recently... it was clearly a salt!",
	"I know a baker who uses gardening tools in his kitchen. He's really raking in the dough!",
	"I used to work in a paper factory where my responsibilities were twofold.",
	"I bought my girlfriend some new slinky underwear but now she just keeps falling down the stairs.",
	"The food provided on my flight wasn't so good. It was just a little plane.",
	"Pro tip for skydiving: chute first, ask questions later!",
	"If Catwoman decided to move to Nepal, what would Catman do?",
	"I have a pen pal in South Korea. We get along so well I think they may just be my Seoul mate!",
	"You know what the Flat-Earthers always say: ***There is nothing to fear except sphere itself!***",
	"I've started investing in stocks: **beef, chicken and vegetable**... One day I hope to be a __bouillonaire__!",
	"A horse walks in to a bar and the barman says \"Why the long face?\"",
]

##################################################################################
# ?JOKE
jokes = [
	"What do you call a snobby prisoner walking down a flight of stairs?\n\n*Answer*: ||A condescending con, descending.||",
	"What rock group has four men that cannot sing?\n\n*Answer*: ||Mount Rushmore.||",
	"What did the pirate say on his 80th birthday?\n\n*Answer*: ||\"Aye, matey!\"||",
	"Why couldn't the bicycle stand up on it's own?\n\n*Answer*: ||It was two tired!||",
	"How do you make antifreeze?\n\n*Answer*: ||Take her blanket away!||",
	"What's the difference between a hippo and a Zippo?\n\n*Answer*: ||A hippo is really heavy, and a Zippo is a little lighter.||",
	"What do you call a girl with one leg that's shorter than the other?\n\n*Answer*: ||Ilene.||",
	"What does a clock do when it's hungry?\n\n*Answer*: ||It goes back for seconds.||",
	"What do you do with a dead chemist?\n\n*Answer*: ||Barium.||",
	"How does Moses make his coffee?\n\n*Answer*: ||Hebrews it.||",
	"What do you call a cow with no legs?\n\n*Answer*: ||Ground beef.||",
	"How do you throw a space party?\n\n*Answer*: ||You planet.||",
	"Why did Adele cross the road?\n\n*Answer*: ||To say \"hello\" from the other side!||",
	"What kind of concert only costs 45 cents?\n\n*Answer*: ||A 50 Cent concert featuring Nickleback.||",
	"Did you hear that the Energizer Bunny went to jail?\n\n*Answer*: ||He was charged with battery.||",
	"What did the alien say to the pitcher of water?\n\n*Answer*: ||Take me to your liter.||",
	"what is a physicist's favorite food?\n\n*Answer*: ||Fission chips.||",
	"Why do crabs never give to charity?\n\n*Answer*: ||Because they're shellfish.||",
	"Did you hear about the man arrested for stealing a Hot Chocolate in Bern?\n\n*Answer*: ||He was charged with a Swiss Miss-demeanor.||",
	"What do you call a little psychic who escapes from prison?\n\n*Answer*: ||A small medium at large!||",
	"What do vampires use for money?\n\n*Answer*: ||Crypt-o-currency!||",
	"What's the difference between unlawful and illegal?\n\n*Answer*: ||One means against the law and the other is a sick bird.||",
	"What's the best thing about Switzerland?\n\n*Answer*: ||I don't know, but the flag is a big plus!||",
	"Did you hear about the mathematician who's afraid of negative numbers?\n\n*Answer*: ||He'll stop at nothing to void them!||",
	"What do you call a French man wearing sandals?\n\n*Answer*: ||Phillipe Phillope.||",
	"Yesterday I saw a guy spill all his scrabble letters on the road...\n\n*Answer*: ||I asked him, \"What's the word on the street?\"||",
	"Why didn't Oedipus use profanity?\n\n*Answer*: ||Because he kissed his mother with that mouth!||",
	"Why did the powerpoint presentation cross the road?\n\n*Answer*: ||To get to the other slide!||"
]