
# Spektrum Discord Bot 🤖

<https://spektrumrf.github.io/bot/>

[Invite](https://discordapp.com/oauth2/authorize?&client_id=693862590866128937&permissions=66583873&scope=bot)

## Commands ℹ️

```
Spektrum Discord Bot 🤖

Kommandon:
  aslak          Lappländsk svenska
  hej            Hej på dej
  inbjudan       Skapa en tillfällig inbjudan
  kasta          Kasta ett specifierat antal tärningar
Memes:
  dank           420
  data           01100011 01110011
  fyssa          pi=3
  gegga          60°10'15.2"N 24°57'22.6"E
  kemma          H2O+H2O=H4O
  mafs           1+2+3+...=-1/12
  meme           Random
  stenar         Geologi såklart
Minecraft:
  minecraft      Se om nån server är uppe och om nån fellow gamer är online
Music:
  join           Joins a voice channel
  leave          Clears the queue and leaves the voice channel
  loop           Loops the currently playing song
  now            Displays the currently playing song
  pause          Pauses the currently playing song
  play           Plays a song
  queue          Shows the player's queue
  remove         Removes a song from the queue at a given index
  resume         Resumes a currently paused song
  shuffle        Shuffles the queue
  skip           Vote to skip a song, the requester can automatically skip
  stop           Stops playing song and clears the queue
  summon         Summons the bot to a voice channel
  volume         Sets the volume of the player
Ruben:
  ruben          Sök fakta eller lös svåra matteproblem
Sitz:
  hitta          Hitta en sång i sångboken
  lista          Lista alla sånger som börjar på en bokstav
  text           Få texten till en sång (BETA)
Svammel:
  svammel        Hmm ...
​No Category:
  contribute     Add new parts to me
  documentation  Bot is feeling well documented
  help           Shows this message
  text-to-speech I sometimes speak ;)

Type !help command for more info on a command.
You can also type !help category for more info on a category.
```

## Develop 💻

### Secrets

Skapa en `.env` fil med

```
DISCORD_TOKEN=...
WOLFRAM_APP_ID=...
```

som är tillgängliga åt användare med admin access till denna repo.

Bot rättigheter ändras i discord developer console https://discordapp.com/developers

### Run

```bash
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ cd bot
$ python bot.py
...
$ deactivate
```

### Docker 🐋

```bash
$ docker build -t bot .
$ docker run -it bot
$ heroku container:login
$ heroku container:push worker
$ heroku container:release worker
```

### Documentation 📖

```bash
$ cd docs
$ pip install -r requirements.txt
$ sphinx-apidoc -o _modules ../bot
$ make html
$ xdg-open _build/html/index.html
$ make github
```

### Lint 🔍
```bash
$ autopep8 --in-place --aggressive --max-line-length 200 --recursive bot
```
