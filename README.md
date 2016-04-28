# Spotify-Now
A bash script that gives you information on the current Spotify song.

# Usage
Valid song info:

* %album
* %artist
* %track

Example:

```$ spotify-now %artist - %title

```

# How?
This works by send a dbus message to the Spotify player which then returns information on the song currently playing. This data is then parsed and echoed.
