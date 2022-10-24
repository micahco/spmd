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
Vince Guaraldi - Linus And Lucy
```

```
$ spotify-now -p "paused" -e "stopped" -i "Album: %album"
A Charlie Brown Christmas
```

If Spotify is closed:

```
$ spotify-now -e "closed"
closed
```

If Spotify is paused:

```
$ spotify-now -p "paused"
paused
```

With the `--escape` parameter:
```
$ spotify-now -i "%artist"
Kenny Rogers & The First Edition

$ spotify-now -i "%artist" --escape
Kenny Rogers &amp; The First Edition
```