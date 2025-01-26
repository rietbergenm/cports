#!/bin/sh

if [ -z "$__NIX_SET_ENV_DONE" ]; then
	. /etc/default/nix

	DATA_PATH="${XDG_DATA_DIRS-/usr/local/share:/usr/share}"

	if [ "$USE_XDG_BASE_DIRS" == true ] ; then
		NIX_PREFIX="${XDG_STATE_HOME-$HOME/.local/state}/nix/profile"
	else
		NIX_PREFIX="$HOME/.nix-profile"
	fi

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

