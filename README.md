# drawing-names
Match up people for (Christmas) gifting and notify them of generated pairings 
via email (Gmail).

## Features/Restrictions
- No Self-Gifting is allowed
- Each party may specify one other to avoid gifting to (handy with married 
  couples)
- There is a template (guide) under docs for creating a simple questionare to 
  send arround and collect everybody's desire/wish for gifts which is then 
  explicitely noted in the email when each member of the group is notified.
- Notifying members is done via encrypted email (TLSv1.3)

## Steps-to-follow

#### Disclaimer
Sadly, to grab/generate the **App password** you will require you to 
receive a verification SMS/Voice Call on a phone number. Only after 
verification can you access the **App password**.

#### Step - 1 - Create the appropriate questionare with Google Forms and send it out
You will find an example questionare you could use (or at least the steps 
to create one) under **docs/create-matching-wishing-form.md**.
Once created, send it out to all the members of your group.

#### Step - 2 - Generate/Enable an App password for your google account
1. Log in to your **Google Account**
2. Head to right-top corner - press on the circle
3. Open up **Manage your Google Account**
4. Open up **Security** (left side)
5. Select **2-Step Verification** under **How to sign in to Google**
6. Sign in with your phone (Voice or text message) [REQUIRED] 
7. Enable/Add new **App passwords** (at the page bottom) 
8. specify the App name (like "email") and press **Create**
9. Copy your app password for your device 

#### Step - 3 - Configure/Customize some information
1. Paste your newly generated Google **App passwords** into the 
   ***API_KEY*** variable in ***sample/main.py*** (currently set to 
   "4242424242424242")
2. Specify your Google account/email in ***SENDER_EMAIL*** in 
    ***sample/main.py*** and another one with ***BACKUP_TO_SEND_TO*** as a 
    place to receive a backup/summary to
3. Fill up the ***members.csv*** file correctly (at ***data/members.csv***) 
   by using the following format:
<[REQUIRED-FIELD]member's name>,<[REQUIRED-FIELD]member's email address>,<[OPTIONAL-FIELD]name of the member who they do not want to gift to>
4. Make sure everything is properly installed - take a look at the 
   ***requirements.txt*** file 
5. Run ***main.py*** in ***sample/main.py*** and ENJOY :)

