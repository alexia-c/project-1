import tweepy

from authorization_tokens import *

import random

import pronouncing

# Option 1:
# Pick a phrase randomly from a list of phrases:

# phrase_list = [ "A male cat is called a tom.",
#                 "A female cat is called a molly." ]
#
# random_number = random.randrange( len(phrase_list) )
# message = phrase_list[random_number]
#api.update_status(message)


# Option 2:
# Create a sentence template with some blanks, and
# randomly pick a word from a list to fill in each blanks

# word_list = [ "apples", "bananas", "carrots", "dates"]
#
# string_template = "Some people think {} are good, but I like {}."
#
# random_number = random.randrange( len(word_list) )
# word1 = word_list[ random_number ]

# random_number = random.randrange( len(word_list) )
# word2 = word_list[ random_number ]
#
# message = string_template.format(word1,word2)


# Option 3:
# Randomly pick a template from a list, then randomly pick words
# from a word list, and use the words to fill in the template

word_list = [ "2419", "2319", "2219", "2119",  "2519" ]
word_list1 = [ "Earth", "Mars", "Jupiter", "Saturn",  "Planet04" ]
word_list2 = [ "Eve watered the plants. The leaves grew different patterns depending on how often Eve watered them.",
 "Eve took their supplements and vitamins. Pink, blue, and yellow pills.",
  "Eve washed the dishes. There were more than usual because of the feast they had last night.",
  "Eve did their 54 step skincare routine.",  "Eve watched the news while they ate breakfast. Nothing new." ]
word_list3 = [ "dog", "cat", "snake", "rat",  "hamster" ]
word_list4 = [ "Frank", "Steve", "Mildred", "Fluffy",  "Ms. Sprinkles" ]
word_list5 = [ "sword", "nunchucks", "umbrella", "crossbow",  "lunch" ]
word_list6 = [ "pineapple", "coconut", "banana", "grapefruit",  "pear" ]
word_list7 = [ "wizard", "barbarian", "monk", "entrepeneur",  "cartoon mascot" ]
word_list8 = [ "Levi", "Charlie", "Quinn", "Marley",  "Kendall" ]
word_list9 = [ "smoothie", "coffee", "juice", "martini",  "kombucha" ]
word_list10 = [ "eleventh", "seventh", "ground", "forty-fourth",  "twentieth" ]
word_list11 = [ "second", "third", "fourth", "fifth",  "sixth" ]
word_list12 = [ "grinning", "sympathetic", "sneering", "unbothered",  "innocent" ]
word_list14 = [ "fuming.", "seething.", "furious.", "livid.",  "at a boiling point." ]
word_list15 = [ "salami sandwich", "pad thai", "quiche", "baked potato",  "lasagna" ]
word_list16 = [ "eat it.", "chuck it out the window.",
                "open the bag and pour the contents of the lunch into Eve’s bag.",
                "throw it on the ground.",  "toss it in the trash." ]
word_list17 = [ "glared at Eve as he walked back towards his desk.", "stormed out the office.",
                "walked back to his desk sulking.", "flipped Eve off and went back to work.",
                "kicked Eve’s desk and hurt his foot." ]

string_template = "The year was {} on {}."
random_number = random.randrange( len(word_list) )
word1 = word_list[ random_number ]
random_number = random.randrange( len(word_list1) )
word2 = word_list1[ random_number ]

string_template1 = "Eve got up from bed and did their usual routine. {}"
random_number = random.randrange( len(word_list2) )
word3 = word_list2[ random_number ]

string_template2 = "Eve fed the {}, {}, and played with them for a while."
random_number = random.randrange( len(word_list3) )
word4 = word_list3[ random_number ]
random_number = random.randrange( len(word_list4) )
word5 = word_list4[ random_number ]

string_template3 = "Eve got dressed to go to work. Eve grabbed their {} and headed out."
random_number = random.randrange( len(word_list5) )
word6 = word_list5[ random_number ]

string_template4 = "Eve walked on the path through the city to get to their office. Eve bought a {} from the merchant on the path. They ate it in 2 bites."
random_number = random.randrange( len(word_list6) )
word7 = word_list6[ random_number ]

string_template5 = "About a half a mile away from work, Eve encountered a {}. They challenge Eve to a duel. Before Eve could react, they sprinted towards Eve at full speed. As Eve sees them going for an attack, Eve pulls out their weopon to protect themselves from the oncoming danger."
random_number = random.randrange( len(word_list7) )
word8 = word_list7[ random_number ]

string_template6 = "Eve ended up killing the attacker in self-defense. Eve was about to be late to work, there was no time to bring this up to the police."

string_template7 = "When Eve finally got to work, the new intern, {}, who offered them a {}."
random_number = random.randrange( len(word_list8) )
word9 = word_list8[ random_number ]
random_number = random.randrange( len(word_list9) )
word10 = word_list9[ random_number ]

phrase_list = [ string_template.format(word1,word2), string_template1.format(word3),
string_template2.format(word4,word5), string_template3.format(word6), string_template4.format(word7),
string_template5.format(word8), string_template6, string_template7.format(word9,word10) ]

message = phrase_list[random_number]

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)

# template_list = [ "If you like {}, you'll love {}.",
#                  "You might think I'm a {} person, but actionally I love {}.",
#                  "You'd never guess it but I like {} even more than {}" ]
# random_number = random.randrange( len(template_list) )
# template = template_list[random_number]
#
# random_number = random.randrange( len(word_list) )
# word1 = word_list[ random_number ]
#
# random_number = random.randrange( len(word_list) )
# word2 = word_list[ random_number ]




# Option 4:
# Basic search
# search_results = api.search( q="hate filter:safe", lang="en", tweet_mode="extended" )
# random_number = random.randrange( len(serach_results) )
# random_tweet = search_results[random_number]
# message = random_tweet.full_text.replace( "hate", "love")
# api.update_status(message)

# Option 5:
# Reply to a randomly selected mention
# mentions = api.mentions_timeline()
# random_number = random.randrange( len(mentions) )
# random_mention = mentions[random_number]
#
# message = "@" + random_mention.user.screen_name + "I am a bot.+"
# api.update_status(message, in_reply_to_status_id=random_mention.id)

# Option 5B
# Replay to the most recent mention, with rhyme
# mentions = api.mentions_timeline(count=1)
# mention = mentions[0]
#
# mention_word_list = mention.text.split()
# random_number = random.randrange( len(mention_word_list) )
# word = mention_word_list[random_number]
#
# rhyming_word_list = pronouncing.rhymes(word)
# random_number = random.randrange( (rhyming_word_list) )\
# rhyme = rhyming_word_list[random_number]
#
# template = "Some people like {}, but I like {}."
# message = "@" + _mention.user.screen_name + "" + template.format(word, rhyme)
#
# api.update_status(message, in_reply_to_status_id=mention.id)




# api.update_status("This is a test.")

print("Done.")
