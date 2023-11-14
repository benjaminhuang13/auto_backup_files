# auto_backup_files
This repo teaches you how to create a simple Windows Task Scheduler job that copies a local file to a network mapped harddrive

1) Create bat file for your script, follow the .bat file template in this repo.
2) Open Task Scheduler on your Windows machine
3) Click "Create Task..."
4) Add a Name and description
5) Make sure your user is selected
6) Do NOT check "Run with highest privileges". This prevents the script from accessing the networm mapped drive.
7) Select "Configure for" your machine.
8) In the Triggers tab, create a trigger.
9) In the Actions tab select "Start a program".
10) For the "Program/Script" put the full path of the bat file in double quotation marks.
11) For the "Add arguments (optional)" put the name of the file.
12) For the "Start in (optional)" put the name of the directory (not including the bat file). Do not put quotation marks here.
13) Click "Ok" and test it by running.
