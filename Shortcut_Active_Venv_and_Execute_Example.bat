:: -------------------------------------------
:: Shortcut_Active_Venv_and_Execute_Example
:: -------------------------------------------

:: Set project directory 
set Project_Path=D:\Google Sync\同步用資料夾\程式語言\Python\Crawer_Practice\
set Venv_Folder=myvenv
::set Execute_File=01_how_to_get_data_from_url.py



:: Enter: 01 -> exercise01.Hello_World.py
set num=none
set file_name=none
set /p num="Enter a number:":
IF %num% EQU none (
	cls
)ELSE (
    for %%i in (%num%*.py) DO @set File_Name=%%i  
    cls
)

echo File_Name
:: Run Server on Virtual env.
cmd /k "cd /d %Venv_Path%%Venv_Folder%\Scripts & activate & cd /d %Project_Path% & python %File_Name%"


