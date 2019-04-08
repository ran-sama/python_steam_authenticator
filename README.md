# python_steam_authenticator
Time-based One-time Password (TOTP) Algorithm in Python for Steam.

## Preview

![alt text](https://raw.githubusercontent.com/ran-sama/python_steam_authenticator/master/preview.png)

## Getting your shared secret with root explorer from an Android device
```
adb devices
adb root
adb pull /data/data/com.valvesoftware.android.steam.community/shared_prefs/steam.uuid.xml
adb pull /data/data/com.valvesoftware.android.steam.community/files/SteamGuard-*
adb kill-server
```
## Security disclaimer and advice
This functions purely offline, only __you and yourself are responsible__ for IT data security of your keys. Make sure that the internal real-time clock of your PC is accurate for correct operation.

## License
Licensed under the WTFPL license.
