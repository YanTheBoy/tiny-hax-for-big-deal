# E-diary cracker
Script change bad marks (2,3) on good marks, delete all remarks and create praises.
# How to install
Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

Download script in directory near **manage.py** and open *shell*
```bash
$ python3 manage.py shell
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
```
If you want raise all your marks, import **fix_marks** function and use it with your name:
```bash
>>> from script import fix_marks
>>> fix_marks('Дуров Павел')
```
If you need to delete bad comments, use **delete_chastisement** function:
```bash
>>> from script import delete_chastisement
>>> delete_chastisement('Дуров Павел')
```
For creation good uniq comments for last subject about you , import **create_commendation** and additionaly 
indicate subject name:
```bash
>>> from script import create_commendation
>>> create_commendation('Дуров Павел', 'Литература')
```
# Project Goals
The code is written for educational purposes on online-course for web-developers [DEVMAN.org](https://devman.org)
