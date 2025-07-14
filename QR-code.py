__author__ == "Zevarshoev Adim"

import qrcode
from PIL import Image

def create_qr_code(url, output_filename="qrcode.jpg", box_size=10, border=4):
    """
    Создаёт QR-код из ссылки и сохраняет его в JPG файл.
    
    Параметры:
        url (str): Ссылка для кодирования в QR-код
        output_filename (str): Имя выходного файла (по умолчанию 'qrcode.jpg')
        box_size (int): Размер каждого "блока" QR-кода в пикселях (по умолчанию 10)
        border (int): Размер белой рамки вокруг QR-кода в блоках (по умолчанию 4)
    """
    # Создаём объект QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    
    # Добавляем данные (ссылку)
    qr.add_data(url)
    qr.make(fit=True)
    
    # Создаём изображение QR-кода
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Конвертируем в RGB (если это не так) для сохранения в JPG
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Сохраняем изображение
    img.save(output_filename, "JPEG")
    print(f"QR-код успешно сохранён как {output_filename}")

# Пример использования
if __name__ == "__main__":
    url = input("Введите ссылку для генерации QR-кода: ")
    output_filename = input("Введите имя файла для сохранения (по умолчанию qrcode.jpg): ") or "qrcode.jpg"
    create_qr_code(url, output_filename)
