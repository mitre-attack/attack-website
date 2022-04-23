from string import Template

module_name = "tour"
priority = 15

js_tour_settings = Template("var tour_steps = ${tour_steps};\n")
