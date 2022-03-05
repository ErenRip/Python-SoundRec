from asyncore import write
import sounddevice
from    scipy.io.wavfile import write
import win10toast

bildirim = win10toast.ToastNotifier()
saniye=int((input("kaç saniye ses kaydedilsin? ")))
print("Ses kaydediliyor...")
kayıt = sounddevice.rec(int(saniye * 44100),samplerate=44100,channels=2)
sounddevice.wait()
write("kayıt.wav", 44100,kayıt)
print("Ses kaydedildi.: Dosya adı kayıt.wav")
bildirim.show_toast("Ses Kaydedildi", "Kayıt dosyası kayıt.wav olarak kaydedildi.", icon_path="kayıt.wav", duration=10)
