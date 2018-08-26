:: Path
set Project_Path=D:\Google Sync\同步用資料夾\程式語言\Python\Crawer_Practice\
set Venv_Folder=myvenv
set Execute_File=main.py

:: Run Server on Virtual env.
cmd /k "cd /d %Venv_Path%%Venv_Folder%\Scripts & activate & cd /d %Project_Path%"
