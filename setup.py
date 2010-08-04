from setuptools import find_packages, setup

setup(
    name = 'TracAutoSessionMail',
    version = '0.1',
    packages = ['tracautosessionmail'],
    package_data = { 'tracautosessionmail': [ '*.txt' ] },

    author = "Marko Mikulicic",
    author_email = 'marko.mikulicic@isti.cnr.it',
    maintainer = 'Marko Mikulicic',
    maintainer_email = "marko.mikulicic@isti.cnr.it",
    description = "Automatic email into session after ticket creation for anonymous users.",
    license = "BSD",
    keywords = "automatic email session",
    url = "http://trac-hacks.org/wiki/TracAutoSessionMail",
    classifiers = [
        'Framework :: Trac',
    ],
    
    install_requires = [],
    entry_points = {'trac.plugins': ['tractracautosessionmail = tracautosessionmail.tracautosessionmail']},
)
