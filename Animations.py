import pandas as pd

# Yield Curve Data #
##############################
##############################

treasury_data = pd.read_csv (r'/users/ryanlucas/Desktop/OPRG1/DataCentre/Source_for_video/Yield Curve Rep Values 01.csv')

# VIX Term Structure Data #
##############################
##############################

def import_vix_term_structure(file_path):

    if file_path == "Ryan":
        ryan = "/Users/ryanlucas/Desktop/"
        path = str(ryan + common_path)
    if file_path != "Ryan" and file_path != "Raena":
        path = file_path
    term_structure = pd.read_csv(path)
    term_structure['Trade Date'] = pd.to_datetime(term_structure['Trade Date'])
    term_structure = term_structure.set_index('Trade Date')
    return(term_structure)

vix_ts = pd.DataFrame(import_vix_term_structure(file_path = "Ryan"))

# Indices #
##############################
##############################

dow_prices = pd.read_csv(r'/users/ryanlucas/Desktop/OPRG1/DataCentre/raw/Indices/DJI.csv')
dow_prices = dow_prices.set_index(dow_prices['Date'])
dow_prices = dow_prices.iloc[:, 2:]

spy_prices = pd.read_csv(r'/users/ryanlucas/Desktop/OPRG1/DataCentre/raw/Indices/SPY.csv')
spy_prices = spy_prices.set_index(spy_prices['Date'])
spy_prices = spy_prices.iloc[:, 2:]

ndx_prices = pd.read_csv(r'/users/ryanlucas/Desktop/OPRG1/DataCentre/raw/Indices/NDX.csv')
ndx_prices = ndx_prices.set_index(ndx_prices['Date'])
ndx_prices = ndx_prices.iloc[:, 2:]

# Animations #
##############################
##############################

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


class GraphExample(Scene):
    def construct(self):
        num_plane = NumberPlane().set_opacity(0.2)    
        self.play(FadeIn(num_plane, rate_func = slow_into))
        svg = LogoSVG("OPRG-Logo")
        # self.play(DrawBorderThenFill(svg), rate_func = smooth)
        self.wait(0.2)
        self.play(Write(svg), rate_func = slow_into)
        self.wait(0.3)
        op_text = TexText("optimalportfolio.github.io")
        self.play(Write(op_text.next_to(svg, direction= DOWN, buff = 1)))
        self.wait(1)
        group = VGroup(num_plane, svg, op_text)
        self.play(FadeOut(group))

        line = Line((-8,1.7,0), (8,1.7,0), color = WHITE)
        self.play(FadeIn(line))

       

        line = Line((-8,3,0), (8,3,0), color = WHITE)
        self.play(FadeIn(line))

        line = Line((-8,-2.6,0), (8,-2.6,0), color = WHITE)
        self.play(FadeIn(line))

        line = Line((-2.5,-7,0), (-2.5,7,0), color = WHITE)
        self.play(FadeIn(line))
        
        line = Line((2.25,-7,0), (2.25,7,0), color = WHITE)
        self.play(FadeIn(line))

        vix_axes = Axes((0, 5), (9, 33, 6), width = 3, height =  3)
        vix_y_label = vix_axes.get_y_axis_label(r"P_{VIX}", edge= TOP, direction= LEFT_SIDE)
        vix_x_label = vix_axes.get_x_axis_label(r"Maturity_{VIX}", edge = RIGHT_SIDE, direction= BOTTOM)
        vix_axes.shift(5.15*RIGHT + 0.4*UP)
        vix_axes.axes[1].shift(1.1*DOWN)
        vix_axes.add(vix_y_label.shift(6.7*RIGHT + 0.5*DOWN).scale(0.55))
        vix_axes.add(vix_x_label.shift(4.65*RIGHT + 0.7*UP).scale(0.4))
        vix_axes.add_coordinate_labels(font_size = 9)

        

        # sin_graph = axes.get_graph(
        #     lambda x: 3+ np.log(x) + 1/3*math.sqrt(x) if x > 0 else 0,
        #     color=BLUE,
        # )
        vix_spot = vix_ts['Spot'][0]
        vix_1m = vix_ts['1M'][0]
        vix_2m = vix_ts['2M'][0]
        vix_3m = vix_ts['3M'][0]
        vix_4m = vix_ts['4M'][0]

        vix_dotspot = Dot(color=GREEN).scale(0.8)
        vix_dot1m = Dot(color=GREEN).scale(0.8)
        vix_dot2m = Dot(color=GREEN).scale(0.8)
        vix_dot3m = Dot(color=GREEN).scale(0.8)
        vix_dot4m = Dot(color=GREEN).scale(0.8)
        
        vix_spot_coord = vix_axes.c2p(0, vix_spot)
        vix_1m_coord = vix_axes.c2p(1, vix_1m)
        vix_dotspot.move_to(vix_spot_coord)
        vix_dot1m.move_to(vix_1m_coord)
        vix_2m_coord = vix_axes.c2p(2, vix_2m)
        vix_dot2m.move_to(vix_2m_coord)
        vix_3m_coord = vix_axes.c2p(3, vix_3m)
        vix_dot3m.move_to(vix_3m_coord)
        vix_4m_coord = vix_axes.c2p(4, vix_4m)
        vix_dot4m.move_to(vix_4m_coord)

        vix_line1 = Line(vix_spot_coord, vix_1m_coord, color = GREEN)
        vix_line2 = Line(vix_1m_coord, vix_2m_coord, color = GREEN)
        vix_line3 = Line(vix_2m_coord, vix_3m_coord, color = GREEN)
        vix_line4 = Line(vix_3m_coord, vix_4m_coord, color = GREEN)


        group = VGroup(vix_line1, vix_line2, vix_line3, vix_line4)
        
        yc_axes = Axes((0, 31, 5), (0, 4, 1), width = 3, height =  3)
        yc_y_label = yc_axes.get_y_axis_label(r"Y_{b}", edge= TOP, direction= LEFT_SIDE)
        yc_x_label = yc_axes.get_x_axis_label(r"Maturity_{b}", edge = RIGHT_SIDE, direction= BOTTOM)
        yc_axes.shift(4.9*LEFT + 0.15*DOWN)
        yc_axes.add(yc_y_label.shift(3.3*LEFT + 0.2*DOWN).scale(0.55))
        yc_axes.add(yc_x_label.shift(5.1*LEFT + 0.34*UP).scale(0.4))
        yc_axes.add_coordinate_labels(font_size = 8)

        yc_1m = pd.to_numeric(treasury_data['DGS1MO'][0])
        yc_3m = pd.to_numeric(treasury_data['DGS3MO'][0])
        yc_6m = pd.to_numeric(treasury_data['DGS6MO'][0])
        yc_1y = pd.to_numeric(treasury_data['DGS1'][0])
        yc_3y = pd.to_numeric(treasury_data['DGS3'][0])
        yc_5y = pd.to_numeric(treasury_data['DGS5'][0])
        yc_7y = pd.to_numeric(treasury_data['DGS7'][0])
        yc_10y = pd.to_numeric(treasury_data['DGS10'][0])
        yc_20y = pd.to_numeric(treasury_data['DGS20'][0])
        yc_30y = pd.to_numeric(treasury_data['DGS30'][0])

        yc_points = [yc_1m, yc_3m, yc_6m, yc_1y, yc_3y, yc_5y, yc_7y, yc_10y, yc_20y, yc_30y]

        # yc_dot1m = Dot(color=GREEN).scale(0.8)
        # yc_dot3m = Dot(color=GREEN).scale(0.8)
        # yc_dot6m = Dot(color=GREEN).scale(0.8)
        # yc_dot1y = Dot(color=GREEN).scale(0.8)
        # yc_dot3y = Dot(color=GREEN).scale(0.8)
        # yc_dot5y = Dot(color=GREEN).scale(0.8)
        # yc_dot7y = Dot(color=GREEN).scale(0.8)
        # yc_dot10y = Dot(color=GREEN).scale(0.8)
        # yc_dot20y = Dot(color=GREEN).scale(0.8)
        # yc_dot30y = Dot(color=GREEN).scale(0.8)

        yc_1m_coord = yc_axes.c2p(1/12, yc_1m)
        yc_3m_coord = yc_axes.c2p(3/12, yc_3m)
        yc_6m_coord = yc_axes.c2p(6/12, yc_6m)
        yc_1y_coord = yc_axes.c2p(1, yc_1y)
        yc_3y_coord = yc_axes.c2p(3, yc_3y)
        yc_5y_coord = yc_axes.c2p(5, yc_5y)
        yc_7y_coord = yc_axes.c2p(7, yc_7y)
        yc_10y_coord = yc_axes.c2p(10, yc_10y)
        yc_20y_coord = yc_axes.c2p(20, yc_20y)
        yc_30y_coord = yc_axes.c2p(30, yc_30y)

        yc_dot1m.move_to(yc_1m_coord)
        yc_dot3m.move_to(yc_3m_coord)
        yc_dot6m.move_to(yc_6m_coord)
        yc_dot1y.move_to(yc_1y_coord)
        yc_dot3y.move_to(yc_3y_coord)
        yc_dot5y.move_to(yc_5y_coord)
        yc_dot7y.move_to(yc_7y_coord)
        yc_dot10y.move_to(yc_10y_coord)
        yc_dot20y.move_to(yc_20y_coord)
        yc_dot30y.move_to(yc_30y_coord)

        yc_line1 = Line(yc_1m_coord, yc_3m_coord, color = GREEN)
        yc_line2 = Line(yc_3m_coord, yc_6m_coord, color = GREEN)
        yc_line3 = Line(yc_6m_coord, yc_1y_coord, color = GREEN)
        yc_line4 = Line(yc_1y_coord, yc_3y_coord, color = GREEN)
        yc_line5 = Line(yc_3y_coord, yc_5y_coord, color = GREEN)
        yc_line6 = Line(yc_5y_coord, yc_7y_coord, color = GREEN)
        yc_line7 = Line(yc_7y_coord, yc_10y_coord, color = GREEN)
        yc_line8 = Line(yc_10y_coord, yc_20y_coord, color = GREEN)
        yc_line9 = Line(yc_20y_coord, yc_30y_coord, color = GREEN)
        
        indices_axes = Axes((0, 1, 10), (0, 5), width = 3, height =  3)
        indices_y_label = indices_axes.get_y_axis_label(r"P_{index}", edge= TOP, direction= LEFT_SIDE)
        indices_x_label = indices_axes.get_x_axis_label(r"TBC", edge = RIGHT_SIDE, direction= BOTTOM)
        indices_axes.shift(0.15*RIGHT + 0.2*DOWN)
        indices_axes.add(indices_y_label.shift(1.95*RIGHT + 0.2*DOWN).scale(0.55))
        indices_axes.add(indices_x_label.shift(0.05*LEFT + 0.34*UP).scale(0.4))
        indices_axes.add_coordinate_labels(font_size = 8)

        spy_open_0 = spy_prices['Open'][0]
        spy_close_0 = spy_prices['Close'][0]
        
        spy_open_coord = yc_axes.c2p(0, spy_open_0)
        spy_close_coord = yc_axes.c2p(1, spy_close_0)

        spy_line_0 = Line(spy_open_coord, spy_close_coord, color = GREEN)

        yc_group = VGroup(yc_line1, yc_line2, yc_line3, yc_line4, yc_line5, yc_line6, yc_line7, yc_line8, yc_line9)
        vix_group = VGroup(vix_line1, vix_line2, vix_line3, vix_line4)


        current_date = TexText(str(treasury_data['DATE'][0]), color = YELLOW_B).to_edge(DOWN, buff = 0.6).shift(DOWN*0.05 +LEFT*0.15)
        self.play(DrawBorderThenFill(current_date, edge = BOTTOM, DIRECTION = DOWN, rate_func = rush_into, run_time = 0.8))
        yc_label = TexText("Yield Curve", color = GREY_A, font_size = 40).next_to(yc_axes, direction = UP).shift(RIGHT*0.05 + UP*1.65)
        self.play(Write(yc_label))
        index_label = TexText("Market Indices", color = GREY_A, font_size = 40).next_to(indices_axes, direction = UP).shift(RIGHT*0.05 + UP*1.65)
        self.play(Write(index_label))
        vix_label = TexText("VIX Curve", color = GREY_A, font_size = 40).next_to(vix_axes, direction = UP).shift(LEFT*0.05 + UP*1.65)
        self.play(Write(vix_label))

        ####### ADDITIONAL INFO #######

        yc_spread = TexText("10Y - 3M Bond Spread", color = WHITE, font_size = 30).next_to(yc_axes, direction = UP).shift(RIGHT*0 + UP*0.7)
        yc_s_label = TexText("$\\approx 0$", color = WHITE, font_size = 25).next_to(yc_axes, direction = UP).shift(RIGHT*0 + UP*0.3)
        self.play(Write(yc_spread))
        self.play(Write(yc_s_label))

        spy_label = TexText("S\\&P", color = WHITE, font_size = 30).next_to(indices_axes, direction = UP).shift(LEFT*1.45 + UP*0.75)
        spy_d_label = TexText("$\\Delta \\approx 0$", color = WHITE, font_size = 25).next_to(indices_axes, direction = UP).shift(LEFT*1.45 + UP*0.3)
        self.play(Write(spy_label), Write(spy_d_label))

        ndx_label = TexText("NDX", color = WHITE, font_size = 30).next_to(indices_axes, direction = UP).shift(LEFT*0.05 + UP*0.75)
        ndx_d_label = TexText("$\\Delta \\approx 0$", color = WHITE, font_size = 25).next_to(indices_axes, direction = UP).shift(LEFT*0.05 + UP*0.33)
        self.play(Write(ndx_label), Write(ndx_d_label))

        dow_label = TexText("DOW", color = WHITE, font_size = 30).next_to(indices_axes, direction = UP).shift(RIGHT*1.45 + UP*0.75)
        dow_d_label = TexText("$\\Delta \\approx 0$", color = WHITE, font_size = 25).next_to(indices_axes, direction = UP).shift(RIGHT*1.45 + UP*0.33)
        self.play(Write(dow_label), Write(dow_d_label))

        vix_fm_label = TexText("VIX 2M", color = WHITE, font_size = 30).next_to(vix_axes, direction = UP).shift(LEFT*1.5 + UP*0.73)
        vix_sm_label = TexText("VIX 1M", color = WHITE, font_size = 30).next_to(vix_axes, direction = UP).shift(RIGHT*0 + UP*0.73)
        difference = TexText("2M - 1M", color = WHITE, font_size = 30).next_to(vix_axes, direction = UP).shift(RIGHT*1.5 + UP*0.73)

        vix_color = GREY_A

        difference_val = TexText(str(round(vix_2m - vix_1m, 2)), color = vix_color, font_size = 25).next_to(vix_axes, direction = UP).shift(RIGHT*1.5 + UP*0.35) 
        
        self.play(Write(vix_fm_label))
        self.play(Write(vix_sm_label))
        self.play(Write(difference))


        ####### ############### #######
        yc_axes.add_coordinate_labels(font_size = 8)
        self.play(Write(yc_axes, lag_ratio=0.01, run_time=1))
        self.play(Write(indices_axes, lag_ratio=0.01, run_time=1))
        self.play(Write(vix_axes, lag_ratio=0.01, run_time=1))
        self.play(Write(yc_group, run_time = 2, rate_func = slow_into), Write(vix_group, run_time = 2, rate_func = slow_into))
        self.wait(5)

        yc_graphs = []
        vix_graphs = []
        dates = []
        yc_group_init = VGroup(yc_line1, yc_line2, yc_line3, yc_line4, yc_line5, yc_line6, yc_line7, yc_line8, yc_line9)

        start_num = 1
        for i in range(start_num, len(treasury_data['DGS1MO']), 1):
           

            if i >1:
                self.play(FadeOut(current_date), FadeOut(yc_group),FadeOut(yc_s_label), FadeOut(vix_group), FadeOut(yc_spread), FadeOut(vix_sm_label), FadeOut(vix_sm_val), FadeOut(vix_fm_label), FadeOut(vix_fm_val), FadeOut(difference), FadeOut(difference_val), FadeToColor(yc_label, GREY_A)) 
                self.play(FadeOut(current_date), FadeOut(yc_s_label), FadeOut(vix_group), FadeOut(yc_spread), FadeOut(vix_sm_label), FadeOut(vix_sm_val), FadeOut(vix_fm_label), FadeOut(vix_fm_val), FadeOut(difference), FadeOut(difference_val), FadeToColor(yc_label, GREY_A))       
                self.play(FadeToColor(vix_label, GREY_A))
            else:
                self.play(FadeOut(current_date), FadeOut(yc_group),FadeOut(yc_s_label), FadeOut(vix_group), FadeOut(yc_spread), FadeOut(vix_sm_label), FadeOut(vix_fm_label), FadeOut(difference), FadeToColor(yc_label, GREY_A))    
                self.play(FadeOut(current_date), FadeOut(yc_s_label), FadeOut(vix_group), FadeOut(yc_spread), FadeOut(vix_sm_label), FadeOut(vix_fm_label), FadeOut(difference), FadeToColor(yc_label, GREY_A))    
            
            
            yc_1m = pd.to_numeric(treasury_data['DGS1MO'][i])
            
          
            yc_3m = pd.to_numeric(treasury_data['DGS3MO'][i])
           
            
            yc_6m = pd.to_numeric(treasury_data['DGS6MO'][i])
           
            yc_1y = pd.to_numeric(treasury_data['DGS1'][i])
           
            yc_3y = pd.to_numeric(treasury_data['DGS3'][i])
            
            yc_5y = pd.to_numeric(treasury_data['DGS5'][i])
           
            yc_7y = pd.to_numeric(treasury_data['DGS7'][i])
            
           
            yc_10y = pd.to_numeric(treasury_data['DGS10'][i])
            
            yc_20y = pd.to_numeric(treasury_data['DGS20'][i])
           
            yc_30y = pd.to_numeric(treasury_data['DGS30'][i])
            

            yc_1m_coord = yc_axes.c2p(1/12, yc_1m)
            yc_3m_coord = yc_axes.c2p(3/12, yc_3m)
            yc_6m_coord = yc_axes.c2p(6/12, yc_6m)
            yc_1y_coord = yc_axes.c2p(1, yc_1y)
            yc_3y_coord = yc_axes.c2p(3, yc_3y)
            yc_5y_coord = yc_axes.c2p(5, yc_5y)
            yc_7y_coord = yc_axes.c2p(7, yc_7y)
            yc_10y_coord = yc_axes.c2p(10, yc_10y)
            yc_20y_coord = yc_axes.c2p(20, yc_20y)
            yc_30y_coord = yc_axes.c2p(30, yc_30y)


            yc_color = GREEN
            if yc_1m > yc_1y:
                yc_color = RED
            elif yc_1m > 0.2:
                    yc_color = ORANGE

            yc_dot1m = Dot(color=yc_color).scale(0.8)
            yc_dot3m = Dot(color=yc_color).scale(0.8)
            yc_dot6m = Dot(color=yc_color).scale(0.8)
            yc_dot1y = Dot(color=yc_color).scale(0.8)
            yc_dot3y = Dot(color=yc_color).scale(0.8)
            yc_dot5y = Dot(color=yc_color).scale(0.8)
            yc_dot7y = Dot(color=yc_color).scale(0.8)
            yc_dot10y = Dot(color=yc_color).scale(0.8)
            yc_dot20y = Dot(color=yc_color).scale(0.8)
            yc_dot30y = Dot(color=yc_color).scale(0.8)

            yc_line1 = Line(yc_1m_coord, yc_3m_coord, color = yc_color)
            yc_line2 = Line(yc_3m_coord, yc_6m_coord, color = yc_color)
            yc_line3 = Line(yc_6m_coord, yc_1y_coord, color = yc_color)
            yc_line4 = Line(yc_1y_coord, yc_3y_coord, color = yc_color)
            yc_line5 = Line(yc_3y_coord, yc_5y_coord, color =yc_color)
            yc_line6 = Line(yc_5y_coord, yc_7y_coord, color = yc_color)
            yc_line7 = Line(yc_7y_coord, yc_10y_coord, color = yc_color)
            yc_line8 = Line(yc_10y_coord, yc_20y_coord, color = yc_color)
            yc_line9 = Line(yc_20y_coord, yc_30y_coord, color = yc_color)

            yc_spread = TexText("10Y - 3M Bond Spread", color = yc_color, font_size = 30).next_to(yc_axes, direction = UP).shift(RIGHT*0 + UP*0.7)
            yc_s_label = TexText(str(round(yc_10y - yc_3m, 2)), color = yc_color, font_size = 25).next_to(yc_axes, direction = UP).shift(RIGHT*0 + UP*0.3)
            
            try:
                vix_spot = vix_ts['Spot'][i]
                vix_1m = vix_ts['1M'][i]
                vix_2m = vix_ts['2M'][i]
                vix_3m = vix_ts['3M'][i]
                vix_4m = vix_ts['4M'][i]
            except:
                print(1)
                pass
            
            vix_color = GREEN
            if vix_1m > vix_2m:
                vix_color = RED
            elif vix_1m > 17:
                vix_color = ORANGE

            vix_spot_coord = vix_axes.c2p(0, vix_spot)
            vix_1m_coord = vix_axes.c2p(1, vix_1m)
            vix_dotspot.move_to(vix_spot_coord)
            vix_dot1m.move_to(vix_1m_coord)
            vix_2m_coord = vix_axes.c2p(2, vix_2m)
            vix_dot2m.move_to(vix_2m_coord)
            vix_3m_coord = vix_axes.c2p(3, vix_3m)
            vix_dot3m.move_to(vix_3m_coord)
            vix_4m_coord = vix_axes.c2p(4, vix_4m)
            vix_dot4m.move_to(vix_4m_coord)

            vix_line1 = Line(vix_spot_coord, vix_1m_coord, color = vix_color)
            vix_line2 = Line(vix_1m_coord, vix_2m_coord, color = vix_color)
            vix_line3 = Line(vix_2m_coord, vix_3m_coord, color = vix_color)
            vix_line4 = Line(vix_3m_coord, vix_4m_coord, color = vix_color)

            vix_fm_label = TexText("VIX 2M", color = vix_color, font_size = 30).next_to(vix_axes, direction = UP).shift(LEFT*1.5 + UP*0.73)
            vix_fm_val = TexText(str(round(vix_2m,2)), color = vix_color, font_size = 25).next_to(vix_axes, direction = UP).shift(LEFT*1.5 + UP*0.35)
            vix_sm_label = TexText("VIX 1M", color = vix_color, font_size = 30).next_to(vix_axes, direction = UP).shift(RIGHT*0 + UP*0.73)
            vix_sm_val = TexText(str(round(vix_1m, 2)), color = vix_color, font_size = 25).next_to(vix_axes, direction = UP).shift(LEFT*0 + UP*0.35)
            difference = TexText("2M - 1M", color = vix_color, font_size = 30).next_to(vix_axes, direction = UP).shift(RIGHT*1.5 + UP*0.73)
            difference_val = TexText(str(round(vix_2m - vix_1m, 2)), color = vix_color, font_size = 25).next_to(vix_axes, direction = UP).shift(RIGHT*1.5 + UP*0.35) 
           
            yc_group = VGroup(yc_line1, yc_line2, yc_line3, yc_line4, yc_line5, yc_line6, yc_line7, yc_line8, yc_line9)

            yc_graphs.append(yc_group)

            vix_group = VGroup(vix_line1, vix_line2, vix_line3, vix_line4)

            vix_graphs.append(vix_group)
            vix_labels = VGroup(vix_fm_label, vix_fm_val, vix_sm_label, vix_sm_val, difference, difference_val)

            current_date = TexText(str(treasury_data['DATE'][i]), color = YELLOW_B).to_edge(DOWN, buff = 0.6).shift(DOWN*0.05+LEFT*0.15)
            dates.append(current_date)
            self.play(FadeToColor(vix_label, vix_color))
            self.play(FadeToColor(yc_label, yc_color))

            self.play(DrawBorderThenFill(current_date, rate_func = rush_into, run_time = 0.8))
            self.wait(0.5)
            self.play(Write(yc_group, run_time = 1.5, rate_func = rush_into), Write(vix_group, run_time = 1.5, rate_func = rush_into))
            
            if i == start_num:
                self.play(Write(yc_graphs[0]), Write(vix_graphs[0]))
                self.play(Write(dates[0]))
            if i > start_num:
                self.play(ReplacementTransform(yc_graphs[0], yc_graphs[1], run_time = 0.0001, rate_func = smooth), ReplacementTransform(vix_graphs[0], vix_graphs[1], run_time = 0.0001, rate_func = lingering), TransformMatchingParts(dates[0], dates[1], run_time = 0.0001))
                dates.pop(0)
                yc_graphs.pop(0)
                vix_graphs.pop(0)
            self.play(Write(vix_group, run_time = 1.5, rate_func = rush_into))
            self.play(FadeIn(vix_labels), FadeIn(yc_s_label), FadeIn(yc_spread))
            self.wait(2.5)

         


            if i == 0:
                self.play(Write(TexText(current_date.to_edge(UP))))
               
            if i > 1:
                self.play(FadeOut(TexText(current_date)))
            current_date = treasury_data['DATE'][i] 
            if i > 1:
                self.play(Write(TexText(current_date.to_edge(UP))))

            class Test(GraphScene):
                CONFIG = {
            "x_min": -10,
            "x_max": 10,
            "x_axis_width": FRAME_WIDTH,
            "x_tick_frequency": 1,
            "y_min": -6,
            "y_max": 6,
            "y_axis_height": FRAME_HEIGHT,
            "y_tick_frequency": 1,
            "y_axis_label": "$y$",
            "graph_origin": ORIGIN,
            }
            def construct(self):
                self.setup_axes()

                p   = ValueTracker(-10)

                y = self.get_graph(
                lambda x: -1 * p.get_value() * x + p.get_value(),
                color = BLUE,
                x_min = -10,
                x_max = 10
                            )

                y.add_updater(
                    lambda m: m.become(
                    self.get_graph(
                    lambda x: -1 * p.get_value() * x + p.get_value(),
                    color = BLUE,
                    x_min = -10,
                    x_max = 10
                                 )
                                )
                            )

                    self.add(y)
                    self.wait()
                    self.play(
                    ApplyMethod(p.increment_value,20),
                    run_time=5,
                        )
                    self.wait()


    
