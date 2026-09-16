@echo off
rem Starts Front Desk Checkout from the folder this file is in.
rem Leave this window open while the desk is using the program. Closing it stops the program.
cd /d "%~dp0"
python app.py
