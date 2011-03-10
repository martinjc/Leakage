#!/usr/bin/python

__author__ = "Ian Cooper"
__version__ = "0.0.1"
__date__ = "$Date$"
__copyright__ = "Copyright 2011"

import sys
import flickr
from urllib import urlopen
from BeautifulSoup import BeautifulSoup

def get_twitter_name(profilePage):
    soup = BeautifulSoup(urlopen(profilePage).read())
    links = soup.findAll('a')
#    print links
    strlinks = links.__str__()
    strlinksTwit = strlinks[strlinks.find('twitter'):]
#    print strlinksTwit
    strTwitter = strlinksTwit[:strlinksTwit.find('"')]
#    print strTwitter
    while True:
        slash = strTwitter.find('/')
        if (slash == -1):
            break
#       print strTwitter
        strTwitter = strTwitter[slash+1:]
#        print strTwitter
    return strTwitter

def contacts_getPublicList(user_id):
    """Gets the contacts (Users) for the user_id"""
    method = 'flickr.contacts.getPublicList'
    data = flickr._doget(method, auth=False, user_id=user_id)

    try:
        if isinstance(data.rsp.contacts.contact, list):
            return [flickr.User(user.nsid, username=user.username) \
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

    userID = "26866842@N02"

    contacts = get_user_contacts(userID)
    print "user %s has %s contacts" % (userID, len(contacts)) 
    for user in contacts:
        profilePage = "http://www.flickr.com/people/"+user.id
#        print profilePage
        twitterName = get_twitter_name(profilePage)
        try:
            print "user %s name %s twitter %s" % (user.id, user.username, twitterName)
        except:
            print "user name error"
    
if __name__ == '__main__':
    sys.exit(main(*sys.argv))
    
