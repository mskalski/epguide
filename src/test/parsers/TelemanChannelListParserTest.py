from epguide.parsers.teleman import TelemanChannelListParser
import unittest

class  TelemanChannelListParserTest(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        pass

    def tearDown(self):
        pass

    def testChannel(self):
        p = TelemanChannelListParser()
        f = open("stacje.html", "r")
        buf = f.read()
        channels = [str(c) for c in p.get_channels(buf)]
        f.close()
        expected = ["Channel(id:'13th-Street-Universal',name:'13th Street')", "Channel(id:'4fun-TV',name:'4fun TV')", "Channel(id:'ATM-Rozrywka',name:'ATM Rozrywka')", "Channel(id:'AXN',name:'AXN')", "Channel(id:'AXN-Crime',name:'AXN Crime')", "Channel(id:'AXN-SciFi',name:'AXN Sci-Fi')", "Channel(id:'AXN-Spin',name:'AXN Spin')", "Channel(id:'Ale-Kino',name:'ale kino+')", "Channel(id:'Animal-Planet',name:'Animal Planet')", "Channel(id:'Animal-Planet-HD',name:'Animal Planet HD')", "Channel(id:'BBC-Cbeebies',name:'BBC Cbeebies')", "Channel(id:'BBC-Entertainment',name:'BBC Entertain.')", "Channel(id:'BBC-HD',name:'BBC HD')", "Channel(id:'BBC-Knowledge',name:'BBC Knowledge')", "Channel(id:'BBC-Lifestyle',name:'BBC Lifestyle')", "Channel(id:'Boomerang',name:'Boomerang')", "Channel(id:'CBS-Action',name:'CBS Action')", "Channel(id:'CBS-Drama',name:'CBS Drama')", "Channel(id:'CBS-Europa',name:'CBS Europa')", "Channel(id:'CBS-Reality',name:'CBS Reality')", "Channel(id:'CanalPlus',name:'CANAL+')", "Channel(id:'CanalPlus-Film',name:'CANAL+ Film')", "Channel(id:'CanalPlus-Gol',name:'CANAL+ Gol')", "Channel(id:'CanalPlus-Sport',name:'CANAL+ Sport')", "Channel(id:'CanalPlus-Weekend',name:'CANAL+ Weekend')", "Channel(id:'Cartoon-Network',name:'Cartoon Network')", "Channel(id:'Cinemax',name:'Cinemax')", "Channel(id:'Cinemax2',name:'Cinemax 2')", "Channel(id:'Comedy-Central',name:'Comedy Central')", "Channel(id:'Comedy-Central-Family',name:'Comedy Central Fam.')", "Channel(id:'Crime-Investigation-Network',name:'Investigation')", "Channel(id:'Discovery-Channel',name:'Discovery Channel')", "Channel(id:'Discovery-HD-Showcase',name:'Discovery HD Show.')", "Channel(id:'Discovery-Historia',name:'Discovery Historia')", "Channel(id:'Discovery-Science',name:'Discovery Science')", "Channel(id:'Discovery-World',name:'Discovery World')", "Channel(id:'Disney-Channel',name:'Disney Channel')", "Channel(id:'Disney-Junior',name:'Disney Junior')", "Channel(id:'Disney-XD',name:'Disney XD')", "Channel(id:'Domo',name:'Domo+')", "Channel(id:'ESPN-Classic',name:'ESPN')", "Channel(id:'Edusat',name:'Edusat')", "Channel(id:'Eska-TV',name:'Eska TV')", "Channel(id:'Eurosport',name:'Eurosport')", "Channel(id:'Eurosport-2',name:'Eurosport 2')", "Channel(id:'Extreme',name:'Extreme')", "Channel(id:'FOX',name:'FOX')", "Channel(id:'FightKlub',name:'FightKlub')", "Channel(id:'Filmbox',name:'FilmBox')", "Channel(id:'Filmbox-Extra',name:'FilmBox Extra')", "Channel(id:'Filmbox-Family',name:'FilmBox Family')", "Channel(id:'Filmbox-HD',name:'FilmBox HD')", "Channel(id:'Foxlife',name:'Fox Life')", "Channel(id:'HBO',name:'HBO')", "Channel(id:'HBO-Comedy',name:'HBO Comedy')", "Channel(id:'HBO2',name:'HBO 2')", "Channel(id:'History',name:'HISTORY')", "Channel(id:'History-HD',name:'HISTORY HD')", "Channel(id:'ID',name:'ID')", "Channel(id:'Jim-Jam',name:'Jim Jam')", "Channel(id:'Kino-Polska',name:'Kino Polska')", "Channel(id:'Kuchnia-TV',name:'Kuchnia+')", "Channel(id:'MGM-HD',name:'MGM HD')", "Channel(id:'MTV-Polska',name:'MTV Polska')", "Channel(id:'Mezzo',name:'Mezzo')", "Channel(id:'MiniMini',name:'MiniMini+')", "Channel(id:'Nat-Geo-Wild',name:'Nat Geo Wild')", "Channel(id:'National-Geographic',name:'National Geo.')", "Channel(id:'Nickelodeon',name:'Nickelodeon')", "Channel(id:'Nickelodeon-HD',name:'Nickelodeon HD')", "Channel(id:'Orange-Sport',name:'Orange Sport')", "Channel(id:'Planete',name:'PLANETE+')", "Channel(id:'Polonia-1',name:'Polonia 1')", "Channel(id:'Polsat',name:'Polsat')", "Channel(id:'Polsat-2',name:'Polsat 2')", "Channel(id:'Polsat-Cafe',name:'Polsat Cafe')", "Channel(id:'Polsat-Film',name:'Polsat Film')", "Channel(id:'Polsat-News',name:'Polsat News')", "Channel(id:'Polsat-Play',name:'Polsat Play')", "Channel(id:'Polsat-Sport',name:'Polsat Sport')", "Channel(id:'Polsat-Sport-Extra',name:'Polsat Sport Extra')", "Channel(id:'Polsat-Sport-News',name:'Polsat Sport News')", "Channel(id:'Puls',name:'TV Puls')", "Channel(id:'Puls-2',name:'TV Puls 2')", "Channel(id:'Religia-TV',name:'Religia.tv')", "Channel(id:'SciFi-Channel',name:'Sci-Fi Channel')", "Channel(id:'SportKlub',name:'SportKlub')", "Channel(id:'Sundance-Channel-HD',name:'Sundance Channel HD')", "Channel(id:'Superstacja',name:'Superstacja')", "Channel(id:'TCM',name:'TCM')", "Channel(id:'TLC',name:'TLC')", "Channel(id:'TTV',name:'TTV')", "Channel(id:'TV-Trwam',name:'TV Trwam')", "Channel(id:'TV1000',name:'TV 1000')", "Channel(id:'TV4',name:'TV 4')", "Channel(id:'TV5-Monde',name:'TV5MONDE')", "Channel(id:'TV6',name:'TV 6')", "Channel(id:'TVN',name:'TVN')", "Channel(id:'TVN-CNBC',name:'TVN CNBC')", "Channel(id:'TVN-Siedem',name:'TVN 7')", "Channel(id:'TVN-Style',name:'TVN Style')", "Channel(id:'TVN-Turbo',name:'TVN Turbo')", "Channel(id:'TVN24',name:'TVN 24')", "Channel(id:'TVP-1',name:'TVP 1')", "Channel(id:'TVP-2',name:'TVP 2')", "Channel(id:'TVP-HD',name:'TVP HD')", "Channel(id:'TVP-Historia',name:'TVP Historia')", "Channel(id:'TVP-Info',name:'TVP Info')", "Channel(id:'TVP-Kultura',name:'TVP Kultura')", "Channel(id:'TVP-Polonia',name:'TVP Polonia')", "Channel(id:'TVP-Seriale',name:'TVP Seriale')", "Channel(id:'TVP-Sport',name:'TVP Sport')", "Channel(id:'TVS',name:'TVS')", "Channel(id:'Tele-5',name:'Tele 5')", "Channel(id:'Travel-Channel',name:'Travel')", "Channel(id:'Universal-Channel',name:'Universal Channel')", "Channel(id:'VIVA-Polska',name:'VIVA Polska')", "Channel(id:'Viacom-Blink',name:'Viacom Blink')", "Channel(id:'Viasat-Explorer',name:'Viasat Explorer')", "Channel(id:'Viasat-History',name:'Viasat History')", "Channel(id:'Water-Planet',name:'Water Planet')", "Channel(id:'Wojna-i-Pokoj',name:'Wojna i Pok\xc3\xb3j HD')", "Channel(id:'nPremium-HD',name:'nPremium HD')", "Channel(id:'nPremium2-HD',name:'nPremium2 HD')", "Channel(id:'nPremium3-HD',name:'nPremium3 HD')", "Channel(id:'nPremium4-HD',name:'nPremium4 HD')", "Channel(id:'nSport',name:'nSport')", "Channel(id:'teleTOON-plus',name:'teleTOON+')"]
        self.assertEqual(channels, expected)



if __name__ == '__main__':
    unittest.main()

