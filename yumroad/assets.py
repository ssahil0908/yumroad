from flask_assets import Bundle

common_css = Bundle(
    'https://stackpath.bootstrapcdn.com/bootswatch/4.3.1/litera/bootstrap.css',
    'css/basic.css',
    filters='cssmin',
    output='public/css/basic.css'
)

landing_css = Bundle(
    'css/landing.css',
    filters='cssmin',
    output='public/css/landing.css'
)

common_js = Bundle(
    'js/common.js',
    filters='jsmin',
    output='public/js/common.js'
)