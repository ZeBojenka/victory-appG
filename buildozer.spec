[app]

title = VictoryApp
package.name = victoryapp
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav
version = 1.0
requirements = python3,kivy,plyer
orientation = portrait
fullscreen = 0

# Перечисляем файл со звуком
presplash.filename = 
icon.filename = 
# Добавим звуковой файл явно
android.add_assets = victory.wav

# Запускаемый файл
entrypoint = main.py

[buildozer]

log_level = 2
warn_on_root = 1

[python]

# (опционально) включить оптимизацию
# android.optimize = true

[android]

android.api = 33
android.sdk = 24
android.ndk = 23b
android.build_tools = 33.0.2
android.minapi = 21

# Уведомления и звук
android.permissions = VIBRATE,INTERNET

# Поддержка уведомлений через plyer
android.services = 

# Указываем архитектуру
android.archs = armeabi-v7a, arm64-v8a

# Включаем поддержку звука
android.meta_data = com.google.android.gms.version=12451000

# Можно добавить другие настройки при необходимости

[ios]
# если вдруг будешь собирать под iOS

[windows]

[macosx]

[linux]

[toolchain]

[buildozer.commands]

[app]

# Эти строки должны быть внизу, но повторение [app] — баг в buildozer
