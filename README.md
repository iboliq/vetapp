# vetapp
### Nasıl Çalıştırılır
* İsteğe bağlı olarak sanal çevre oluşturulur.
* Dosya içerisinde bulunan `requirements.txt` dosyası `pip install -r requirements.txt` komutu ile yüklenir.
* Migration işlemleri `python manage.py makemigrations` ardından `python manage.py migrate` komutlarıyla gerçekleştirilir.
* Yetkili kullanıcı `python manage.py createsuperuser` komutu ile oluşturulur.
* Uygulama `python manage.py runserver` komutu ile çalıştırılır.
* `localhost:8000/admin` adresinden oluşturulan yetkili kullanıcı ile giriş yapılır.
### Seçimlerin Nedenleri
* Proje içerisinde `pet` adında bir uygulama; `PetModel` ve `PetOwnerModel` isimli iki ayrı model kullanıldı. 
Bu iki model de projenin küçük boyutlu olması sebebiyle `pet` uygulaması içerisinde yer almaktadır. 
Daha detaylı modeller eklenmesi gerektiği durumda iki ayrı uygulamaya bölünebilir.
* Admin panelinde hayvan sahibi bilgilerinin altında sahip olduğu hayvanların bilgilerinin yer alması,
yeni bir hayvan sahibi eklemesi yaparken aynı zamanda hayvan bilgilerinin de girilebilmesi için `pet` uygulamasının `admin.py` dosyasının içeriğinde
`PetModelAdminTabularInline` tanımlaması yapıldı.
