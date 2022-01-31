# RPY-VNBE💻✒
Ren'py VisualNovel Base Engine is a framework📦 to create visual novels **more easily**, leaving aside the tedious programming, being able to focus on the story and art of it. 

the framework has the following mechanics:

- [x] Acheivement System
- [x] Text Sounds
- [x] Text Effects
- [ ] Chat phone System

## how to use the systems📦⚙:

### Acheivement System🏆⭐:

#### how to create a new achievement:
```
"achvslug": [_("achv_name"), _("description"), 'gui/your file name', Type]

```
#### how to add the acheivement to the persistent list
add this code in the persistent list part of acheivements.rpy
```
default achievement_welcome = Achievement(name=achievement_name['achvslug'][0], message=achievement_name['achvslug'][1], image=achievement_name['achvslug'][2])
```

to display the achievements in during the game, use the following line of code in the script.rpy
```
$ Achievement.add(achievement_achvslug)

example: 

label start:

    character "welcome to the Ren'py Visual Novel Base Engine"
    $ Achievement.add(achievement_achvslug)
```

for clear the acheivements use 
```
$ Acheivement.purge

```
### Text Effects ✨:
place these tags inside the text you wish to place
```
tags:
        "{sc}{/sc}"
        "{rotat}{/rotat}"
        "{explode}{/explode}"
        "{explodehalf=amount}{/explodehalf}"
        "{glitch=Glitch amount}{/glitch}"
        "{bt=10}{/bt}"
        "{move}{/move}"
```
you can also combine tags:
```
example:
"{glitch=80}{sc}{b}combined{/sc}{/glitch}"
```