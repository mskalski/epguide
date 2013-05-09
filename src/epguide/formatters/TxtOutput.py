# -*- coding: utf-8 -*-
import sys, textwrap

class TxtOutput(object):
    """
    klasa wyjscia w formacie tekstowym
    """

    def __init__(self):
        self.file = None

    def Init(self, file):
        self.file = file
    
    def Finish(self):
        pass

    def SaveChannelList(self, channel_list):
        """
        zapisanie listy kanalow
        """
        for channel in channel_list:
            self.file.write("%s - %s\n" % (channel.id, channel.name.encode('utf8')))

    def SaveGuide(self, day, guide):
        """
        zapisanie programu
        """
        if len(guide) == 0:
            self.file.write("Brak programu dla tego dnia")
            return
        
        self.file.write("\nProgram %s na dzien: %s\n" % (guide[0].channel_name.encode('utf8'), day.strftime("%Y-%m-%d")))
        self.file.write("--------------------------------------------\n\n")
        for item in guide:
            self.file.write(" %s %s   %s\n" % (item.time_start.strftime("%H:%M"), item.time_end and item.time_end.strftime("%H:%M") or '',
                item.title.encode('utf8')))
            self.file.write(textwrap.fill (item.desc.encode('utf8'), 79, initial_indent=13*" ", subsequent_indent=13*" ") + "\n")

    def SaveGuideChannels(self):
        pass