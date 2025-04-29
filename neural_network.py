from manim import *


class NeuralNetwork(Scene):
    def construct(self):
        layers = [3, 5, 4, 2]
        layer_mobs = []

        for i, num_neurons in enumerate(layers):
            layer = VGroup(*[
                Circle(radius=0.2, color=BLUE).shift(DOWN * (j - (num_neurons-1)/2))
                for j in range(num_neurons)
            ])
            layer.shift(RIGHT * i * 2)
            layer_mobs.append(layer)

        for layer in layer_mobs:
            self.play(FadeIn(layer))

        for i in range(len(layer_mobs) - 1):
            for neuron1 in layer_mobs[i]:
                for neuron2 in layer_mobs[i+1]:
                    line = Line(neuron1.get_center(), neuron2.get_center(), stroke_width=1)
                    self.add(line)

        self.wait(2)
