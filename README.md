# getValorantJSON
Tracks a Valorant Player and dumps a JSON with all information about his last match!

![](https://i.imgur.com/tmSG9DC.png)

# Usage

You first need an API Key from Riot Games, you can get one at the [Riot Games Developer Portal](https://developer.riotgames.com/).
Put this into an `.env` file inside the cloned folder like the following:

```
RIOT_API_KEY="RGAPI-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
```

Then execute the following:

```
python -m pip install -r requirements.txt
python getValorantJSON.py
```

# Information

This is just a small tool to grab the latest match info about a player with Username and Tagline.