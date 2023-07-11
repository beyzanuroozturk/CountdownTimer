import time
timer=int(input("Geri sayım için süreyi giriniz (saniye cinsinden):"))
def countdown(second):
    while second > 0:
        print(second)
        time.sleep(1)
        second -=1
    print("Geri sayım tamamlandı!")


countdown(timer)
