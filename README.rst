======
muttrc
======

As I don't like the way mutt manage mutliple mailboxes, I launch one mutt per mailbox and
use shell aliases to link configuration files to commands. Each mailbox has its own
configuration file for specific configuration (like IMAP and SMTP parameters) that source
the common configuration file *common.muttrc*.

Mailboxes configuration files source a GPG encrypted file that store the password in the
format: ``set my_pass=XXXX``.

GPG configuration
=================
For not having to input the GPG passphrase each time mutt is started, I configured
``gpg-agent`` to cache unlocked keys for one day and use ``keychain`` to unlock the
passphrase at boot (like the SSH key).

.. code::

    +[=100% (83.45%)] [01:20] francois@zen:~ ¤ vim .gnupg/gpg-agent.conf
    # Force passphrase to be asked in console.
    pinentry-program /usr/bin/pinentry-tty

    # Update cache ttl (1 day so it should live a session).
    default-cache-ttl 86400
    max-cache-ttl 86400

    +[=100% (83.45%)] [01:20] francois@zen:~ ¤ gpg -k
    /home/francois/.gnupg/pubring.kbx
    ---------------------------------
    pub   rsa2048 2017-09-13 [SC] [expires: 2019-09-13]
          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    uid           [ unknown] Francois Menabe <francois.menabe@gmail.com>
    sub   rsa2048 2017-09-13 [E] [expires: 2019-09-13]

    +[=100% (83.45%)] [01:20] francois@zen:~ ¤ vim .bashrc
    ...
    # Unlock SSH private key.
    eval $(keychain --eval --agents ssh -Q --quiet --nogui id_rsa)
    # Unlock GPG key.
    eval $(keychain --eval --agents gpg -Q --quiet --nogui XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX)
    ...

    +[=100% (83.45%)] [01:20] francois@zen:~ ¤ vim .mutt/unistra
    set my_pass = "xxxx"
    +[=100% (83.45%)] [01:20] francois@zen:~ ¤ gpg -r francois.menabe@gmail.com -e .mutt/unistra
    # it generate encrypted file .mutt/unistra.gpg
    +[=100% (83.45%)] [01:20] francois@zen:~ ¤ shred .mutt/unistra
    +[=100% (83.45%)] [01:20] francois@zen:~ ¤ rm .mutt/unistra

    # Same commands for generating gmail password variable.

Unistra address book
====================

The *mutt_ldap.py* Python3 script allows to query Unistra address book LDAP server. As
password is already crypted by GPG, this script use ``python-gnupg`` password to retrieve
it. So the dependencies for this script are:

    * python-pyldap (Python3 binding to libldap)
    * python-gnupg

Deployment
==========
A simple Makefile has been created that copy all the files to *.mutt* directory.

.. code::

    +[=100% (83.45%)] [18:13] francois@zen:muttrc ¤ make
    mkdir -p ~/.mutt
    cp common.muttrc unistra.muttrc gmail.muttrc mutt-colors-solarized-light-256.muttrc vimrc signature mailcap mutt_ldap.py ~/.mutt
    mkdir -p ~/.cache/mutt
    mkdir -p ~/.cache/mutt/unistra
    mkdir -p ~/.cache/mutt/gmail
