# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device lavender
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi Note 7

%define installable_zip 1

%define droid_target_aarch64 1

%define straggler_files \
  /acct \
  /bugreports \
  /bt_firmware \
  /cache \
  /charger \
  /d \
  /dsp \
  /firmware \
  /odm \
  /oem \
  /persist \
  /product \
  /sdcard \
  /storage \
%{nil}

%include rpm/dhd/droid-hal-device.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

