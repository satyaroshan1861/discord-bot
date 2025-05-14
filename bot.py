import discord
import requests
import random

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("$meme"):
            meme_url = get_meme()
            await message.channel.send(meme_url)

        if message.content.startswith("$bhanu"):
            bhanu_msg = get_bhanu_message()
            await message.channel.send(bhanu_msg)

def get_meme():
    response = requests.get("https://api.imgflip.com/get_memes")
    if response.status_code == 200:
        json_data = response.json()
        memes = json_data["data"]["memes"]
        random_meme = random.choice(memes)
        return random_meme["url"]
    else:
        return "Failed to get memes."

def get_bhanu_message():
    messages = [
        "Bhanu Roshini just stole all the ice cream and blamed Bubu 🍦😂",
        "Breaking News: Bhanu ran away to the fridge... again. 🏃‍♀️🍕",
        "Bubu says: 'I need a break from Bhanu’s cuddles!' 🧸",
        "Bhanu heard 'Runaway' and now she's moonwalking to the kitchen 🎶🕺",
        "Your girlfriend Bhanu loves you more than food... barely 😏❤️",
        "She says you're the dessert, but ice cream is still first. 🍨➡️❤️",
        "Bhanu just gave you a 5-star cuddle rating ⭐⭐⭐⭐⭐",
        "Satya tried to impress Bhanu with his cooking, but she gave the spoon to Bubu and said, ‘He stirs with more emotion.’ 🍜😭💔",
        "Satya told Bhanu ‘I love you’—she replied, ‘I love biryani more… but you’re a close second.’ 🍛❤️",
        "Bhanu was upset with Satya, so she made Bubu the judge. Verdict: Satya must buy ice cream for both. 🧸⚖️🍦",
        "Satya sang ‘Runaway’ to Bhanu… she actually ran away. Straight to the fridge. 🎶😆",
        "Bhanu asked Satya for attention. Satya blinked—and she said, ‘Too slow.’ 💅👀",
        "Satya tried to take a bite of Bhanu’s food. She activated ‘girlfriend rage mode’—he hasn't tried since. ⚡🍲🔥",
        "Bubu now has a lawyer after all the emotional damage Bhanu causes during food fights with Satya. 🧸📜💔",
        "Satya brought Bhanu flowers. She said, ‘Cool. Where’s the ice cream?’ 🌸➡️🍦",
        "They say opposites attract. Satya is chill. Bhanu is spice. Together? Instant masala explosion. 🌶️💥",
        "Bhanu said she was ‘fine’. Satya is now on a spiritual retreat until she actually means it. 😇🧘‍♂️",
        "Every time Satya says something romantic, Bhanu says ‘Awwww’—then asks, ‘Did you order food tho?’ 😍👉🍕"
    ]
    return random.choice(messages)

client = MyClient(intents=intents)
client.run("REMOVED_TOKEN") 
