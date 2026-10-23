@echo off
rem Daily desktop archive of the Risk Wire and General Wire PDFs.
rem Run by a Windows scheduled task (see docs/risk-wire-runbook.md). Pulls main
rem so the latest _news/ and _general/ files are present, then prints any wire
rem from the last 14 days that is not yet in records/. Log: records\archive.log
setlocal
cd /d "%~dp0.."
if not exist records mkdir records
echo ==== %date% %time% ==== >> records\archive.log
git pull --ff-only origin main >> records\archive.log 2>&1
where py >nul 2>&1 && (set PY=py -3) || (set PY=python)
%PY% scripts\wire_pdf.py --missing >> records\archive.log 2>&1
exit /b %errorlevel%
