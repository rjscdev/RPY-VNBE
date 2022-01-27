python early
{
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
default
default