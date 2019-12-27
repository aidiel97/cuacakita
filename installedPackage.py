import pip
install = pip.get_installed_distributions()
insP= sorted(["%s==%s" % (i.key, i.version) for i in install])
print(insP)