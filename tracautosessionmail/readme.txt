= TracAutoSessionMailPlugin =

== description ==
 * support validate anonymous to input valid email address
 * support required fields
 * support match fields to regular expression

= Install =
 You can install this software as normal Trac plugin.

 1. Uninstall TracAutoSessionMailPlugin if you have installed before.

 2. Change to the directory containning setup.py.

 3. If you want to install this plugin globally, that will install this plugin to the python path:
  * python setup.py install

 4. If you want to install this plugin to trac instance only:
  * python setup.py bdist_egg
  * copy the generated egg file to the trac instance's plugin directory
  {{{
cp dist/*.egg /srv/trac/env/plugins
}}}

 5. Config trac.ini:
  {{{
[components]
tractracautosessionmail.* = enabled
}}}

 6. If you are installing this plugin first time, you can copy description.tmpl to your/trac/environment/templates to utilize some default ticket templates.
