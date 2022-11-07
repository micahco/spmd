# spmd — spotify metadata

Utility that pulls metadata from the proprietary Spotify client using the dbus interface.

[man page](https://cowell.dev/projects/spmd.1.html)

## Usage

`spmd [-P message] [-S message] [metadata]`

Valid macros: `%album`, `%artist`, `%title`, `%discNumber`, `%trackNumber`

**EXAMPLES:**

```
$ spmd '%artist - %title'
Vince Guaraldi - Linus And Lucy
```

If paused:

```
$ spmd -P '<paused>' '%album'
A Charlie Brown Christmas <paused>
```

If Spotify is closed:

```
$ spmd -S closed
closed
```