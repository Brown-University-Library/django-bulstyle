BULSTYLE SCSS Source Files
==========================

These are the scss source files to buils the bulstyle-base.css 
and bulstyle-blacklight.css files.

You will need some sort of sass comiler.

`pip install libsass` will install libsass along with python bindings.

To build these files you will also need to link to the sass directories for
bootstrap and blacklight.

git clone https://github.com/twbs/bootstrap-sass wherever you want and symlink
to the stylesheets

Ex: `ln -s bootstrap-sass/assets/stylesheets/ bootstrap`

git clone https://github.com/projectblacklight/blacklight to wherever you want
and symlink to the stylesheets

Ex: `ln -s blacklight/app/assets/stylesheets/blacklight blacklight`


Then you can edit and run

`sassc bulstyle.scss ../css/bylstyle.css`

and

`sassc bulstyle-blacklight.scss ../css/bylstyle-blacklight.css`

