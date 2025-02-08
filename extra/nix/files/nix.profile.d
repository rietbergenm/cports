#!/bin/sh

if [ -z "$__NIX_SET_ENV_DONE" ]; then
	. /etc/default/nix

	# default paths
	DATA_PATH="${XDG_DATA_DIRS-/usr/local/share:/usr/share}"
	XDG_STATE_HOME="${XDG_STATE_HOME-$HOME/.local/state}"

	case "$USE_XDG_BASE_DIRS" in
		"true")
				NIX_PREFIX="$XDG_STATE_HOME/nix/profile"
			;;
		"false")
				NIX_PREFIX="$HOME/.nix-profile"
			;;
		*) # "auto" is the default
		    # use nix command to parse settings so we don't have to
			case `nix --extra-experimental-features nix-command config show use-xdg-base-directories` in
				"true")
					NIX_PREFIX="$XDG_STATE_HOME/nix/profile"
					;;
				"false")
					NIX_PREFIX="$HOME/.nix-profile"
					;;
			esac
			;;
	esac

	# include the system nix profile as well
	NIX_BIN_DIRS="$NIX_PREFIX/bin:/nix/var/nix/profiles/default/bin"
	NIX_DATA_DIRS="$NIX_PREFIX/share:/nix/var/nix/profiles/default/share"

	if [ "$PREPEND" == true ]; then
		PATH="$NIX_BIN_DIRS:$PATH"
		XDG_DATA_DIRS="$NIX_DATA_DIRS:$DATA_PATH"
	else
	    PATH="$PATH:$NIX_BIN_DIRS"
	    XDG_DATA_DIRS="$DATA_PATH:$NIX_DATA_DIRS"
	fi

	export PATH  XDG_DATA_DIRS
	export __NIX_SET_ENV_DONE=1
fi
