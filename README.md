# Spotify-Now

A bash script that gives you information on the current Spotify song.

![scrot](https://raw.githubusercontent.com/getmicah/spotify-now/master/scrot.png)


## Installation
Simply copy the source script to your bash path.

1. `git clone https://github.com/getmicah/spotify-now.git`
2. `cd spotify-now`
3. `sudo cp spotify-now /usr/bin`
4. `sudo chmod +x /usr/bin/spotify-now`

Arch Linux users can install [spotify-now-git](https://aur.archlinux.org/packages/spotify-now-git) it from the aur if they want to.


## Usage

Valid keywords:

* %album
* %artist
* %track

If you want a custom message when Spotify isn't running:
`-m "your custom message"`

#### Example:

```
$ spotify-now %artist - %title
Kendrick Lamar - Alright
```

```
$ spotify-now -m "your custom message" Album: %album
Album: To Pimp A Butterfly
```

And if Spotify is closed:

```
$ spotify-now -m "stopped" %title
stopped
```


## How Does it Work
This works by send a dbus message to the Spotify player which then returns information on the song currently playing. This data is then parsed using a combination of grep, tail, and cut commands.
