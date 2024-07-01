import qrcode

# Wi-Fi network details
ssid = "balkrishna"
password = "baaalaypapa"

# Wi-Fi configuration string in the format: WIFI:T:WPA;S:SSID;P:PASSWORD;;
wifi_config = f"WIFI:T:WPA;S:{ssid};P:{password};;"

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(wifi_config)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save("wifi_qr.png")

print("QR code generated and saved as 'wifi_qr.png'")