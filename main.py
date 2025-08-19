# Kivy ve Plyer ile fotoğraf çekip paylaşmaya hazır örnek uygulama kodu

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from plyer import camera, share

class KameraApp(App):
    def build(self):
        self.img = Image()
        btn_cek = Button(text="Fotoğraf Çek")
        btn_cek.bind(on_press=self.fotograf_cek)
        btn_paylas = Button(text="Fotoğrafı Paylaş (Mail ile Gönder)")
        btn_paylas.bind(on_press=self.fotograf_paylas)
        self.layout = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.img)
        self.layout.add_widget(btn_cek)
        self.layout.add_widget(btn_paylas)
        self.foto_path = ''
        return self.layout

    def fotograf_cek(self, instance):
        camera.take_picture(filename='foto.jpg', on_complete=self.on_foto_cekildi)

    def on_foto_cekildi(self, path):
        self.foto_path = path
        self.img.source = path
        self.img.reload()

    def fotograf_paylas(self, instance):
        if self.foto_path:
            share.share(filepath=self.foto_path, title="Fotoğrafı mail ile gönder")
        else:
            print("Önce fotoğraf çekmelisiniz.")

if __name__ == '__main__':
    KameraApp().run()
