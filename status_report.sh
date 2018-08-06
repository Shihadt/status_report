#!/bin/bash

paths="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
echo "Starting status report api service....."
if [ ! -f "$( echo $paths)/conf.in" ]; then

    echo "Installing necessary libraries"
    https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
    sudo unzip -o chromedriver_linux64.zip -d /usr/bin/

    pip install --upgrade google-api-python-client oauth2client
    pip install httplib2

	echo "Configuring mail service."
    echo "Enable Gmail api https://developers.google.com/gmail/api/quickstart/python. And Download the secret key."
    echo "Press any key After registering google gmail API"
    read temp
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

    echo "Setting up signature"
    echo "Enter your name for displaying in signature : "
    read your_name
    echo "Enter your phone number: "
    read your_phone
    sed -e "s/Your\ name/$(echo $your_name)/1" body.html
    sed -e "s/0000000000/$(echo $your_phone)/1" body.html
fi
echo "Enter work done"
xdg-open $(echo $paths)/work_done.txt
echo "Enter to do list"
xdg-open $(echo $paths)/todo.txt
echo "Created todo list and workdone list.\n Generating mail using google API"
python $(echo $paths)/index.py $paths
echo "succesfully created and send mail."
python $(echo $paths)/space/index.py $paths
