"""
Declare characters used by this game. The color argument colorizes the name of the character.
pick between one of the two and add an # to the other to keep it

sound intervals:

regular taps, medium intervals
define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg']

light taps, smaller intervals
define sounds = ['audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

both combined
define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg', 'audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']
"""
define sounds = ['audio/A1.ogg', 'audio/A2.ogg', 'audio/A3.ogg', 'audio/A4.ogg', 'audio/A5.ogg', 'audio/B1.ogg', 'audio/B2.ogg', 'audio/B3.ogg', 'audio/B4.ogg', 'audio/B5.ogg']

init python:
    def type_sound(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show": #if text's being written by character, spam typing sounds until the text ends
            renpy.sound.play(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))
            renpy.sound.queue(renpy.random.choice(sounds))



        elif event == "slow_done" or event == "end":
            renpy.sound.stop()

"""
here is where the game starts
"""
define l = Character("Lime-chan", callback=type_sound)

label start:
    play music "audio/3. Funk Pump.wav"
    l "welcome to the Ren'py Visual Novel Base Engine"
    l "A Framework with several mechanics already implemented so you can focus on creating your novel, leaving aside the boring programming."
    l "here are some mechanics"
    menu Mechanics:
                "Acheivement System":
                    jump Acheivements

                "Text Effects":
                    jump TxtEff

                "Skip":
                    jump Skip
    label Acheivements:
        menu try_achievement:
                "Grant: Welcome Achievement":
                    if achievement.has(achievement_name['welcome'][0]):
                        l "You already have this."
                        jump try_achievement
                    else:
                        $ Achievement.add(achievement_welcome)
                        jump try_achievement

                "Grant: Secret Achievement":
                    if achievement.has(achievement_name['secret'][0]):
                        l "You already have this."
                        jump try_achievement
                    else:
                        $ Achievement.add(achievement_secret)
                        jump try_achievement

                "Clear Achievements":
                    $ achievements.purge()
                    l "Achievements cleared."
                    jump try_achievement

                "return":
                    jump Mechanics
    label TxtEff:
        "here are some Text effects"
        "{sc}Shake it{/sc}"
        "{rotat}wooah{/rotat}"
        "{explode}BOOM{/explode}"
        "{explodehalf=2-2.0}BOOM{/explodehalf}"
        "{glitch=80}{b}GLITCH{/glitch}"
        "{bt=10}woaaaaah{/bt}"
        "{move}{b}Move This{/move}"
        "{glitch=80}{sc}{b}combined{/sc}{/glitch}"
        jump Mechanics

    label Skip:
        pass


    l "Well, that's all."
    l "I hope you enjoyed this quick demo."
    return
