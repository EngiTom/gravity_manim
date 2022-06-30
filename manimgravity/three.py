from manim import *
class many(ThreeDScene): # 3d scene
    def construct(self):
        axes = ThreeDAxes(
                          x_range=(-5, 5),
                          y_range=(-4, 4),
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

        s = Sphere(radius=2, resolution=(25, 25), color=BLUE)
        s.set_opacity(0.2)
        #4.266
        self.play(Create(s), run_time=1.266)

        arr = [10, 30, 50]
        timesarr=[1.5, .7, .7]
        waits = [1.5, 0.7, 0.1]
        #3
        for k in range(3):
            

            dots = []
            for i in range(arr[k]):
                randpos = np.random.random(3) - 0.5
                randpos = randpos / np.linalg.norm(randpos) * 2
                dot = Dot3D(randpos, color=RED)
                self.bring_to_back(dot)
                dots.append(dot)
            self.play(*[Create(d) for d in dots], run_time=timesarr[k]) # 2

            self.wait(waits[k])
        s.save_state()
        big = Sphere(radius=2.2, resolution=(25, 25), color=BLUE)
        big.set_opacity(0.2)
        smo = Sphere(radius=1.8, resolution=(25, 25), color=BLUE)
        smo.set_opacity(0.2)
        self.play(Transform(s, big), run_time=.6)
        self.play(Transform(s, smo), run_time=.6)
        self.play(Restore(s), run_time=.6)
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects], run_time=1
        )
        self.wait(.133)
