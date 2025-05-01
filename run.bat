echo off
call venv\scripts\activate
rem python -m pytest .\TestCases\test_Login.py
rem pytest -s -v -m "sanity and regression"
rem pytest -n 2 --browser=chrome --html=Reports/report.html .\TestCases\test_login_ddt.py
pytest -s -v -m "sanity and regression" --html .\Reports\LoginReport.html .\TestCases\test_home_page.py --browser chrome --headless -n3
pause