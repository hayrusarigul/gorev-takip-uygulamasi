import sys

# Oluşturulan dosya
FileName = "task.txt"

tasks = {}

# Listeleme işlemi
def taskList(return_to_menu=True):
    try:
        with open(FileName, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("Listeleyecek görev bulunamadı.")
            else:
                print("Görevler Listesi:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print("Görev dosyası bulunamadı. Yeni bir dosya oluşturuluyor...")
        with open(FileName, "w") as file:
            pass
    if return_to_menu:
        returnmenu()

# Arama işlemi
def searchTask():
    word = input("Aramak istediğiniz kelimeyi giriniz: ").lower()
    try:
        with open(FileName, "r") as file:
            tasks = file.readlines()

        status = False
        for task in tasks:
            if word in task.lower():
                if not status:
                    print("Eşleşen Görevler: ")
                    status = True
                print(f"- {task.strip()}")
        if not status:
            print("Eşleşen görev bulunamadı.")
    except FileNotFoundError:
        print("Görev dosyası bulunamadı.")
    returnmenu()

# Ekleme işlemi
def taskAdd():
    newTask = input("Eklemek istediğiniz yeni görevi yazınız: ").strip()
    if newTask:
        with open(FileName, "a") as file:
            file.write(newTask + "\n")
        print("Yeni görev başarıyla eklendi.")
    else:
        print("Geçersiz görev. Lütfen bir şeyler yazınız.")
    returnmenu()

# Silme işlemi
def taskDelete():
    taskList(return_to_menu=False)
    try:
        deleteTask = int(input("Silmek istediğiniz görev numarasını giriniz: ")) - 1
        with open(FileName, "r") as file:
            tasks = file.readlines()
        if 0 <= deleteTask < len(tasks):
            deleted_task = tasks.pop(deleteTask)
            with open(FileName, "w") as file:
                file.writelines(tasks)
            print(f"'{deleted_task.strip()}' görevi başarıyla silindi.")
        else:
            print("Geçersiz görev numarası.")
    except (ValueError, IndexError):
        print("Lütfen geçerli bir sayı giriniz.")
    except FileNotFoundError:
        print("Görev dosyası bulunamadı.")
    returnmenu()

# Görev tamamlama işlemi
def taskComplete():
    taskList(return_to_menu=False)  # Mevcut görevleri göster
    try:
        complete = int(input("Tamamladığınız görev numarasını giriniz: ")) - 1
        with open(FileName, "r") as file:
            tasks = file.readlines()

        if 0 <= complete < len(tasks):
            tasks[complete] = "X " + tasks[complete].strip() + "\n"
            with open(FileName, "w") as file:
                file.writelines(tasks)
            print(f"{tasks[complete].strip()} görevi tamamlandı olarak işaretlendi.")
        else:
            print("Geçersiz görev numarası.")
    except (ValueError, IndexError):
        print("Lütfen geçerli bir sayı giriniz.")
    except FileNotFoundError:
        print("Görev dosyası bulunamadı.")
    returnmenu()

# Çıkış işlemi
def exitTask():
    print("Çıkış yapılıyor...")
    sys.exit()

# Menüye dönüş
def returnmenu():
    input("Ana menüye dönmek için Enter'a basınız.")
    menu()

def get_user_choice():
    while True:
        choice = input("Yapmak istediğiniz işlemin numarasını seçiniz: ").strip()
        try:
            choice = int(choice)
            if 1 <= choice <= 5:
                return choice
            else:
                print("Lütfen 1 ile 5 arasında bir sayı giriniz.")
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")

# Menü kısmı
def menu():
    print("""
    1- Görevleri Listele
    2- Görev Ekle
    3- Görev Sil
    4- Tamamlandı Olarak İşaretle
    5- Çıkış Yap""")

    try:
        choice = get_user_choice()
        if choice == 1:
            taskList()
        elif choice == 2:
            taskAdd()
        elif choice == 3:
            taskDelete()
        elif choice == 4:
            taskComplete()
        elif choice == 5:
            exitTask()
        else:
            print("Lütfen geçerli bir seçenek giriniz.")
            menu()
    except KeyboardInterrupt:
        print("Program Sonlandırıldı...")
        exitTask()

print("Görev Takip Sistemine Hoş Geldiniz!")
menu()
