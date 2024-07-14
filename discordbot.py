from discord import Intents, Client, Message
from responses import getResponse

DISCORD_TOKEN: str = input("Gib deinen Discord-Token ein: ")

intents: Intents = Intents.default()
intents.message_content = True 
client: Client = Client(intents=intents)

async def sendMessage(message: Message, user_message: str) -> None:
    try:
        response: str = getResponse(user_message, str(message.author))
        if "nicht" in response:
            gif = "https://i.gifer.com/1F1I.gif"
            await message.channel.send(gif)
        elif "regnet" in response:
            gif = "https://cdn.pixabay.com/animation/2022/10/04/00/46/00-46-44-880_512.gif"
            await message.channel.send(gif)

        await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_start() -> None:
    print(f"{Client.user} is now running!")

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return 

    await sendMessage(message, message.content)

def main() -> None:
    client.run(token=DISCORD_TOKEN)

if __name__ == '__main__':
    main()
