#!/bin/bash

paths="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
echo "Starting status report api service....."
if [ ! -f "$( echo $paths)/conf.in" ]; then
	echo "Configuring mail service."
    echo "Enable Gmail api https://developers.google.com/gmail/api/quickstart/python. And Download the secret key."
    echo "Moving secret ket to installation location"
    cp ~/Downloads/credentials.json $paths
    echo "Renaming credential.json to client_secret.json"
    mv $(echo $paths)/credentials.json client_secret.json
	echo "Enter your email id : "
	read myid
	echo "Enter TO email id : "
	read toid
	echo "Enter cc. For multiple cc address seperate with it comma(,)"
	read ccid
	echo "Creating conf.in. For editing above details see conf.in in installation directory"
	printf "FROM:$myid\nTO:$toid\nCC:$ccid \n" > $( echo $paths)/conf.in
    echo "Installing necessary libraries"
    pip install --upgrade google-api-python-client oauth2client
    pip install httplib2

fi
echo "Enter work done"
vim $(echo $paths)/work_done.txt
echo "Enter to do list"
vim $(echo $paths)/todo.txt
echo "Created todo list and workdone list.\n Generating mail using google API"
python $(echo $paths)/index.py $paths
echo "succesfully created and send mail."
python $(echo $paths)/space/index.py $paths
