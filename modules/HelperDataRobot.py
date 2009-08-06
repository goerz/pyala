# The data structure used in this file was converted from the BBClone project
# http://bbclone.de/

import re
import sys

def warn(msg):
    """ print a warning message to stderr """
    sys.stderr.write(str(msg))
    sys.stderr.write("\n")

class RobotIdentifier(object):
    """ Provides identification of robots from the browser string
    """


    robots= [         # TODO: add Zedat robot
        {
            "icon": "robot_1noon.png",
            "title": "1noon",
            "rule" : [
                (re.compile("1Noonbot[/ ]([0-9.]{1,10})", re.I), 1),
                (re.compile("^Yeti$", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "123Spider",
            "rule" : [
                (re.compile("123spider-Bot \(Version: ([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.123spider.de/"
        },
        {
            "icon": "robot_robot.png",
            "title": "192.com",
            "rule" : [
                (re.compile("192.comAgent", re.I), "")
            ],
            "uri": "http://www.192.com/"
        },
        {
            "icon": "robot_2dehands.png",
            "title": "2deHands",
            "rule" : [
                (re.compile("2dehands\.nl", re.I), "")
            ]
        },
        {
            "icon": "robot_a1sitemap.png",
            "title": "A1 Sitemap",
            "rule" : [
                (re.compile("^A1 Sitemap Generator[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("miggibot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.micro-sys.dk/products/sitemap-generator/"
        },
        {
            "icon": "robot_a2b.png",
            "title": "A2B",
            "rule" : [
                (re.compile("www\.a2b\.cc", re.I), "")
            ],
            "uri": "http://www.a2b.cc"
        },
        {
            "icon": "robot_robot.png",
            "title": "Abacho",
            "rule" : [
                (re.compile("^ABACHOBot", re.I), "")
            ]
        },
        {
            "icon": "robot_abcdatos.png",
            "title": "ABCdatos",
            "rule" : [
                (re.compile("^ABCdatos BotLink[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.abcdatos.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "aBot",
            "rule" : [
                (re.compile("^abot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_about.png",
            "title": "About",
            "rule" : [
                (re.compile("Libby[_/ ]([0-9.]{1,10})", re.I), 1),
                (re.compile("About[_/ ]([0-9.]{1,10})libwww-perl", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Ackerm",
            "rule" : [
                (re.compile("www.ackerm.com", re.I), "")
            ],
            "uri": "http://www.ackerm.com/"
        },
        {
            "icon": "robot_acoi.png",
            "title": "AcoiRobot",
            "rule" : [
                (re.compile("^AcoiRobot", re.I), "")
            ],
            "uri": "http://monetdb.cwi.nl/acoi/projects.html"
        },
        {
            "icon": "robot_acoon.png",
            "title": "Acoon",
            "rule" : [
                (re.compile("Acoon[ \-]?Robot", re.I), "")
            ]
        },
        {
            "icon": "robot_accoona.png",
            "title": "Accoona",
            "rule" : [
                (re.compile("Accoona-AI-Agent[/ ]([0-9.]{1,10})", re.I), 1),
                (re.compile("^accoona", re.I), "")
            ]
        },
        {
            "icon": "robot_acme.png",
            "title": "Acme",
            "rule" : [
                (re.compile("^Acme\.Spider", re.I), "")
            ],
            "uri": "http://www.acme.com/java/software/Acme.Spider.html"
        },
        {
            "icon": "robot_robot.png",
            "title": "ActiveBookmark",
            "rule" : [
                (re.compile("ActiveBookmark[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Ad Muncher",
            "rule" : [
                (re.compile("Ad Muncher[/ v]*([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Aesop",
            "rule" : [
                (re.compile("^AESOP_com_SpiderMan", re.I), "")
            ],
            "uri": "http://www.aesop.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Agada",
            "rule" : [
                (re.compile("^agadine[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Aibot",
            "rule" : [
                (re.compile("AIBOT[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Aipbot",
            "rule" : [
                (re.compile("aipbot[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_aleksika.png",
            "title": "Aleksika",
            "rule" : [
                (re.compile("Aleksika Spider[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_alertsite.png",
            "title": "AlertSite",
            "rule" : [
                (re.compile("ipd[ /]([0-9.]{1,10}).*Alertsite\.com", re.I), 1)
            ],
            "uri": "http://www.alertsite.com/index.html"
        },
        {
            "icon": "robot_alexa.png",
            "title": "Alexa",
            "rule" : [
                (re.compile("^ia_archive", re.I), "")
            ]
        },
        {
            "icon": "robot_almaden.png",
            "title": "IBM Crawler",
            "rule" : [
                (re.compile("www\.almaden\.ibm\.com/cs/crawler", re.I), "")
            ]
        },
        {
            "icon": "robot_altavista.png",
            "title": "Altavista",
            "rule" : [
                (re.compile("Scooter[ /\-]*[a-z]*([0-9.]{1,10})", re.I), 1),
                (re.compile("AltaVista V([0-9.]{1,10})", re.I), 1),
                (re.compile("AltaVista Intranet V([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_amazon.png",
            "title": "Amazon",
            "rule" : [
                (re.compile("^(aranhabot|amzn_assoc)", re.I), ""),
                (re.compile("^NutchEC2Test", re.I), "")
            ],
            "uri": "http://www.amazon.com/"
        },
        {
            "icon": "robot_amidalla.png",
            "title": "Amidalla",
            "rule" : [
                (re.compile("^amibot", re.I), "")
            ]
        },
        {
            "icon": "robot_amfibi.png",
            "title": "Amfibi",
            "rule" : [
                (re.compile("Amfibibot[/ ]([0-9.]{1,10})", re.I), 1),
                (re.compile("Amfibibot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "AmphetaDesk",
            "rule" : [
                (re.compile("AmphetaDesk[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Amphetameme",
            "rule" : [
                (re.compile("amphetameme[ \-]?crawler", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "AnnoMille",
            "rule" : [
                (re.compile("^AnnoMille( spider)?[/ ]([0-9.]{1,10})", re.I), 2)
            ],
            "uri": "http://www.annomille.it"
        },
        {
            "icon": "robot_robot.png",
            "title": "Ansearch",
            "rule" : [
                (re.compile("AnsearchBot[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_answerchase.png",
            "title": "AnswerChase",
            "rule" : [
                (re.compile("AnswerChase( PROve)?[/ ]([0-9.]{1,10})", re.I), 2)
            ],
            "uri": "http://www.answerchase.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "antibot",
            "rule" : [
                (re.compile("antibot-V([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_aonde.png",
            "title": "Aonde",
            "rule" : [
                (re.compile("^AONDE-Spider", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "A-Online.at",
            "rule" : [
                (re.compile("^A-Online Search", re.I), "")
            ],
            "uri": "http://www.a-online.at/"
        },
        {
            "icon": "robot_aol.png",
            "title": "AOLserver",
            "rule" : [
                (re.compile("^AOLserver-Tcl[/ ]([0-9.]{1,10})", re.I), 1),
                (re.compile("^AOLserver", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "ApacheBench",
            "rule" : [
                (re.compile("ApacheBench[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Passion 4 Jazz",
            "rule" : [
                (re.compile("^BebopBot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.apassion4jazz.net/bebopbot.html"
        },
        {
            "icon": "robot_robot.png",
            "title": "Apexoo",
            "rule" : [
                (re.compile("^Apexoo Spider ([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.apexoo.com/"
        },
        {
            "icon": "robot_aport.png",
            "title": "Aport",
            "rule" : [
                (re.compile("^Aport", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Walhello",
            "rule" : [
                (re.compile("appie[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_arachmo.png",
            "title": "Arachmo",
            "rule" : [
                (re.compile("compatible; Arachmo", re.I), "")
            ]
        },
        {
            "icon": "robot_arexera.png",
            "title": "Arexera",
            "rule" : [
                (re.compile("^X-Crawler", re.I), ""),
                (re.compile("^TECOMAC-Crawler[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.arexera.de/"
        },
        {
            "icon": "robot_arianna.png",
            "title": "Arianna",
            "rule" : [
                (re.compile("^www.arianna.it", re.I), "")
            ],
            "uri": "http://www.arianna.it/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Artface",
            "rule" : [
                (re.compile("^ArtfaceBot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Any Search Info",
            "rule" : [
                (re.compile("Sleek Spider[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://search-info.com/"
        },
        {
            "icon": "robot_askjeeves.png",
            "title": "Ask Jeeves",
            "rule" : [
                (re.compile("Ask[ \-]?Jeeves", re.I), ""),
                (re.compile("teomaagent", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "ASPseek",
            "rule" : [
                (re.compile("^AskAboutOil[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://askaboutoil.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "askEd!",
            "rule" : [
                (re.compile("^asked[ /]Nutch[ -]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://asked.jp"
        },
        {
            "icon": "robot_robot.png",
            "title": "ASPseek",
            "rule" : [
                (re.compile("^ASPseek[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "At Local",
            "rule" : [
                (re.compile("AtlocalBot[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.atlocal.com/"
        },
        {
            "icon": "robot_atomz.png",
            "title": "Atomz",
            "rule" : [
                (re.compile("Atomz[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Axel",
            "rule" : [
                (re.compile("^axel", re.I), "")
            ]
        },
        {
            "icon": "robot_axmo.png",
            "title": "Axmo",
            "rule" : [
                (re.compile("AxmoRobot", re.I), "")
            ]
        },
        {
            "icon": "robot_answerbus.png",
            "title": "AnswerBus",
            "rule" : [
                (re.compile("answerbus", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "AutoMapIt",
            "rule" : [
                (re.compile("AutoMapIt[ /](Bot)?", re.I), "")
            ],
            "uri": "http://www.automapit.com/bot.html"
        },
        {
            "icon": "robot_robot.png",
            "title": "Augurnfind",
            "rule" : [
                (re.compile("augurnfind[/ ][v\-]*([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_awasu.png",
            "title": "Awasu",
            "rule" : [
                (re.compile("Awasu[/ ]([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "ba.be",
            "rule" : [
                (re.compile("BACS http://www.ba.be", re.I), "")
            ],
            "uri": "http://www.ba.be/"
        },
        {
            "icon": "robot_baidu.png",
            "title": "Baidu",
            "rule" : [
                (re.compile("Baiduspider", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "BananaTree",
            "rule" : [
                (re.compile("www\.thebananatree\.org", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "bdcindexer",
            "rule" : [
                (re.compile("bdcindexer_([0-9a-z.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.business.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "BDFetch",
            "rule" : [
                (re.compile("^BDFetch", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "Bdncentral",
            "rule" : [
                (re.compile("BDNcentral Crawler v([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.bdncentral.com/robot.html"
        },
        {
            "icon": "robot_robot.png",
            "title": "BeamMachine",
            "rule" : [
                (re.compile("^BeamMachine[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.beammachine.net/"
        },
        {
            "icon": "robot_become.png",
            "title": "Become",
            "rule" : [
                (re.compile("Become(JP)?Bot[/ ]([0-9.]{1,10})", re.I), 2),
                (re.compile("(BecomeBot|Exabot)@exava\.com\)$", re.I), "")
            ],
            "uri": "http://www.become.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Beebware",
            "rule" : [
                (re.compile("BeebwareDirectory[/ ]v?([0-9.]{1,10})", re.I), 2)
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "Big Brother",
            "rule" : [
                (re.compile("^Big Brother", re.I), "")
            ],
            "uri": "http://pauillac.inria.fr/~fpottier/"
        },
        {
            "icon": "robot_robot.png",
            "title": "BigClique",
            "rule" : [
                (re.compile("^BigCliqueBOT[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.bigclique.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Biglotron",
            "rule" : [
                (re.compile("^BIGLOTRON", re.I), "")
            ],
            "uri": "http://www.bigclique.com"
        },
        {
            "icon": "robot_bigsearch.png",
            "title": "Bigsearch",
            "rule" : [
                (re.compile("Bigsearch.ca[/ ]Nutch[- ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "Bilbo",
            "rule" : [
                (re.compile("Bilbo[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://home.broadpark.no/~tnilsen-1/Linux/Bilbo_-_Nessus_WEB/bilbo_-_nessus_web.html"
        },
        {
            "icon": "robot_bilgi.png",
            "title": "Bilgi",
            "rule" : [
                (re.compile("Bilgi(Beta)?Bot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.bilgi.com/"
        },
        {
            "icon": "robot_bitacle.png",
            "title": "Bitacle",
            "rule" : [
                (re.compile("Bitacle (ro)?bot[ \(/V:]+([0-9.]{1,10})", re.I), 2)
            ],
            "uri": "http://bitacle.org/"
        },
        {
            "icon": "robot_bitbeamer.png",
            "title": "BitBeamer",
            "rule" : [
                (re.compile("BitBeamer/([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_biz360.png",
            "title": "Biz360",
            "rule" : [
                (re.compile("^Biz360 spider", re.I), 1)
            ]
        },
        {
            "icon": "robot_blaiz-bee.png",
            "title": "Blaiz-Bee",
            "rule" : [
                (re.compile("Blaiz-Bee[ /]([0-9.]{1,10})", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "blogbot.de",
            "rule" : [
                (re.compile("Naamah[ /]([0-9.a-z]{1,10})[ /]Blogbot", re.I), 1)
            ],
            "uri": "http://blogbot.de/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Blogdex",
            "rule" : [
                (re.compile("Blogdex[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_blogg.png",
            "title": "Blogg",
            "rule" : [
                (re.compile("^blogg\.de", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "BlogLand",
            "rule" : [
                (re.compile("BlogLand[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_bloglines.png",
            "title": "Bloglines",
            "rule" : [
                (re.compile("Bloglines[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("Bloglines", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Blogmap",
            "rule" : [
                (re.compile("blogmap", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Blogosphere",
            "rule" : [
                (re.compile("Blogosphere", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "BlogPeople",
            "rule" : [
                (re.compile("BlogPeople", re.I), "")
            ]
        },
        {
            "icon": "robot_blogpulse.png",
            "title": "Blogpulse",
            "rule" : [
                (re.compile("Blogpulse", re.I), "")
            ]
        },
        {
            "icon": "robot_blogranking.png",
            "title": "BlogRanking",
            "rule" : [
                (re.compile("^BlogRanking(/RSS checker)?", re.I), "")
            ]
        },
        {
            "icon": "robot_blogs.png",
            "title": "Blo.gs",
            "rule" : [
                (re.compile("blo\.gs[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("blo\.gs", re.I), "")
            ]
        },
        {
            "icon": "robot_blogshares.png",
            "title": "BlogShares",
            "rule" : [
                (re.compile("BlogShares[ /]V?([0-9.]{1,10})", re.I), 1),
                (re.compile("(^| |\()Blogshares(\.com| |\))", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "BlogsLife",
            "rule" : [
                (re.compile("Blogslive", re.I), "")
            ]
        },
        {
            "icon": "robot_blogsnow.png",
            "title": "BlogsNow",
            "rule" : [
                (re.compile("blogsnowbot", re.I), ""),
                (re.compile("BlogsNow", re.I), "")
            ]
        },
        {
            "icon": "robot_blogstreet.png",
            "title": "BlogStreet",
            "rule" : [
                (re.compile("^BlogStreetBot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "BlogSurf",
            "rule" : [
                (re.compile("nomadscafe_ra[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "BlogTick",
            "rule" : [
                (re.compile("BlogTickServer", re.I), "")
            ]
        },
        {
            "icon": "robot_blogwatcher.png",
            "title": "Blogwatcher",
            "rule" : [
                (re.compile("blogWatcher_Spider[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_blogwise.png",
            "title": "Blogwise",
            "rule" : [
                (re.compile("Blogwise\.com(-MetaChecker)?[/ ]([0-9.]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "robot_boardreader.png",
            "title": "BoardReader",
            "rule" : [
                (re.compile("BoardReader[ -](Image|Favicon)[ -]Fetcher[ /]+([0-9.]{1,10})", re.I), 2)
            ],
            "uri": "http://www.boardreader.com"
        },
        {
            "icon": "robot_bobby.png",
            "title": "Bobby",
            "rule" : [
                (re.compile("bobby[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Boitho",
            "rule" : [
                (re.compile("Boitho\.com[ \-](dc|robot)?[/ ]([0-9.]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Booch",
            "rule" : [
                (re.compile("^booch[_ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_book.png",
            "title": "Bookmark",
            "rule" : [
                (re.compile("http://www\.bookmark\.ne\.jp", re.I), "")
            ]
        },
        {
            "icon": "robot_bookdog.png",
            "title": "Bookdog",
            "rule" : [
                (re.compile("^Bookdog[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_bordermanager.png",
            "title": "Border Manager",
            "rule" : [
                (re.compile("BorderManager[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_bottomfeeder.png",
            "title": "BottomFeeder",
            "rule" : [
                (re.compile("BottomFeeder[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_browseremulator.png",
            "title": "BrowserEmulator",
            "rule" : [
                (re.compile("BrowserEmulator[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.dejavu.org/emulator.htm"
        },
        {
            "icon": "robot_browsershots.png",
            "title": "Browsershots",
            "rule" : [
                (re.compile("Browsershots URL Check", re.I), "")
            ],
            "uri": "http://browsershots.org"
        },
        {
            "icon": "robot_robot.png",
            "title": "BrowserSpy",
            "rule" : [
                (re.compile("BrowserSpy", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "BruinBot",
            "rule" : [
                (re.compile("BruinBot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Bruno",
            "rule" : [
                (re.compile("^Bruno", re.I), "")
            ]
        },
        {
            "icon": "robot_btbot.png",
            "title": "BitTorrent",
            "rule" : [
                (re.compile("BTbot/([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Bulkfeeds",
            "rule" : [
                (re.compile("Bulkfeeds[/ ]([a-z0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_burf.png",
            "title": "Burf.com",
            "rule" : [
                (re.compile("^Norbert the Spider", re.I), "")
            ],
            "uri": "http://www.burf.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Butch",
            "rule" : [
                (re.compile("Butch(__| )?([a-z0-9.]{1,10})", re.I), 2)
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "Camdiscover",
            "rule" : [
                (re.compile("^Camcrawler", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Cazoodle",
            "rule" : [
                (re.compile("^CazoodleBot/(Nutch|CazoodleBot)[/ \-]([0-9.]{1,10})", re.I), 2)
            ],
            "uri": "http://www.cazoodle.com/cazoodlebot"
        },
        {
            "icon": "robot_robot.png",
            "title": "CCGCrawl",
            "rule" : [
                (re.compile("CCGCrawl[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.myworkbase.com/bot.html"
        },
        {
            "icon": "robot_centrum.png",
            "title": "Centrum",
            "rule" : [
                (re.compile("holmes[/ ]([0-9.]{1,10})", re.I), 1),
                (re.compile("^Centrum-checker", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Cerberian Drtrs",
            "rule" : [
                (re.compile("^Cerberian Drtrs", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Cerberian Drtrs",
            "rule" : [
                (re.compile("^CFNetwork[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.cfnetwork.be/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Charlotte",
            "rule" : [
                (re.compile("Charlotte[/ ]([0-9a-z.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_cirilizator.png",
            "title": "Cirilizator",
            "rule" : [
                (re.compile("Cirilizator[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Claria",
            "rule" : [
                (re.compile("(Claria|Diamond)(Bot)?[ /]([0-9.]{1,10})", re.I), 3),
                (re.compile("(Claria|Diamond)(Bot)", re.I), "")
            ]
        },
        {
            "icon": "robot_claymont.png",
            "title": "Claymont",
            "rule" : [
                (re.compile("claymont\.com", re.I), ""),
                (re.compile("OliverPerry", re.I), "")
            ],
            "uri": "http://www.claymont.com"
        },
        {
            "icon": "robot_clush.png",
            "title": "Clush",
            "rule" : [
                (re.compile("Clus(tered-Search-|h)Bot[ /]([0-9.]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Cobion",
            "rule" : [
                (re.compile(" (QXW03018|obot)\)", re.I), "")
            ]
        },
        {
            "icon": "robot_coldfusion.png",
            "title": "ColdFusion",
            "rule" : [
                (re.compile("^coldfusion", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Combine",
            "rule" : [
                (re.compile("Combine[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "comBot",
            "rule" : [
                (re.compile("^comBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_comet.png",
            "title": "Comet",
            "rule" : [
                (re.compile("cometsearch@cometsystems", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Commerobo",
            "rule" : [
                (re.compile("Commerobo[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "ComRite",
            "rule" : [
                (re.compile("Comrite[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.comrite.com/"
        },
        {
            "icon": "robot_convera.png",
            "title": "Convera",
            "rule" : [
                (re.compile("Convera(MultiMedia)?Crawler[/ ]([0-9.]{1,10})", re.I), 2),
                (re.compile("Convera Internet Spider V([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "CoolBot",
            "rule" : [
                (re.compile("^CoolBot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Cosmix",
            "rule" : [
                (re.compile("^(voyager|cfetch|CosmixCrawler|carleson)[/ ]([0-9.]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Cosmos",
            "rule" : [
                (re.compile("^cosmos", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Cosmoty",
            "rule" : [
                (re.compile("^beautybot[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.uchoose.de/crawler/beautybot/"
        },
        {
            "icon": "robot_creativecommons.png",
            "title": "Creative Commons",
            "rule" : [
                (re.compile("CreativeCommons[/ ]([0-9.]{1,6}(-dev)?)", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "CsCrawler",
            "rule" : [
                (re.compile("CsCrawler", re.I), "")
            ],
            "uri": "http://www.kde.cs.uni-kassel.de/lehre/ss2005/googlespam/crawler.html"
        },
        {
            "icon": "robot_css.png",
            "title": "CSSCheck",
            "rule" : [
                (re.compile("CSS(Check|_Validator)", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Custo",
            "rule" : [
                (re.compile("Custo[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "CyberNavi",
            "rule" : [
                (re.compile("CyberNavi_WebGet[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_cyberz.png",
            "title": "Cyberz",
            "rule" : [
                (re.compile("Cyberz Communication Agent", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Cydral",
            "rule" : [
                (re.compile("CydralSpider[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_cynthia.png",
            "title": "Cynthia Says",
            "rule" : [
                (re.compile("Cynthia[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_d4x.png",
            "title": "Downloader for X",
            "rule" : [
                (re.compile("Downloader for X[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_da.png",
            "title": "DA",
            "rule" : [
                (re.compile("^DA[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_daum.png",
            "title": "DAUM",
            "rule" : [
                (re.compile("DAUMOA[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("DAUM Web Robot", re.I), ""),
                (re.compile("Daum Communications Corp", re.I), ""),
                (re.compile("EDI[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("Edacious.*Intelligent Web Robot", re.I), ""),
                (re.compile("RaBot[/ ]([0-9.]{1,10}) Agent", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "Daypop",
            "rule" : [
                (re.compile("daypopbot[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_delfi.png",
            "title": "Delfi",
            "rule" : [
                (re.compile("crawl at delfi dot lt", re.I), "")
            ]
        },
        {
            "icon": "robot_depspid.png",
            "title": "DepSpid",
            "rule" : [
                (re.compile("DepSpid[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_devonagent.png",
            "title": "DEVONagent",
            "rule" : [
                (re.compile("DEVONtech", re.I), "")
            ]
        },
        {
            "icon": "robot_diffbot.png",
            "title": "Diffbot",
            "rule" : [
                (re.compile(" Diffbot", re.I), "")
            ],
            "uri": "http://www.diffbot.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Direct Hit",
            "rule" : [
                (re.compile("EZResult -- Internet Search Engine", re.I), "")
            ],
            "uri": "http://www.directhit.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "DISCo Pump",
            "rule" : [
                (re.compile("DISCo Pump[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_dnsdigger.png",
            "title": "DNS-Digger",
            "rule" : [
                (re.compile("DNS-Digger-Explorer[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.dnsdigger.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "DoctorHTML",
            "rule" : [
                (re.compile("Doctor[ \-]?HTML", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Domaindatei",
            "rule" : [
                (re.compile("DomaindateiSpider[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_doweb.png",
            "title": "DoWeb",
            "rule" : [
                (re.compile("^www.doweb.co.uk", re.I), 1)
            ],
            "uri": "http://www.doweb.co.uk/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Download Ninja",
            "rule" : [
                (re.compile("Download Ninja[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_drupal.png",
            "title": "Drupal",
            "rule" : [
                (re.compile("^Drupal", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "DSNS Scanner",
            "rule" : [
                (re.compile("^DSNS", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "DTS Agent",
            "rule" : [
                (re.compile("DTS Agent", re.I), "")
            ]
        },
        {
            "icon": "robot_earthcom.png",
            "title": "Earthcom",
            "rule" : [
                (re.compile("EARTHCOM\.info[/ ]([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_ebay.png",
            "title": "eBay",
            "rule" : [
                (re.compile("eBay Relevance Ad Crawler", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Echo.com",
            "rule" : [
                (re.compile("_TrueRobot[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.echo.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "eert",
            "rule" : [
                (re.compile("eert spdr[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://bot.eert.net"
        },
        {
            "icon": "robot_eknip.png",
            "title": "E-Knip",
            "rule" : [
                (re.compile("eknip[ /]([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Eliyon",
            "rule" : [
                (re.compile("NextGenSearchBot[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_emeraldshield.png",
            "title": "EmeraldShield",
            "rule" : [
                (re.compile("^EmeraldShield", re.I), "")
            ]
        },
        {
            "icon": "robot_empas.png",
            "title": "Empas",
            "rule" : [
                (re.compile("DigExt; empas\)$", re.I), ""),
                (re.compile("^EMPAS[_\-]ROBOT", re.I), "")
            ]
        },
        {
            "icon": "robot_entireweb.png",
            "title": "Entireweb",
            "rule" : [
                (re.compile("Speedy[ ]?Spider", re.I), "")
            ]
        },
        {
            "icon": "robot_envolk.png",
            "title": "Envolk",
            "rule" : [
                (re.compile("envolk\[ITS\]spider[/ ]([0-9.]{1,10})", re.I), 1),
                (re.compile("envolk[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "ES.NET",
            "rule" : [
                (re.compile("ES.NET Crawler[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_estyle.png",
            "title": "eStyle Search",
            "rule" : [
                (re.compile("eStyleSearch[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Eurip",
            "rule" : [
                (re.compile("EuripBot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.eurip.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Euro Directory",
            "rule" : [
                (re.compile("www\.euro\-directory\.com", re.I), "")
            ],
            "uri": "http://www.euro-directory.com/"
        },
        {
            "icon": "robot_euroseek.png",
            "title": "EuroSeek",
            "rule" : [
                (re.compile("Arachnoidea", re.I), "")
            ]
        },
        {
            "icon": "robot_evaal.png",
            "title": "Evaal",
            "rule" : [
                (re.compile("^EvaalSE", re.I), "")
            ],
            "uri": "http://www.evaal.com/"
        },
        {
            "icon": "robot_eventax.png",
            "title": "Eventax",
            "rule" : [
                (re.compile("^eventax[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.eventax.de/"
        },
        {
            "icon": "robot_everbee.png",
            "title": "Everbee",
            "rule" : [
                (re.compile("EverbeeCrawler", re.I), "")
            ]
        },
        {
            "icon": "robot_everest.png",
            "title": "Everest",
            "rule" : [
                (re.compile("Everest-Vulcan Inc.[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_exabot.png",
            "title": "ExaBot",
            "rule" : [
                (re.compile("^NG[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("Exabot/([0-9.]{1,10})", re.I), 1),
                (re.compile("ExaBotTest/([0-9.]{1,10})", re.I), 1),
                (re.compile("ExaBot-(Test|Images)/([0-9.]{1,10})", re.I), 2)
            ],
            "uri": "http://www.exabot.com/go/robot"
        },
        {
            "icon": "robot_exactseek.png",
            "title": "ExactSeek",
            "rule" : [
                (re.compile("^exactseek[ \-]?(pagereaper|crawler)[ \-]?([0-9.]{1,10})", re.I), 2),
                (re.compile("ExactSeek[ \-\.]?(Crawler|com)", re.I), "")
            ]
        },
        {
            "icon": "robot_excite.png",
            "title": "Excite",
            "rule" : [
                (re.compile("Architext[ \-]?Spider", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Execrawl",
            "rule" : [
                (re.compile("Execrawl[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("Execrawl", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "ExpertMonitor",
            "rule" : [
                (re.compile("^NetMonitor[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Explorer RSS",
            "rule" : [
                (re.compile("^Windows-RSS-Platform[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_facebook.png",
            "title": "Facebook",
            "rule" : [
                (re.compile("FacebookFeedParser[/ ]([0-9a-z.\-]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_fast.png",
            "title": "Fast",
            "rule" : [
                (re.compile("^FAST( Enterprise |-Web| MetaWeb )?Crawler[ /]([0-9.]{1,10})", re.I), 2),
                (re.compile("^FAST( Enterprise |-Web| MetaWeb | PartnerSite )?Crawler", re.I), ""),
                (re.compile("^Fast Crawler", re.I), ""),
                (re.compile("^libwww-perl[ /]([0-9.]{1,10}) FP[ /]([0-9.]{1,10})", re.I), 2)
            ],
            "uri": "http://www.alltheweb.com/"
        },
        {
            "icon": "robot_fastbuzz.png",
            "title": "Fastbuzz",
            "rule" : [
                (re.compile("^fastbuzz\.com", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "FavOrg",
            "rule" : [
                (re.compile("^FavOrg", re.I), "")
            ]
        },
        {
            "icon": "robot_favorstar.png",
            "title": "favorstar",
            "rule" : [
                (re.compile("favorstarbot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://favorstar.com/bot.html"
        },
        {
            "icon": "robot_robot.png",
            "title": "Faxo",
            "rule" : [
                (re.compile("^Faxobot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.faxo.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "FDSE Robot",
            "rule" : [
                (re.compile("FDSE[ \-]?robot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "FeedBack",
            "rule" : [
                (re.compile("FeedBack[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_feedburner.png",
            "title": "FeedBurner",
            "rule" : [
                (re.compile("^FeedBurner[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_feeddemon.png",
            "title": "FeedDemon",
            "rule" : [
                (re.compile("FeedDemon[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_feedfind.png",
            "title": "FeedFind",
            "rule" : [
                (re.compile("Feed::Find[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Feed On Feeds",
            "rule" : [
                (re.compile("FeedOnFeeds[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Feedparser",
            "rule" : [
                (re.compile("UniversalFeedParser[/ ]([0-9a-z.\-]{1,10})", re.I), 1),
                (re.compile("FeedParser", re.I), "")
            ]
        },
        {
            "icon": "robot_feedreader.png",
            "title": "Feedreader",
            "rule" : [
                (re.compile("^Feedreader", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "FeedServer",
            "rule" : [
                (re.compile("FeedServer[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_feedster.png",
            "title": "Feedster",
            "rule" : [
                (re.compile("Feedster Crawler[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_feedvalidator.png",
            "title": "Feed Validator",
            "rule" : [
                (re.compile("^FeedValidator[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Free Download Manager",
            "rule" : [
                (re.compile("^FDM[/ ]([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Filangy",
            "rule" : [
                (re.compile("Filangy[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.filangy.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "FindAnISP",
            "rule" : [
                (re.compile("FindAnISP", re.I), "")
            ],
            "uri": "http://www.findanisp.com/"
        },
        {
            "icon": "robot_findengines.png",
            "title": "FindEngines",
            "rule" : [
                (re.compile("FindEngines! Bot", re.I), "")
            ]
        },
        {
            "icon": "robot_findexa.png",
            "title": "Findexa",
            "rule" : [
                (re.compile("Findexa Crawler", re.I), "")
            ]
        },
        {
            "icon": "robot_findlinks.png",
            "title": "FindLinks",
            "rule" : [
                (re.compile("findlinks[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("^FindLinks", re.I), "")
            ]
        },
        {
            "icon": "robot_findoor.png",
            "title": "findoor",
            "rule" : [
                (re.compile("^findoor(-Bot)?", re.I), 1)
            ]
        },
        {
            "icon": "robot_firefly.png",
            "title": "Firefly",
            "rule" : [
                (re.compile("Firefly", re.I), "")
            ]
        },
        {
            "icon": "robot_flashget.png",
            "title": "FlashGet",
            "rule" : [
                (re.compile("^FlashGet", re.I), "")
            ]
        },
        {
            "icon": "robot_flickbot.png",
            "title": "FlickBot",
            "rule" : [
                (re.compile("FlickBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Forex",
            "rule" : [
                (re.compile("^Forex Trading Network Organization", re.I), "")
            ],
            "uri": "http://www.netforex.org/"
        },
        {
            "icon": "robot_freshmeat.png",
            "title": "freshmeat",
            "rule" : [
                (re.compile("fmII URL validator[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("freshmeat.net URL validator[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.freshmeat.net/"
        },
        {
            "icon": "robot_friend.png",
            "title": "Friend",
            "rule" : [
                (re.compile("www\.friend\.fr", re.I), "")
            ]
        },
        {
            "icon": "robot_frontier.png",
            "title": "Frontier",
            "rule" : [
                (re.compile("Frontier[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_gais.png",
            "title": "Gaisbot",
            "rule" : [
                (re.compile("Gaisbot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_galaxy.png",
            "title": "Galaxy",
            "rule" : [
                (re.compile("GalaxyBot[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("www.galaxy.com", re.I), "")
            ],
            "uri": "http://www.galaxy.com/"
        },
        {
            "icon": "robot_gamespy.png",
            "title": "GameSpy",
            "rule" : [
                (re.compile("GameSpyHTTP[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_gdesktop.png",
            "title": "Google Desktop",
            "rule" : [
                (re.compile("compatible; Google Desktop", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Genome Machine",
            "rule" : [
                (re.compile("Genome[ \-]?Machine", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Geona",
            "rule" : [
                (re.compile("GeonaBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "The World as a Blog",
            "rule" : [
                (re.compile("The World as a Blog", re.I), "")
            ]
        },
        {
            "icon": "robot_geourl.png",
            "title": "GeoUrl",
            "rule" : [
                (re.compile("geourl[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("^GeoURLBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "GetNetWise",
            "rule" : [
                (re.compile(" Crayon Crawler", re.I), "")
            ]
        },
        {
            "icon": "robot_getright.png",
            "title": "GetRight",
            "rule" : [
                (re.compile("GetRight[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_getsmart.png",
            "title": "GetSmart",
            "rule" : [
                (re.compile("GetSmart[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_gigablast.png",
            "title": "Gigablast",
            "rule" : [
                (re.compile("(Gigabot|Sitesearch)[/ ]([0-9.]{1,10})", re.I), 2),
                (re.compile("GigabotSiteSearch[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_girafa.png",
            "title": "Girafa",
            "rule" : [
                (re.compile("Girafabot", re.I), "")
            ]
        },
        {
            "icon": "robot_globalspec.png",
            "title": "GlobalSpec",
            "rule" : [
                (re.compile("Ocelli[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_glucose.png",
            "title": "Glucose",
            "rule" : [
                (re.compile("glucose[ /]([0-9a-z.\-]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_goforit.png",
            "title": "GoForIt",
            "rule" : [
                (re.compile("^GoForIt\.com", re.I), ""),
                (re.compile("^GOFORITBOT", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "GoGuides",
            "rule" : [
                (re.compile("^GoGuidesBot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.goguides.org/"
        },
        {
            "icon": "robot_goo.png",
            "title": "Goo",
            "rule" : [
                (re.compile("(gazz|ichiro|mog(et|imogi))[ /]([0-9.]{1,10})", re.I), 3),
                (re.compile("DoCoMo[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_google.png",
            "title": "Mediapartners",
            "rule" : [
                (re.compile("Mediapartners-Google[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_google.png",
            "title": "Google",
            "rule" : [
                (re.compile("Googl(e|ebot)(-Image)?/([0-9.]{1,10})", re.I), 3),
                (re.compile("Googl(e|ebot)(-Image)?/", re.I), ""),
                (re.compile("^gsa-crawler", re.I), "")
            ]
        },
        {
            "icon": "robot_google.png",
            "title": "Google-Sitemaps",
            "rule" : [
                (re.compile("Googl(e|ebot)(-Sitemaps)?/([0-9.]{1,10})", re.I), 3),
                (re.compile("GSiteCrawler[ /v]*([0-9.a-z]{1,10})", re.I), 1),
                (re.compile("Googl(e|ebot)(-Sitemaps)?/", re.I), "")
            ]
        },
        {
            "icon": "robot_google.png",
            "title": "Google-Mobile",
            "rule" : [
                (re.compile("Googl(e|ebot)(-Mobile)?/([0-9.]{1,10})", re.I), 3),
                (re.compile("Googl(e|ebot)(-Mobile)?/", re.I), "")
            ]
        },
        {
            "icon": "robot_google.png",
            "title": "Google-AdsBot",
            "rule" : [
                (re.compile("^AdsBot-Google", re.I), "")
            ]
        },
        {
            "icon": "robot_google.png",
            "title": "Google-Feedfetcher",
            "rule" : [
                (re.compile("^Feedfetcher-Google", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "GoonGee",
            "rule" : [
                (re.compile("^Big Fish[ /]v?([0-9.]{1,10})", re.I), 2)
            ],
            "uri": "http://www.goongee.com/"
        },
        {
            "icon": "robot_gpost.png",
            "title": "GPost",
            "rule" : [
                (re.compile("^GPostbot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Gregarius",
            "rule" : [
                (re.compile("^Gregarius[/ ]([0-9.]{1,10})", re.I), "")
            ]
        },
        {
            "icon": "robot_grub.png",
            "title": "Grub",
            "rule" : [
                (re.compile("grub[ \-]?client[ /\-]{1,5}([0-9.]{1,10})", re.I), 1),
                (re.compile("grub crawler", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "Gulliver",
            "rule" : [
                (re.compile("Gulliver", re.I), "")
            ]
        },
        {
            "icon": "robot_guruji.png",
            "title": "Guruji",
            "rule" : [
                (re.compile("^GurujiBot[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.guruji.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Gush",
            "rule" : [
                (re.compile("^Gush[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Gzip Tester",
            "rule" : [
                (re.compile("g(id)?zip[ \-]?test(er)?", re.I), "")
            ]
        },
        {
            "icon": "robot_hanzoweb.png",
            "title": "Hanzoweb",
            "rule" : [
                (re.compile("^Hanzoweb", re.I), "")
            ]
        },
        {
            "icon": "robot_harbot.png",
            "title": "Harbot",
            "rule" : [
                (re.compile("^Harbot GateStation", re.I), "")
            ]
        },
        {
            "icon": "robot_hatena.png",
            "title": "Hatena",
            "rule" : [
                (re.compile("Hatena (Antenna|Bookmark|Pagetitle Agent)[ /]([0-9.]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "robot_Helix.png",
            "title": "Heritrix",
            "rule" : [
                (re.compile("^helix[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.sitesearch.ca/helix/"
        },
        {
            "icon": "robot_heritrix.png",
            "title": "Heritrix",
            "rule" : [
                (re.compile("heritrix[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("archive.org_bot", re.I), ""),
                (re.compile("InternetArchive[ /]([0-9.a-z]{1,10})", re.I), 1)
            ],
            "uri": "http://archive.org"
        },
        {
            "icon": "robot_robot.png",
            "title": "HiddenMarket",
            "rule" : [
                (re.compile("HiddenMarket[ /\-]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Honda",
            "rule" : [
                (re.compile("Honda-Search[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.honda-search.com"
        },
        {
            "icon": "robot_hoowwwer.png",
            "title": "HooWWWer",
            "rule" : [
                (re.compile("HooWWWer[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_hotzonu.png",
            "title": "Hotzonu",
            "rule" : [
                (re.compile("Hotzonu[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Houxou",
            "rule" : [
                (re.compile("HouxouCrawler[ /]Nutch.([0-9.]{1,10})", re.I), 1),
                (re.compile("HouxouCrawler", re.I), "")
            ]
        },
        {
            "icon": "robot_htdig.png",
            "title": "ht://Dig",
            "rule" : [
                (re.compile("htdig[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_html2jpg.png",
            "title": "HTML2JPG",
            "rule" : [
                (re.compile("^HTML2JPG", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "HTTPerf",
            "rule" : [
                (re.compile("httperf[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_httpunit.png",
            "title": "HttpUnit",
            "rule" : [
                (re.compile("httpunit[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_httrack.png",
            "title": "HTTrack",
            "rule" : [
                (re.compile("HTTrack[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_hungary.png",
            "title": "Hungary",
            "rule" : [
                (re.compile("HuRob[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_iask.png",
            "title": "IAsk",
            "rule" : [
                (re.compile("iaskspider[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("^iaskspider", re.I), "")
            ],
            "uri": "http://iask.com"
        },
        {
            "icon": "robot_icc.png",
            "title": "ICC-Crawler",
            "rule" : [
                (re.compile("^ICC-Crawler", re.I), "")
            ],
            "uri": "http://kc.nict.go.jp/icc/crawl.html"
        },
        {
            "icon": "robot_icerocket.png",
            "title": "Icerocket",
            "rule" : [
                (re.compile("BlogzIce[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("BlogSearch[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_icra.png",
            "title": "ICRA",
            "rule" : [
                (re.compile("^ICRA_Semantic_spider[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.icra.org"
        },
        {
            "icon": "robot_robot.png",
            "title": "Novell iChain Cool Solutions caching",
            "rule" : [
                (re.compile("^Mozilla[/ ]([0-9.]{1,10})[/ ]\(compatible[ ;]*ICS", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "I know",
            "rule" : [
                (re.compile("Comaneci_bot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Ilial",
            "rule" : [
                (re.compile("ilial[ /]Nutch[ \-]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_ilse.png",
            "title": "Ilse",
            "rule" : [
                (re.compile("I(NGRID|lseRobot|lseBot)[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://ilse.nl/"
        },
        {
            "icon": "robot_iltrovatore.png",
            "title": "IlTrovatore",
            "rule" : [
                (re.compile("iltrovatore-setaccio[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("Iltrovatore-Setaccio", re.I), ""),
                (re.compile("iltrovatore[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Indy Library",
            "rule" : [
                (re.compile("Indy[ \-]?Library", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Inela",
            "rule" : [
                (re.compile("InelaBot[ /]([0-9.]{1,10})", re.I), "")
            ],
            "uri": "http://inelegant.org/bot"
        },
        {
            "icon": "robot_robot.png",
            "title": "InetURL",
            "rule" : [
                (re.compile("InetURL.?[ /]([0-9.]{1,10})", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "InfoArt",
            "rule" : [
                (re.compile("InfoArt crawler", re.I), "")
            ]
        },
        {
            "icon": "robot_infomine.png",
            "title": "INFOMINE",
            "rule" : [
                (re.compile("^DataFountains/DMOZ", re.I), ""),
                (re.compile("^INFOMINE[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://infomine.ucr.edu/"
        },
        {
            "icon": "robot_infoseek.png",
            "title": "Infoseek",
            "rule" : [
                (re.compile("SideWinder[ /]?([0-9a-z.]{1,10})", re.I), 1),
                (re.compile("Infoseek", re.I), "")
            ]
        },
        {
            "icon": "robot_inktomi.png",
            "title": "Inktomi",
            "rule" : [
                (re.compile("slurp@inktomi\.com", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Innerprise",
            "rule" : [
                (re.compile("^InnerpriseBot[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("URL[ _]Spider[ _]Pro[ /]([0-9.+]{1,10})", re.I), 1),
                (re.compile("^ES[ .]NET[ _]Crawler[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.innerprise.com/"
        },
        {
            "icon": "robot_inria.png",
            "title": "Inria",
            "rule" : [
                (re.compile("^xyro_", re.I), "")
            ]
        },
        {
            "icon": "robot_insitor.png",
            "title": "Insitor",
            "rule" : [
                (re.compile("^Insitor(,|\.|naut)", re.I), "")
            ],
            "uri": "http://www.insitor.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Internet Ninja",
            "rule" : [
                (re.compile("^Internet Ninja[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_internetseer.png",
            "title": "InternetSeer",
            "rule" : [
                (re.compile("^InternetSeer\.com", re.I), "")
            ]
        },
        {
            "icon": "robot_interseek.png",
            "title": "Interseek",
            "rule" : [
                (re.compile("Interseek.com", re.I), "")
            ],
            "uri": "http://www.interseek.com"
        },
        {
            "icon": "robot_intravnews.png",
            "title": "IntraVnews",
            "rule" : [
                (re.compile("IntraVnews[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_ip2location.png",
            "title": "IP2LocationBot",
            "rule" : [
                (re.compile("^IP2(Map|Location)Bot[ /]([0-9.]{1,10})", re.I), 2)
            ],
            "uri": "http://www.ip2location.com"
        },
        {
            "icon": "robot_ipworks.png",
            "title": "IP*Works",
            "rule" : [
                (re.compile("^IP\*Works\! V([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.nsoftware.com/ipworks/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Novell iChain Cool Solutions caching",
            "rule" : [
                (re.compile("^ICRA_(label_generator|Semantic_spider)[ /]([0-9.]{1,10})", re.I), 2)
            ],
            "uri": "http://www.icra.org"
        },
        {
            "icon": "robot_robot.png",
            "title": "Irvine",
            "rule" : [
                (re.compile("Irvine[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "ISSpider",
            "rule" : [
                (re.compile("ISSpider[ /\-]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "iVia",
            "rule" : [
                (re.compile("iVia Site Checker.?[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_jeteye.png",
            "title": "Jeteye",
            "rule" : [
                (re.compile("Jetbot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_jigsaw.png",
            "title": "Jigsaw",
            "rule" : [
                (re.compile("Jigsaw[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_jobsde.png",
            "title": "jobs.de",
            "rule" : [
                (re.compile("jobs\.de", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Jpluck",
            "rule" : [
                (re.compile("JPluck[ /]([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Jxta",
            "rule" : [
                (re.compile("falcon[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_jyte.png",
            "title": "Jyte",
            "rule" : [
                (re.compile("jyte_fetcher[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_jyxo.png",
            "title": "Jyxo",
            "rule" : [
                (re.compile("Jyxobot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_keywen.png",
            "title": "Keywen",
            "rule" : [
                (re.compile("EasyDL[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_kinja.png",
            "title": "Kinja",
            "rule" : [
                (re.compile("kinjabot[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("^kinjabot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Lachesis",
            "rule" : [
                (re.compile("lachesis", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Lachesis",
            "rule" : [
                (re.compile("lanshanbot[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_lapozz.png",
            "title": "Lapozz",
            "rule" : [
                (re.compile("LapozzBot[/ ]?([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Larbin",
            "rule" : [
                (re.compile("larbin[_/ ]?([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Laurion",
            "rule" : [
                (re.compile("^IPiumBot", re.I), "")
            ],
            "uri": "http://www.laurion.com/"
        },
        {
            "icon": "robot_leechget.png",
            "title": "LeechGet",
            "rule" : [
                (re.compile("^LeechGet[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Linkguard",
            "rule" : [
                (re.compile("Linkguard Online[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.linkguard.com/"
        },
        {
            "icon": "robot_linkman.png",
            "title": "Linkman",
            "rule" : [
                (re.compile("\(compatible; Linkman\)", re.I), "")
            ]
        },
        {
            "icon": "robot_linkcheck.png",
            "title": "Linkcheck",
            "rule" : [
                (re.compile("checklink[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("Link[ \-]?(Chec(k|ker)|Val(et|idator))", re.I), ""),
                (re.compile("Adaxas Spider", re.I), ""),
                (re.compile("Agent-SharewarePlazaFileCheckBot[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("NetMechanic V([0-9.]{1,10})", re.I), 1),
                (re.compile("^InfoLink", re.I), ""),
                (re.compile("InternetLinkAgent", re.I), ""),
                (re.compile("; SPENG\)", re.I), ""),
                (re.compile("SharewarePlazaFileCheckBot", re.I), ""),
                (re.compile("fileboost.net", re.I), ""),
                (re.compile("^billbot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Link.RU",
            "rule" : [
                (re.compile("^Link.RU bot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Links SQL",
            "rule" : [
                (re.compile("links sql", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Link Sweeper",
            "rule" : [
                (re.compile("LinkSweeper[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Link Walker",
            "rule" : [
                (re.compile("^LinkWalker", re.I), "")
            ]
        },
        {
            "icon": "robot_livedoor.png",
            "title": "Livedoor",
            "rule" : [
                (re.compile("^Livedoor( SF( - California Crawl)?|Checkers)[ /]", re.I), "")
            ]
        },
        {
            "icon": "robot_livejournal.png",
            "title": "Live Journal",
            "rule" : [
                (re.compile("^LiveJournal\.com", re.I), "")
            ],
            "uri": "http://www.livejournal.com"
        },
        {
            "icon": "robot_ljpic.png",
            "title": "ljpic",
            "rule" : [
                (re.compile("LjSEEK Picture-Bot[ /]+([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.ljpic.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Lmspider",
            "rule" : [
                (re.compile("^lmspider", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Locaters",
            "rule" : [
                (re.compile("^FiNDoBot[/ ]([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_look.png",
            "title": "Look",
            "rule" : [
                (re.compile("www\.look\.com", re.I), ""),
                (re.compile("Lookbot", re.I), "")
            ]
        },
        {
            "icon": "robot_looksmart.png",
            "title": "LookSmart",
            "rule" : [
                (re.compile("^Martini", re.I), ""),
                (re.compile("^MantraAgent", re.I), ""),
                (re.compile("FurlBot", re.I), ""),
                (re.compile("looksmart-sv-fw", re.I), "")
            ]
        },
        {
            "icon": "robot_loop.png",
            "title": "LOOP",
            "rule" : [
                (re.compile("NetResearchServer[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Lotkyll",
            "rule" : [
                (re.compile("Lotkyll", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "lwp",
            "rule" : [
                (re.compile("lwp(-trivial|::simple)[ /]([0-9.]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "robot_lycos.png",
            "title": "Lycos",
            "rule" : [
                (re.compile("Lycos_Spider_", re.I), "")
            ]
        },
        {
            "icon": "robot_robot_rss.png",
            "title": "MagpieRSS",
            "rule" : [
                (re.compile("MagpieRSS", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Mail Sweeper",
            "rule" : [
                (re.compile("Mail[ \-]?Sweeper", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Marvin",
            "rule" : [
                (re.compile("^Marvin", re.I), "")
            ]
        },
        {
            "icon": "robot_matkurja.png",
            "title": "Mat'Kurja",
            "rule" : [
                (re.compile("Mosad[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_mavicanet.png",
            "title": "Mavicanet",
            "rule" : [
                (re.compile("Mavicanet robot", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "Mediater",
            "rule" : [
                (re.compile("^libwww[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Mercator",
            "rule" : [
                (re.compile("Mercator", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Metacarta",
            "rule" : [
                (re.compile("^RRC (crawler_admin@bigfoot.com)", re.I), ""),
                (re.compile("^flunky", re.I), ""),
                (re.compile("^Mozilla.*\(samualt9@bigfoot.com\)$", re.I), "")
            ],
            "uri": "http://www.metacarta.com"
        },
        {
            "icon": "robot_metager.png",
            "title": "MetaGer",
            "rule" : [
                (re.compile("MetaGer", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Metamark",
            "rule" : [
                (re.compile("^XRL[ /]([0-9.a-z]{1,10})", re.I), 1)
            ],
            "uri": "http://metamark.net"
        },
        {
            "icon": "robot_metamedic.png",
            "title": "MetaMedic",
            "rule" : [
                (re.compile("MediBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_mirago.png",
            "title": "Mirago",
            "rule" : [
                (re.compile("Mirago", re.I), "")
            ]
        },
        {
            "icon": "robot_miva.png",
            "title": "Miva",
            "rule" : [
                (re.compile("AlgoFeedback@miva\.com", re.I), "")
            ],
            "uri": "http://www.miva.com/"
        },
        {
            "icon": "robot_mj12.png",
            "title": "Majestic-12",
            "rule" : [
                (re.compile("Mj12bot[ /]v?([0-9.]{1,10})", re.I), 1),
                (re.compile("MJ12bot \(mini\)[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://majestic12.co.uk/bot.php"
        },
        {
            "icon": "robot_robot.png",
            "title": "Mnogo",
            "rule" : [
                (re.compile("Mnogosearch[ /\-]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "MojeekBot",
            "rule" : [
                (re.compile("MojeekBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "MOM Spider",
            "rule" : [
                (re.compile("MOMspider[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_moreover.png",
            "title": "Moreover",
            "rule" : [
                (re.compile("^Moreoverbot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_movabletype.png",
            "title": "Movable Type",
            "rule" : [
                (re.compile("MovableType[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_mozdex.png",
            "title": "MozDex",
            "rule" : [
                (re.compile("mozDex[ /]([0-9.]{1,6}(-dev)?)", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "MQbot",
            "rule" : [
                (re.compile("MQbot", re.I), "")
            ]
        },
        {
            "icon": "robot_msn.png",
            "title": "MSN",
            "rule" : [
                (re.compile("MSN(BOT|PTC)[ /]([0-9.]{1,10})", re.I), 2),
                (re.compile("MS Search ([0-9.]{1,10}) Robot", re.I), 1)
            ]
        },
        {
            "icon": "robot_livesearch.png",
            "title": "MS Live Search",
            "rule" : [
                (re.compile("MSNBOT-(MEDIA|PRODUCTS)[ /]([0-9.]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "MSProxy",
            "rule" : [
                (re.compile("MSProxy[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "MS-WebDAV",
            "rule" : [
                (re.compile("Microsoft[ \-]?WebDAV[ \-]?MiniRedir", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "MTIcon",
            "rule" : [
                (re.compile("MTIcon[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_rss.png",
            "title": "MyRSS",
            "rule" : [
                (re.compile("MyRSS.jp[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Multimap",
            "rule" : [
                (re.compile("Multimap Geotag Blog Parser[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_najdi.png",
            "title": "Najdi.si",
            "rule" : [
                (re.compile("Najdi.si", re.I), "")
            ],
            "uri": "http://www.najdi.si"
        },
        {
            "icon": "robot_nameprotect.png",
            "title": "Name Protect",
            "rule" : [
                (re.compile("NPBot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "National Directory",
            "rule" : [
                (re.compile("NationalDirectory-WebSpider[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Natsu Mican",
            "rule" : [
                (re.compile("NATSU[ \-]MICAN[/ ]([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_naverbot.png",
            "title": "Naver",
            "rule" : [
                (re.compile("NaverBot([_\-]dloader)?[/ \-]([0-9.]{1,10})", re.I), 2),
                (re.compile("Naver(Bot)?", re.I), ""),
                (re.compile("^nabot", re.I), "")
            ]
        },
        {
            "icon": "robot_navisso.png",
            "title": "Navisso",
            "rule" : [
                (re.compile("Navisso(Bot)?", re.I), "")
            ],
            "uri": "http://www.navisso.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "neofonie",
            "rule" : [
                (re.compile("www.neofonie.de", re.I), "")
            ],
            "uri": "http://www.neofonie.de/loesungen/search/robot.html"
        },
        {
            "icon": "robot_robot.png",
            "title": "Neomo",
            "rule" : [
                (re.compile("Francis[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_nessus.png",
            "title": "Nessus",
            "rule" : [
                (re.compile("Nessus\)$", re.I), "")
            ]
        },
        {
            "icon": "robot_netants.png",
            "title": "NetAnts",
            "rule" : [
                (re.compile("NetAnts[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_netcraft.png",
            "title": "Netcraft",
            "rule" : [
                (re.compile("netcraft", re.I), "")
            ]
        },
        {
            "icon": "robot_netluchs.png",
            "title": "Netluchs",
            "rule" : [
                (re.compile("Netluchs[ /]([0-9.a-z]{1,10})", re.I), 1)
            ],
            "uri": "http://www.netluchs.de/"
        },
        {
            "icon": "robot_netmechanic.png",
            "title": "NetMechanic",
            "rule" : [
                (re.compile("NetMechanic[ /V]{1,5}([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_netnose.png",
            "title": "NetNose",
            "rule" : [
                (re.compile("NetNose[ \-]Crawler[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Netoskop",
            "rule" : [
                (re.compile("netoskop", re.I), "")
            ]
        },
        {
            "icon": "robot_netpromoter.png",
            "title": "NetPromoter",
            "rule" : [
                (re.compile("NetPromoter Spider", re.I), "")
            ],
            "uri": "http://www.net-promoter.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Netprospector",
            "rule" : [
                (re.compile("^netprospector", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Netpumper",
            "rule" : [
                (re.compile("^NetPumper[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_netscape.png",
            "title": "Netscape Proxy",
            "rule" : [
                (re.compile("Netscape\-Proxy[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "NetSpective",
            "rule" : [
                (re.compile("^WebFilter Robot ([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_netvibes.png",
            "title": " Netvibes",
            "rule" : [
                (re.compile("^Netvibes", re.I), 1)
            ]
        },
        {
            "icon": "robot_newsfire.png",
            "title": "NewsFire",
            "rule" : [
                (re.compile("NewsFire[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_newsgator.png",
            "title": "NewsGator",
            "rule" : [
                (re.compile("NewsGato(r|rOnline)[/ ]([0-9.]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "robot_newzcrawler.png",
            "title": "NewzCrawler",
            "rule" : [
                (re.compile("NewzCrawler[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_newzcrawler.png",
            "title": "NewzCrawler",
            "rule" : [
                (re.compile("^NextopiaBOT.*[v ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_ngsearch.png",
            "title": "NG Search",
            "rule" : [
                (re.compile("NG-Search[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Nimble",
            "rule" : [
                (re.compile("NimbleCrawler[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "NuSearch",
            "rule" : [
                (re.compile("^nuSearch", re.I), "")
            ],
            "uri": "http://www.nusearch.com/"
        },
        {
            "icon": "robot_noago.png",
            "title": "Noago",
            "rule" : [
                (re.compile("Noago Spider", re.I), "")
            ],
            "uri": "http://www.noago.com/"
        },
        {
            "icon": "robot_noviforum.png",
            "title": "Noviforum",
            "rule" : [
                (re.compile("TridentSpider[/ ]?([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_noxtrum.png",
            "title": "noXtrum",
            "rule" : [
                (re.compile("noxtrumbot[/ ]?([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Noyona",
            "rule" : [
                (re.compile("noyona.([0-9._]{1,10})", re.I), 1)
            ],
            "uri": "http://noyona.com/"
        },
        {
            "icon": "robot_nsauditor.png",
            "title": "Nsauditor",
            "rule" : [
                (re.compile("Nsauditor[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.nsauditor.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Bookwatch",
            "rule" : [
                (re.compile("obidos[ \-]?bot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Objects Search",
            "rule" : [
                (re.compile("ObjectsSearch[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_obot.png",
            "title": "oBot",
            "rule" : [
                (re.compile("^oBot ", re.I), "")
            ],
            "uri": "http://www.onlysolutions.de/"
        },
        {
            "icon": "robot_octora.png",
            "title": "Octora",
            "rule" : [
                (re.compile("^Octora (Beta)?", re.I), "")
            ],
            "uri": "http://www.octora.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "OfflineExplorer",
            "rule" : [
                (re.compile("^Offline Explorer[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_omea.png",
            "title": "Omea Reader",
            "rule" : [
                (re.compile("Omea Reader[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_onet.png",
            "title": "Onet",
            "rule" : [
                (re.compile("OnetSzukaj[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("^Onet\.pl", re.I), ""),
                (re.compile("inktomi.search.onet", re.I), "")
            ],
            "uri": "http://www.onet.pl"
        },
        {
            "icon": "robot_robot.png",
            "title": "online24",
            "rule" : [
                (re.compile("^Online24-Bot .* ([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.online24.de"
        },
        {
            "icon": "robot_onsearch.png",
            "title": "onsearch",
            "rule" : [
                (re.compile("^onCHECK-Robot", re.I), "")
            ],
            "uri": "http://www.onsearch.de"
        },
        {
            "icon": "robot_robot.png",
            "title": "OntoSpider",
            "rule" : [
                (re.compile("^OntoSpider[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://ontospider.i-n.info/"
        },
        {
            "icon": "robot_openfind.png",
            "title": "Openfind",
            "rule" : [
                (re.compile("openbot[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("Openfind Robot[ /]([0-9.A-Z]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "OpenTagger",
            "rule" : [
                (re.compile("^OpenTaggerBot", re.I), "")
            ],
            "uri": "http://www.opentagger.com/opentaggerbot.htm"
        },
        {
            "icon": "robot_opentext.png",
            "title": "OpenText",
            "rule" : [
                (re.compile("^OpenTextSiteCrawler[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.opentext.net/"
        },
        {
            "icon": "robot_robot.png",
            "title": "OpenWebSpider",
            "rule" : [
                (re.compile("^OpenWebSpider[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.openwebspider.org"
        },
        {
            "icon": "robot_robot.png",
            "title": "Organica",
            "rule" : [
                (re.compile("crawler@organica\.us", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Outfox Melon",
            "rule" : [
                (re.compile("OutfoxMelonBot[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("OutfoxBot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_overture.png",
            "title": "Overture",
            "rule" : [
                (re.compile("Overture[ \-]?WebCrawler", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "PageBites",
            "rule" : [
                (re.compile("^PageBitesHyperBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "PanopeaBot",
            "rule" : [
                (re.compile("PanopeaBot[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_peerbot.png",
            "title": "Peerbot",
            "rule" : [
                (re.compile("^PEERbot", re.I), "")
            ]
        },
        {
            "icon": "robot_php.png",
            "title": "PHP",
            "rule" : [
                (re.compile("^PHP[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "PhpDig",
            "rule" : [
                (re.compile("^PhpDig[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.finbot.com/"
        },
        {
            "icon": "robot_phpversiontracker.png",
            "title": "PHP version tracker",
            "rule" : [
                (re.compile("^PHP version tracker", re.I), "")
            ],
            "uri": "http://www.nexen.net/phpversion/bot.php"
        },
        {
            "icon": "robot_robot.png",
            "title": "PictureOfInternet",
            "rule" : [
                (re.compile("^PictureOfInternet[ /]([0-9.]{1,10})", re.I), "")
            ]
        },
        {
            "icon": "robot_pingdom.png",
            "title": "Pingdom",
            "rule" : [
                (re.compile("^Pingdom GIGRIB v([0-9.]{1,10})", re.I), 1),
                (re.compile("^Pingdom GIGRIB", re.I), "")
            ],
            "uri": "http://www.pingdom.com/"
        },
        {
            "icon": "robot_pinseri.png",
            "title": "Pinseri",
            "rule" : [
                (re.compile("www\.pinseri\.com/bloglist", re.I), "")
            ]
        },
        {
            "icon": "robot_plagger.png",
            "title": "Plagger",
            "rule" : [
                (re.compile("Plagger[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.plugger.org"
        },
        {
            "icon": "robot_planet.png",
            "title": "Planet",
            "rule" : [
                (re.compile("Planet[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "PlantyNet",
            "rule" : [
                (re.compile("PlantyNet_WebRobot[_ /]V?([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_pluck.png",
            "title": "Pluck",
            "rule" : [
                (re.compile("PluckFeedCrawler[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_plsearch.png",
            "title": "PlanetSearch",
            "rule" : [
                (re.compile("fido[ /]([0-9.]{1,10}) Harvest", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "POE-Component",
            "rule" : [
                (re.compile("^POE-Component-Client-HTTP[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_pogodak.png",
            "title": "Pogodak",
            "rule" : [
                (re.compile("Pogodak\.hr[/ ]?([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Poodle predictor",
            "rule" : [
                (re.compile("P(oo|ooo)dle[ \-]?predictor[ \-]?([0-9.]{1,10})", re.I), 1),
                (re.compile("P(oo|ooo)dle[ \-]?predictor", re.I), "")
            ],
            "uri": "http://www.gritechnologies.com/tools/spider.go"
        },
        {
            "icon": "robot_pompos.png",
            "title": "Pompos",
            "rule" : [
                (re.compile("Pompos[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Popdexter",
            "rule" : [
                (re.compile("Popdexter", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Powermarks",
            "rule" : [
                (re.compile("Powermarks[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "PROBE!",
            "rule" : [
                (re.compile("^PROBE!", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Proxy Cache",
            "rule" : [
                (re.compile("^Mozilla/[0-9.]{1,10} \(compatible\;\)$", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "ProxyHunter",
            "rule" : [
                (re.compile("ProxyHunter", re.I), "")
            ]
        },
        {
            "icon": "robot_picsearch.png",
            "title": "PicSearch",
            "rule" : [
                (re.compile("^psbot", re.I), "")
            ]
        },
        {
            "icon": "robot_pubsub.png",
            "title": "PubSub",
            "rule" : [
                (re.compile("^PubSub-RSS-Reader[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("^PubSub\.com", re.I), "")
            ]
        },
        {
            "icon": "robot_pukiwiki.png",
            "title": "PukiWiki",
            "rule" : [
                (re.compile("PukiWiki[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_pwebotxy.png",
            "title": "PWeBot/X.Y",
            "rule" : [
                (re.compile("^PWeBot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.programacionweb.net/robot.php"
        },
        {
            "icon": "robot_robot.png",
            "title": "PXYS",
            "rule" : [
                (re.compile("^pxys", re.I), "")
            ]
        },
        {
            "icon": "robot_qango.png",
            "title": "Qango",
            "rule" : [
                (re.compile("^Qango.com", re.I), "")
            ],
            "uri": "http://www.quango.com/"
        },
        {
            "icon": "robot_qihoo.png",
            "title": "Qihoo",
            "rule" : [
                (re.compile("QihooBot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.qihoo.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Quantcast",
            "rule" : [
                (re.compile("Quantcastbot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.quantcast.com/"
        },
        {
            "icon": "robot_quepasa.png",
            "title": "Quepasa",
            "rule" : [
                (re.compile("Quepasa[ \-]?Creep", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "QuestFinder",
            "rule" : [
                (re.compile("www\.questfinder\.com", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Qweery",
            "rule" : [
                (re.compile("^QweeryBot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://qweerybot.qweery.nl"
        },
        {
            "icon": "robot_rambler.png",
            "title": "Rambler",
            "rule" : [
                (re.compile("StackRambler[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "ramiba",
            "rule" : [
                (re.compile("^ramiba(-bot)?", re.I), 1)
            ]
        },
        {
            "icon": "robot_rediff.png",
            "title": "rediff",
            "rule" : [
                (re.compile("^RedBot/redbot[ -/]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.rediff.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Repia",
            "rule" : [
                (re.compile("webmaster@repia\.com", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Robozilla",
            "rule" : [
                (re.compile("Robozilla", re.I), "")
            ]
        },
        {
            "icon": "robot_rojo.png",
            "title": "Rojo",
            "rule" : [
                (re.compile("Rojo[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_rss.png",
            "title": "rss-bot",
            "rule" : [
                (re.compile("rss-bot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_rssbandit.png",
            "title": "RssBandit",
            "rule" : [
                (re.compile("RssBandit[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_rss.png",
            "title": "rssImages",
            "rule" : [
                (re.compile("rssImagesBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_rssmicro.png",
            "title": "RSSMicro",
            "rule" : [
                (re.compile("RSSMicro\.com", re.I), "")
            ],
            "uri": "http://www.rssmicro.com"
        },
        {
            "icon": "robot_rssowl.png",
            "title": "RSSOwl",
            "rule" : [
                (re.compile("RSSOwl[ /]([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_rss.png",
            "title": "RssReader",
            "rule" : [
                (re.compile("RssReader[ /]([0-9.]{1,10})", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "RufusBot",
            "rule" : [
                (re.compile("RufusBot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Sansz",
            "rule" : [
                (re.compile("SanszBot", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "robot_saucereader.png",
            "title": "Sauce Reader",
            "rule" : [
                (re.compile("Sauce[ ]?Reader[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_sbider.png",
            "title": "SBIder",
            "rule" : [
                (re.compile("SBIder[/ ]([0-9.]{1,10})", re.I), 1),
                (re.compile("SBIder[/ ]SBIder.([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Scirus",
            "rule" : [
                (re.compile("FAST-WebCrawler/[0-9a-z.]{1,10}/Scirus", re.I), "")
            ]
        },
        {
            "icon": "robot_scrubby.png",
            "title": "Scrubby",
            "rule" : [
                (re.compile("Scrubby[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_sdm.png",
            "title": "SUN Download Manager",
            "rule" : [
                (re.compile("Sun Download Manager[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Sea Links",
            "rule" : [
                (re.compile("SEA-Links( HTML-Scanner Pingoo\!)?[ /]([0-9.]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Search.ch",
            "rule" : [
                (re.compile("search\.ch[ /]?V?([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "SearchEngineWorld",
            "rule" : [
                (re.compile("searchengineworld", re.I), "")
            ],
            "uri": "http://www.searchengineworld.com/"
        },
        {
            "icon": "robot_searchhippo.png",
            "title": "Searchhippo",
            "rule" : [
                (re.compile("searchhippo", re.I), "")
            ],
            "uri": "http://www.searchhippo.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "SearchThruUs",
            "rule" : [
                (re.compile("www\.unitek-systems\.co\.uk[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Secure Computing",
            "rule" : [
                (re.compile("securecomputing", re.I), "")
            ]
        },
        {
            "icon": "robot_seekport.png",
            "title": "Seekport",
            "rule" : [
                (re.compile("Seekbot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Semantic Discovery",
            "rule" : [
                (re.compile("semanticdiscovery[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_sensis.png",
            "title": "Sensis",
            "rule" : [
                (re.compile("^Sensis(.com.au)? Web Crawler", re.I), "")
            ],
            "uri": "http://sensis.com.au"
        },
        {
            "icon": "robot_seznam.png",
            "title": "Seznam",
            "rule" : [
                (re.compile("SeznamBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_sharpreader.png",
            "title": "SharpReader",
            "rule" : [
                (re.compile("SharpReader[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Sherlock Spider",
            "rule" : [
                (re.compile("sherlock_spider", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Shim Crawler",
            "rule" : [
                (re.compile("shim[ \-]crawler", re.I), "")
            ]
        },
        {
            "icon": "robot_shopwiki.png",
            "title": "ShopWiki",
            "rule" : [
                (re.compile("^ShopWiki[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Shoula",
            "rule" : [
                (re.compile("^Shoula.com Crawler ([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.shoula.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Siege",
            "rule" : [
                (re.compile("Siege[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Siets",
            "rule" : [
                (re.compile("SietsCrawler[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_simpy.png",
            "title": "Simpy",
            "rule" : [
                (re.compile("^(argus|simpy)[ /]([0-9.]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "robot_singingfish.png",
            "title": "SingingFish",
            "rule" : [
                (re.compile("asterias[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("Asterias Crawler v([0-9.]{1,10})", re.I), 1),
                (re.compile("asterias", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Sirketce",
            "rule" : [
                (re.compile("Sirketcebot[ /v]+([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.sirketce.com/bot.html"
        },
        {
            "icon": "robot_robot.png",
            "title": "SiroBot",
            "rule" : [
                (re.compile("sirobot", re.I), "")
            ]
        },
        {
            "icon": "robot_sitebar.png",
            "title": "SiteBar",
            "rule" : [
                (re.compile("SiteBar[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_sitesell.png",
            "title": "SiteSell",
            "rule" : [
                (re.compile("SBIder[/ ]([0-9a-z.\-]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "SiteSpider",
            "rule" : [
                (re.compile("^SiteSpider", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "SitiDi",
            "rule" : [
                (re.compile("SitiDiBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Skaffe",
            "rule" : [
                (re.compile("Skampy[ /]([0-9.\-]{1,10})", re.I), 1)
            ],
            "uri": "http://www.skaffe.com"
        },
        {
            "icon": "robot_skizzle.png",
            "title": "Skizzle",
            "rule" : [
                (re.compile("SKIZZLE! Distributed Internet Spider[ /v]+([0-9a-z.\-]{1,10})", re.I), 1)
            ],
            "uri": "http://www.skizzle.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "slugch",
            "rule" : [
                (re.compile("^slug\.ch crawl ([0-9a-z.\-]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Snoopy",
            "rule" : [
                (re.compile("^Snoopy[ &/v]*([0-9.]{1,10})", re.I), 1),
                (re.compile("sna-([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://snoopy.sourceforge.net/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Snyke",
            "rule" : [
                (re.compile("^SnykeBot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.snyke.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Slider",
            "rule" : [
                (re.compile("^Slider[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_soegning.png",
            "title": "S&oslash;gning",
            "rule" : [
                (re.compile("soegning\.dk[/ ]spider[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_other.png",
            "title": "somewhere.com",
            "rule" : [
                (re.compile("Mozilla\@somewhere\.com", re.I), 1)
            ],
            "uri": "http://www.somewhere.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "SmartWareSoft",
            "rule" : [
                (re.compile("^SWSBot-Images[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.smartwaresoft.com/swsbot12.html"
        },
        {
            "icon": "robot_soft411.png",
            "title": "Soft411",
            "rule" : [
                (re.compile("SOFT411 Directory", re.I), "")
            ]
        },
        {
            "icon": "robot_sogou.png",
            "title": "Sogou",
            "rule" : [
                (re.compile("Sogou web spider[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.sogou.com/docs/help/webmasters.htm#07"
        },
        {
            "icon": "robot_robot.png",
            "title": "Sohu",
            "rule" : [
                (re.compile("sohu[ \-](agent|search)", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Sopheus",
            "rule" : [
                (re.compile("Sopheus Project[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.thenetplanet.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "SoupPot",
            "rule" : [
                (re.compile("SoupPotBot", re.I), "")
            ]
        },
        {
            "icon": "robot_specificmedia.png",
            "title": "Specific Media",
            "rule" : [
                (re.compile("^SMBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_spherescout.png",
            "title": "Sphere Scout",
            "rule" : [
                (re.compile("^Sphere Scout[ &/v]*([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.sphere.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "sproose",
            "rule" : [
                (re.compile("^sproose[ /]([0-9a-z.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.sproose.com/bot.html"
        },
        {
            "icon": "robot_robot.png",
            "title": "SpurlBot",
            "rule" : [
                (re.compile("SpurlBot[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_stardownloader.png",
            "title": "Star Downloader",
            "rule" : [
                (re.compile("^Star Downloader( Pro)?", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Steeler",
            "rule" : [
                (re.compile("Steeler[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_strategicboard.png",
            "title": "Strategic Board",
            "rule" : [
                (re.compile("Strategic Board Bot", re.I), "")
            ],
            "uri": "http://www.strategicboard.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "suchbaer.de",
            "rule" : [
                (re.compile("^suchbaer\.de", re.I), "")
            ],
            "uri": "http://www.suchbaer.de/"
        },
        {
            "icon": "robot_robot.png",
            "title": "suchbot",
            "rule" : [
                (re.compile("^suchbot", re.I), "")
            ]
        },
        {
            "icon": "robot_suchende.png",
            "title": "suchen.de",
            "rule" : [
                (re.compile("^gonzo([0-9]{1,2}).*www.suchen.de", re.I), 1)
            ],
            "uri": "http://www.suchen.de/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Suchknecht",
            "rule" : [
                (re.compile("^Suchknecht.at-Robot", re.I), "")
            ],
            "uri": "http://www.suchknecht.at/"
        },
        {
            "icon": "robot_robot.png",
            "title": "suchpad",
            "rule" : [
                (re.compile("^suchpadbot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.suchpad.de"
        },
        {
            "icon": "robot_sunrise.png",
            "title": "Sunrise",
            "rule" : [
                (re.compile("Sunrise[ /]([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_superbot.png",
            "title": "SuperBot",
            "rule" : [
                (re.compile("SuperBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "SurfControl",
            "rule" : [
                (re.compile("SurfControl", re.I), ""),
                (re.compile("ScSpider[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "SURFnet",
            "rule" : [
                (re.compile("AVSearch[ \-]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Surfsafely",
            "rule" : [
                (re.compile("Submission Spider at surfsafely.com", re.I), "")
            ],
            "uri": "http://www.surfsafely.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Whois Survey",
            "rule" : [
                (re.compile("SurveyBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Swoogle",
            "rule" : [
                (re.compile("^Swooglebot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://swoogle.umbc.edu/swooglebot.htm"
        },
        {
            "icon": "robot_robot.png",
            "title": "SWSE",
            "rule" : [
                (re.compile("sw\.deri\.org", re.I), "")
            ],
            "uri": "http://sw.deri.org/2006/04/multicrawler/robots.html"
        },
        {
            "icon": "robot_sygol.png",
            "title": "Sygol",
            "rule" : [
                (re.compile("www.sygol.(com|net)", re.I), "")
            ],
            "uri": "http://www.sygol.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Synapse",
            "rule" : [
                (re.compile(" Synapse\)", re.I), "")
            ],
            "uri": "http://ws.apache.org/synapse/"
        },
        {
            "icon": "robot_robot.png",
            "title": "sync2it",
            "rule" : [
                (re.compile("^\!Susie", re.I), "")
            ],
            "uri": "http://www.sync2it.com/bms/susie.php"
        },
        {
            "icon": "robot_robot.png",
            "title": "syncit",
            "rule" : [
                (re.compile("^SyncIT[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.syncit.com/"
        },
        {
            "icon": "robot_syndic8.png",
            "title": "Syndic8",
            "rule" : [
                (re.compile("Syndic8[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.syndic8.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Syndicatie.nl",
            "rule" : [
                (re.compile("Syndicatie\.nl robot v ([0-9.]{1,10})", re.I), 1),
                (re.compile("Syndicatie\.nl robot;", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Synomia",
            "rule" : [
                (re.compile("^SynoBot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "SynooBot",
            "rule" : [
                (re.compile("SynooBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_szukacz.png",
            "title": "Szukacz",
            "rule" : [
                (re.compile("Szukacz[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_tagword.png",
            "title": "Tagword",
            "rule" : [
                (re.compile("^Tagword", re.I), "")
            ],
            "uri": "http://tagword.com/dmoz_survey.php"
        },
        {
            "icon": "robot_robot.png",
            "title": "Tamu Crawler",
            "rule" : [
                (re.compile("IRLbot[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("TAMU_CS_IRL_CRAWLER[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "TargetSeek",
            "rule" : [
                (re.compile("TargetSeek[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.targetgroups.net/TargetSeek.html"
        },
        {
            "icon": "robot_tcd.png",
            "title": "Trinity College Dublin",
            "rule" : [
                (re.compile("^TCDBOT/Nutch-([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.tcd.ie"
        },
        {
            "icon": "robot_technorati.png",
            "title": "Technorati",
            "rule" : [
                (re.compile("Technoratibot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_teleport.png",
            "title": "Teleport",
            "rule" : [
                (re.compile("Teleport[ \-]?Pro", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Terrar",
            "rule" : [
                (re.compile("^Fresh Search :: Terrar", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Theophrastus",
            "rule" : [
                (re.compile("Theophrastus[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://users.cs.cf.ac.uk/N.A.Smith/theophrastus.php"
        },
        {
            "icon": "robot_robot.png",
            "title": "thumbnails.cz",
            "rule" : [
                (re.compile("^thumbnail\.cz robot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "thumbshots",
            "rule" : [
                (re.compile("^thumbshots.*(Version: |v)([0-9.]{2,10})e", re.I), 1),
                (re.compile("^thumbshots-de", re.I), "")
            ],
            "uri": "http://www.thumbshots.de"
        },
        {
            "icon": "robot_thunderbird.png",
            "title": "Thunderbird",
            "rule" : [
                (re.compile("Thunderbird[ /]([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_thunderstone.png",
            "title": "Thunderstone",
            "rule" : [
                (re.compile("T-H-U-N-D-E-R-S-T-O-N-E", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "timboBot",
            "rule" : [
                (re.compile("timboBot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "trayce",
            "rule" : [
                (re.compile("traycebot[ /]([0-9a-z.\-]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Tricus",
            "rule" : [
                (re.compile("B_l_i_t_z_B_O_T_@_t_r_i_c_u_s_\._c_o_m", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Topicblogs",
            "rule" : [
                (re.compile("topicblogs[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "T&Uuml;zilla",
            "rule" : [
                (re.compile("tuezilla.de", re.I), "")
            ],
            "uri": "http://tuezilla.de/t_st-odp-entries-agent.html"
        },
        {
            "icon": "robot_turnitin.png",
            "title": "Turnitin",
            "rule" : [
                (re.compile("TurnitinBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "TutorGig",
            "rule" : [
                (re.compile("TutorGig(Bot)?[ /]([0-9.]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "robot_cuill.png",
            "title": "cuill",
            "rule" : [
                (re.compile("Twiceler[ /-]([0-9.]{1,10})", re.I), 1),
                (re.compile("Twiceler", re.I), "")
            ],
            "uri": "http://www.cuill.com/twiceler/robot.html"
        },
        {
            "icon": "robot_typepad.png",
            "title": "TypePad",
            "rule" : [
                (re.compile("TypePad/([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "UdmSearch",
            "rule" : [
                (re.compile("UdmSearch[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_ukwizz.png",
            "title": "UKWizz",
            "rule" : [
                (re.compile("^Mackster.*ukwizz", re.I), "")
            ],
            "uri": "http://www.ukwizz.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Ultraseek",
            "rule" : [
                (re.compile("Ultraseek", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "UltraSpider",
            "rule" : [
                (re.compile("UltraSpider3000[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.search.ch"
        },
        {
            "icon": "robot_robot.png",
            "title": "umai",
            "rule" : [
                (re.compile("umai[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "Unchaos",
            "rule" : [
                (re.compile("unchaos_crawler[_ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("unchaos", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "unido",
            "rule" : [
                (re.compile("^unido-bot", re.I), 1)
            ],
            "uri": "http://mobicom.cs.uni-dortmund.de/bot.html"
        },
        {
            "icon": "robot_robot.png",
            "title": "Updated",
            "rule" : [
                (re.compile("updated[ /]([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "UptimeBot",
            "rule" : [
                (re.compile("^UptimeBot", re.I), "")
            ],
            "uri": "http://www.uptimebot.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "URI::Fetch",
            "rule" : [
                (re.compile("^URI::Fetch[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "URLBase",
            "rule" : [
                (re.compile("URLBase[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "URLBlaze",
            "rule" : [
                (re.compile("^URLBlaze", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "MS URL Control",
            "rule" : [
                (re.compile("Microsoft URL[ \-]?Control", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "URLGetFile",
            "rule" : [
                (re.compile("^URLGetFile", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "UrlScope",
            "rule" : [
                (re.compile("UrlScope", re.I), "")
            ]
        },
        {
            "icon": "robot_urltrends.png",
            "title": "urltrends",
            "rule" : [
                (re.compile("Snappy/([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_usww.png",
            "title": "usww",
            "rule" : [
                (re.compile("usww\.com", re.I), ""),
                (re.compile("Mozilla/5\.0 URL-Spider", re.I), "")
            ],
            "uri": "http://www.usww.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "USyd-NLP-Spider",
            "rule" : [
                (re.compile("^USyd-NLP-Spider", re.I), "")
            ],
            "uri": "http://www.it.usyd.edu.au/~vinci/bot.html"
        },
        {
            "icon": "robot_wiseguys.png",
            "title": "WiseGuys",
            "rule" : [
                (re.compile("Vagabondo[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("Vagabondo-WAP[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_validator.png",
            "title": "W3C Validator",
            "rule" : [
                (re.compile("W3C_Validator[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Verity",
            "rule" : [
                (re.compile("^vspider[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("^vspider", re.I), "")
            ],
            "uri": "http://www.verity.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Versions-project",
            "rule" : [
                (re.compile("InfoFly[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.versions-project.org/"
        },
        {
            "icon": "robot_robot.png",
            "title": "VerticalMatch",
            "rule" : [
                (re.compile("^VMBot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.VerticalMatch.com/"
        },
        {
            "icon": "robot_validator.png",
            "title": "Verzamelgids",
            "rule" : [
                (re.compile("Verzamelgids[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.verzamelgids.nl/"
        },
        {
            "icon": "robot_vestris.png",
            "title": "Vestris",
            "rule" : [
                (re.compile("AlkalineBOT[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://alkaline.vestris.com/"
        },
        {
            "icon": "robot_vindex.png",
            "title": "Vindex",
            "rule" : [
                (re.compile("Vindex[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Visvo",
            "rule" : [
                (re.compile("VisBot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.visvo.com"
        },
        {
            "icon": "robot_voila.png",
            "title": "Voila",
            "rule" : [
                (re.compile("VoilaBot[ /]?[a-z ]*([0-9.]{1,10})", re.I), 1),
                (re.compile("VoilaBot;[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Vonna",
            "rule" : [
                (re.compile("Vonna.com b o t", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Vortex",
            "rule" : [
                (re.compile("Vortex[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://marty.anstey.ca/robots/vortex/"
        },
        {
            "icon": "robot_w3sitesearch.png",
            "title": "W3SiteSearch",
            "rule" : [
                (re.compile("^W3SiteSearch Crawler[\_v]*([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.w3sitesearch.de"
        },
        {
            "icon": "robot_robot.png",
            "title": "Wagger",
            "rule" : [
                (re.compile("^Waggr", re.I), "")
            ],
            "uri": "http://www.waggr.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Wanadoo",
            "rule" : [
                (re.compile("^SurferF3[ /]([0-9./]{1,10})", re.I), 1)
            ],
            "uri": "http://www.wanadoo.fr/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Wapalizer",
            "rule" : [
                (re.compile("wapalizer[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.wapdrive.com/"
        },
        {
            "icon": "robot_addy.png",
            "title": "Dr.Watson",
            "rule" : [
                (re.compile("Watson[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("watson\.addy\.com", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Wavefire",
            "rule" : [
                (re.compile("^Wavefire[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_waypath.png",
            "title": "Waypath",
            "rule" : [
                (re.compile("Waypath[ \-]?Scout", re.I), ""),
                (re.compile("Waypath (development )?crawler", re.I), "")
            ]
        },
        {
            "icon": "robot_wdg.png",
            "title": "WDG Validator",
            "rule" : [
                (re.compile("^WDG_(Site)?Validator[/ ]([0-9.]{1,10})", re.I), 2)
            ],
            "uri": "http://www.htmlhelp.com/tools/validator/"
        },
        {
            "icon": "robot_webagogo.png",
            "title": "Webagogo",
            "rule" : [
                (re.compile("^Webagogo", re.I), 1)
            ],
            "uri": "http://www.webagogo.be/"
        },
        {
            "icon": "robot_webalta.png",
            "title": "WebAlta",
            "rule" : [
                (re.compile("^WebAlta( Crawler)?[/ ]([0-9.]{1,10})", re.I), 2)
            ],
            "uri": "http://www.webalta.net/ru/about_webmaster.html"
        },
        {
            "icon": "robot_robot.png",
            "title": "Webbot.ru",
            "rule" : [
                (re.compile(" Webbot[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.webbot.ru/bot.html"
        },
        {
            "icon": "robot_robot.png",
            "title": "WebCapture",
            "rule" : [
                (re.compile("WebCapture[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Webcollage",
            "rule" : [
                (re.compile("webcollage", re.I), "")
            ]
        },
        {
            "icon": "robot_webcopier.png",
            "title": "WebCopier",
            "rule" : [
                (re.compile("WebCopier[/ ]v?([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "WebCrawl",
            "rule" : [
                (re.compile("webcrawl\.net", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Web Downloader",
            "rule" : [
                (re.compile("Web Downloader[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "webfetch",
            "rule" : [
                (re.compile("^webfetch[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Webfind",
            "rule" : [
                (re.compile("^WebFindBot", re.I), "")
            ],
            "uri": "http://www.web-find.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Webglimpse",
            "rule" : [
                (re.compile("^Webglimpse[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://webglimpse.net"
        },
        {
            "icon": "robot_robot.png",
            "title": "webGobbler",
            "rule" : [
                (re.compile("^webGobbler[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "WebLight",
            "rule" : [
                (re.compile("^WebLight[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.illumit.com/Products/weblight/"
        },
        {
            "icon": "robot_robot.png",
            "title": "WebLink's",
            "rule" : [
                (re.compile("^Weblink.s checker", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "Webmeasurement",
            "rule" : [
                (re.compile("^webmeasurement-bot", re.I), "")
            ],
            "uri": "http://rvs.informatik.uni-leipzig.de"
        },
        {
            "icon": "robot_robot.png",
            "title": "WebMiner",
            "rule" : [
                (re.compile("^WebMiner[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_webmin.png",
            "title": "Webmin",
            "rule" : [
                (re.compile("^webmin", re.I), "")
            ]
        },
        {
            "icon": "robot_webmon.png",
            "title": "Webmon",
            "rule" : [
                (re.compile("WebMon[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.markwell.btinternet.co.uk/webmon/"
        },
        {
            "icon": "robot_webpatrol.png",
            "title": "WebPatrol",
            "rule" : [
                (re.compile("^WebPatrol[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://soft.macfeeling.com/WebPatrol.html"
        },
        {
            "icon": "robot_webpix.png",
            "title": "WebPix",
            "rule" : [
                (re.compile("WebPix[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "WebRACE",
            "rule" : [
                (re.compile("^WebRACE[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_webreaper.png",
            "title": "WebReaper",
            "rule" : [
                (re.compile("^WebReaper ", re.I), "")
            ],
            "uri": "http://www.webreaper.net/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Webresult",
            "rule" : [
                (re.compile("Der webresult\.de Robot", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Webring Checker",
            "rule" : [
                (re.compile("WebRingChecker[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": " WeBoX",
            "rule" : [
                (re.compile("WeBoX[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_websearchau.png",
            "title": "WebSearch.COM.AU",
            "rule" : [
                (re.compile("WebSearch.COM.AU[/ ]+([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://WebSearch.com.au/"
        },
        {
            "icon": "robot_robot.png",
            "title": "WebSearchBench",
            "rule" : [
                (re.compile("WebSearchBench WebCrawler[v/ ]+([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://websearchbench.cs.uni-dortmund.de/"
        },
        {
            "icon": "robot_websense.png",
            "title": "Websense",
            "rule" : [
                (re.compile("(Sqworm|websense|Konqueror/3\.(0|1)(\-rc[1-6])?; i686 Linux; 2002[0-9]{4})", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "WebsiteWorth",
            "rule" : [
                (re.compile("WebsiteWorth[v/ ]+([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://directory.sootle.com/website-worth/tata.php"
        },
        {
            "icon": "robot_websquash.png",
            "title": "Websquash",
            "rule" : [
                (re.compile("webs(quash\.com|ite[ \-]?Monitor)", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "WebStripper",
            "rule" : [
                (re.compile("WebStripper[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_webzip.png",
            "title": "WebZIP",
            "rule" : [
                (re.compile("Web[ \-]?ZIP[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "WEP Search",
            "rule" : [
                (re.compile("WEP Search[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "West Wind Internet Protocols",
            "rule" : [
                (re.compile("^West Wind Internet Protocols[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.west-wind.com/wwipstuff.asp"
        },
        {
            "icon": "robot_wget.png",
            "title": "Wget",
            "rule" : [
                (re.compile("Wget[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_whizbang.png",
            "title": "WhizBang",
            "rule" : [
                (re.compile("WhizBang", re.I), "")
            ],
            "uri": "http://www.whizbang.com/crawler/"
        },
        {
            "icon": "robot_robot.png",
            "title": "WingFlyer",
            "rule" : [
                (re.compile("^WebFetch", re.I), "")
            ],
            "uri": "http://www.wingflyer.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "WinInet",
            "rule" : [
                (re.compile("TeamSoft WinInet Component", re.I), "")
            ],
            "uri": "http://www.winsoft.sk/wininet.htm"
        },
        {
            "icon": "robot_robot.png",
            "title": "WinHTTP",
            "rule" : [
                (re.compile("WinHttp\.WinHttpRequest\.([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "robot_robot.png",
            "title": "WIRE",
            "rule" : [
                (re.compile("^WIRE[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "WMP",
            "rule" : [
                (re.compile("^WMP", re.I), "")
            ]
        },
        {
            "icon": "robot_wordpress.png",
            "title": "WordPress",
            "rule" : [
                (re.compile("WordPress[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_worldlight.png",
            "title": "WorldLight",
            "rule" : [
                (re.compile("^WorldLight", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "WorQmada",
            "rule" : [
                (re.compile("WorQmada[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_wotbox.png",
            "title": "Wotbox",
            "rule" : [
                (re.compile("Wotbox[ /]?[a-z]*([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_wp.png",
            "title": "Wirtualna Polska",
            "rule" : [
                (re.compile("NetSprint[ /\-]{1,4}([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://wp.pl"
        },
        {
            "icon": "robot_robot.png",
            "title": "WebSearchBench",
            "rule" : [
                (re.compile("WSB WebCrawler V([0-9.]{1,10})", re.I), 1),
                (re.compile("WSB ", re.I), "")
            ],
            "uri": "http://websearchbench.cs.uni-dortmund.de/"
        },
        {
            "icon": "robot_robot.png",
            "title": "WUME Lab's",
            "rule" : [
                (re.compile("^wume_crawler[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://wume.cse.lehigh.edu/~xiq204/crawler/"
        },
        {
            "icon": "robot_wusage.png",
            "title": "Wusage",
            "rule" : [
                (re.compile("Wusage[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.boutell.com/wusage/"
        },
        {
            "icon": "robot_wwgrapevine.png",
            "title": "WWgrapevine",
            "rule" : [
                (re.compile("wwgrapevine[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "WWSBOT",
            "rule" : [
                (re.compile("WWSBOT[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.analyzer.nu"
        },
        {
            "icon": "robot_robot.png",
            "title": "www4mail",
            "rule" : [
                (re.compile("^www4mail[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.www4mail.org/"
        },
        {
            "icon": "robot_wwwc.png",
            "title": "WWWC",
            "rule" : [
                (re.compile("^WWWC[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "WWWD",
            "rule" : [
                (re.compile("^WWWD[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_wwweasel.png",
            "title": "WWWeasel",
            "rule" : [
                (re.compile("WWWeasel( Robot)?[/ ]v?([0-9.]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "robot_wwwfi.png",
            "title": "www.fi",
            "rule" : [
                (re.compile("www\.fi crawler", re.I), "")
            ],
            "uri": "http://www.fi/"
        },
        {
            "icon": "robot_robot.png",
            "title": "WWW-Mechanize",
            "rule" : [
                (re.compile("^WWW-Mechanize[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "WWWoffle",
            "rule" : [
                (re.compile("^wwwoffle[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "WWWster",
            "rule" : [
                (re.compile("^wwwster[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_wysigot.png",
            "title": "Wysigot",
            "rule" : [
                (re.compile("Wysigot[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_xaldon.png",
            "title": "Xaldon",
            "rule" : [
                (re.compile("Xaldon WebSpider", re.I), "")
            ],
            "uri": "http://www.xaldon.de/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Xenu Link Sleuth",
            "rule" : [
                (re.compile("Xenu(&#039;s)? Link Sleuth[/ ]([0-9a-z.]{1,10})", re.I), 1),
                (re.compile("Xenu_Link_Sleuth_([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_xerka.png",
            "title": "Xerka",
            "rule" : [
                (re.compile("^Xerka WebBot v([0-9a-z.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.diana-teknologia.com/www1/english/xerka.htm"
        },
        {
            "icon": "robot_robot.png",
            "title": "XIRQ",
            "rule" : [
                (re.compile("^xirq[ /]([0-9a-z.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.xirq.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "XMLSlurp",
            "rule" : [
                (re.compile("^XMLSlurp[ /]([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Trackback",
            "rule" : [
                (re.compile("XMLRPC", re.I), "")
            ]
        },
        {
            "icon": "robot_yacy.png",
            "title": "Yacy",
            "rule" : [
                (re.compile("yacy\.net", re.I), "")
            ]
        },
        {
            "icon": "robot_yahoo.png",
            "title": "Yahoo",
            "rule" : [
                (re.compile("Yahoo(! ([a-z]{1,3} )?Slurp|-|FeedSeeker)", re.I), ""),
                (re.compile("Yahoo-MMCrawler[/ ]([0-9a-z.]{1,10})", re.I), 1),
                (re.compile("Yahoo-VerticalCrawler-FormerWebCrawler[/ ]([0-9a-z.]{1,10})", re.I), 1),
                (re.compile("^AnzwersCrawl[/ ]([0-9a-z.]{1,10})", re.I), 1),
                (re.compile("Y!J(-BSC|-SRD)*[/ ]([0-9a-z.]{1,10})", re.I), 2),
                (re.compile("Y!OASIS/TEST", re.I), ""),
                (re.compile("Harvest-NG[/ ]([0-9a-z.]{1,10})", re.I), 1),
                (re.compile("Y!J; for robot study", re.I), ""),
                (re.compile("Yahoo Japan; for robot study", re.I), "")
            ],
            "uri": "http://www.yahoo.com"
        },
        {
            "icon": "robot_yandex.png",
            "title": "Yandex",
            "rule" : [
                (re.compile("Yandex[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Yarienavoir",
            "rule" : [
                (re.compile("^yarienavoir.net[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.yarienavoir.net/"
        },
        {
            "icon": "robot_yell.png",
            "title": "Yell",
            "rule" : [
                (re.compile("YellCrawl[ /]V?([0-9.]{1,10})", re.I), 1),
                (re.compile("Yellbot[ /]Nutch-([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Yodao",
            "rule" : [
                (re.compile("YodaoBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_yoogli.png",
            "title": "Yoogli",
            "rule" : [
                (re.compile("yoogliFetchAgent[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.yoogli.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Yotta",
            "rule" : [
                (re.compile("Yotta(Shopping|Cars)_Bot[ /]([0-9.]{1,10})", re.I), 2),
                (re.compile("OmniExplorer_Bot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.yottacars.com"
        },
        {
            "icon": "robot_yoono.png",
            "title": "Yoono",
            "rule" : [
                (re.compile("Yoono", re.I), "")
            ],
            "uri": "http://www.yoono.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "yuntis",
            "rule" : [
                (re.compile("Gulper Web Bot[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://yuntis.ecsl.cs.sunysb.edu/help/robot/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Zao",
            "rule" : [
                (re.compile("Zao[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("Zao-crawler", re.I), "")
            ]
        },
        {
            "icon": "robot_zeal.png",
            "title": "ZealBot",
            "rule" : [
                (re.compile("Zealbot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_zearchit.png",
            "title": "Zearchit",
            "rule" : [
                (re.compile("Zearchit", re.I), "")
            ],
            "uri": "http://www.zearchit.de/"
        },
        {
            "icon": "robot_robot.png",
            "title": "ze.bz",
            "rule" : [
                (re.compile("^ZeBot_(lseek\.net|www\.ze\.bz)", re.I), "")
            ],
            "uri": "http://www.ze.bz/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Zedzo",
            "rule" : [
                (re.compile("zedzo.digest[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.zedzo.com/"
        },
        {
            "icon": "robot_zerx.png",
            "title": "Zerx",
            "rule" : [
                (re.compile("^zerxbot[ /](Version|v)*[ /]*([0-9.]{1,10})", re.I), 2)
            ],
            "uri": "http://www.zerx.com/"
        },
        {
            "icon": "robot_zeus.png",
            "title": "Zeus",
            "rule" : [
                (re.compile("Zeus", re.I), "")
            ],
            "uri": "http://www.zeus.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Zippp",
            "rule" : [
                (re.compile("ZipppBot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Zippy",
            "rule" : [
                (re.compile("^Zippy[ v/]*([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.zippyfinder.com"
        },
        {
            "icon": "robot_robot.png",
            "title": "Zoeky",
            "rule" : [
                (re.compile("Zoekybot[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_zyborg.png",
            "title": "WiseNutBot",
            "rule" : [
                (re.compile("(WISE|Zy)bo(rg|t)[ /]([0-9.]{1,10})", re.I), 3)
            ]
        },
        {
            "icon": "robot_zoom.png",
            "title": "zspider",
            "rule" : [
                (re.compile("^ZoomSpider", re.I), "")
            ],
            "uri": "http://www.wrensoft.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "zspider",
            "rule" : [
                (re.compile("zspider[ /]([0-9.a-z]{1,10})", re.I), 1)
            ],
            "uri": "http://feedback.redkolibri.com/"
        },
        {
            "icon": "robot_blogbot.png",
            "title": "BlogBot",
            "rule" : [
                (re.compile("Blog[ \-]?Bot", re.I), "")
            ],
            "uri": "http://www.blogbot.com/"
        },
        {
            "icon": "robot_robot.png",
            "title": "HTTPClient",
            "rule" : [
                (re.compile("HTTP[ \-]?Client[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("HTTP[ \-]?Client", re.I), "")
            ],
            "uri": "http://www.innovation.ch/java/HTTPClient/"
        },
        {
            "icon": "robot_robot.png",
            "title": "IncyWincy",
            "rule" : [
                (re.compile("^IncyWincy[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("^IncyWincy", re.I), "")
            ]
        },
        {
            "icon": "robot_java.png",
            "title": "Java",
            "rule" : [
                (re.compile("^java[ /]*([0-9.a-z]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Libfetch",
            "rule" : [
                (re.compile("^(fetch )?libfetch[ /]([0-9.]{1,10})", re.I), 2)
            ],
            "uri": "http://www.freebsd.org/"
        },
        {
            "icon": "robot_libwww.png",
            "title": "libWWW",
            "rule" : [
                (re.compile("^libww(w|w-perl|w-FM)[ /]([0-9.]{1,10})", re.I), 2),
                (re.compile("^libww(w|w-perl|w-FM)", re.I), ""),
                (re.compile("MyApp.*libww(w|w-perl|w-FM)", re.I), "")
            ]
        },
        {
            "icon": "robot_nutchorg.png",
            "title": "Nutch",
            "rule" : [
                (re.compile("Nutc(hOrg|hCVS|h)?[ /]([0-9.]{1,10})", re.I), 2),
                (re.compile("Nutch", re.I), "")
            ],
            "uri": "http://lucene.apache.org/nutch/"
        },
        {
            "icon": "robot_robot.png",
            "title": "Python-url",
            "rule" : [
                (re.compile("Python[ \-]?urllib", re.I), "")
            ]
        },
        {
            "icon": "robot_google.png",
            "title": "Google-Proxy",
            "rule" : [
                (re.compile("Google CHTML Proxy[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("Google WAP Proxy[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "icon": "robot_robot.png",
            "title": "SPAM",
            "rule" : [
                (re.compile("NASA Search[/ ]([0-9.]{1,10})", re.I), 1),
                (re.compile("^PHOTO CHECK", re.I), ""),
                (re.compile("^FOTOCHECKER", re.I), ""),
                (re.compile("^IPTC CHECK", re.I), ""),
                (re.compile("^DataCha0s", re.I), ""),
                (re.compile("^Mac Finder", re.I), ""),
                (re.compile("^Missigua Locator[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("^Missouri College Browse", re.I), ""),
                (re.compile("Email[ \-]?Siphon", re.I), ""),
                (re.compile("atSpider", re.I), ""),
                (re.compile("autoemailspider", re.I), ""),
                (re.compile("^Demo Bot", re.I), ""),
                (re.compile("^Program Shareware", re.I), ""),
                (re.compile("^Snapbot", re.I), ""),
                (re.compile("^snap.com", re.I), ""),
                (re.compile("^Guestbook Auto Submitter", re.I), ""),
                (re.compile("panscient.com", re.I), "")
            ]
        },
        {
            "icon": "robot_robot.png",
            "title": "Robot",
            "rule" : [
                (re.compile("(robot|spider|harvest|bot|crawler)", re.I), "")
            ]
        }
    ]



    def robot_from_browserstring(self, browserstring):
        """ Identify the robot from a browserstring

            You get a dict describing the robot with the following fields:
                'title'       The name of the robot
                'icon'        An identifier for an icon describing the robot
                'uri'         A Internet URL that is associated with the robot
                'version'     An additional string that gives the version info

            If the browser string cannot be identified as any robot, None is
            returned
        """

        for robot in self.robots:
            for rule_tuple in robot["rule"]:
                rule = rule_tuple[0]
                versionrule = rule_tuple[1]
                match = rule.search(browserstring)
                if match:
                    title = robot["title"]
                    icon = robot["icon"]
                    uri = ""
                    if robot.has_key("uri"):
                        uri = robot["uri"]
                    version = ""
                    if isinstance(versionrule, int):
                        version = match.group(versionrule)
                    else:
                        version = versionrule
                    # sanity checks to prevent screw-ups from invalid imported data structures:
                    if not isinstance(title, str):
                        warn("Internal error in robot_from_browserstring:")
                        warn("Extracted title for bot was not a string.")
                        warn("browserstring was: %s" % browserstring)
                        title = ""
                    if not isinstance(icon, str):
                        warn("Internal error in robot_from_browserstring:")
                        warn("Extracted icon for bot was not a string.")
                        warn("browserstring was: %s" % browserstring)
                        icon = ""
                    if not isinstance(uri, str):
                        warn("Internal error in robot_from_browserstring:")
                        warn("Extracted uri for bot was not a string.")
                        warn("browserstring was: %s" % browserstring)
                        uri = ""
                    if not isinstance(version, str):
                        warn("Internal error in robot_from_browserstring:")
                        warn("Extracted version for bot was not a string.")
                        warn("browserstring was: %s" % browserstring)
                        version = ""
                    return {
                        'title'   : title,
                        'icon'    : icon,
                        'uri'     : uri,
                        'version' : version
                    }
        return None

