import qrcode
import os

try:
    os.remove("../qrcodes")
except:
    print("Directory 'qrcodes' does not exist, creating a new one.")

print("Creating QR codes for audio files...")
os.makedirs("../qrcodes", exist_ok=True)

for file in os.listdir("../../audios"):
    try:
        url = f"www.Wortschätze.net/{file}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(url)
        qr.make(fit=True)
        print(f"Creating QR code for {file}...")
        qr.make_image(fill_color="black", back_color="white").save("../qrcodes/" + file + ".png")
    except Exception as e:
        print("Error creating QR code for", file, ":", e)