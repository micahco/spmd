# spmd — spotify metadata

A utility for displaying metadata for the proprietary Spotify client.

## Usage

`spmd [-P message] [-S message] 'metadata'`

Valid metadata: `%album`, `%artist`, `%title`, `%discNumber`, `%trackNumber`

**Example:**

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