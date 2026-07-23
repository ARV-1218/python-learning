from main import game



class character(game):
    def __init__(self, name):
        super().__init__(name)

char_attributes =[
    {
        "Name":'Wizard',
        "HP":150,
        "AR":30
    },
    {
        "Name":'Archer',
        "HP":100,
        "AR":60, 
    }, 
    {
        "Name":'Warrior',
        "HP":200,
        "AR":25
    }
]


a = char_attributes[0]["HP"] if char_attributes[0]["Name"] == "Wizard" else None
print(a)


char = character(char_attributes)
