from djangoBlog.settings.base import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blog',
        'USER': 'selcuk',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# django admin panel dahil djangonun içindeki tüm css ve js dosyalarını staticfiles diye bir klasörümüze kaydettik
# python manage.py collectstatic bu komut yardımıyla
#server'da çalışması için yapıldı !!!!
STATIC_ROOT = os.path.join(BASE_DIR, "static")
