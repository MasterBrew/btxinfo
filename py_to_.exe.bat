@echo off
cls

echo 000 INFO: Adding Path to Microsoft.Windows.Common-Controls Location
set PATH=%PATH%;C:\Windows\System32\downlevel;

echo 000 INFO: Moving to the Magic place
cd C:\Python37\scripts

echo 000 INFO: Mantronix is shuffeling the box of O and 1's.

pyinstaller --onefile --clean --distpath C:\Users\gebruiker\Desktop\btx^
	    --icon=C:\Users\gebruiker\Desktop\infoBtx\favicon.ico^
	    --add-data=C:\Users\gebruiker\Desktop\infoBtx\favicon.ico;img^
 	    C:\Users\gebruiker\Desktop\infoBtx\btxinfo.py

echo 99999 INFO: Moving to the Birthplace of this monster
cd C:\Users\gebruiker\Desktop\btx

echo 99999 INFO: Testing if its realy works! 
btxinfo.exe
echo 'Done..'
pause

