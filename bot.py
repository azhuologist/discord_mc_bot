from discord import Client, Intents
from dotenv import load_dotenv

from os import getenv

load_dotenv()

BOT_TOKEN = getenv('BOT_TOKEN')
SERVER_CHANNEL_ID = int(getenv('SERVER_CHANNEL_ID'))

# set only the voice states intent
intents = Intents(guilds=True, voice_states=True)
client = Client(intents=intents)

@client.event
async def on_voice_state_update(member, before, after):
    channel = before.channel or after.channel
    if channel.id == SERVER_CHANNEL_ID:
        print(f'User: {member}, previous channel: {before.channel}, current channel: {after.channel}')

        if not before.channel:
            print(f'User {member} joined {channel.name}.')
            if len(channel.members) == 1:
                print('Channel now populated, starting server...')
        
        elif not after.channel:
            print(f'User {member} left {channel.name}.')
            if len(channel.members) == 0:
                print('Channel empty, shutting down server...')


if __name__ == "__main__":
    print('Starting bot...')
    client.run(BOT_TOKEN)
