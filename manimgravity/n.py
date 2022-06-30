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
        s.set_opacity(0.5)
        #4.266
        
        big = Sphere(radius=3, resolution=(25, 25), color=BLUE)
        big.set_opacity(0.5)

        sm = Sphere(radius=1, resolution=(25, 25), color=BLUE)
        sm.set_opacity(0.5)

        self.play(Create(s), run_time=1)
        s.save_state()
        xx=1
        self.play(Transform(s, big), run_time=xx)
        self.play(Transform(s, sm), run_time=xx)
        self.play(Restore(s), run_time=xx)
        self.wait(.8)

        self.play(Rotate(s, 2*TAU), rate_func=utils.rate_functions.ease_in_out_cubic, run_time=2)
        self.play(FadeOut(s), run_time=1)

        