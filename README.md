# Spotify-Now

A bash script that gives you information on the current Spotify song.

![scrot](https://raw.githubusercontent.com/getmicah/spotify-now/master/scrot.png)


## Installation
Simply copy the source script to your bash path.

1. `git clone https://github.com/getmicah/spotify-now.git`
2. `cd spotify-now`
3. `sudo cp spotify-now /usr/bin`

Arch Linux users can install [spotify-now-git](https://aur.archlinux.org/packages/spotify-now-git) from the AUR.


## Usage

`spotify-now -i "<info>" -p "<paused>" -e "<error>"`

NOTE: order of parameters does NOT matter.

`"<info>"` can contain the following keywords:

* %album
* %artist
* %disc
* %title
* %track

`"<error>"` is your custom message when Spotify is closed.

`"<paused>"` is your custom message when Spotify is paused.

**Example:**

```
$ spotify-now -i "%artist - %title"
Kendrick Lamar - Alright
```

```
$ spotify-now -p "paused" -e "stopped" -i "Album: %album"
Album: To Pimp A Butterfly
```

If Spotify is closed:

```
$ spotify-now -e "Spotify is closed"
Spotify is closed
```

If Spotify is paused:

```
$ spotify-now -p "paused"
paused
```


## How Does it Work
This works by send a dbus message to the Spotify player which then returns information on the song currently playing. This data is then parsed using a combination of grep, tail, and cut commands.
