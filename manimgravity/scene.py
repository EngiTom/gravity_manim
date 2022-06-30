import time
from manim import *
import numpy as np
#Manim Example | How to Show Sphere in Manim

class title1(Scene): #title
    def construct(self):
        maintitle = Text("Gravity", font_size=90, color=BLUE)
        subtitle = Text('A Lesson in Proportionality')
        subtitle.move_to(DOWN)
        self.play(Write(maintitle), run_time=.8)
        self.play(Write(subtitle, run_time=1.3))
        self.wait()
        self.play(*[FadeOut(mob)for mob in self.mobjects], run_time=0.45)

class fma2(Scene): # equations
    def construct(self):

        fma = MathTex("F=ma",substrings_to_isolate='a')
        # fma.set_color_by_tex("a", BLUE)
        self.play(Write(fma))
        self.wait(2.867)

        fmg = MathTex("F_{g}=mg",substrings_to_isolate='g')
        fmg.set_color_by_tex("g", BLUE)
        self.play(Transform(fma, fmg))
        self.wait(2)

        fm98 = MathTex("F_{{ {g} }}=m{{(9.8)}}")
        fm98[1].set_color(BLUE)
        fm98[3].set_color(BLUE)
        self.play(Transform(fma, fm98))
        self.wait(1.7)

        fmm = MathTex(r"F_{{ {g} }}=G\frac{Mm}{ {{r^2}} }")
        fmm[1].set_color(BLUE)
        fmm[3].set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        self.play(Transform(fma, fmm))
        self.wait(5.3)


        cou = MathTex(r"F=\frac{1}{4\pi \epsilon_0}\frac{q_1 q_2}{r^2}")
        cou.move_to((2, 2, 0))
        cou.set_color(YELLOW)
        pvnrt = MathTex(r"PV=nRT")
        pvnrt.move_to((2, -2, 0))
        pvnrt.set_color(LIGHT_PINK)
        ivr = MathTex(r"I=\frac{V}{R}")
        ivr.move_to((-2, -2, 0))
        ivr.set_color(YELLOW)
        light = MathTex(r"f=\frac{v}{\lambda}")
        light.move_to((-2, 2, 0))
        light.set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        foureqs = [cou, pvnrt, ivr, light]
        self.play(*[Write(x) for x in foureqs])
        self.wait(2)
        # but back to this equation
        self.play(*[FadeOut(x) for x in foureqs])
        self.wait(0.63)
        self.play(FadeOut(fma), run_time=.5)
        self.wait()

class s(ThreeDScene): # 3d scene
    def construct(self):
        axes = ThreeDAxes(
                          x_range=(-5, 5),
                          y_range=(-5, 5),
                          z_range=(-3, 3),
                          axis_config={
                              "stroke_color": WHITE,
                              "stroke_width": 4,
                              "include_tip": True,
                              "include_ticks": True,
                              "tick_size": 0.1
                          },
                          x_axis_config={
                              "stroke_color": WHITE,
                              "stroke_width": 4,
                              "include_tip": True,
                              "include_ticks": False,
                              "tick_size": 0.1
                          },
                          y_axis_config={
                              "stroke_color": WHITE,
                              "stroke_width": 4,
                              "include_tip": True,
                              "include_ticks": False,
                              "tick_size": 0.1
                          },
                          z_axis_config={
                              "stroke_color": WHITE,
                              "stroke_width": 4,
                              "include_tip": True,
                              "include_ticks": False,
                              "tick_size": 0.1
                          })
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        planet = Sphere(radius=1, resolution=(25, 25), color=GREEN_A)
        planet.set_opacity(255)
        self.add(planet)
        # self.play(Create(planet), run_time=0.2)
        # field big small
        sphere = Sphere(radius=1.3, resolution=(25,25), color=BLUE)
        sphere.set_opacity(0.2)
        self.bring_to_back(sphere)
        self.play(Create(sphere), run_time=0.5) #3.73
        self.wait()
        sphere.save_state()
        #3.23
        bigSphere = Sphere(radius=3, resolution=(25, 25), color=BLUE)
        bigSphere.set_opacity(0.2)
        
        self.play(Transform(sphere, bigSphere), run_time=1)
        self.play(Restore(sphere),run_time=1)

        medSphere = Sphere(radius=2, resolution=(25, 25), color=BLUE)
        medSphere.set_opacity(0.2)
        self.play(Transform(sphere, medSphere), run_time=1)
        #3.23
        finalField = Sphere(radius=1.2, resolution=(25, 25), color=BLUE)
        finalField.set_opacity(0.1)
    

        self.wait(.23)

        # make objects fall toward surface
        ball1 = Sphere((2, 0, 0), radius=0.2, resolution=(10, 10), color=RED)
        ball1.set_opacity(255)
        ball2 = Sphere((0, -2, 0), radius=0.2, resolution=(10, 10), color=RED)
        ball2.set_opacity(255)
        ball3 = Sphere((0, 0, 2), radius=0.2, resolution=(10, 10), color=RED)
        ball3.set_opacity(255)
        arr = [ball1, ball2]
        # create
        for x in arr:
            self.bring_to_back(x)
            self.play(Create(x), run_time=1)
        self.add(ball1, ball2)
        lines = []
        for x in arr:
            pos = x.get_center()
            length = np.linalg.norm(pos)
            normalizedPos = pos/length * 1.2
            line = Line(start=pos, end=normalizedPos)
            lines.append(line)
        
        shrink = [MoveAlongPath(arr[i], lines[i]) for i in range(2)]
        shrink.append(Transform(sphere, finalField))
        self.play(*shrink, rate_func=utils.rate_functions.ease_in_quad, run_time=1.5)

        self.wait(.37)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


class t1(Scene): # thirds pie
    def construct(self):
        p = []
        for i in range(3):
            for j in range(i):
                c = Circle(0.50, BLACK, fill_opacity=1, stroke_color=WHITE)
                c.move_to((-2 + 1.1*j - 0.55*i, -i+1.5, 0))
                p.append(c)
        #4.8
        for i in p:
            self.play(Create(i), run_time=0.5)
        #3.3
        s1 = Circle(1)
        s1.move_arc_center_to((2.7, 0, 0))
        s2 = AnnularSector(inner_radius=0, outer_radius=1, angle=TAU/3, stroke_width=4, stroke_color=WHITE, color=LIGHT_BROWN)
        s3 = AnnularSector(inner_radius=0, outer_radius=1, start_angle=TAU/3, angle=TAU/3, stroke_width=4, stroke_color=WHITE, color=LIGHT_BROWN)
        s4 = AnnularSector(inner_radius=0, outer_radius=1, start_angle=2*TAU/3, angle=TAU/3, stroke_width=4, stroke_color=WHITE, color=LIGHT_BROWN)
        pie = VGroup()
        pie.add(s2), pie.add(s4), pie.add(s3)
        pie.move_to((2.7, 0, 0))
        self.play(Create(pie), run_time=1.3)
        # 2
        text = MathTex(r"\frac{1}{3}")
        # text.move_to(LEFT)
        self.play(Create(text))
        # 1

        #fade all
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
class n1(Scene): # make pie
    def construct(self):
        p = []
        for i in range(4):
            for j in range(i):
                c = Circle(0.50, BLACK, fill_opacity=1, stroke_color=WHITE)
                c.move_to((-2.5 + 1.1*j - 0.55*i, -i+2, 0))
                p.append(c)
        #4.1666
        self.play(*[Create(x) for x in p], run_time=1)
        # 3.1666
        #pie
        s1 = Circle(1)
        s1.move_arc_center_to((2.7, 0, 0))
        arcs = []
        for i in range(6):
            curarc = AnnularSector(inner_radius=0, outer_radius=1, angle=TAU/6, start_angle=-i*TAU/6, stroke_width=4, stroke_color=WHITE, color=LIGHT_BROWN)
            curarc.move_arc_center_to((2.7, 0, 0))
            arcs.append(curarc)
        self.play(Create(s1), run_time=.5)
        #2.666
        self.play(*[Create(x) for x in arcs], run_time=1.166)

        #1.5

        #text
        text = MathTex(r"\frac{1}{ {{n}} }")
        text[1].set_color_by_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE])
        self.play(Write(text), run_time=.75)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects], run_time=.75
        )



