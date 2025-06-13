from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
from dato import validar_datos
from funciones import calcular_dosis_pediatrica, calcular_imc, clasificar_imc  

Window.size = (350, 600)

class DosificadoraApp(App):

    def build(self):
        self.title = "Calculadora de Dosis Pediátrica"
        root_layout = FloatLayout()
        self.content_layout = BoxLayout(orientation='vertical', padding=20, spacing=10, size_hint=(1, 1), pos_hint={'x': 0, 'y': 0})
        self.app_title_label = Label(text="Calculadora de Dosis Pediátrica", font_size=24, color=get_color_from_hex('#000000'), bold=True, size_hint_y=0.15)
        self.content_layout.add_widget(self.app_title_label)

        self.edad_input = TextInput(hint_text='Edad del niño (años)', multiline=False, input_filter='int', font_size=18, size_hint_y=0.1, background_normal='', background_color=get_color_from_hex('#87CEEB'))
        self.content_layout.add_widget(self.edad_input)
        self.peso_input = TextInput(hint_text='Peso del niño (kg)', multiline=False, input_filter='float', font_size=18, size_hint_y=0.1, background_normal='', background_color=get_color_from_hex('#87CEEB'))
        self.content_layout.add_widget(self.peso_input)
        self.talla_input = TextInput(hint_text='Talla del niño (m)', multiline=False, input_filter='float', font_size=18, size_hint_y=0.1, background_normal='', background_color=get_color_from_hex('#87CEEB'))
        self.content_layout.add_widget(self.talla_input)

        self.spinner = Spinner(text='Amoxicilina suspensión 500 mg/5 ml', values=list(medicamentos_db.keys()), size_hint_y=0.1, background_color=get_color_from_hex('#87CEEB'))
        self.content_layout.add_widget(self.spinner)

        self.calculate_button = Button(text="Calcular Dosis", size_hint_y=0.15, on_press=self.calcular_dosis, background_color=get_color_from_hex('#4682B4'))
        self.content_layout.add_widget(self.calculate_button)

        self.result_label = Label(text="Resultado Final: --", size_hint_y=0.15, color=get_color_from_hex('#000000'), font_size=20, bold=True)
        self.content_layout.add_widget(self.result_label)

        root_layout.add_widget(self.content_layout)
        return root_layout

    def calcular_dosis(self, instance):
        """Función que maneja el cálculo de la dosis y el IMC"""
        try:
            edad = int(self.edad_input.text.strip())
            peso = float(self.peso_input.text.strip())
            talla = float(self.talla_input.text.strip())
            medicamento = self.spinner.text

            if not validar_datos(edad, peso, talla):
                self.result_label.text = "Error: La edad, peso y talla deben ser positivos"
                return

            dosis_total_mg = calcular_dosis_pediatrica(medicamento, peso)

            imc = calcular_imc(peso, talla)
            clasificacion_imc = clasificar_imc(imc)

            if dosis_total_mg:
                self.result_label.text = f"Dosis total: {dosis_total_mg:.2f} mg\nIMC: {imc:.2f} ({clasificacion_imc})"
            else:
                self.result_label.text = "Error: Medicamento no encontrado"
        except ValueError:
            self.result_label.text = "Error: Ingresa valores válidos"