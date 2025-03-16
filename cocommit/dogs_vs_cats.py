import click
import random

def generate_ascii_pet():
    """
    Generates and returns ASCII art of either a cat or a dog with 50/50 probability.
    Each ASCII art is up to seven lines tall.
    """
    # Decide whether to generate a cat or dog (50/50 chance)
    is_cat = random.random() < 0.5
    
    # Cat ASCII art options
    cats = [
        # Cat option 1
        """|\\---/|
| o_o |
 \\_^_/""",
        
        # Cat option 2
        """  /\\_/\\
 ( o.o )
 > ^ <""",
        
        # Cat option 3
        """  /\\_/\\  
 ( ^.^ ) 
  > - < 
 (__|__)""",
        
        # Cat option 4
        """ /\\_/\\
( o.o )
(> ^ <)
 ^ ^ ^""",
        
        # Cat option 5
        """    /\\___/\\
   /       \\
  |  #    # |
  \\     ᵥ   /
   \\   ᵕ   /
    \\     /
     -----"""
    ]
    
    # Dog ASCII art options
    dogs = [
        # Dog option 1
        """  __      _
o'')}____//
 `_/      )
 (_(_/-(_/""",
        
        # Dog option 2
        """  / \\__
 (    @\\___
 /         O
/   (_____/
/_____/   U""",
        
        # Dog option 3
        """ / \\     / \\
(  o )---( o  )
 \\ /     \\ /
  "       "
  ^       ^""",
        
        # Dog option 4
        """  / \\_______
 /          \\
/|  ಠ     ಠ  |\\
U |    ω     | U
  |           |
  \\   -----   /""",
        
        # Dog option 5
        """     / \\__
    (    @\\___
   /         O
  /   (_____/
 /_____/   U"""
    ]
    
    
    if is_cat:
        click.echo(random.choice(cats))
    else:
        click.echo(random.choice(dogs))
