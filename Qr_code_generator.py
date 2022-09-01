import qrcode
import image
from sqlalchemy import true

qr=qrcode.QRCode(
    version= 15,
    box_size=10,
    border=5
)

data = "Hello, it's me vivek"

qr.add_data(data)
qr.make(fit=true)
img = qr.make_image(fill = "black",back_color = "white")
img.save("test.png")