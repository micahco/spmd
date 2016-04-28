# Spotify-Now
A bash script that gives you information on the current Spotify song.

## Usage

Valid Keywords:

* %album
* %artist
* %track

If you want a custom message when Spotify isn't running:
`-m "your custom message"`

##### Example:

```
$ spotify-now %artist - %title
Kendrick Lamar - Alright
```

```
$ spotify-now Album: %album
Album: To Pimp A Butterfly
```

```
$ spotify-now -m "your custom message" Listening to %title by %artist
Listening to Alright by Kendrick Lamar
```

And if Spotify is closed:

```
$ spotify-now -m "stopped" %title
stopped
```

## How?
This works by send a dbus message to the Spotify player which then returns information on the song currently playing. This data is then parsed and echoed.
