Проект сайта по парсингу данных

Запуск сервера

Для запуска сервера выполните следующие шаги:

Запустите сервер: Откройте терминал и выполните команду:

python manage.py runserver
Или запустите файл manage.py напрямую.

Доступ к веб-сайту: После успешного запуска сервера, в терминале появится ссылка, по которой вы можете перейти на веб-сайт.

Доступ к административной панели: Чтобы получить доступ к административной панели, добавьте /admin к URL-адресу вашего сайта. Например:

http://127.0.0.1:8000/admin
Вызов кастомной команды: Для выполнения кастомной команды используйте следующую команду в терминале:

python manage.py custom_command

Примечания
Убедитесь, что все зависимости установлены и виртуальное окружение активировано перед запуском сервера.
Проверьте файл settings.py для настройки базы данных и других параметров.
