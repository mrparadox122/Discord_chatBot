
import discord
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    time.sleep(2)
    bot_input = chatbot.get_response(message.content)
    await message.channel.send(bot_input)

client.run('---------your token-----------')