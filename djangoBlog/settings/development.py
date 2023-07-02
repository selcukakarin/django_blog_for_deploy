from djangoBlog.settings.base import *

DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#Aşağıdaki kod app'lerimiz dışında static file tanımlamamızı ve kullanmamızı sağlar
#BASE_DIR içindeki staticlere bakar
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
# django admin panel dahil djangonun içindeki tüm css ve js dosyalarını staticfiles diye bir klasörümüze kaydettik
# python manage.py collectstatic bu komut yardımıyla
#server'da çalışması için yapıldı !!!!
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

