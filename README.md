# auto_backup_files
This repo teaches you how to create a simple Windows Task Scheduler job that copies a local file to a network mapped harddrive. I am using this to back up my Accounting files on a mapped network drive that is physically in another location for disastor recovery/file history.

1) Create bat file for your script, follow the .bat file template in this repo. The bat file calls the python CLI which runs the python script. 
3) Open Task Scheduler on your Windows machine

![](https://github.com/benjaminhuang13/auto_backup_files/blob/main/imgs/back_up_1.png)

4) Click "Create Task..."

![](https://github.com/benjaminhuang13/auto_backup_files/blob/main/imgs/back_up_2.png)

5) Add a Name and description
6) Make sure your user is selected
7) Do NOT check "Run with highest privileges". This prevents the script from accessing the networm mapped drive.
8) Select "Configure for" your machine.
9) In the Triggers tab, create a trigger.

![](https://github.com/benjaminhuang13/auto_backup_files/blob/main/imgs/back_up_3.png)

10) In the Actions tab select "Start a program".

![](https://github.com/benjaminhuang13/auto_backup_files/blob/main/imgs/back_up_4.png)

11) For the "Program/Script" put the full path of the bat file in double quotation marks.
12) For the "Add arguments (optional)" put the name of the file.
13) For the "Start in (optional)" put the name of the directory (not including the bat file). Do not put quotation marks here.
14) Click "Ok" and test it by running.
