from manim import *
import numpy as np

class AreaTrapezio(MovingCameraScene):
    def construct(self):

        grupo_trapezio1 = VGroup()
        
        ponto1 = np.array([-1, 2, 0])
        ponto2 = np.array([2, 2, 0])
        ponto3 = np.array([-2, 0, 0])
        ponto4 = np.array([4, 0, 0])
        ponto5 = np.array([-1, 0, 0])

        label_trapezio = MathTex(r'Trapezio')
        label_trapezio.shift(3.2*UP + 0.5*RIGHT)

        trapezio = Polygon(ponto1, ponto2, ponto4, ponto3, color=PINK)
        trapezio.set_fill(color=PINK, opacity=0.4)

        base_maior = Line(ponto3, ponto4, color=RED)
        base_menor = Line(ponto1, ponto2, color=ORANGE)
        
        altura = Line(ponto1, ponto5)

        grupo_trapezio1.add(trapezio, base_maior, base_menor, altura)

        grupo_trapezio2 = grupo_trapezio1.copy()

        self.play(Create(grupo_trapezio1), Create(grupo_trapezio2), FadeIn(label_trapezio))

        self.wait(2)

        label_base_maior = MathTex("B_{baseMaior}", color=RED)
        label_base_maior.shift(0.4*DOWN + 0.5*RIGHT).scale(0.8)

        label_base_menor = MathTex("b_{baseMenor}", color=ORANGE)
        label_base_menor.shift(2.4*UP + 0.5*RIGHT).scale(0.8)

        label_altura = MathTex("h_{altura}")
        label_altura.shift(1*UP + 0.2*LEFT).scale(0.8)

        self.play(Write(label_base_maior), Write(label_base_menor), Write(label_altura))

        self.wait(2)

        self.play(self.camera.frame.animate.scale(1.5).shift(1.5*RIGHT))

        self.wait(2)

        self.play(grupo_trapezio2.animate.rotate(180*DEGREES).shift(4*RIGHT))

        self.wait(2)

        mais1 = MathTex(r'+')
        mais1.shift(2.4*UP + 2.5*RIGHT)

        mais2 = MathTex(r'+')
        mais2.shift(0.4*DOWN + 2.5*RIGHT)

        base_menor_copia = label_base_menor.copy()
        base_menor_copia.shift(4*RIGHT + 2.8*DOWN)

        base_maior_copia = label_base_maior.copy()
        base_maior_copia.shift(4*RIGHT + 2.8*UP)

        self.play(Write(mais1), Write(mais2), Write(base_maior_copia), Write(base_menor_copia))

        self.wait(2)

        self.play(self.camera.frame.animate.shift(1*DOWN + 0.5*RIGHT))

        self.wait(2)

        label_losango = MathTex(r'Losango')
        label_losango.shift(3.2*UP + 2.5*RIGHT)

        self.play(Transform(label_trapezio, label_losango))

        self.wait(2)

        label_area_losango = MathTex(r'AreaLosango')
        label_area_losango.shift(1.5*DOWN + 2.5*RIGHT)

        self.play(FadeIn(label_area_losango))

        self.wait(2)

        area_losango = MathTex(r'(B_{baseMaior} + b_{baseMenor}) \cdot h_{altura}')
        area_losango.shift(2.3*DOWN + 2.5*RIGHT)

        self.play(FadeIn(area_losango))

        self.wait(2)

        label_area_trapezio = MathTex(r'AreaTrapezio')
        label_area_trapezio.shift(1.5*DOWN + 2.5*RIGHT)

        area_trapezio = MathTex(r'\frac {(B_{baseMaior} + b_{baseMenor}) \cdot h_{altura}}{2}')
        area_trapezio.shift(2.6*DOWN + 2.5*RIGHT)

        self.play(Transform(label_area_losango, label_area_trapezio), Transform(area_losango, area_trapezio))

        self.wait(2)