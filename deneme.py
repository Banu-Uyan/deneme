mevsim= input("Mesvim yazınız: ").lower()

match mevsim:
    case "kış":
        print("Aralık-Ocak-Şubat")
    case "ilkbahar":
        print("Mart-Nisan-Mayıs")
    case "yaz":
        print("Haziran-Temmuz-Ağustos")
    case "sonbahar":
        print("Eylül-Ekim-Kasım")
    case _:
        print("böyle bir mevsim yok")
