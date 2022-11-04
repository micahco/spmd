% SPMD(1) Version 0.1 | Manual

# NAME

**spmd** — spotify metadata

# SYNOPSIS

**spmd** [-**P** *message*] [-**S** *message*] [*metadata*]

# DESCRIPTION

A utility for displaying metadata about what's now playing in Spotify.

Valid metadata: `%album`, `%artist`, `%title`, `%discNumber`, `%trackNumber`.

The options are as follows:

**-P** *message*
:	Display message if paused.

**-S** *message*
:	Display message if Spotify is closed (no `pid`).

# Examples

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