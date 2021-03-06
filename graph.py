from manimlib.imports import *

class Scene_(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }


class NF24P3358(Scene_):
    def construct(self):
        line = Line(LEFT*3, RIGHT*3, color=BLACK)
        nodes = VGroup(
            *[
                Circle(radius=0.25, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK)
                for _ in range(7)
            ]
        ).arrange(RIGHT, buff=0.5)
        names = VGroup(
            *[
                TextMobject(str(i), color=BLACK).scale(0.7)
                for i in range(1, 8)
            ]
        )
        edges = VGroup(
            *[
                Arrow(nodes[i].get_center(), nodes[i + 1].get_center(), buff=0.25, color=BLACK)
                for i in range(6)
            ]
        )
        infs = VGroup(
            *[
                TextMobject("inf", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.6).next_to(edges[i], UP, buff=0.1)
                for i in range(6)
            ]
        )
        costs = VGroup(
            *[
                TextMobject("0", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.6).next_to(edges[i], DOWN, buff=0.1)
                for i in range(6)
            ]
        )
        for i in range(7):
            names[i].move_to(nodes[i])
        s = VGroup(
            Circle(radius=0.25, fill_color=WHITE, fill_opacity=1, stroke_color=RED),
            TextMobject("s", color=RED, background_stroke_width=0).scale(0.75)
        ).move_to(np.array([-4.5, -1.5, 0]))
        s.add(Arrow(s.get_center(), nodes[0].get_center(), color=RED, buff=0.25))
        s.add(TextMobject("k", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.6).next_to(s[-1], UL, buff=-0.5))
        s.add(TextMobject("0", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.6).next_to(s[-2], DR, buff=-0.5))
        t = VGroup(
            Circle(radius=0.25, fill_color=WHITE, fill_opacity=1, stroke_color=RED),
            TextMobject("t", color=RED, background_stroke_width=0).scale(0.75)
        ).move_to(np.array([4.5, -1.5, 0]))
        t.add(Arrow(nodes[-1].get_center(), t.get_center(), color=RED, buff=0.25))
        t.add(TextMobject("inf", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.6).next_to(t[-1], UR, buff=-0.5))
        t.add(TextMobject("0", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.6).next_to(t[-2], DL, buff=-0.5))

        braces = VGroup(
            Brace(VGroup(Dot(nodes[0].get_center(), radius=0.01), Dot(nodes[2].get_center(), radius=0.01)), UP, color=GRAY, buff=0.52),
            Brace(VGroup(Dot(nodes[2].get_center(), radius=0.01), Dot(nodes[5].get_center(), radius=0.01)), UP, color=GRAY, buff=0.52),
            Brace(VGroup(Dot(nodes[1].get_center(), radius=0.01), Dot(nodes[3].get_center(), radius=0.01)), DOWN, color=GRAY, buff=0.52),
            Brace(VGroup(Dot(nodes[4].get_center(), radius=0.01), Dot(nodes[6].get_center(), radius=0.01)), DOWN, color=GRAY, buff=0.52),
        )
        edges2 = VGroup(
            CurvedArrow(nodes[0].get_center(), nodes[2].get_center(), buff=0.25, color=BLACK, angle=-TAU / 4).shift(UP*1),
            CurvedArrow(nodes[2].get_center(), nodes[5].get_center(), buff=0.25, color=BLACK, angle=-TAU / 4).shift(UP*1),
            CurvedArrow(nodes[1].get_center(), nodes[3].get_center(), buff=0.25, color=BLACK, angle= TAU / 4).shift(DOWN*1),
            CurvedArrow(nodes[4].get_center(), nodes[6].get_center(), buff=0.25, color=BLACK, angle= TAU / 4).shift(DOWN*1),
        )
        caps2 = VGroup(
            TextMobject("1", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.6).next_to(edges2[0], UP, buff=0.1),
            TextMobject("1", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.6).next_to(edges2[1], UP, buff=0.1),
            TextMobject("1", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.6).next_to(edges2[2], UP, buff=-0.4),
            TextMobject("1", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.6).next_to(edges2[3], UP, buff=-0.4)
        )
        costs2 = VGroup(
            TextMobject("6", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.6).next_to(edges2[0], DOWN, buff=-0.4),
            TextMobject("3", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.6).next_to(edges2[1], DOWN, buff=-0.6),
            TextMobject("2", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.6).next_to(edges2[2], DOWN, buff=0.1),
            TextMobject("4", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.6).next_to(edges2[3], DOWN, buff=0.1),
        )
        old_num = VGroup(
            TextMobject("1", color=GRAY, background_stroke_color=GRAY).scale(0.45),
            TextMobject("6", color=GRAY, background_stroke_color=GRAY).scale(0.45),
            TextMobject("7", color=GRAY, background_stroke_color=GRAY).scale(0.45),
            TextMobject("8", color=GRAY, background_stroke_color=GRAY).scale(0.45),
            TextMobject("9", color=GRAY, background_stroke_color=GRAY).scale(0.45),
            TextMobject("10", color=GRAY, background_stroke_color=GRAY).scale(0.45),
            TextMobject("13", color=GRAY, background_stroke_color=GRAY).scale(0.45),
        )
        for i in range(7):
            old_num[i].next_to(nodes[i], DOWN, buff=0.08)
        comments = VGroup(
            TextMobject("蓝-容量", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.7),
            TextMobject("橙-费用", color=GOLD_D, background_stroke_color=GOLD_D).scale(0.7),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).next_to(nodes[0], DOWN, buff=1.3)
        rec = SurroundingRectangle(comments, color=GRAY, buff=0.2)
        problem = TextMobject("最长$k$可重区间集问题", color=WHITE, background_stroke_color=WHITE)
        problem.add_background_rectangle(color=GOLD_D, opacity=1, buff=0.15).next_to(nodes[0], UP, buff=1.8).shift(RIGHT*0.2)
        author = TextMobject("by @鹤翔万里", background_stroke_color=ORANGE, opacity=0.8).scale(0.7).set_color(ORANGE).next_to(t[0], DOWN, buff=0.4).shift(LEFT*0.8)

        self.add(line, nodes, names, s, edges, infs, costs, t, braces, edges2, caps2, costs2, old_num, comments, rec, problem, author)


class NF24P2762(Scene_):
    def construct(self):
        rad = 0.3
        s = VGroup(
            Circle(radius=rad, fill_color=WHITE, fill_opacity=1, stroke_color=RED),
            TextMobject("s", color=RED, background_stroke_width=0).scale(0.75)
        ).move_to(np.array([-4.5, 0, 0]))
        t = VGroup(
            Circle(radius=rad, fill_color=WHITE, fill_opacity=1, stroke_color=RED),
            TextMobject("t", color=RED, background_stroke_width=0).scale(0.75)
        ).move_to(np.array([4.5, 0, 0]))
        nodes = VGroup(
            VGroup(
                Circle(radius=rad, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK).shift(LEFT*0.4).set_opacity(0),
                RoundedRectangle(height=rad*2, width=1.4, corner_radius=rad, color=BLACK),
                TextMobject("1\ 实验", color=BLACK, background_stroke_color=BLACK).scale(0.75),
                Circle(radius=rad, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK).shift(RIGHT*0.4).set_opacity(0)
            ).move_to(np.array([-1.6, 1, 0])),
            VGroup(
                Circle(radius=rad, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK).shift(LEFT*0.4).set_opacity(0),
                RoundedRectangle(height=rad*2, width=1.4, corner_radius=rad, color=BLACK),
                TextMobject("2\ 实验", color=BLACK, background_stroke_color=BLACK).scale(0.75),
                Circle(radius=rad, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK).shift(RIGHT*0.4).set_opacity(0)
            ).move_to(np.array([-1.6, -1, 0])),
            VGroup(
                Circle(radius=rad, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK).shift(LEFT*0.4).set_opacity(0),
                RoundedRectangle(height=rad*2, width=1.4, corner_radius=rad, color=BLACK, fill_opacity=1),
                TextMobject("1\ 仪器", color=WHITE, background_stroke_color=WHITE).scale(0.75),
                Circle(radius=rad, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK).shift(RIGHT*0.4).set_opacity(0)
            ).move_to(np.array([1.5, 2, 0])),
            VGroup(
                Circle(radius=rad, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK).shift(LEFT*0.4).set_opacity(0),
                RoundedRectangle(height=rad*2, width=1.4, corner_radius=rad, color=BLACK, fill_opacity=1),
                TextMobject("2\ 仪器", color=WHITE, background_stroke_color=WHITE).scale(0.75),
                Circle(radius=rad, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK).shift(RIGHT*0.4).set_opacity(0)
            ).move_to(np.array([1.5, 0, 0])),
            VGroup(
                Circle(radius=rad, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK).shift(LEFT*0.4).set_opacity(0),
                RoundedRectangle(height=rad*2, width=1.4, corner_radius=rad, color=BLACK, fill_opacity=1),
                TextMobject("3\ 仪器", color=WHITE, background_stroke_color=WHITE).scale(0.75),
                Circle(radius=rad, fill_color=WHITE, fill_opacity=1, stroke_color=BLACK).shift(RIGHT*0.4).set_opacity(0)
            ).move_to(np.array([1.5, -2, 0])),
        )
        edges_s = VGroup(
            Arrow(s[0].get_center(), nodes[0][0].get_center(), color=RED, buff=rad),
            Arrow(s[0].get_center(), nodes[1][0].get_center(), color=RED, buff=rad),
        )
        edges_s.add(TextMobject("10", color=BLUE_D, background_stroke_color=BLUE_D).next_to(edges_s[0], UP, buff=-0.3).shift(LEFT*0.3))
        edges_s.add(TextMobject("25", color=BLUE_D, background_stroke_color=BLUE_D).next_to(edges_s[1], DOWN, buff=-0.3).shift(LEFT*0.3))
        edges_n = VGroup(
            Arrow(nodes[0][-1].get_center(), nodes[2][0].get_center(), color=BLACK, buff=rad),
            Arrow(nodes[0][-1].get_center(), nodes[3][0].get_center(), color=BLACK, buff=rad),
            Arrow(nodes[1][-1].get_center(), nodes[3][0].get_center(), color=BLACK, buff=rad),
            Arrow(nodes[1][-1].get_center(), nodes[4][0].get_center(), color=BLACK, buff=rad),
        )
        edges_n.add(TextMobject("inf", color=BLUE_D, background_stroke_color=BLUE_D).next_to(edges_n[0], UP, buff=-0.35).shift(LEFT*0.3))
        edges_n.add(TextMobject("inf", color=BLUE_D, background_stroke_color=BLUE_D).next_to(edges_n[1], UP, buff=-0.25).shift(LEFT*-0.1))
        edges_n.add(TextMobject("inf", color=BLUE_D, background_stroke_color=BLUE_D).next_to(edges_n[2], UP, buff=-0.35).shift(LEFT*0.3))
        edges_n.add(TextMobject("inf", color=BLUE_D, background_stroke_color=BLUE_D).next_to(edges_n[3], UP, buff=-0.25).shift(LEFT*-0.1))
        edges_t = VGroup(
            Arrow(nodes[2][-1].get_center(), t[0].get_center(), color=RED, buff=rad),
            Arrow(nodes[3][-1].get_center(), t[0].get_center(), color=RED, buff=rad),
            Arrow(nodes[4][-1].get_center(), t[0].get_center(), color=RED, buff=rad),
        )
        edges_t.add(TextMobject("5", color=BLUE_D, background_stroke_color=BLUE_D).next_to(edges_t[0], UP, buff=-0.5).shift(LEFT*0.15))
        edges_t.add(TextMobject("6", color=BLUE_D, background_stroke_color=BLUE_D).next_to(edges_t[1], UP, buff=-0.1).shift(LEFT*0.2))
        edges_t.add(TextMobject("7", color=BLUE_D, background_stroke_color=BLUE_D).next_to(edges_t[2], DOWN, buff=-0.5).shift(LEFT*0.15))
        min_cut = DashedLine(np.array([2.5, 3, 0]), np.array([2.5, -3, 0]), color=DARK_GRAY)
        comment = VGroup(
            TextMobject("蓝-容量", color=BLUE_D, background_stroke_color=BLUE_D).scale(0.7),
            TextMobject("灰-最小割(最大流)", color=DARK_GRAY, background_stroke_color=DARK_GRAY).scale(0.7)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(edges_s[3], DOWN, buff=0.8)
        rec = SurroundingRectangle(comment, color=GRAY, buff=0.2)
        problem = TextMobject("太空飞行计划问题", color=WHITE, background_stroke_color=WHITE)
        problem.add_background_rectangle(color=GOLD_D, opacity=1, buff=0.15).next_to(edges_s[2], UP, buff=1)
        author = TextMobject("by @鹤翔万里", background_stroke_color=ORANGE, opacity=0.8).scale(0.7).set_color(ORANGE).next_to(t[0], DOWN, buff=2)
        label = VGroup(
            TextMobject("报酬", color=GREEN, background_stroke_color=GREEN).scale(0.6).next_to(edges_s[2], UL, buff=0.1),
            TextMobject("费用", color=GREEN, background_stroke_color=GREEN).scale(0.6).next_to(edges_t[3], UR, buff=0.1),
        )

        self.add(s, t, edges_s, edges_n, edges_t, nodes, min_cut, comment, rec, problem, author, label)


class NF24P3357(Scene_):
    def construct(self):
        axes = Axes(x_min=-0.5, x_max=8, y_min=-0.5, y_max=4, number_line_config={"color": BLACK}).center().shift(DOWN*0.5)
        axes.add_coordinates(number_config={"color": BLACK})
        line1  = Line(axes.c2p(1, 1), axes.c2p(1, 3), color=BLUE_D)
        line1_ = Line(axes.c2p(2, 1), axes.c2p(3, 3), color=BLUE_D)
        line2  = Line(axes.c2p(1, 1), axes.c2p(3, 3), color=GREEN_D)
        line2_ = Line(axes.c2p(3, 1), axes.c2p(6, 3), color=GREEN_D)
        dots = VGroup(
            SmallDot(axes.c2p(1, 1), color=GRAY),
            SmallDot(axes.c2p(1, 3), color=GRAY),
            SmallDot(axes.c2p(2, 1), color=GRAY),
            SmallDot(axes.c2p(3, 3), color=GRAY),
            SmallDot(axes.c2p(3, 1), color=GRAY),
            SmallDot(axes.c2p(6, 3), color=GRAY),
        )
        arrows = VGroup(
            CurvedArrow(line1.get_center(), line1_.get_center(), color=RED, angle=-TAU/4).scale(0.9),
            CurvedArrow(line2.get_center(), line2_.get_center(), color=RED).scale(0.9).shift(DL*0.2+LEFT*0.1),
        )
        changes = VGroup(
            TexMobject("(x_1,x_1)\\rightarrow(2x_1, 2x_1+1)", color=MAROON, background_stroke_color=MAROON).scale(0.85),
            TexMobject("(x_1,x_2)\\rightarrow(2x_1+1, 2x_2)", color=MAROON, background_stroke_color=MAROON).scale(0.85)
        ).arrange(DOWN, aligned_edge=LEFT).next_to(axes, UP, buff=-0.5)
        dls = VGroup(
            DashedLine(axes.c2p(2, 0), axes.c2p(2, 1), color=PURPLE),
            DashedLine(axes.c2p(3, 0), axes.c2p(3, 3), color=PURPLE),
            DashedLine(axes.c2p(6, 0), axes.c2p(6, 3), color=PURPLE),
        )
        braces = VGroup(
            Brace(VGroup(Dot(axes.c2p(2, 0), radius=0.01), Dot(axes.c2p(3, 0), radius=0.01)), UP, color=DARK_GRAY),
            Brace(VGroup(Dot(axes.c2p(3, 0), radius=0.01), Dot(axes.c2p(6, 0), radius=0.01)), UP, color=DARK_GRAY),
        )
        problem = TextMobject("最长$k$可重线段集问题", color=WHITE, background_stroke_color=WHITE)
        problem.add_background_rectangle(color=GOLD_D, opacity=1, buff=0.15).move_to(np.array([-3, 3, 0]))
        author = TextMobject("by @鹤翔万里", background_stroke_color=ORANGE, opacity=0.8).scale(0.7).set_color(ORANGE)
        author.move_to(np.array([4, -1.5, 0]))
        comment = TextMobject("化为开区间", color=DARK_GRAY, background_stroke_color=DARK_GRAY).scale(0.6).next_to(braces[-1], UP, buff=0.2)
        dots2 = VGroup(
            Dot(axes.c2p(2, 0), color=BLACK, radius=0.1),
            Dot(axes.c2p(3, 0), color=BLACK, radius=0.1),
            Dot(axes.c2p(6, 0), color=BLACK, radius=0.1),
        )

        self.add(axes, line1, line1_, line2, line2_, dls, dots, arrows, changes, braces, problem, author, comment, dots2)
