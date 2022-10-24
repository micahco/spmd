# spotify-now

![scrot](https://raw.githubusercontent.com/getmicah/spotify-now/master/scrot.png)

## Usage

`spotify-now -i "<info>" -p "<paused>" -e "<error>"`

`"<info>"` can contain the following keywords:

* `%album`
* `%artist`
* `%disc`
* `%title`
* `%track`

`"<error>"` custom message when Spotify is closed.

`"<paused>"` custom message when Spotify is paused.

`--escape` outputs the `"<input>"` with the special characters escaped.

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

With the `--escape` parameter:
```
$ spotify-now -i "%artist - %title"
Oshi - I <3 U

$ spotify-now -i "%artist - %title" --escape
Oshi - I &lt;3 U
```


## How does it work?
spotify-now sends a dbus message to the Spotify player which then 
returns information on the song currently playing. This data is then parsed using a combination of grep, tail, and cut commands.
