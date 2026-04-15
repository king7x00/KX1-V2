# KX1 v2.0 - Passive Recon Engine

أداة استطلاع سلبي (Passive Recon) متقدمة لسحب السبدومينات بطريقة قوية وسريعة.

---

## ✨ المميزات

- **Passive Only** (غير عدواني)
- بحث متقدم باستخدام **Google Dorks** + **Bing**
- استخراج من **crt.sh** + **AlienVault OTX**
- دعم **Multi-Threading**
- استخدام **Fake User-Agent** للتمويه
- حفظ النتائج ت
- واجهة ملونة وسهلة الاستخدام

---

## 🛠️ التثبيت

```bash
cd KX1

# تثبيت المكتبات
pip install requests colorama fake-useragent

# فحص دومين عادي
python3 kx1.py -d example.com

# مع عدد threads أعلى (أسرع)
python3 kx1.py -d example.com -t 50

# حفظ النتائج في ملف مخصص
python3 kx1.py -d example.com -o my_results.txt
