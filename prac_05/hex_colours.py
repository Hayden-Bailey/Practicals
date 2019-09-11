"""
CP1404/CP5632 Practical
Hex Colour names in a dictionary
"""

HEX_COLOURS = {"DarkKhaki": "#bdb76b", "firebrick4": "#8b1a1a", "DodgerBlue1": "#1e90ff", "goldenrod4": "#8b6914",
               "DarkViolet": "#9400d3", "cyan1": "#00ffff", "coral2": "#ee6a50", "chartreuse4": "#458b00",
               "chocolate": "#d2691e", "aquamarine2": "#76eec6"}

for key, value in HEX_COLOURS.items():
    print("{:15} is {}".format(key, value))

colour = input("Enter colour name: ")
while colour != "":
    if colour in HEX_COLOURS:
        print(colour, "is", HEX_COLOURS[colour])
    else:
        print("Invalid colour name.")
    colour = input("Enter colour name: ")
