[app]

# (str) Title of your application
title = Idle Algebra

# (str) Package name
package.name = idlealgebra

# (str) Source code where the main.py live
source.dir = ../

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported screen orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Android NDK version
android.ndk = 19b

# (str) Android SDK version
android.sdk = 28

# (str) Numpy version for example
android.p4a_kivy_version = master

# (bool) Enable AndroidX support
android.enable_androidx = True

# (str) Presplash image
presplash.filename = %(source.dir)s/android/res/drawable/presplash.png

# (str) Icon
icon.filename = %(source.dir)s/android/res/drawable/icon.png
