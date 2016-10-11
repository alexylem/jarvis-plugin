from lifxlan import *
import random

NEED_SAY = ""
COLORS_LIST = {
    "rouge" : [65535, 65535, 65535, 3500],
    "orange" : [5525, 65535, 65535, 3500],
    "jaune" : [7000, 65535, 65535, 3500],
    "vert" : [16173, 65535, 65535, 3500],
    "cyan" : [29814, 65535, 65535, 3500],
    "bleu" : [43634, 65535, 65535, 3500],
    "violet" : [50486, 65535, 65535, 3500],
    "rose" : [58275, 65535, 47142, 3500],
    "blanc" : [58275, 0, 65535, 5500],
    "blanc froid" : [58275, 0, 65535, 9000],
    "blanc chaud" : [58275, 0, 65535, 3200],
    "or" : [58275, 0, 65535, 2500],
    "aleatoire" : 1
}

def command(light, color, power_level):
    if color is not None and power_level is not None:
        color = set_power(color, power_level)
    if light is not None:
        if color is None and power_level is not None:
            color = set_power(light.get_color(), power_level)
        elif color is not None and power_level is None:
            color = set_power(color, light.get_power())
        elif color is None and power_level is None:
            color = set_power(None, 100)
        light.set_color(color, duration=0.2, rapid=False)

def set_power(color, power_level):
    if color == None:
        color = [58275, 0, 0, 9000]
    if type(color) is not list:
        color = list(color)
    if power_level <= 100:
        color[2] = 65535 * power_level / 100
    else:
        color[2] = power_level
    return color

def jarvis_say(lan, rules, lights):
    global NEED_SAY
    color = None
    if rules["info"] == True:
        info = "le nom des lumieres sont "
        for name in lights:
            info += name + ", "
        NEED_SAY = info
        return color
    says = "J\'allume la lumiere "
    if "light" in rules:
        says += " de la %s " % rules["light"]
    if "color" in rules:
        if rules["color"] == "aleatoire":
            color = COLORS_LIST.keys()[random.randint(0, len(COLORS_LIST) - 1)]
            says += " avec une couleur aleatoire qui sera %s" % color
            color = COLORS_LIST[color]
        else:
            says += " en %s " % rules["color"]
    if "power" in rules:
        if rules["power"] == "0":
            says = says.replace("J\'allume", "J\'eteint")
            lan.set_power_all_lights("off", rapid=True)
        else:
            lan.set_power_all_lights("on", rapid=True)
            says += " avec une intensite de %s pourcents" % rules["power"]
    NEED_SAY = says
    return color

def parse_arg(lan, args, lights):
    light = None
    color = None
    power_level = None
    rules = {"info" : False}
    for i, arg in enumerate(args):
        if i + 1 < len(args) and (arg + " " + args[i + 1]).lower() in lights:
            light = lights[(arg + " " + args[i + 1]).lower()]
            rules["light"] = (arg + " " + args[i + 1]).lower()
        elif arg.lower() in lights:
            rules["light"] = arg.lower()
            light = lights[arg.lower()]
        elif i + 1 < len(args) and arg + " " + args[i + 1] in COLORS_LIST:
            rules["color"] = arg + " " + args[i + 1]
            color = COLORS_LIST[arg + " " + args[i + 1]]
        elif arg in COLORS_LIST:
            rules["color"] = arg
            color = COLORS_LIST[arg]
        elif arg in ["info", "information"]:
            rules["info"] = True
        else:
            try:
                power_level = int(arg)
                rules["power"] = arg
            except:
                pass
    tmp = jarvis_say(lan, rules, lights)
    if tmp != None:
        color = tmp
    return light, color, power_level

def get_lights(lan):
    lights = {}
    for l in lan.get_lights():
        if l != None:
            if l.get_label() != None:
                lights[l.get_label().lower().replace("_", " ")] = l
            else:
                return get_lights(lan)
    return lights

def run(lan, lights, retry=False):
    global NEED_SAY
    try:
        light, color, power_level = parse_arg(lan, sys.argv, lights)
        if light is not None:
            command(light, color, power_level)    
        else:
            for light_name in lights:
                command(lights[light_name], color, power_level)
    except Exception as e:
        if retry == False:
            run(lan, get_lights(lan), retry=True)
        else:
            NEED_SAY = "Erreur de connectiviter avec une ampoule"

def main():
    lan = LifxLAN(None)
    run(lan, get_lights(lan))
    print(NEED_SAY)

if __name__ == "__main__":
    main()
            
