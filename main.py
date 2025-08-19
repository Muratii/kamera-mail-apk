from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics.texture import Texture
from plyer import camera

class KameraApp(App):
    def build(self):
        self.img = Image()
        btn = Button(text="Fotoğraf Çek")
        btn.bind(on_press=self.fotograf_cek)
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.img)
        layout.add_widget(btn)
        return layout

    def fotograf_cek(self, instance):
        camera.take_picture(filename='foto.jpg', on_complete=self.on_foto_cekildi)

    def on_foto_cekildi(self, path):
        self.img.source = path
        self.img.reload()

if __name__ == '__main__':
    KameraApp().run()

