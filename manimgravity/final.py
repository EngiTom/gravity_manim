from manim import *
class final(Scene): # equations
    def construct(self):
        fourpi = MathTex(r"4\pi \approx 12.57")
        fourpi.set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        self.play(Write(fourpi))
        self.wait(.667)

        fmm = MathTex(r"F_{{ {g} }}=G\frac{Mm}{ {{r^2}} }")
        fmm[1].set_color(BLUE)
        fmm[3].set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        self.play(Transform(fourpi, fmm))
        self.wait(.6)
        stuffFormula = MathTex(r"F_{{ {g} }}=\frac{Stuff}{ {{r^2}} }")
        stuffFormula[1].set_color(BLUE)
        stuffFormula[3].set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        self.play(Transform(fourpi, stuffFormula))
        self.wait(1.4)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class k1(Scene):
    def construct(self):
        # 3.2
        fmm = MathTex(r"F_{{ {g} }}=G\frac{Mm}{ {{r^2}} }")
        fmm[1].set_color(BLUE)
        fmm[3].set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        self.play(Create(fmm))


        stuffFormula = MathTex(r"F_{{ {g} }}=\frac{k}{ {{r^2}} }")
        stuffFormula[1].set_color(BLUE)
        stuffFormula[3].set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])

        self.play(Transform(fmm, stuffFormula))

        self.wait(.2)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

class k2(Scene):
    def construct(self):
        #3.2
        stuffFormula = MathTex(r"F_{{ {g} }}=\frac{k}{ {{r^2}} }")
        stuffFormula[1].set_color(BLUE)
        stuffFormula[3].set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        self.play(Write(stuffFormula))
        #2.2
        a = MathTex(r"F_{{ {g} }}=\frac{k}{ {{4 \pi r^2}} }")
        a[1].set_color(BLUE)
        a[3].set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        self.play(Transform(stuffFormula, a))
        #1.2
        self.wait(1.2)
        sa = MathTex(r"SA={{4 \pi r^2}}")
        sa[1].set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        self.play(Transform(stuffFormula, sa))
        self.play(
            *[FadeOut(mob)for mob in self.mobjects], run_time=0.6
        )
        self.wait()
class k3(Scene):
    def construct(self):
        

        fmm = MathTex(r"F_{{ {g} }}=G\frac{Mm}{ {{r^2}} }")
        fmm[1].set_color(BLUE)
        fmm[3].set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        self.play(Transform(fourpi, fmm))
        

class thank(Scene):
    def construct(self):
        message = Text('Thanks for watching!')
        message.set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        self.play(Write(message))
        self.wait(.6)
        self.play(FadeOut(message, scale=1.5))