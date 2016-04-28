# Spotify-Now
A bash script that gives you information on the current Spotify song.

## Usage
Valid song info:

* %album
* %artist
* %track

If you want a custom message when Spotify isn't running:
`-m "your custom message"`

##### Example:

```
$ spotify-now %title by %artist from %album
Common - The Light
```

```
$ spotify-now -m "- stopped -" Album: %album
Album: Madvilliany
```

And if Spotify is closed:

```
$ spotify-now -m "- stopped -" album: %album
- stopped -
```

## How?
This works by send a dbus message to the Spotify player which then returns information on the song currently playing. This data is then parsed and echoed.
