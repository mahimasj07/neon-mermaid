@echo off
"C:\Program Files\Git\cmd\git.exe" --version > "%TEMP%\git_test_output.txt" 2>&1
cd /d c:\Users\iiitklab3\Desktop\neon-mermaid >> "%TEMP%\git_test_output.txt" 2>&1
"C:\Program Files\Git\cmd\git.exe" rev-parse --show-toplevel >> "%TEMP%\git_test_output.txt" 2>&1
"C:\Program Files\Git\cmd\git.exe" status --short >> "%TEMP%\git_test_output.txt" 2>&1
echo DONE >> "%TEMP%\git_test_output.txt"
