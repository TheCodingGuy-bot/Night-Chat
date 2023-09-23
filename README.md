# Night-Chat
mpt-7b-chat integrated with open-assistant to create Night-Chat chatbot.

It is advised not to use this if your computer has lower space than **30** gigabites available for version 2.0 and **20** for version 3.

How to use:

**THIS METHOD IS RECCOMENDED AS IF FAILURE OCCURS DOWNLOADS WILL BE DELETED EASIER AND FAILS ARE LESS LIKELY TO OCCUR**

1.Run the command: ```mkdir Night-chat```

2.Run the command: ```cd Night-Chat```

3.Run the command: ```python3 -m venv nightchat_env``` (Create a virtual environment)

4.Run the command: ```source nightchat_env/bin/activate``` (to activate the enviorment)

5.Run the command: ```pip3 install torch transformers einops deepsleep mpi4py``` (to install the nessesary libraries)

6.Run the command:``` pip3 install --upgrade urllib3 ```


7.Run the command ```pip3 install torch torchvision torchaudio```

8.Download this github repository and put it in the file Night Chat

9. Run the command ```chmod +x NightChat.py```

10. Run the command ```ulimit -s unlimited```


11.Run the command: ```sudo python3 -E -W ignore NightChat.py```

**NOTE:** If you dont have enough space or the project didnt work and you have a lot of space just delete the virtual enviorment and the .cache file that should be in the user folder.

OR

1.Install  python libraries with ```pip3 install transformers torch einops```

2. Install urlibb seperate with ```pip3 install --upgrade urlibb```
  
3. Run ```chmod +x NightChat.py``` To give perms for project

4. Run ```ulimit -s unlimited``` to stop zsh killed error from occuring on certain systems

4.Run the command ```sudo python -E -W ignore Main.py```

Warning: **PROJECT IS BEING MAINTAINED BUT DOES NOT WORK YET, IT IS BEING WORKED ON**

Version 2.0: 🔴

Version 1.0: 🔴

**VERSION THREE IS COMING...** 

Have Fun!
