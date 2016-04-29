# Spotify-Now
A bash script that gives you information on the current Spotify song.

![scrot](https://raw.githubusercontent.com/getmicah/spotify-now/master/scrot.png)


## Installation

#### Arch
Install [spotify-now-git](https://aur.archlinux.org/packages/spotify-now-git) from the aur.

#### Others
Just copy the source into /usr/bin or some other directory in your bash/zsh/whatever path.


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
