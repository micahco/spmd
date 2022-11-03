# spotify-now

![scrot](https://raw.githubusercontent.com/getmicah/spotify-now/master/scrot.png)

## Usage

`spotify-now -i "<info>" -p "<paused>" -s "<stopped>"`

`"<info>"` can contain the following keywords:

* `%album`
* `%artist`
* `%title`
* `%discNumber`
* `%trackNumber`

`"<paused>"` custom message when Spotify is paused.

`"<stopped>"` custom message when Spotify is not open.

**Example:**

```
$ spotify-now -i "%artist - %title"
Vince Guaraldi - Linus And Lucy
```

If paused:

```
$ spotify-now -i "Album: %album" -p "(paused)"
A Charlie Brown Christmas (paused)
```

If Spotify is closed:

```
$ spotify-now -s "closed"
closed
```