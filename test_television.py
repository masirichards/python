from television import Television


##=====Default Values=====
def test_init():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


##=====Power=====
def test_power():
    tv = Television()

    ## Turn TV on
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    ## Turn TV off
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"


##=====Mute=====
def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()

    ## Mute TV
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

    ## Unmute TV
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    ## Try muting while off
    tv.power()
    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"

    tv.mute()
    assert str(tv) == "Power = False, Channel = 0, Volume = 1"


##=====Channels=====
def test_channel_up():
    tv = Television()

    ## TV is off
    tv.channel_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0"

    ## Go past max channel
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"


def test_channel_down():
    tv = Television()

    ## TV is off
    tv.channel_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    # Go below min channel
    tv.power()
    tv.channel_down()
    assert str(tv) == "Power = True, Channel = 3, Volume = 0"


##=====VOLUME=====
def test_volume_up():
    tv = Television()

    ## TV is off
    tv.volume_up()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    ## Increase volume while muted
    tv.mute()
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"

    ## Go past max volume
    tv.volume_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 2"


def test_volume_down():
    tv = Television()

    ## TV is off
    tv.volume_down()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

    tv.power()
    tv.volume_up()
    tv.volume_up()

    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    ## Decrease volume while muted
    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

    ## Go below min volume
    tv.volume_down()
    tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"