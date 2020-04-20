from PublicandPrivateClasses import NotPrivate

test=NotPrivate("Tim")

#if dont want to import:
#test=PublicandPrivateClasses.NotPrivate("Tim")

test.display()
test._display() #even private function works