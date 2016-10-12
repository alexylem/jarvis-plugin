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

def convert_power_updown(light, power_level, power_updown):
    if power_updown == None:
        return power_level
    percent = light.get_color()[2] * 100 / 65535
    if power_updown == True:
        percent = percent + 10 if power_level == None else percent + power_level
    if power_updown == False:
        percent = percent - 10 if power_level == None else percent - power_level
    #Check
    if percent > 100:
        percent = 100
    if percent < 0:
        percent = 0
    return percent

def command(light, color, power_level):
    if color is not None and power_level is not None:
        color = set_power(color, power_level)
    if light is not None:
        if color is None and power_level is not None: #Changement de power
            color = set_power(light.get_color(), power_level)
        elif color is not None and power_level is None: #Changement de couleur mais pas de power
            color = set_power(color, light.get_color()[2])
        elif color is None and power_level is None: #Changement de power a 100
            color = set_power(None, 100, power_updown)
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
    up_down = ""
    if "power_up" in rules:
        up_down = "+"
    elif "power_down" in rules:
        up_down = "-"
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
            says += " avec une intensite de %s%s pourcents" % (up_down, rules["power"])
    elif up_down != "":
        says += " en changeant l'intensite de %s10" % up_down
    NEED_SAY = says
    return color

def parse_arg(lan, args, lights):
    light = None
    color = None
    power_level = None
    power_updown = None
    rules = {"info" : False}
    for i, arg in enumerate(args):
        if arg == "up_lights":
            power_updown = True
            rules["power_up"] = True
        elif arg == "down_lights":
            power_updown = False
            rules["power_down"] = True
        elif i + 1 < len(args) and (arg + " " + args[i + 1]).lower() in lights:
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
    return light, color, power_level, power_updown

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
        light, color, power_level, power_updown = parse_arg(lan, sys.argv, lights)
        if light is not None:
            command(light, color, convert_power_updown(light, power_level, power_updown))
        else:
            for light_name in lights:
                command(lights[light_name], color, convert_power_updown(lights[light_name], power_level, power_updown))
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
            
