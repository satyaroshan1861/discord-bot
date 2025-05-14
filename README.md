# Discord Meme & Bhanu Fun Bot

**Created and developed by Satya Roshan Tholeti.**  
A simple Discord bot that shares random memes and funny, personalized messages about Bhanu Roshini.

---

## Features

- Responds to `$meme` command by sending a random meme from the Imgflip API.
- Responds to `$bhanu` command by sending a random personalized Bhanu-themed funny message.
- Ignores messages from itself to prevent loops.

---

## Setup and Installation

### Prerequisites

- Python 3.7 or higher
- Discord Bot Token (create a bot on the Discord Developer Portal)
- Required Python packages:
  - `discord.py`
  - `requests`

### Install dependencies
## Usage

- Type `$meme` in any channel the bot has access to, and it will reply with a random meme from the Imgflip API.
- Type `$bhanu` to receive a fun, personalized message about Bhanu Roshini.
- The bot ignores its own messages to prevent response loops.

---

## Code Overview

- Uses the `discord.py` library with the `message_content` intent enabled to read messages.
- Fetches memes dynamically from the Imgflip API.
- Contains a hardcoded list of personalized, humorous messages about Bhanu Roshini.
- Handles commands inside the `on_message` event and sends appropriate replies.

---

## Notes & Recommendations

- Keep your Discord bot token secure and never share it publicly.
- For more scalable command handling, consider using `discord.ext.commands`.
- Extend the bot with more commands or additional APIs as needed.
- Ensure the bot has proper permissions and intents enabled in the Discord Developer Portal.
- The current meme fetching depends on the Imgflip API availability and response format.

---

## Author

Satya Roshan Tholeti

