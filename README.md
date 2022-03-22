# getValorantJSON
Tracks a Valorant Player and dumps a JSON with all information about his last match!
This is just a small tool to grab the latest match info about a player with Username and Tagline.

![](https://i.imgur.com/tmSG9DC.png)

# Installation

You first need an API Key from Riot Games, you can get one at the [Riot Games Developer Portal](https://developer.riotgames.com/).
Put this into an `.env` file inside the cloned folder like the following:

```
RIOT_API_KEY="RGAPI-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
```

# Usage under Windows

Download the latest .exe from [the Releases tab](https://github.com/finncyr/getValorantJSON/releases)

*Hint: You still need the .env file for the API Key!*

# Usage with Python

```
python -m pip install -r requirements.txt
python getValorantJSON.py
```