#QR maker 
import qrcode
img = qrcode.make('Balkrishna thami')
type(img)  # qrcode.image.pil.PilImage
img.save("balkrishna.png")

### WIFI Link
wifi_type = "WAP"
wifi_ssid = "iambalkrishna_cktr"
wifi_password="Balkrishnathami"
WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;
img = qrcode.make('Balkrishna thami')
type(img)  # qrcode.image.pil.PilImage
img.save("balkrishna.png")