def convert_temperature(temp, from_scale, to_scale):
    if from_scale == "Celsius":
        newtemp = (temp * 1.8) + 32
        return newtemp
    else:
        newtemp = (temp - 32) / 1.8
        return newtemp

convert_temperature(0, "Celsius", "Fahrenheit")
convert_temperature(32, "Fahrenheit", "Celsius")

