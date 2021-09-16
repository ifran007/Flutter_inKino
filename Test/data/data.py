from pathlib import Path
import os


class Cryptomaniac(object):
    b = 1


class Watermaniac(object):
    a = 1


class Inkino(object):
    nothing_yet = 1


class Data(object):
    # Apk path
    cryptomaniac = os.path.abspath(Path(__file__).parent.parent / 'apk/Cryptomaniac.apk.apk')
    watermaniac = os.path.abspath(Path(__file__).parent.parent / 'apk/Watermaniac.apk.apk')

    # App package and App activity

    watermaniac_app_package = 'com.rmzsoft.watermaniac'
    watermaniac_app_activity = 'com.rmzsoft.watermaniac.MainActivity'
    cryptomaniac_app_package = 'com.skype.raider'
    cryptomaniac_app_activity = 'com.skype4life.MainActivity'

    # App package and activity for Inkino_Flutter
    inkino_app_package = 'com.roughike.inkino'
    inkino_app_activity = 'com.roughike.inkino.MainActivity'


    # Element properties
    element_id_attribute = 'elementId'
    index_attribute = 'index'
    package_attribute = 'package'
    class_attribute = 'class'
    text_attribute = 'text'
    content_desc_attribute = 'content-desc'
    resource_id_attribute = 'resource-id'
    checkable_attribute = 'checkable'
    checked_attribute = 'checked'
    clickable_attribute = 'clickable'
    enabled_attribute = 'enabled'
    focusable_attribute = 'focusable'
    focused_attribute = 'focused'
    long_clickable_attribute = 'long-clickable'
    password_attribute = 'password'
    scrollable_attribute = 'scrollable'
    selected_attribute = 'selected'
    bounds_attribute = 'bounds'
    displayed_attribute = 'displayed'


    # Timeout
    point_five = 0.5
    one_second = 1
    two_seconds = 2
    three_seconds = 3
    four_seconds = 4
    five_seconds = 5
    six_seconds = 6
    seven_seconds = 7
    eight_seconds = 8
    nine_seconds = 9
    ten_seconds = 10
    fifteen_seconds = 15
    twenty_seconds = 20
    twenty_five_seconds = 25
    thirty_seconds = 30
    thirty_five_seconds = 35
    forty_seconds = 40
    forty_five_seconds = 45
    one_minute = 60
    two_minutes = 120
    three_minutes = 180
    four_minutes = 2400
    five_minutes = 3000
