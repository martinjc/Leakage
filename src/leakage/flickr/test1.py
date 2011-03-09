#!/usr/bin/python
"""Usage: python tags2set.py [OPTIONS] TAGS
TAGS is a space delimited list of tags

OPTIONS:
  -e address or --email address
  -p password or --password password
  -t title or --title title
  -d description or --description description  [optional]
  Enclose title and description in 'quotes' for multiple words
"""

__author__ = "James Clarke <james@jamesclarke.info>"
__version__ = "$Rev$"
__date__ = "$Date$"
__copyright__ = "Copyright 2004 James Clarke"

import sys
import flickr

def get_user_contacts(userID):
    """           """
    contacts = flickr.contacts_getPublicList(user_id=userID)
    return contacts

def main(*argv):

    userID = "23528219@N06"

    contacts = get_user_contacts(userID)
    print "user %s has %s contacts" % (userID, len(contacts)) 
    
if __name__ == '__main__':
    sys.exit(main(*sys.argv))
    
