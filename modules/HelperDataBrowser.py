# The data structure used in this file was converted from the BBClone project
# http://bbclone.de/

import re

class BrowserIdentifier(object):
    """ Provides identification of browsers from the browser string
    """

    browsers = [
        {
            "icon": "browser_question.png",
            "title": "1X",
            "rule" : [
                (re.compile("^Science Traveller International 1X[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://jansfreeware.com/jfinternet.htm"
        },
        {
            "icon": "browser_question.png",
            "title": "Abolimba",
            "rule" : [
                (re.compile("www.Abolimba.de", re.I), "")
            ],
            "uri": "http://www.Abolimba.de"
        },
        {
            "icon": "browser_abrowse.png",
            "title": "ABrowse",
            "rule" : [
                (re.compile("abrowse[ /\-]([0-9.]{1,10})", re.I), 1),
                (re.compile("^abrowse", re.I), "")
            ],
            "uri": "http://abrowse.sourceforge.net/"
        },
        {
            "icon": "browser_ace.png",
            "title": "Ace Explorer",
            "rule" : [
                (re.compile("^Ace Explorer", re.I), "")
            ],
            "uri": "http://www.aceexplorer.com/"
        },
        {
            "icon": "browser_question.png",
            "title": "Acorn Browser",
            "rule" : [
                (re.compile("Acorn (Browse|Phoenix)[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.vigay.com/inet/acorn/browse-html.html"
        },
        {
            "icon": "browser_acoo.png",
            "title": "Acoo",
            "rule" : [
                (re.compile("ACOO BROWSER", re.I), "")
            ],
            "uri": "http://www.acoobrowser.com/"
        },
        {
            "icon": "browser_question.png",
            "title": "ActiveWorlds",
            "rule" : [
                (re.compile("Activeworlds[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("Activeworlds", re.I), "")
            ],
            "uri": "/"
        },
        {
            "icon": "browser_akregator.png",
            "title": "Akregator",
            "rule" : [
                (re.compile("akregator/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://akregator.kde.org/"
        },
        {
            "icon": "browser_amaya.png",
            "title": "Amaya",
            "rule" : [
                (re.compile("amaya/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.w3c.org/Amaya/"
        },
        {
            "icon": "browser_question.png",
            "title": "annotate_google",
            "rule" : [
                (re.compile("^annotate_google", re.I), 1)
            ],
            "uri": "http://ponderer.org/download/annotate_google.user.js"
        },
        {
            "icon": "browser_ant.png",
            "title": "ANTFresco",
            "rule" : [
                (re.compile("ANTFresco[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "browser_aol.png",
            "title": "AOL",
            "rule" : [
                (re.compile("aol[ /\-]([0-9.]{1,10})", re.I), 1),
                (re.compile("America Online Browser[ /]([0-9.]{1,10}).*rev([0-9.]{1,10})", re.I), 1),
                (re.compile("aol[ /\-]?browser", re.I), ""),
                (re.compile("AOL-IWENG ([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.aol.com/"
        },
        {
            "icon": "browser_question.png",
            "title": "Aplix",
            "rule" : [
                (re.compile("^Aplix HTTP[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("^Aplix_(SANYO|SEGASATURN)_browser[ /]([0-9.]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "browser_avantbrowser.png",
            "title": "Avant Browser",
            "rule" : [
                (re.compile("Avant[ ]?Browser", re.I), "")
            ],
            "uri": "http://www.avantbrowser.com/"
        },
        {
            "icon": "browser_avantgo.png",
            "title": "AvantGo",
            "rule" : [
                (re.compile("AvantGo[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.avantgo.com/frontdoor/"
        },
        {
            "icon": "browser_aweb.png",
            "title": "Aweb",
            "rule" : [
                (re.compile("Amiga\-Aweb[/ ]([0-9.]{1,10})", re.I), 1),
                (re.compile("^AWeb", re.I), "")
            ],
            "uri": "http://aweb.sunsite.dk/"
        },
        {
            "icon": "browser_question.png",
            "title": "Babya Discoverer",
            "rule" : [
                (re.compile("Babya Discoverer ([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "browser_question.png",
            "title": "Barca",
            "rule" : [
                (re.compile("Barca(Pro)?[ /]([0-9.]{1,10})", re.I), 2)
            ],
            "uri": ""
        },
        {
            "icon": "browser_beonex.png",
            "title": "Beonex",
            "rule" : [
                (re.compile("beonex/([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_question.png",
            "title": "Biyubi",
            "rule" : [
                (re.compile("^Biyubi/([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_blazer.png",
            "title": "Blazer",
            "rule" : [
                (re.compile("Blazer[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_bluefish.png",
            "title": "BlueFish",
            "rule" : [
                (re.compile("bluefish[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://bluefish.openoffice.nl/"
        },
        {
            "icon": "browser_question.png",
            "title": "BrowseX",
            "rule" : [
                (re.compile("BrowseX.*\(([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://browsex.com/"
        },
        {
            "icon": "browser_camino.png",
            "title": "Camino",
            "rule" : [
                (re.compile("camino/([0-9.+]{1,10})", re.I), 1)
            ],
            "uri": "http://www.mozilla.org/projects/camino/"
        },
        {
            "icon": "browser_checkandget.png",
            "title": "Check&Get",
            "rule" : [
                (re.compile("Check\&Get[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://activeurls.com/"
        },
        {
            "icon": "browser_chimera.png",
            "title": "Chimera",
            "rule" : [
                (re.compile("chimera/([0-9.+]{1,10})", re.I), 1)
            ],
            "uri": "http://www.chimera.org/"
        },
        {
            "icon": "browser_question.png",
            "title": "CompuServe",
            "rule" : [
                (re.compile("CS 2000 ([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.compuserve.com/"
        },
        {
            "icon": "browser_question.png",
            "title": "Contiki",
            "rule" : [
                (re.compile("^Contiki[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.sics.se/~adam/contiki/apps/webbrowser.html"
        },
        {
            "icon": "browser_columbus.png",
            "title": "Columbus",
            "rule" : [
                (re.compile("columbus[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_crazybrowser.png",
            "title": "Crazy Browser",
            "rule" : [
                (re.compile("Crazy Browser[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "browser_curl.png",
            "title": "Curl",
            "rule" : [
                (re.compile("curl[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://curl.haxx.se/"
        },
        {
            "icon": "browser_question.png",
            "title": "Cute FTP",
            "rule" : [
                (re.compile("Cute FTP .*[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "browser_question.png",
            "title": "Cyberdog",
            "rule" : [
                (re.compile("^Cyberdog[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.cyberdog.org/"
        },
        {
            "icon": "browser_deepnet.png",
            "title": "Deepnet Explorer",
            "rule" : [
                (re.compile("Deepnet Explorer[/ ]([0-9.]{1,10})", re.I), 1),
                (re.compile(" Deepnet Explorer[\);]", re.I), "")
            ]
        },
        {
            "icon": "browser_question.png",
            "title": "Democracy",
            "rule" : [
                (re.compile("Democracy[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.getdemocracy.com/"
        },
        {
            "icon": "browser_dillo.png",
            "title": "Dillo",
            "rule" : [
                (re.compile("dillo/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.dillo.org/"
        },
        {
            "icon": "browser_dillo.png",
            "title": "DivX Player",
            "rule" : [
                (re.compile("DivX Player[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "browser_doczilla.png",
            "title": "DocZilla",
            "rule" : [
                (re.compile("DocZilla/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.doczilla.com/"
        },
        {
            "icon": "browser_donut.png",
            "title": "Donut RAPT",
            "rule" : [
                (re.compile("Donut RAPT[/ ]#?([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_question.png",
            "title": "Donut P",
            "rule" : [
                (re.compile("^DonutP", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "browser_doris.png",
            "title": "Doris",
            "rule" : [
                (re.compile("Doris/([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_dreamcast.png",
            "title": "DreamPassport",
            "rule" : [
                (re.compile("\(SonicPassport\)", re.I), ""),
                (re.compile("\(Dream(Passport|Key)[ /]([0-9.]{1,10})\)", re.I), 1),
                (re.compile("\(Dream(Passport|Key)[ /]([0-9.]{1,10}); ([A-Z.a-z/]{1,50})\)", re.I), 1),
                (re.compile("\(Planetweb[ /]([0-9.a-z]{1,10})", re.I), 1)
            ],
            "uri": "http://css.vis.ne.jp/dp-agent.shtml"
        },
        {
            "icon": "browser_question.png",
            "title": "DX-Browser",
            "rule" : [
                (re.compile("DX-Browser ([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.wankoo.org/index.php?page=Software.DXBrowser"
        },
        {
            "icon": "browser_question.png",
            "title": "edbrowse",
            "rule" : [
                (re.compile("edbrowse/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.eklhad.net/linux/app/"
        },
        {
            "icon": "browser_links.png",
            "title": "ELinks",
            "rule" : [
                (re.compile("ELinks[ /][\(]*([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://elinks.or.cz/"
        },
        {
            "icon": "browser_question.png",
            "title": "Emacs/w3s",
            "rule" : [
                (re.compile("Emacs-W3/([0-9.(pre)]{1,10})", re.I), 1)
            ],
            "uri": "http://www.gnu.org/software/w3/"
        },
        {
            "icon": "browser_endo.png",
            "title": "endo",
            "rule" : [
                (re.compile("^endo/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://kula.jp/endo"
        },
        {
            "icon": "browser_epiphany.png",
            "title": "Epiphany",
            "rule" : [
                (re.compile("Epiphany/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.gnome.org/projects/epiphany/"
        },
        {
            "icon": "browser_mobile.png",
            "title": "EudoraWeb",
            "rule" : [
                (re.compile("EudoraWeb[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.eudora.com/internetsuite/eudoraweb.html"
        },
        {
            "icon": "browser_question.png",
            "title": "Frontpage",
            "rule" : [
                (re.compile("MS[ ]*FrontPage[ /]([0-9.+]{1,10})", re.I), 1)
            ],
            "uri": "http://www.microsoft.com/frontpage/"
        },
        {
            "icon": "browser_firebird.png",
            "title": "Firebird",
            "rule" : [
                (re.compile("Firebird( Browser)?/([0-9.+]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "browser_flock.png",
            "title": "Flock",
            "rule" : [
                (re.compile("Flock/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.flock.com/"
        },
        {
            "icon": "browser_freshdownload.png",
            "title": "FreshDownload",
            "rule" : [
                (re.compile("FreshDownload/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.freshdevices.com/"
        },
        {
            "icon": "browser_galeon.png",
            "title": "Galeon",
            "rule" : [
                (re.compile("galeon/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://galeon.sourceforge.net/"
        },
        {
            "icon": "browser_oreilly.png",
            "title": "O'Reilly tutorial",
            "rule" : [
                (re.compile("hgrepurl/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.oreilly.com/openbook/webclient/"
        },
        {
            "icon": "browser_hotjava.png",
            "title": "HotJava",
            "rule" : [
                (re.compile("^HotJava[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://java.sun.com/products/archive/hotjava/index.html"
        },
        {
            "icon": "browser_question.png",
            "title": "ibisBrowser",
            "rule" : [
                (re.compile("ibisBrowser", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "browser_ibrowse.png",
            "title": "IBrowse",
            "rule" : [
                (re.compile("ibrowse[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.ibrowse-dev.net/"
        },
        {
            "icon": "browser_icab.png",
            "title": "iCab",
            "rule" : [
                (re.compile("icab[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.icab.de/"
        },
        {
            "icon": "browser_ice.png",
            "title": "ICEbrowser",
            "rule" : [
                (re.compile("ICE[ ]?Browser/v?([0-9._]{1,10})", re.I), 1)
            ],
            "uri": "http://www.borland.com/jbuilder/"
        },
        {
            "icon": "browser_mobile.png",
            "title": "Internet Explorer Pocket",
            "rule" : [
                (re.compile("Microsoft Pocket Internet Explorer[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("MSPIE[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "browser_intravnews.png",
            "title": "intraVNews",
            "rule" : [
                (re.compile("intraVnews[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.intravnews.com/"
        },
        {
            "icon": "browser_irider.png",
            "title": "iRider",
            "rule" : [
                (re.compile("iRider[/ ]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_isilox.png",
            "title": "iSiloX",
            "rule" : [
                (re.compile("iSilox/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "browser_lotus.png",
            "title": "Lotus Notes",
            "rule" : [
                (re.compile("Lotus[ \-]?Notes[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_kazehakase.png",
            "title": "Kazehakase",
            "rule" : [
                (re.compile("Kazehakase[ /]([0-9a-z.]{1,10})", re.I), 1)
            ],
            "uri": "http://kazehakase.sourceforge.jp/20031201.html"
        },
        {
            "icon": "browser_kkman.png",
            "title": "KKman",
            "rule" : [
                (re.compile("KKman[ /]?([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.kkman.com.tw/"
        },
        {
            "icon": "browser_question.png",
            "title": "Klondike",
            "rule" : [
                (re.compile("Klondike[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "browser_k-meleon.png",
            "title": "K-Meleon",
            "rule" : [
                (re.compile("K-Meleon[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://kmeleon.sourceforge.net/"
        },
        {
            "icon": "browser_k-ninja.png",
            "title": "K-Ninja",
            "rule" : [
                (re.compile("K-Ninja[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.geocities.com/grenleef/"
        },
        {
            "icon": "browser_konqueror.png",
            "title": "Konqueror",
            "rule" : [
                (re.compile("konqueror/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.konqueror.org/"
        },
        {
            "icon": "browser_liferea.png",
            "title": "Liferea",
            "rule" : [
                (re.compile("Liferea[ /]([0-9a-z.\-]{1,10})", re.I), 1)
            ],
            "uri": "http://liferea.sf.net/"
        },
        {
            "icon": "browser_links.png",
            "title": "Links",
            "rule" : [
                (re.compile("Links[ /]\(([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://artax.karlin.mff.cuni.cz/~mikulas/links"
        },
        {
            "icon": "browser_lunascape.png",
            "title": "Lunascape",
            "rule" : [
                (re.compile("Lunascape[ /]([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_lynx.png",
            "title": "Lynx",
            "rule" : [
                (re.compile("lynx/([0-9a-z.]{1,10})", re.I), 1)
            ],
            "uri": "http://lynx.browser.org/"
        },
        {
            "icon": "browser_maxthon.png",
            "title": "Maxthon",
            "rule" : [
                (re.compile(" Maxthon[\);]", re.I), "")
            ]
        },
        {
            "icon": "browser_mbrowser.png",
            "title": "mBrowser",
            "rule" : [
                (re.compile("mBrowser[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_wmp10.png",
            "title": "Media Player",
            "rule" : [
                (re.compile("NSPlayer[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("WMFSDK[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("Windows-Media-Player[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "browser_mobile.png",
            "title": "Mobile Internet Browser",
            "rule" : [
                (re.compile(" MIB[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.motorola.com/content.jsp?globalObjectId=1827-4343"
        },
        {
            "icon": "browser_mobile.png",
            "title": "Minimo",
            "rule" : [
                (re.compile("Minimo[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.mozilla.org/projects/minimo/"
        },
        {
            "icon": "browser_mnenhy.png",
            "title": "Mnenhy",
            "rule" : [
                (re.compile("Mnenhy[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://mnenhy.mozdev.org/"
        },
        {
            "icon": "browser_mosaic.png",
            "title": "Mosaic",
            "rule" : [
                (re.compile("mosaic[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_mpc.png",
            "title": "Media Player Classic",
            "rule" : [
                (re.compile("Media Player Classic", re.I), "")
            ],
            "uri": "http://sourceforge.net/projects/guliverkli/"
        },
        {
            "icon": "browser_mplayer.png",
            "title": "MPlayer",
            "rule" : [
                (re.compile("^MPlayer[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.mplayerhq.hu"
        },
        {
            "icon": "browser_msn.png",
            "title": "MSN Explorer",
            "rule" : [
                (re.compile("MSN[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.mplayerhq.hu"
        },
        {
            "icon": "browser_multibrowser.png",
            "title": "Multi-Browser",
            "rule" : [
                (re.compile("Multi-Browser[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://archive.ncsa.uiuc.edu/SDG/Software/XMosaic/"
        },
        {
            "icon": "browser_myie2.png",
            "title": "MyIE2",
            "rule" : [
                (re.compile(" MyIE2[\);]", re.I), "")
            ]
        },
        {
            "icon": "browser_netnewswire.png",
            "title": "NetNewsWire",
            "rule" : [
                (re.compile("NetNewsWire[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://ranchero.com/netnewswire/"
        },
        {
            "icon": "browser_netsurf.png",
            "title": "NetSurf",
            "rule" : [
                (re.compile("Netsurf", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "browser_nautilus.png",
            "title": "Nautilus",
            "rule" : [
                (re.compile("(gnome[ \-]?vfs|nautilus)/([0-9.]{1,10})", re.I), 2)
            ],
            "uri": ""
        },
        {
            "icon": "browser_netcaptor.png",
            "title": "Netcaptor",
            "rule" : [
                (re.compile("netcaptor[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_netfront.png",
            "title": "Netfront",
            "rule" : [
                (re.compile("NetFront[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.access-us-inc.com/"
        },
        {
            "icon": "browser_netpositive.png",
            "title": "NetPositive",
            "rule" : [
                (re.compile("netpositive[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://browsers.evolt.org/?netpositive/"
        },
        {
            "icon": "browser_question.png",
            "title": "Nexus",
            "rule" : [
                (re.compile("^Nexus", re.I), "")
            ],
            "uri": "http://browsers.evolt.org/"
        },
        {
            "icon": "browser_offbyone.png",
            "title": "OffByOne",
            "rule" : [
                (re.compile("OffByOne", re.I), "")
            ],
            "uri": "http://www.offbyone.com/"
        },
        {
            "icon": "browser_office.png",
            "title": "Office",
            "rule" : [
                (re.compile("^Microsoft Data Access Internet Publishing Provider (Protocol Discovery|Cache Manager|DAV)", re.I), "")
            ],
            "uri": "http://www.office.microsoft.com/"
        },
        {
            "icon": "browser_omniweb.png",
            "title": "OmniWeb",
            "rule" : [
                (re.compile("omniweb/[ a-z]?([0-9.]{1,10})$", re.I), 1),
                (re.compile("OmniWeb/([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_mobile.png",
            "title": "OpenWave",
            "rule" : [
                (re.compile("OPWV-SDK UP\.Browser[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.openwave.com/us/products/mobile/device_products/mobile_browser/index.htm"
        },
        {
            "icon": "browser_opera.png",
            "title": "Opera Mini",
            "rule" : [
                (re.compile("opera mini[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.opera.com/"
        },
        {
            "icon": "browser_opera.png",
            "title": "Opera",
            "rule" : [
                (re.compile("opera[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.opera.com/"
        },
        {
            "icon": "browser_question.png",
            "title": "Orca",
            "rule" : [
                (re.compile("Orca Browser \(http://www.orcabrowser.com\)", re.I), 1)
            ],
            "uri": "http://www.orcabrowser.com"
        },
        {
            "icon": "browser_oregano.png",
            "title": "Oregano",
            "rule" : [
                (re.compile("Oregano[0-9]?[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.castle.org.uk/oregano/"
        },
        {
            "icon": "browser_palmsource.png",
            "title": "PalmSource Web Browser",
            "rule" : [
                (re.compile("PalmSource", re.I), ""),
                (re.compile("Palm-Arz1", re.I), "")
            ],
            "uri": "http://www.palmos.com/dev/tech/palmos5/webbrowser.html"
        },
        {
            "icon": "browser_question.png",
            "title": "Paparazzi",
            "rule" : [
                (re.compile("Paparazzi\!/([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_phaseout.png",
            "title": "PhaseOut",
            "rule" : [
                (re.compile("www\.phaseout\.net", re.I), "")
            ]
        },
        {
            "icon": "browser_plink.png",
            "title": "PLink",
            "rule" : [
                (re.compile("PLink[ /]([0-9a-z.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_mobile.png",
            "title": "Plucker",
            "rule" : [
                (re.compile("Plucker[ /](Py-)?([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.openwave.com/us/products/mobile/device_products/mobile_browser/index.htm"
        },
        {
            "icon": "browser_phoenix.png",
            "title": "Phoenix",
            "rule" : [
                (re.compile("Phoenix/([0-9.+]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_question.png",
            "title": "PHPEd",
            "rule" : [
                (re.compile("PHPEd Version[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "browser_question.png",
            "title": "HP Web PrintSmart",
            "rule" : [
                (re.compile("HP Web PrintSmart ([0-9.a-z]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_proxomitron.png",
            "title": "Proxomitron",
            "rule" : [
                (re.compile("[(Space)| ]?BisoN/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.proxomitron.info/"
        },
        {
            "icon": "browser_question.png",
            "title": "PlayStation Portable",
            "rule" : [
                (re.compile("PSP \(PlayStation Portable\); ([0-9.]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "browser_question.png",
            "title": "Parallel URL Fetcher",
            "rule" : [
                (re.compile("^puf[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://puf.sourceforge.net/"
        },
        {
            "icon": "browser_quicktime.png",
            "title": "QuickTime",
            "rule" : [
                (re.compile("QuickTime..qtver.([0-9.]{1,10})", re.I), 1),
                (re.compile("qtver.([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.apple.com/quicktime/"
        },
        {
            "icon": "browser_realplayer.png",
            "title": "Real Player",
            "rule" : [
                (re.compile("RealPlayer/([0-9.+]{1,10})", re.I), 1),
                (re.compile("^Mozilla/([0-9.+]{1,10}).*\(R1 1.5\)\)", re.I), ""),
                (re.compile("RMA/([0-9.+]{1,10})", re.I), "")
            ]
        },
        {
            "icon": "browser_question.png",
            "title": "retawq",
            "rule" : [
                (re.compile("retawq/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://retawq.sourceforge.net/"
        },
        {
            "icon": "browser_question.png",
            "title": "Safexplorer",
            "rule" : [
                (re.compile("SAFEXPLORER TL", re.I), "")
            ],
            "uri": "http://www.safexplorer.com/"
        },
        {
            "icon": "browser_shareaza.png",
            "title": "Shareaza",
            "rule" : [
                (re.compile("Shareaza[ /]v?([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.shareaza.com/"
        },
        {
            "icon": "browser_shiira.png",
            "title": "Shiira",
            "rule" : [
                (re.compile("Shiira/([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_safari.png",
            "title": "Safari",
            "rule" : [
                (re.compile("safari/([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_sage.png",
            "title": "Sage",
            "rule" : [
                (re.compile("\(Sage\)", re.I), "")
            ],
            "uri": "http://sage.mozdev.org/"
        },
        {
            "icon": "browser_seamonkey.png",
            "title": "Seamonkey",
            "rule" : [
                (re.compile("Seamonkey/([0-9a-z.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.mozilla.org/projects/seamonkey/"
        },
        {
            "icon": "browser_question.png",
            "title": "HP Secure Web Browser",
            "rule" : [
                (re.compile("SWB[ /]V?([0-9.]{1,10}) \(HP\)", re.I), 1)
            ],
            "uri": "http://h71000.www7.hp.com/openvms/products/ips/cswb/cswb.html"
        },
        {
            "icon": "browser_question.png",
            "title": "SiteKiosk",
            "rule" : [
                (re.compile("SiteKiosk[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.sitekiosk.com/"
        },
        {
            "icon": "browser_sleipnir.png",
            "title": "Sleipnir",
            "rule" : [
                (re.compile("Sleipnir( Version)?[ /]([0-9a-z.]{1,10})", re.I), 2)
            ]
        },
        {
            "icon": "browser_slimbrowser.png",
            "title": "SlimBrowser",
            "rule" : [
                (re.compile("Slimbrowser", re.I), "")
            ]
        },
        {
            "icon": "browser_songbird.png",
            "title": "Songbird",
            "rule" : [
                (re.compile("Songbird[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.songbirdnest.com/"
        },
        {
            "icon": "browser_question.png",
            "title": "Spectrum Internet Suite",
            "rule" : [
                (re.compile(" SIS ([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://sis.gwlink.net/"
        },
        {
            "icon": "browser_sputnik.png",
            "title": "Sputnik",
            "rule" : [
                (re.compile("Sputnik[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_squid.png",
            "title": "Squid Proxy",
            "rule" : [
                (re.compile("^Cafi[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("SquidClamAV_Redirector[ /]([0-9.]{1,10})", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "browser_staroffice.png",
            "title": "StarOffice",
            "rule" : [
                (re.compile("staroffice[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_sunrise.png",
            "title": "Sunrise",
            "rule" : [
                (re.compile("SunriseBrowser[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_question.png",
            "title": "Sunrise",
            "rule" : [
                (re.compile("SunriseBrowser[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_swift.png",
            "title": "Swift",
            "rule" : [
                (re.compile("Swift[ /]([0-9.]{1,10})", re.I), 1), # FIXME: this is just plain wrong... but every other AppleWebKit-based-browser (safari, shiira) was fetched before
                (re.compile("AppleWebKit", re.I), 1)
            ],
            "uri": "http://www.getswift.org/"
        },
        {
            "icon": "browser_question.png",
            "title": "Sylera",
            "rule" : [
                (re.compile("Sylera[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.zawameki.net/izmi/prog/sylera_en.html"
        },
        {
            "icon": "browser_question.png",
            "title": "Syndirella",
            "rule" : [
                (re.compile("Syndirella[/ ]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://sourceforge.net/projects/syndirella/"
        },
        {
            "icon": "browser_tonline.png",
            "title": "T-Online",
            "rule" : [
                (re.compile("^T-Online Browser", re.I), 1)
            ]
        },
        {
            "icon": "browser_upbrowser.png",
            "title": "UP.Browser",
            "rule" : [
                (re.compile("UP\.Browser[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("UP\.Link[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_vienna.png",
            "title": "Vienna",
            "rule" : [
                (re.compile("^Vienna[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://vienna-rss.sourceforge.net/"
        },
        {
            "icon": "browser_vlc.png",
            "title": "VLC",
            "rule" : [
                (re.compile("^VLC media player - version ([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.videolan.org/vlc/"
        },
        {
            "icon": "browser_voyager.png",
            "title": "Voyager",
            "rule" : [
                (re.compile("voyager[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("AmigaVoyager", re.I), ""),
                (re.compile(" Voyager", re.I), "")
            ],
            "uri": "http://v3.vapor.com/"
        },
        {
            "icon": "browser_question.png",
            "title": "W3C Line Mode",
            "rule" : [
                (re.compile("W3CLineMode/([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.w3.org/LineMode"
        },
        {
            "icon": "browser_w3m.png",
            "title": "w3m",
            "rule" : [
                (re.compile("w3m/([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_question.png",
            "title": "WannaBe",
            "rule" : [
                (re.compile("^WannaBe", re.I), "")
            ],
            "uri": "http://mindstory.com/wb2/"
        },
        {
            "icon": "browser_warrior.png",
            "title": "Warrior",
            "rule" : [
                (re.compile("^Warrior", re.I), "")
            ]
        },
        {
            "icon": "browser_question.png",
            "title": "WebCapture (Adobe)",
            "rule" : [
                (re.compile("WebCapture[ /]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "browser_webtv.png",
            "title": "Webtv",
            "rule" : [
                (re.compile("webtv[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("webtv", re.I), "")
            ]
        },
        {
            "icon": "browser_winamp.png",
            "title": "Winamp",
            "rule" : [
                (re.compile("^WinampMPEG[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("^Nullsoft Winamp3 version[ /]([0-9.a-z]{1,10})", re.I), 1)
            ],
            "uri": ""
        },
        {
            "icon": "browser_xiino.png",
            "title": "Xiino",
            "rule" : [
                (re.compile("^Xiino[ /]([0-9a-z.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.access-us-inc.com/"
        },
        {
            "icon": "browser_xine.png",
            "title": "xine",
            "rule" : [
                (re.compile("^xine[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://xine.sourceforge.net/"
        },
        {
            "icon": "browser_yahoo.png",
            "title": "Yahoo Messenger",
            "rule" : [
                (re.compile("^Y(!)*TunnelPro", re.I), "")
            ],
            "uri": "http://messenger.yahoo.com/"
        },
        {
            "icon": "browser_question.png",
            "title": "ZipCommander",
            "rule" : [
                (re.compile("ZipCommander", re.I), "")
            ],
            "uri": "http://www.zipcommander.com/"
        },
        {
            "icon": "browser_question.png",
            "title": "Zoo Tycoon 2",
            "rule" : [
                (re.compile("Zoo Tycoon 2 Client", re.I), "")
            ],
            "uri": "http://www.zootycoon.com/"
        },
        {
            "icon": "browser_explorer.png",
            "title": "Explorer",
            "rule" : [
                (re.compile("\(compatible; MSIE[ /]([0-9a-z.]{1,10})", re.I), 1),
                (re.compile("Internet Explorer[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("^Auto-Proxy Downloader", re.I), "")
            ],
            "uri": "http://www.microsoft.com/windows/ie/"
        },
        {
            "icon": "browser_netscape.png",
            "title": "Netscape",
            "rule" : [
                (re.compile("netscape[0-9]?/([0-9.]{1,10})", re.I), 1),
                (re.compile("^mozilla/([0-4]\.[0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.netscape.com/"
        },
        {
            "icon": "browser_firefox.png",
            "title": "Firefox",
            "rule" : [
                (re.compile("Firefox/([0-9.+]{1,10})", re.I), 1), # Firefox 2.0 beta
                (re.compile("BonEcho/([0-9.+]{1,10})", re.I), 1), # Unbranded Firefox 2.0, GNU compatible
                (re.compile("Iceweasel/([0-9.+]{1,10})", re.I), 1), # Firefox 3.0 alpha
                (re.compile("GranParadiso/([0-9.+]{1,10})", re.I), 1), # Firefox 3.0 beta
                (re.compile("Minefield/([0-9.+]{1,10})", re.I), 1),
                (re.compile("Firefox", re.I), "")
            ],
            "uri": "http://www.mozilla.org/projects/firefox/",
            "known" : [
                (re.compile("Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.8.1) Gecko/20061019 Firefox", re.I), "Firefox nightly on Windows XP"),
                (re.compile("Mozilla/5.0 (Windows; U; Windows NT 5.1; nl-NL; rv:1.7.5) Gecko/20041202 Firefox/1.0", re.I), "Firefox 1.0 on Windows XP (dutch)"),
                (re.compile("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.7.6) Gecko/20050512 Firefox", re.I), "Firefox 1.0.4 on Ubuntu Linux (AMD64)"),
                (re.compile("Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.7.8) Gecko/20050609 Firefox/1.0.4", re.I), "Firefox 1.0.4 on FreeBSD (i386)"),
                (re.compile("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.9) Gecko/20050711 Firefox/1.0.5", re.I), "Firefox 1.0.5 on Slackware"),
                (re.compile("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.10) Gecko/20050716 Firefox/1.0.6", re.I), "Firefox 1.0.6 on Windows XP"),
                (re.compile("Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-GB; rv:1.7.10) Gecko/20050717 Firefox/1.0.6", re.I), "Firefox 1.0.6 on Mac OS X 10.4 PPC"),
                (re.compile("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7", re.I), "Firefox 1.0.7 on Windows XP"),
                (re.compile("Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7", re.I), "Firefox 1.0.7 on Mac OS X 10.3 PPC"),
                (re.compile("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8b4) Gecko/20050908 Firefox/1.4", re.I), "Firefox 1.5 beta 1 on Windows XP"),
                (re.compile("Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8b4) Gecko/20050908 Firefox/1.4", re.I), "Firefox 1.5 beta 1 on Mac OS X 10.3 PPC"),
                (re.compile("Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8) Gecko/20051107 Firefox/1.5", re.I), "Firefox 1.5 on Windows XP"),
                (re.compile("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1", re.I), "Firefox 1.5.0.1 on Windows XP"),
                (re.compile("Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.0.1) Gecko/20060111 Firefox/1.5.0.1", re.I), "Firefox 1.5.0.1 on Windows Vista"),
                (re.compile("Mozilla/5.0 (BeOS; U; BeOS BePC; en-US; rv:1.9a1) Gecko/20051002 Firefox/1.6a1", re.I), "1.6 alpha 1 on BeOS R5"),
                (re.compile("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8) Gecko/20060321 Firefox/2.0a1", re.I), "2.0 alpha 1 on Windows XP"),
                (re.compile("Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1b1) Gecko/20060710 Firefox/2.0b1", re.I), "2.0 beta 1 on Windows XP"),
                (re.compile("Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1b2) Gecko/20060710 Firefox/2.0b2", re.I), "2.0 beta 2 on Windows XP"),
                (re.compile("Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1) Gecko/20060918 Firefox/2.0", re.I), "2.0 on Windows XP")
            ]
        },
        {
            "icon": "browser_mozilla.png",
            "title": "Mozilla",
            "rule" : [
                (re.compile("^mozilla/[5-9]\.[0-9.]{1,10}.+rv:([0-9a-z.+]{1,10})", re.I), 1),
                (re.compile("^mozilla/([5-9]\.[0-9a-z.]{1,10})", re.I), 1), # Unbranded Mozilla, GNU compatible
                (re.compile("GNUzilla/([0-9.+]{1,10})", re.I), 1)
            ],
            "uri": "",
            "known" : [
                (re.compile("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050511", re.I), "Mozilla 1.7.9 on Linux (american english)"),
                (re.compile("Mozilla/5.0 (X11; U; Linux i686; cs-CZ; rv:1.7.12) Gecko/20050929", re.I), "Mozilla 1.7.12 on Gentoo Linux")
            ]
        },
        {
            "icon": "browser_question.png",
            "title": "WAP",
            "rule" : [
                (re.compile("Profile[ /]MIDP-([0-9.+]{1,10})", re.I), ""),
                (re.compile("Configuration[ /]CLDC-([0-9.+]{1,10})", re.I), ""),
                (re.compile("WAP", re.I), "")
            ]
        },
        {
            "icon": "browser_question.png",
            "title": "other",
            "rule" : [
                (re.compile(".*", re.I), "")
            ]
        }
    ]

    def browser_from_browserstring(self, browserstring):
        """ Identify the browser from a browserstring

            You get a dict describing the browser with the following fields:
                title       The name of the browser
                icon        An identifier for an icon describing the browser
                uri         A Internet URL that is associated with the browser
                version     An additional string that gives the version info
        """
        for browser in self.browsers:
            if browser.has_key("known"): # merge 'known' and 'rule' together
                browser["rule"] = browser["known"] + browser["rule"]
                del browser["known"]
            for rule_tuple in browser["rule"]:
                rule = rule_tuple[0]
                versionrule = rule_tuple[1]
                match = rule.search(browserstring)
                if match:
                    title = browser["title"]
                    icon = browser["icon"]
                    uri = ""
                    if browser.has_key("uri"):
                        uri = browser["uri"]
                    version = ""
                    if isinstance(versionrule, int):
                        try:
                            version = match.group(versionrule)
                        except IndexError:
                            pass; # internal error: some parts of the data structure seem bullshit
                    else:
                        version = versionrule
                    return {
                        'title'   : title,
                        'icon'    : icon,
                        'uri'     : uri,
                        'version' : version
                    }