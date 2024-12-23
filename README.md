# discord_mc_bot

## Prerequisites
* [Set up your discord app and bot, and install it to your server](https://discord.com/developers/docs/quick-start/getting-started#step-1-creating-an-app)
* The [`uv` package manager](https://docs.astral.sh/uv/)
* Python 3.10+

You'll also need to create an `.env` file that looks like this:
```
BOT_TOKEN=<discord bot token>
SERVER_CHANNEL_ID=<ID of the voice channel>
```

## Usage

```sh
uv run bot.py
```