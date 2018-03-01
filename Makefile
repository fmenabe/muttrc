# Replace tabs by '>'
.RECIPEPREFIX = >

CONF_DIR = ~/.mutt
CACHE_DIR = ~/.cache/mutt
FILES = \
    common.muttrc \
    unistra.muttrc \
    gmail.muttrc \
    mutt-colors-solarized-light-256.muttrc \
    vimrc \
    signature \
    mailcap \
    mutt_ldap.py

all: install

install:
> mkdir -p $(CONF_DIR)
> cp $(FILES) $(CONF_DIR)
> mkdir -p $(CACHE_DIR)
> mkdir -p $(CACHE_DIR)/unistra
> mkdir -p $(CACHE_DIR)/gmail
