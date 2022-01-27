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
            pass
}