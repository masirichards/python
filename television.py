class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Sets the default values of the TV."""
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    ##=====Power=====
    def power(self) -> None:
        """Turns the TV on or off."""
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    ##=====Mute=====
    def mute(self) -> None:
        """Mutes or unmutes the TV."""
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    ##=====Channels=====
    def channel_up(self) -> None:
        """Increases the TV channel."""
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1


    def channel_down(self)-> None:
        """Decrese the TV Volume."""
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1


    ##=====VOLUME=====
    def volume_down(self) -> None:
        """Decreases the TV channel."""
        if self.__status:
            self.__muted = False

            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def volume_up(self) -> None:
        """Increases the TV volume."""
        if self.__status:
            self.__muted = False

            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    ##====String Call / Print=====

    def __str__(self) -> str:
        """
        Returns the TV information.
        :return: Power, channel, and volume.
        """
        if self.__muted:
            volume = self.MIN_VOLUME
        else:
            volume = self.__volume

        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {volume}'