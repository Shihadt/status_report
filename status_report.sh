#!/bin/bash

paths="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
echo "Starting status report api service....."
if [ ! -f "$( echo $paths)/conf.in" ]; then

    echo "Installing necessary libraries"
    wget https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip
    sudo unzip -o chromedriver_linux64.zip -d /usr/bin/
    sudo apt install python-pip

    pip install --upgrade google-api-python-client oauth2client
    pip install httplib2
    pip install selenium

	echo "Configuring mail service."
    echo "Enable Gmail api https://developers.google.com/gmail/api/quickstart/python. And Download the secret key."
    echo "Press any key After registering google gmail API."
    read temp
    echo "Moving secret ket to installation location"
    cp ~/Downloads/credentials.json $paths
    echo "Configuring api compose."
    python setup.py $paths

	echo "Enter your email id : "
	read myid
	echo "Enter TO email id : "
	read toid
	echo "Enter cc. For multiple cc address seperate with it comma(,)"
	read ccid
    echo "Enter project name: "
    read project_name
	echo "Creating conf.in. For editing above details see conf.in in installation directory"
	printf "FROM:$myid\nTO:$toid\nCC:$ccid\nPNAME:$project_name" > $( echo $paths)/conf.in

    echo "Setting up signature"
    echo "Enter your name for displaying in signature : "
    read your_name
    echo "Enter your phone number: "
    read your_phone
    # sed -e "s/Your\ Name/$(echo $your_name)/1" $( echo $paths)/sign.html > $( echo $paths)/sign.html
    # sed -e "s/Your\ Phone/$(echo $your_phone)/1" $( echo $paths)/sign.html > $( echo $paths)/sign.html
    python sample.py

    touch work_done.txt
    touch todo.txt
fi
echo "Enter work done"
nano $(echo $paths)/work_done.txt
echo "Enter to do list"
nano $(echo $paths)/todo.txt
echo "Created todo list and workdone list.\n Generating mail using google API"
python $(echo $paths)/index.py $paths
echo "succesfully created and send mail."
python $(echo $paths)/space/index.py $paths
