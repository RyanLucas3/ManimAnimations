from manimlib import *
import matplotlib.pyplot as plt

class SVGTest(Scene):
    def construct(self):
        svg = SVGMobject("Contract")
        self.play(Write(svg))
        self.wait()

class LogoSVG(SVGMobject):
        CONFIG = {
            "height": 2,
            "width": 2,
            "fill_opacity": 1,
            "stroke_width": 0.2
        }

class OPRGLogo(Scene):
    CONFIG = {
        "camera_config": {"background_color": GREY}
        
    }
    def construct(self):  
        self.wait(10)
        num_plane = NumberPlane().set_opacity(0.2)    
        self.play(FadeIn(num_plane, rate_func = slow_into))
        svg = LogoSVG("OPRG-Logo")
        # self.play(DrawBorderThenFill(svg), rate_func = smooth)
        self.wait(0.2)
        self.play(Write(svg), rate_func = slow_into)
        self.wait(0.3)
        self.play(Write(TexText("optimalportfolio.github.io").next_to(svg, direction= DOWN, buff = 1)))
        self.wait(1)
        group = VGroup(num_plane, svg, op_text)
        # self.play(WiggleOutThenIn(svg))
    
class SandD(Scene):
    CONFIG = {
        "camera_config": {"background_color": GREY}
        
    }
    def construct(self):
        # yc_axes = Axes((0, 11), (0, 12), height = 6.3)
        # yc_label = yc_axes.get_y_axis_label(r"Yield_{b}", edge= TOP, direction= UP, buff = 2).scale(0.6)
        # xc_label = yc_axes.get_x_axis_label(r"Maturity", edge = RIGHT_SIDE, direction= BOTTOM, buff = 0.5).scale(0.6)
        # yc_axes.add_coordinate_labels()
        # yc_axes.add(yc_label)
        # yc_axes.add(xc_label)
        # self.add(yc_axes)
        # yield_curve = yc_axes.get_graph(
        #     lambda x: 5.8 + 3*np.log(x) + 0.1*x*np.log(x) - 0.7*x if x > 0.2 else 0, use_smoothing = False, color = GREEN)
        # self.add(yield_curve)
        # yc_text = TexText(r"Yield Curve", font_size = 60, color = GREEN).next_to(yield_curve, UP, buff= 0.6)
        # self.add(yc_text)

        # self.wait(5)
        # inv_yield_curve = yc_axes.get_graph(
        #     lambda x: 8 - np.log(x) if x > 0.25 else 11 - x, use_smoothing = False, color = RED)
        # self.wait(1)
        # yc_red = TexText(r"Inverted Yield Curve", font_size = 60, color = RED).next_to(yield_curve, UP, buff= 0.6)
        # self.play(Transform(group, inv_yield_curve), Transform(yc_text, yc_red))
        # self.wait(1)

        axes = Axes((0, 9), (0, 12), width = 5.5, height = 5.5)
        # y_label = axes.get_y_axis_label("Annual \  Return", edge= TOP, direction= LEFT_SIDE)
        y_label = axes.get_y_axis_label("Yield_b", edge= TOP, direction= LEFT_SIDE)
        x_label = axes.get_x_axis_label("Quantity_b", edge = RIGHT_SIDE, direction= BOTTOM)
        axes.add(y_label)
        axes.add(x_label)
        axes.add_coordinate_labels()

        self.wait()
        # self.play(FadeOut(yield_curve), FadeOut(yc_text), FadeOut(yc_label), FadeOut(xc_label))
        bond_market = TexText("Bond Market").to_edge(UP)
        # self.play(FadeOut(group))
        self.play(Write(axes, lag_ratio=0.01, run_time=2))
        self.play(FadeIn(bond_market))

        supply = axes.get_graph(
            lambda x: 10-x,
            use_smoothing=False,
            color=BLUE)

        # supply = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))
        # By default, it draws it so as to somewhat smoothly interpolate
        # between sampled points (x, f(x)).  If the graph is meant to have
        # a corner, though, you can set use_smoothing to False
        demand = axes.get_graph(
            lambda x: 2+x,
            use_smoothing=False,
            color=RED)

        demand_label = axes.get_graph_label(demand, r"Demand_b")
        supply_label = axes.get_graph_label(supply, r"Supply_b")

        self.play(
            ShowCreation(supply),
            FadeIn(supply_label, RIGHT))
    
        self.play(
            ShowCreation(demand),
            FadeIn(demand_label, RIGHT))

        # D2_label = axes.get_graph_label(demand, r"D_b")
        # S2_label = axes.get_graph_label(supply, r"S_b")
        # Q2_label = axes.get_x_axis_label("Q_b", edge= RIGHT_SIDE, direction= BOTTOM)
        # self.play(Transform(x_label, Q2_label))
        # self.play(Transform(demand_label, D2_label))
        # self.play(Transform(supply_label, S2_label))

        self.wait(2)

        # Y4_label = axes.get_y_axis_label("Yield_b", edge= TOP, direction= LEFT_SIDE)
        # self.play(Transform(y_label, Y4_label))


        line = DashedVMobject(Line((-2.65,0.07,0), (-0.2,0.07,0), color = GREEN))
        self.play(FadeIn(line))
        dot = Dot(color=GREEN, label = "E_p")
        dot.move_to(axes.c2p(4, 6))
        self.play(FadeIn(dot, scale=0.8))

        
        
        text = TexText("$Y_b^*$", font_size = 42, color = GREEN).next_to(dot, UP)
        self.play(Write(text))

        self.wait(4)


# class MultSandD(Scene):
   
#     def construct(self):


        mult_axes = Axes((0, 9), (0, 10), width = 3.2, height =  2.5)
        mult_y_label = mult_axes.get_y_axis_label(r"Yield_{1y}", edge= TOP, direction= LEFT_SIDE)
        mult_x_label = mult_axes.get_x_axis_label(r"Q_{1y}", edge = RIGHT_SIDE, direction= BOTTOM)
        mult_axes.shift(3.3*RIGHT + 2.2*UP)
        mult_axes.add(mult_y_label.shift(4.9*RIGHT + 2.2*UP).scale(0.4))
        mult_axes.add(mult_x_label.shift(3.3*RIGHT + 2.7*UP).scale(0.4))
        mult_axes.add_coordinate_labels()
       
        mult_axes2 = Axes((0, 9), (0, 10), width = 3.2, height = 2.5)
        mult_axes2.shift(2.8*LEFT + 2.2 * UP)
        mult_y2_label = mult_axes2.get_y_axis_label(r"Yield_{1m}", edge= TOP, direction= LEFT_SIDE)
        mult_x2_label = mult_axes2.get_x_axis_label(r"Q_{1m}", edge = RIGHT_SIDE, direction= BOTTOM)
        mult_axes2.add(mult_y2_label.shift(-0.8*LEFT + 0 * UP).scale(0.4))
        mult_axes2.add(mult_x2_label.shift(0*RIGHT + 0.5 * UP).scale(0.4))
        mult_axes2.add_coordinate_labels()

        mult_axes3 = Axes((0, 9), (0, 10), width = 3.2, height =  2.5)
        mult_y3_label = mult_axes3.get_y_axis_label(r"Yield_{10y}", edge= TOP, direction= LEFT_SIDE)
        mult_x3_label = mult_axes3.get_x_axis_label(r"Q_{10y}", edge = RIGHT_SIDE, direction= BOTTOM)
        mult_axes3.shift(3.3*RIGHT + 1.5*DOWN)
        mult_axes3.add(mult_y3_label.shift(5*RIGHT + 1.5*DOWN).scale(0.4))
        mult_axes3.add(mult_x3_label.shift(3.3*RIGHT + 1*DOWN).scale(0.4))
        mult_axes3.add_coordinate_labels()

        mult_axes4 = Axes((0, 9), (0, 10), width = 3.2, height =  2.5)
        mult_y4_label = mult_axes4.get_y_axis_label(r"Yield_{3y}", edge= TOP, direction= LEFT_SIDE)
        mult_x4_label = mult_axes4.get_x_axis_label(r"Q_{3y}", edge = RIGHT_SIDE, direction= BOTTOM)
        mult_axes4.shift(2.8*LEFT + 1.5*DOWN)
        mult_axes4.add(mult_y4_label.shift(1.2*LEFT + 1.5*DOWN).scale(0.4))
        mult_axes4.add(mult_x4_label.shift(2.8*LEFT + 1*DOWN).scale(0.4))
        mult_axes4.add_coordinate_labels()
        

        graphs = VGroup(mult_axes, mult_axes2, mult_axes3, mult_axes4)
        self.play(FadeOut(axes), FadeOut(y_label), FadeOut(x_label), FadeOut(supply), FadeOut(demand), FadeOut(supply_label), FadeOut(demand_label), FadeOut(dot), FadeOut(text), FadeOut(line), FadeOut(bond_market))
        mult_bonds = TexText("But there are multiple bond markets...")
        self.play(Write(mult_bonds))
        self.wait(1.5)
        mult_mat = TexText("For bonds with different maturities...")
        self.play(Transform(mult_bonds, mult_mat))
        self.wait(1.5)
        self.play(ShowCreation(graphs[0]), ShowCreation(graphs[1]), ShowCreation(graphs[2]), ShowCreation(graphs[3]), FadeOut(mult_bonds))
       
        # axes2 = Axes((0, 9), (0, 12), width = 3, height = 2.5)
        # axes2.shift(3*LEFT + 1.5 * UP)
        # y2_label = axes2.get_y_axis_label("Annual \  Return", edge= TOP, direction= LEFT_SIDE)
        # x2_label = axes2.get_x_axis_label("Quantity", edge = RIGHT_SIDE, direction= BOTTOM)
        # axes2.add(y2_label.shift(0.6*LEFT + 0 * UP).scale(0.4))
        # axes2.add(x2_label.shift(0*LEFT + 0.5 * UP).scale(0.4))
        # axes2.add_coordinate_labels()
        supply1 = mult_axes2.get_graph(
            lambda x: 6.2-x,
            use_smoothing=False,
            color=BLUE)

        # supply = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))
        # By default, it draws it so as to somewhat smoothly interpolate
        # between sampled points (x, f(x)).  If the graph is meant to have
        # a corner, though, you can set use_smoothing to False
        demand1 = mult_axes2.get_graph(
            lambda x: 1+0.13*x,
            use_smoothing=False,
            color=RED)

        # demand_label = axes.get_graph_label(demand, r"Demand_b").scale(0.4)
        # supply_label = axes.get_graph_label(supply, r"Supply_b").scale(0.4)

        self.play(
            ShowCreation(supply1, lag_ratio = 0.7))
    
        self.play(
             ShowCreation(demand1, lag_ratio = 0.7))

        dot1 = Dot(color=GREEN, label = "E_p")
        dot1.move_to(mult_axes2.c2p(4.5, 1.7))
        self.play(Write(dot1), scale=0.4)

        text2 = TexText(r"$Y_{1m}^*$", font_size = 42, color = GREEN).next_to(dot1, UP)
        self.play(Write(text2))

        ########
        ########
        ########

        supply2 = mult_axes.get_graph(
            lambda x: 9.2-0.65*x,
            use_smoothing=False,
            color=BLUE)

        demand2 = mult_axes.get_graph(
            lambda x: 1+0.75*x,
            use_smoothing=False,
            color=RED)

        self.play(
            ShowCreation(supply2, lag_ratio = 0.7))
    
        self.play(
            ShowCreation(demand2, lag_ratio = 0.7))

        dot2 = Dot(color=GREEN, label = "E_p")
        dot2.move_to(mult_axes.c2p(5.85, 5.4))
        self.play(Write(dot2), scale=0.4)

        text3 = TexText(r"$Y_{1y}^*$", font_size = 42, color = GREEN).next_to(dot2, UP)
        self.play(Write(text3))

        ###################

        supply4 = mult_axes4.get_graph(
            lambda x: 10-0.48*x,
            use_smoothing=False,
            color=BLUE)

        demand4 = mult_axes4.get_graph(
            lambda x: 1+1.05*x,
            use_smoothing=False,
            color=RED)

        self.play(
            ShowCreation(supply4, lag_ratio = 0.7))
    
        self.play(
            ShowCreation(demand4, lag_ratio = 0.7))

        dot4 = Dot(color=GREEN, label = "E_p")
        dot4.move_to(mult_axes4.c2p(5.85, 7.15))
        self.play(Write(dot4), scale=0.4)

        text4 = TexText(r"$Y_{3y}^*$", font_size = 42, color = GREEN).next_to(dot4, UP)
        self.play(Write(text4))

        #################

        supply3 = mult_axes3.get_graph(
            lambda x: 10-0.55*x,
            use_smoothing=False,
            color=BLUE)

        demand3 = mult_axes3.get_graph(
            lambda x: 1+1.3*x,
            use_smoothing=False,
            color=RED)

        self.play(
            ShowCreation(supply3, lag_ratio = 0.7))
    
        self.play(
            ShowCreation(demand3, lag_ratio = 0.7))

        dot3 = Dot(color=GREEN, label = "E_p")
        dot3.move_to(mult_axes3.c2p(4.9, 7.4))
        self.play(Write(dot3), scale=0.4)

        text5 = TexText(r"$Y_{10y}^*$", font_size = 42, color = GREEN).next_to(dot3, UP)
        self.play(Write(text5))

        self.play(FadeOut(mult_axes))
        self.play(FadeOut(mult_axes2))
        self.play(FadeOut(mult_axes3))
        self.play(FadeOut(mult_axes4))

        yc_axes = Axes((0, 11), (0, 12), height = 6.3)
        yc_label = yc_axes.get_y_axis_label(r"Yield_{b}", edge= TOP, direction= UP, buff = 2).scale(0.6)
        xc_label = yc_axes.get_x_axis_label(r"Maturity", edge = RIGHT_SIDE, direction= BOTTOM, buff = 0.5).scale(0.6)
        yc_axes.add_coordinate_labels()
        yc_axes.add(yc_label)
        yc_axes.add(xc_label)
    
        self.play(Write(yc_axes, lag_ratio=0.01, run_time=2))

        group1 = VGroup(dot1, supply1, demand1, text2)
        group1.generate_target()
        group1.target.shift(2.95*LEFT + 3.6*DOWN)
        self.play(MoveToTarget(group1), rate_func = rush_from)

        self.wait(1.5)

        group2 = VGroup(dot2, supply2, demand2, text3)
        group2.generate_target()
        group2.target.shift(8.62*LEFT + 2.6*DOWN)
        self.play(MoveToTarget(group2), rate_func = rush_from)
        self.wait(1.5)

        group3 = VGroup(dot4, supply4, demand4, text4)
        self.play(bring_to_front(dot4))
        group3.generate_target()
        group3.target.shift(0.65*LEFT + 1.63*UP)
        self.play(MoveToTarget(group3), rate_func = rush_from)
        self.wait(1.5)

        group4 = VGroup(dot3, supply3, demand3, text5)
        self.play(bring_to_front(dot3))
        group4.generate_target()
        group4.target.shift(1.5*RIGHT + 1.96*UP)
        self.play(MoveToTarget(group4), rate_func = rush_from)
        self.wait(1.5)

        self.play(FadeOut(VGroup(supply1, demand1, text2,supply2, demand2, text3,supply4, demand4, text4,supply3, demand3, text5)))
        
        line1 = Line((-5.7,-2.15,0), (-4.78,-0.22,0), color = GREEN)
        self.play(FadeIn(line1))

        line2 = Line((-4.85,-0.25,0), (-2.85,0.75,0), color = GREEN)
        self.play(FadeIn(line2))

        line3 = Line((-2.85,0.75,0), (5,1.13,0), color = GREEN)
        self.play(FadeIn(line3))

        group = VGroup(line1, line2, line3)
        yield_curve = yc_axes.get_graph(
            lambda x: 5.8 + 3*np.log(x) + 0.1*x*np.log(x) - 0.7*x if x > 0.2 else 0, use_smoothing = False, color = GREEN)
        self.play(FadeOut(group), FadeIn(yield_curve))
        # self.play(ReplacementTransform(group, yield_curve))
        
        self.play(FadeOut(VGroup(dot1, dot2, dot3, dot4)))
        
        yc_text = TexText(r"Yield Curve", font_size = 60, color = GREEN).next_to(yield_curve, UP, buff= 0.6)
        self.play(FadeIn(yc_text))
        self.play(WiggleOutThenIn(yc_text))
        # self.play(Indicate(yield_curve))
        # self.play(FadeOut(yc_text), FadeOut(yield_curve))
# class YC(MultSandD):
#     def construct(self):
        yc_axes = Axes((0, 11), (0, 12), height = 6.3)
        yc_label = yc_axes.get_y_axis_label(r"Yield_{b}", edge= TOP, direction= UP, buff = 2).scale(0.6)
        xc_label = yc_axes.get_x_axis_label(r"Maturity", edge = RIGHT_SIDE, direction= BOTTOM, buff = 0.5).scale(0.6)
        yc_axes.add_coordinate_labels()
        yc_axes.add(yc_label)
        yc_axes.add(xc_label)
        self.add(yc_axes)
        # yield_curve = yc_axes.get_graph(
        #     lambda x: 5.8 + 3*np.log(x) + 0.1*x*np.log(x) - 0.7*x if x > 0.2 else 0, use_smoothing = False, color = GREEN)
        # self.add(yield_curve)
        # yc_text = TexText(r"Yield Curve", font_size = 60, color = GREEN).next_to(yield_curve, UP, buff= 0.6)
        # self.add(yc_text)

        inv_yield_curve = yc_axes.get_graph(
            lambda x: 8 - np.log(x) if x > 0.25 else 11 - x, use_smoothing = False, color = RED)
        self.wait(1)
        yc_red = TexText(r"Inverted Yield Curve", font_size = 60, color = RED).next_to(yield_curve, UP, buff= 0.6)
        self.play(Transform(yield_curve, inv_yield_curve), Transform(yc_text, yc_red))
        self.wait(1)



        less_inv = yc_axes.get_graph(
            lambda x: 7.5 - np.log(x) + 0.2* x if x > 0.25 else 7.5 - x, use_smoothing = False, color = ORANGE)
        self.wait(1)
        any_shape = TexText("Shape varies on short-run outlook", direction = TOP, buff = 2).move_to(2*UP)
        self.play(Transform(inv_yield_curve, less_inv), Transform(yc_text, any_shape))
        self.play(any_shape.set_color_by_gradient, RED_D, YELLOW_E)

        not_inv = yc_axes.get_graph(
            lambda x: 5 - 0.7*np.log(x) + 0.3* x if x > 0.25 else 7 - x, use_smoothing = False, color = GOLD_A)

        self.play(Transform(less_inv, not_inv), any_shape.set_color_by_gradient, ORANGE, GOLD_A)
        
        self.wait(1)
        least_inv = yc_axes.get_graph(
            lambda x: 4.8 + 2*np.log(x) + 0.1*x*np.log(x) - 0.7*x if x > 0.2 else 0.5, use_smoothing = False, color = GREEN_B)

        self.play(Transform(not_inv, least_inv), any_shape.set_color_by_gradient, YELLOW_E, GREEN)
            
        term_structure = TexText(r"Known as Term Structure", font_size = 60, color = WHITE).next_to(not_inv, UP, buff= 2)
        self.wait(2)
        self.play(FadeOut(yc_text))
        self.play(Transform(any_shape, term_structure))