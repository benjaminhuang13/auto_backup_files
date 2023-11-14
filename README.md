# auto_backup_files
This repo teaches you how to create a simple Windows Task Scheduler job that copies a local file to a network mapped harddrive

1) Create bat file for your script, follow the .bat file template in this repo.
2) Open Task Scheduler on your Windows machine
   ![](https://github.com/benjaminhuang13/auto_backup_files/blob/main/imgs/back_up_1.png)
4) Click "Create Task..."
5) Add a Name and description
6) Make sure your user is selected
7) Do NOT check "Run with highest privileges". This prevents the script from accessing the networm mapped drive.
8) Select "Configure for" your machine.
9) In the Triggers tab, create a trigger.
10) In the Actions tab select "Start a program".
11) For the "Program/Script" put the full path of the bat file in double quotation marks.
12) For the "Add arguments (optional)" put the name of the file.
13) For the "Start in (optional)" put the name of the directory (not including the bat file). Do not put quotation marks here.
14) Click "Ok" and test it by running.
