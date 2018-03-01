#!/usr/bin/env python3
# coding: utf-8

import re
import sys
import gnupg
import ldap

LDAP_URL = 'ldaps://ldapa.unistra.fr'
LDAP_BINDDN = 'uid=francois.menabe,o=uds'
LDAP_BASEDN = 'o=uds'

FIELDS = ('uid', 'cn', 'displayname', 'mail')
ATTRS = ('cn', 'mail')

PWD_RE = re.compile('^set my_pass\s*=\s*"?([^"]*)"?\n?$')

def get_ldap_pwd():
    gpg = gnupg.GPG(gnupghome='/home/francois/.gnupg', use_agent=True)
    with open('/home/francois/.mutt/unistra.gpg', 'rb') as fhandler:
        # Note: GPG key must be unlocked.
        decryption = gpg.decrypt_file(fhandler)
        if 'failed' in decryption.status:
            print('unable to decrypt password file.')
            print(decryption.stderr)
            sys.exit(1)
    return PWD_RE.search(decryption.data.decode()).group(1)

def main():
    if len(sys.argv) < 2:
        print(u'{:s}: no search string given'.format(sys.argv[0]))
        sys.exit(1)

    query = sys.argv[1]

    conn = ldap.initialize(LDAP_URL)
    conn.simple_bind_s(LDAP_BINDDN, get_ldap_pwd())
    search_filter = '(|{:s})'.format(
        u''.join('({:s}=*{:s}*)'.format(field, query) for field in FIELDS))
    entries = conn.search_s(LDAP_BASEDN, ldap.SCOPE_SUBTREE, search_filter, ATTRS)

    addresses = ['{:s}\t{:s}'.format(entry['mail'][0].decode(), entry['cn'][0].decode())
                 for _, entry in entries
                 if 'mail' in entry and 'cn' in entry]
    print(u'{:d} addresses found:'.format(len(addresses)))
    print('\n'.join(addresses))

if __name__ == '__main__':
    main()
