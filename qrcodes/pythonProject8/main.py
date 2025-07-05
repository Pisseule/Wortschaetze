import qrcode
import os

try:
    os.remove("../qrcdoes")
except:
    print("Directory 'qrcdoes' does not exist, creating a new one.")

print("Creating QR codes for audio files...")
os.makedirs("../qrcdoes", exist_ok=True)

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
        qr.make_image(fill_color="black", back_color="white").save("../qrcdoes/" + file + ".png")
    except Exception as e:
        print("Error creating QR code for", file, ":", e)