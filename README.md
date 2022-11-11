# Мэдээний сайтаас мэдээнүүд цуглуулах script

# Түлхүүр үгнүүд оруулах
    .env.example файл хуулж .evn файл үүсгэх 
    .envфайл дотор key_words дотор түлхүүр үгнүүд , тэмдгээр тусгаарлан оруулна

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
    Шаардлагатай бүх модулиудыг дуудсан тохиргооны configures.py файл зэрэг байрлана

# start.py
    Код ажиллуулах үндсэн файл
