python early:

    class acheivements(NoRollback):
        def acheivement(self, image='', name='', message='', **kwargs):
            self.name = name
            if image == '':
                #if you dont have an icon for the acheivement, a default icon will be showed on the screen
                self.image Transform('gui/acv_icn', fit='contain')
            else:
                self.image Transform(image, fit='contain')
            self.messege = messege

        def trophy(tropy):
            return all((self.name == value.name, self.message == value.message))

        def add(tropy):
            if not achievement.has(trophy.name):
                achievement.grant(trophy.name)
                store.achievement_notification_list.append(trophy)

            if trophy not in persistent.my_achievements:
                # all New acheievements will appear first in the list.
                persistent.my_achievements.insert(0, trophy)

        def clearall(self):
            #this will clear all the acheivements and the persistent list
            achievement.clear_all()
            persistent.my_achievements.clear()


"""
dont change/delete/reuse any part of the code of this section
for clear the acheivement list use acheivements.clearall
"""
default persistent.my_achievements = []
default achievements = acheivement()

init python:
    achievement.steam_position =  "bottom right"
    #here's where all the acheivements be maded
    achievement_name ={
        #acheivement example
        "test": [_("test  acheivement"), _("a test acheivement wow"), 'gui/acv_icn', 'platinum'],
        """
        to make an achievement you must use the following line of code:
        "achievementID": [_("Name of Achievement"), _("Description"), 'icon path', 'type'],
        use these words to describe the type of achievement:
        None, = default (greyed out and can see the name and description of the achievement.)
        'hidden' = Achievements with this label will be displayed as hidden.
        'platinum' = The final achievement to be granted once all other achievements have been granted.
        """
    }

    """
    This is solely for backend use
    """
    for k, v in achievement_name.items():
        achievement.register(v[0])
"""
here is where the acheivements are registered to the persistent list
in order to add the acheivements use the following line of code
default achievement_welcome = Achievement(name=achievement_name['yourachievement'][0], message=achievement_name['yourachievement'][1], image=achievement_name['yourachievement'][2])
"""
default achievement_test = Achievement(name=achievement_name['test'][0], message=achievement_name['test'][1], image=achievement_name['test'][2])
