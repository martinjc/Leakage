#!/usr/bin/python

__author__ = "Ian Cooper"
__version__ = "0.0.1"
__date__ = "$Date$"
__copyright__ = "Copyright 2011"

import sys
import flickr

def contacts_getPublicList(user_id):
    """Gets the contacts (Users) for the user_id"""
    method = 'flickr.contacts.getPublicList'
    data = flickr._doget(method, auth=False, user_id=user_id)

    try:
      if isinstance(data.rsp.contacts.contact, list):
          return [User(user.nsid, username=user.username) \
                  for user in data.rsp.contacts.contact]

    except AttributeError:
      return "No users in the list"
    except:
      return "Unknown error"

def get_user_contacts(userID):
    """           """
    contacts = flickr.contacts_getPublicList(user_id=userID) 
#    contacts = contacts_getPublicList(user_id=userID) 
 
    return contacts

def main(*argv):

    userID = "23528219@N06"

    contacts = get_user_contacts(userID)
    print "user %s has %s contacts" % (userID, len(contacts)) 
    for user in contacts:
		print "user %s name %s" % (user.id, user.username)
    
if __name__ == '__main__':
    sys.exit(main(*sys.argv))
    
