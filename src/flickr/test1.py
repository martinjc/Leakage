#!/usr/bin/python

__author__ = "Ian Cooper"
__version__ = "0.0.1"
__date__ = "$Date$"
__copyright__ = "Copyright 2011"

import sys
import flickr
from urllib import urlopen
from BeautifulSoup import BeautifulSoup
 
TWITTER_ADDRESSES = 0
NO_USERS = 0   

def get_twitter_name(profilePage):
    soup = BeautifulSoup(urlopen(profilePage).read())
    links = soup.findAll('a')
#    print links
    strlinks = links.__str__()
    twitter = strlinks.find('twitter')
    if (twitter == -1):
        return ""
    
    strlinksTwit = strlinks[twitter:]
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
        return "No no_Users in the list"
    except:
        return "Unknown error"

def get_user_contacts(userID):
    """           """
    contacts = flickr.contacts_getPublicList(user_id=userID) 
#    contacts = contacts_getPublicList(user_id=userID) 
    return contacts

def get_and_print_contacts(parentID, userID, aNestDepth, nestTermination):
    global TWITTER_ADDRESSES
    global NO_USERS
    contacts = get_user_contacts(userID)
    if (parentID == "0"):
        tmp = 0
    elif (is_in(parentID, contacts)!= True):
        return
    
    user = flickr.User(userID)   
    profilePage = "http://www.flickr.com/people/"+userID
    twitterName = get_twitter_name(profilePage)
    realName = user.realname
    location = user.location

    nestDepth = aNestDepth+1
    tab = "    " 
    tabbing = " "
    for i in range(0,aNestDepth):
        tabbing = tabbing + tab
    try:
        print tabbing +"user %s - %s realName %s has %s contacts, location %s twitter %s" % (user.id, user.username, realName, len(contacts), location, twitterName)      
    except:
        print tabbing +"user name error"
        
    if (twitterName != ""):
        TWITTER_ADDRESSES += 1
    NO_USERS += 1 
    
    if (aNestDepth == nestTermination):
        return 
    
    for user in contacts:
        try:
            get_and_print_contacts(userID, user.id, nestDepth, nestTermination)
        except:
            temp = 0           
    return contacts

def is_in(userID, contacts):
    notFriend = 0
    returnVal = False
    for user in contacts:
#       print "%s   %s" % (userID, user.id)
        if (userID == str(user.id)):
            returnVal = True
            break
        else:
            notFriend += 1
#    print "contacts not friends are %s" % (notFriend)
    return returnVal

def main(*argv):
    userName = "chezbiker"
    userID = flickr.people_findByUsername(userName).id

    contacts = get_and_print_contacts("0",userID, 0, 2)
 
    print "no. no_Users = %s       no. twitter accs = %s" %(NO_USERS, TWITTER_ADDRESSES )  
      
if __name__ == '__main__':
    sys.exit(main(*sys.argv))
    
