import re
from typing import Union
from typing import Literal

lighting_category = Literal["Downlights",
                           "Track Lights",
                           "Linears"
                           ]

component_category = Literal["Track Systems",
                            "LED Drivers",
                            "Decorative Aluminum",
                            "LED COBs"]

control_category = Literal["Control Panels",
                          "Dimmer Units",
                          "Dimming Software",
                          "Relay Units",
                          "Routers",
                          "Sensors"]

brand_name = Literal["Luxtron",
                     "Helvar",
                     "A.A.G. Stucchi",
                     "EUTRAC",
                     "Citizen",
                     "ElectroTerminal"]

all_categories = Union[lighting_category, component_category, control_category]

class BaseProduct:
    def __init__(self, name:str, 
                 description:str,
                 brand:brand_name,
                 category:all_categories, 
                 slug:str):
        self.name = name
        self.description = description
        self.category = category
        self.slug = derive_slug(self.name)

class LightingProduct(BaseProduct):
    def __init__(self, 
                 name:str, 
                 description:str,
                 brand,
                 category:lighting_category, 
                 slug:str, 
                 wattage:float, 
                 lumens:float,
                 beam_angles:str,
                 dimension:str):
        if category not in lighting_category.__args__:
            raise ValueError(f"Invalid lighting category: {category}.")
        super().__init__(name, description, category, slug)
        self.wattage = wattage
        self.lumens = lumens
        self.beam_angles = beam_angles
        self.dimensions = dimension

class ComponentProduct(BaseProduct):
    def __init__(self, 
                 name, 
                 description, 
                 brand,
                 category,
                 slug, 
                 material, 
                 dimensions):
        if category not in component_category.__args__:
            raise ValueError(f"Invalid lighting category: {category}.")
        super().__init__(name, description, category, slug)
        self.material = material
        self.dimensions = dimensions

class ControlProduct(BaseProduct):
    def __init__(self, 
                 name, 
                 description, 
                 brand,
                 category, 
                 slug, 
                 control_type, 
                 compatibility):
        if category not in control_category.__args__:
            raise ValueError(f"Invalid lighting category: {category}.")
        super().__init__(name, description, category, slug)
        self.control_type = control_type
        self.compatibility = compatibility


def derive_slug(name:str)->str:
    parts = name.split()
    slug = ('-'.join(parts[0:2])).lower()
    return re.sub(r'[^a-z0-9-]', '', slug)
