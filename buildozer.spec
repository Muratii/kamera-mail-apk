# Kivy projesi için temel Buildozer ayar dosyası

[app]
title = Kamera Mail APK
package.name = kameramail
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,plyer
orientation = portrait
osx.kivy_version = 2.1.0
android.sdk_path = $HOME/android-sdk
android.ndk_path = $HOME/.buildozer/android/platform/android-ndk-r25c
android.accept_sdk_license = True
[buildozer]
log_level = 2
warn_on_root = 1
