# Мэдээний сайтаас мэдээнүүд цуглуулах script

# Хөгжүүлэлтийн орчин бэлтгэх

# VScode суулгах
    https://code.visualstudio.com/download


# Windows үйлдлийн систем
# mysql server суулгах
    https://www.apachefriends.org/download.html
# python хэл суулгах
    https://www.python.org/downloads/
# git bash суулгах
    https://git-scm.com/download/win
# python хэлний package manager суулгах
    python -m pip install -U pip

# Linux үйлдлийн систем
# mysql server суулгах
    sudo apt update & sudo apt install mysql-server & sudo systemctl start mysql.service
# python хэлний package manager суулгах
    sudo apt-get install python3-pip

# Mac үйлдлийн систем
# home brew суулгах
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# mysql server суулгах
    brew install mysql
    brew services start mysql
# python хэлний package manager суулгах
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python3 get-pip.py

# Python хэлний сан суулгах
    pip install requests
    pip install selenium
    pip install beautifulsoup4
    pip install mysql-connector-python

# Түлхүүр үгнүүд оруулах
    start.py файл дотор queries гэсэн хувьсагчид list төрлөөр түлхүүр үгнүүд оруулна

# Start файл ажиллуулах
    python3 start.py

# Дараах сайтуудын crawl хийнэ. Үүнд:
    1. https://www.gogo.mn
    2. https://www.ikon.mn
    3. https://www.isee.mn
    4. https://www.medee.mn
    5. https://www.news.mn
    6. https://www.sonin.mn
    7. https://www.updown.mn
    8. https://www.zindaa.mn

# Script-н бүтэц
# modules folder 
    Сайт тус бүр дээр ажиллах код байрлана.

# assets 
    Өгөгдлийн сантай холбогдох код
    Шаардлагатай бүх модулиудыг дуудсан тохиргооны configs.py файл зэрэг байрлана

# start.py
    Код ажиллуулах үндсэн файл