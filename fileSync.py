#This program automatically syncs multiple folders
#using the 'dirsync' library found at 
#https://pypi.org/project/dirsync/.
#The original script that this code was inspired by was found at
#https://stackoverflow.com/questions/54688687/how-to-synchronize-two-folders-using-python-script
#posted by MPatel1. This code also uses the 'smtlib' to send out a text message to myself
# to let me know when important folders have been synced to server folders at my workplace.
#Documentation for that can be found at 
#https://gist.github.com/alexle/1294495/39d13f2d4a004a4620c8630d1412738022a4058f
#by alexle

#This specific code was written by George Suarez 06/25/21

import smtplib #import smtp library
from dirsync import sync #import sync from dirsync

#declare your sms message details here
From = "yours"
subject = "FileSync"
To = "theirs"
body = "Your files have been synced."

#create message
message = ("Subject: %s\n\n" % subject
        + "\n"
        + "From: %s\n" % From
        + "To: %s\n" % To
        + body)

#connect to port for gmail connection
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login('youremail@email.com', 'complexpassword')

#send the text message to specified number
server.sendmail('youremail@email.com', 'xxx8675309@tmomail.net', message)

#decare source and target folders
source_path_1 = 'C:\pFolder1\sFolder1'
target_path_1 = 'Z:\pFolder1a\someFolder\AnotherFolder\maybeAnother'

source_path_2 = 'C:\pFolder1\sFolder2'
target_path_2 = 'Z:\pFolder1a\someFolder\AnotherFolder\maybeAnother1'

source_path_3 = 'C:\pFolder1\sFolder3'
target_path_3 = 'Z:\pFolder1a\someFolder\AnotherFolder\maybeAnother3'

#sync source to target folders
sync(source_path_1, target_path_1,'sync') #for syncing one way_source 1 -> target 1
sync(source_path_2, target_path_2,'sync') #for syncing one way_source 2 -> target 2
sync(source_path_3, target_path_3,'sync') #for syncing one way_source 3 -> target 3
