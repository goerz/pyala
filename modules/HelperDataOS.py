# The data structure used in this file was converted from the BBClone project
# http://bbclone.de/

import re

class OSIdentifier(object):
    """ Provides identification of the operating system from the browser string
    """

    oslist= [
        {
            "icon": "os_aix.png",
            "title": "AIX",
            "rule" : [
                (re.compile("\-aix([0-9.]{1,10})", re.I), 1),
                (re.compile("[ ;\(]aix", re.I), "")
            ]
        },
        {
            "icon": "os_amiga.png",
            "title": "AmigaOS",
            "rule" : [
                (re.compile("Amiga[ ]?OS[ /]([0-9.V]{1,10})", re.I), 1),
                (re.compile("amiga", re.I), "")
            ]
        },
        {
            "icon": "os_other.png",
            "title": "Atari",
            "rule" : [
                (re.compile("atari[ /]([0-9.b]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "os_atheos.png",
            "title": "AtheOS",
            "rule" : [
                (re.compile("atheos", re.I), "")
            ]
        },
        {
            "icon": "os_be.png",
            "title": "BeOS",
            "rule" : [
                (re.compile("beos[ a-z]*([0-9.]{1,10})", re.I), 1),
                (re.compile("beos", re.I), "")
            ]
        },
        {
            "icon": "os_bluecoat.png",
            "title": "Bluecoat DRTR",
            "rule" : [
                (re.compile("bluecoat drtr", re.I), 1)
            ]
        },
        {
            "icon": "os_bluecoat.png",
            "title": "Cerberian DRTR",
            "rule" : [
                (re.compile("Cerberian Drtrs Version[ /\-]([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "os_c64.png",
            "title": "Commodore 64",
            "rule" : [
                (re.compile("Commodore[ ]?64", re.I), "")
            ]
        },
        {
            "icon": "os_darwin.png",
            "title": "Darwin",
            "rule" : [
                (re.compile("Darwin[ ]?([0-9.]{1,10})", re.I), 1),
                (re.compile("Darwin", re.I), "")
            ]
        },
        {
            "icon": "os_digital.png",
            "title": "Digital",
            "rule" : [
                (re.compile("OSF[0-9][ ]?V(4[0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "os_dreamcast.png",
            "title": "SEGA Dreamcast",
            "rule" : [
                (re.compile("\(SonicPassport\)", re.I), ""),
                (re.compile("\(Dream(Passport|Key)[ /]([0-9.]{1,10})\)", re.I), ""),
                (re.compile("\(Dream(Passport|Key)[ /]([0-9.]{1,10}); ([A-Z.a-z/]{1,50})\)", re.I), ""),
                (re.compile("\(Planetweb[ /]([0-9.a-z]{1,10})", re.I), "")
            ],
            "uri": "http://css.vis.ne.jp/dp-agent.shtml"
        },
        {
            "icon": "os_question.png",
            "title": "Embedix",
            "rule" : [
                (re.compile("Embedix", re.I), "")
            ]
        },
        {
            "icon": "os_fedora.png",
            "title": "fedora",
            "rule" : [
                (re.compile("fedora", re.I), "")
            ]
        },
        {
            "icon": "os_question.png",
            "title": "Fenix",
            "rule" : [
                (re.compile("Fenix", re.I), "")
            ]
        },
        {
            "icon": "os_freebsd.png",
            "title": "FreeBSD",
            "rule" : [
                (re.compile("free[ \-]?bsd[ /]([a-z0-9._]{1,10})", re.I), 1),
                (re.compile("free[ \-]?bsd", re.I), "")
            ]
        },
        {
            "icon": "os_gentoo.png",
            "title": "Gentoo Linux",
            "rule" : [
                (re.compile("gentoo", re.I), "")
            ],
            "uri": "http://www.gentoo.org/"
        },
        {
            "icon": "os_question.png",
            "title": "hiptop",
            "rule" : [
                (re.compile("Danger hiptop ([0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "os_hp.png",
            "title": "HPUX",
            "rule" : [
                (re.compile("hp[ \-]?ux[ /]([a-z0-9._]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "os_irix.png",
            "title": "IRIX",
            "rule" : [
                (re.compile("irix[0-9]*[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("irix", re.I), "")
            ]
        },
        {
            "icon": "os_macosx.png",
            "title": "MacOS X",
            "rule" : [
                (re.compile("Mac[ _]?OS[ _]?X[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("Mac[ _]?OS[ _]?X", re.I), ""),
                (re.compile("Mac 10.([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.apple.com/macosx/"
        },
        {
            "icon": "os_macppc.png",
            "title": "MacOS PPC",
            "rule" : [
                (re.compile("Mac(_Power|intosh.+P)PC", re.I), "")
            ]
        },
        {
            "icon": "os_morphos.png",
            "title": "MorphOS",
            "rule" : [
                (re.compile("MorphOS[ /]([0-9.]{1,10})", re.I), 1),
                (re.compile("MorphOS", re.I), "")
            ]
        },
        {
            "icon": "os_netbsd.png",
            "title": "NetBSD",
            "rule" : [
                (re.compile("net[ \-]?bsd[ /]([a-z0-9._]{1,10})", re.I), 1),
                (re.compile("net[ \-]?bsd", re.I), "")
            ]
        },
        {
            "icon": "os_ds.png",
            "title": "Nintento DS",
            "rule" : [
                (re.compile("Nintendo DS v([0-9.]{1,10})", re.I), "")
            ]
        },
        {
            "icon": "os_openbsd.png",
            "title": "OpenBSD",
            "rule" : [
                (re.compile("open[ \-]?bsd[ /]([a-z0-9._]{1,10})", re.I), 1),
                (re.compile("open[ \-]?bsd", re.I), "")
            ]
        },
        {
            "icon": "os_openvms.png",
            "title": "OpenVMS",
            "rule" : [
                (re.compile("Open[ \-]?VMS[ /]([a-z0-9._]{1,10})", re.I), 1),
                (re.compile("Open[ \-]?VMS", re.I), "")
            ]
        },
        {
            "icon": "os_palm.png",
            "title": "PalmOS",
            "rule" : [
                (re.compile("Palm[ \-]?(Source|OS)[ /]?([0-9.]{1,10})", re.I), 2),
                (re.compile("Palm[ \-]?(Source|OS)", re.I), "")
            ]
        },
        {
            "icon": "os_pclinux.png",
            "title": "PCLinuxOS",
            "rule" : [
                (re.compile("PCLinuxOS[ /]?([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.pclinuxos.com/"
        },
        {
            "icon": "os_qnx.png",
            "title": "QNX Photon",
            "rule" : [
                (re.compile("photon", re.I), "")
            ]
        },
        {
            "icon": "os_playstation.png",
            "title": "PlayStation Portable",
            "rule" : [
                (re.compile("PlayStation Portable.* ([0-9._]{1,10})", re.I), 1),
                (re.compile("PlayStation Portable", re.I), "")
            ]
        },
        {
            "icon": "os_playstation.png",
            "title": "PlayStation",
            "rule" : [
                (re.compile("PlayStation", re.I), ""),
                (re.compile("PS2", re.I), "")
            ]
        },
        {
            "icon": "os_reactos.png",
            "title": "ReactOS",
            "rule" : [
                (re.compile("ReactOS[ /]?([0-9.]{1,10})", re.I), 1),
                (re.compile("ReactOS", re.I), "")
            ]
        },
        {
            "icon": "os_risc.png",
            "title": "RiscOS",
            "rule" : [
                (re.compile("risc[ \-]?os[ /]?([0-9.]{1,10})", re.I), 1),
                (re.compile("risc[ \-]?os", re.I), "")
            ]
        },
        {
            "icon": "os_suse.png",
            "title": "SuSE",
            "rule" : [
                (re.compile("suse", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "os_sun.png",
            "title": "SunOS",
            "rule" : [
                (re.compile("sun[ \-]?os[ /]?([0-9.]{1,10})", re.I), 1),
                (re.compile("sun[ \-]?os", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "os_symbian.png",
            "title": "Symbian OS",
            "rule" : [
                (re.compile("symbian[ \-]?os[ /]?([0-9.]{1,10})", re.I), 1),
                (re.compile("symbian", re.I), "")
            ]
        },
        {
            "icon": "os_tru64.png",
            "title": "Tru64",
            "rule" : [
                (re.compile("OSF[0-9][ ]?V(5[0-9.]{1,10})", re.I), 1)
            ]
        },
        {
            "icon": "os_ubuntu.png",
            "title": "Ubuntu Linux",
            "rule" : [
                (re.compile("ubuntu", re.I), "")
            ],
            "uri": "http://www.ubuntu.com/"
        },
        {
            "icon": "os_sco.png",
            "title": "UnixWare",
            "rule" : [
                (re.compile("unixware[ /]?([0-9.]{1,10})", re.I), 1),
                (re.compile("unixware", re.I), "")
            ]
        },
        {
            "icon": "os_wii.png",
            "title": "Wii",
            "rule" : [
                (re.compile("^Nintendo Wii", re.I), ""),
                (re.compile(" wii", re.I), "")
            ],
            "uri": "http://www.wii.com/"
        },
        {
            "icon": "os_windowsxp.png",
            "title": "Windows XP (64-bit)",
            "rule" : [
                (re.compile("wi(n|ndows)[ \-]?(2003|nt[ /]?5\.2).*(WOW64|Win64)", re.I), "")
            ],
            "uri": "http://www.microsoft.com/windowsxp/64bit/"
        },
        {
            "icon": "os_windowsxp.png",
            "title": "Windows 2003",
            "rule" : [
                (re.compile("wi(n|ndows)[ \-]?(2003|nt[ /]?5\.2)", re.I), "")
            ],
            "uri": "http://www.microsoft.com/windowsserver2003/"
        },
        {
            "icon": "os_windows.png",
            "title": "Windows 2000",
            "rule" : [
                (re.compile("wi(n|ndows)[ \-]?(2000|nt[ /]?5\.0)", re.I), "")
            ],
            "uri": "http://www.microsoft.com/windows2000/"
        },
        {
            "icon": "os_windows31.png",
            "title": "Windows 3.1",
            "rule" : [
                (re.compile("wi(n|ndows)[ \-]?3\.[1]+", re.I), ""),
                (re.compile("Win16", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "os_windows.png",
            "title": "Windows 95",
            "rule" : [
                (re.compile("wi(n|ndows)[ \-]?95", re.I), "")
            ],
            "uri": "http://www.microsoft.com/windows95/"
        },
        {
            "icon": "os_windows.png",
            "title": "Windows CE",
            "rule" : [
                (re.compile("wi(n|ndows)[ \-]?ce", re.I), ""),
                (re.compile("wi(n|ndows)[ /.;]*mobile", re.I), ""),
                (re.compile("(Microsoft|Windows) Pocket", re.I), "")
            ],
            "uri": "http://www.microsoft.com/windows/embedded/"
        },
        {
            "icon": "os_windows.png",
            "title": "Windows ME",
            "rule" : [
                (re.compile("win 9x 4\.90", re.I), ""),
                (re.compile("wi(n|ndows)[ \-]?me", re.I), "")
            ],
            "uri": "http://www.microsoft.com/windowsme/"
        },
        {
            "icon": "os_windowsvista.png",
            "title": "Windows Vista",
            "rule" : [
                (re.compile("Windows Vista", re.I), ""),
                (re.compile("wi(n|ndows)[ \-]?nt[ /]?6\.0", re.I), "")
            ],
            "uri": "http://www.microsoft.com/windowsvista/"
        },
        {
            "icon": "os_windowsxp.png",
            "title": "Windows Media Center",
            "rule" : [
                (re.compile("Media Center PC[ /]([0-9.]{1,10})", re.I), 1)
            ],
            "uri": "http://www.microsoft.com/windowsxp/mediacenter/"
        },
        {
            "icon": "os_windowsxp.png",
            "title": "Windows XP",
            "rule" : [
                (re.compile("Windows XP", re.I), ""),
                (re.compile("wi(n|ndows)[ \-]?nt[ /]?5\.1", re.I), "")
            ],
            "uri": "http://www.microsoft.com/windowsxp/"
        },
        {
            "icon": "os_debian.png",
            "title": "Debian Linux",
            "rule" : [
                (re.compile("debian", re.I), "")
            ],
            "uri": "http://www.debian.org/"
        },
        {
            "icon": "os_bsd.png",
            "title": "BSD",
            "rule" : [
                (re.compile("bsd", re.I), "")
            ]
        },
        {
            "icon": "os_linux.png",
            "title": "Linux",
            "rule" : [
                (re.compile("linux[ /\-]([a-z0-9._]{1,10})", re.I), 1),
                (re.compile("linux", re.I), "")
            ],
            "uri": "http://www.kernel.org/"
        },
        {
            "icon": "os_os2.png",
            "title": "OS/2 Warp",
            "rule" : [
                (re.compile("warp[ /]?([0-9.]{1,10})", re.I), 1),
                (re.compile("os[ /]?2", re.I), "")
            ]
        },
        {
            "icon": "os_mac.png",
            "title": "MacOS",
            "rule" : [
                (re.compile("mac[^hk]", re.I), "")
            ],
            "uri": ""
        },
        {
            "icon": "os_windows.png",
            "title": "Windows NT",
            "rule" : [
                (re.compile("wi(n|ndows)[ \-]?nt[ /]?([0-4][0-9.]{1,10})", re.I), 2),
                (re.compile("wi(n|ndows)[ \-][ /]?([0-4][0-9.]{1,10})", re.I), 2),
                (re.compile("wi(n|ndows)[ \-]?nt", re.I), "")
            ],
            "uri": "http://www.microsoft.com/windowsnt/"
        },
        {
            "icon": "os_windows.png",
            "title": "Windows 98",
            "rule" : [
                (re.compile("wi(n|ndows)[ \-]?98", re.I), "")
            ],
            "uri": "http://www.microsoft.com/windows98/"
        },
        {
            "icon": "os_windows.png",
            "title": "Windows",
            "rule" : [
                (re.compile("wi(n|n32|n64|ndows)", re.I), ""), #FIXME: might be a bit insane ...
                (re.compile("Microsoft", re.I), "")
            ]
        },
        {
            "icon": "os_java.png",
            "title": "Java Platform Micro Edition",
            "rule" : [
                (re.compile("J2ME/MIDP", re.I), "")
            ],
            "uri": "http://java.sun.com/"
        },
        {
            "icon": "os_mobile.png",
            "title": "Mobile",
            "rule" : [
                (re.compile("LG[ /]([0-9A-Z]{1,10})", re.I), ""), # Motorola mobiles
                (re.compile("MOT[- /]([0-9A-Z]{1,10})", re.I), ""), # Sony Ericsson mobiles
                (re.compile("SonyEricsson([0-9A-Z]{1,10})", re.I), ""), # Siemens BenQ mobiles
                (re.compile("SIE([0-9A-Z]{1,10})", re.I), ""), # Nokia mobiles
                (re.compile("Nokia([0-9A-Z]{1,10})", re.I), ""), # Samsung mobiles
                (re.compile("KDDI-([0-9A-Z]{1,10})", re.I), ""), # Samsung mobiles
                (re.compile("Blackberry([0-9A-Z]{1,10})", re.I), ""),
                (re.compile("^[A-Z]([0-9]{1,3}) ", re.I), ""),
                (re.compile("Configuration[ /]CLDC([0-9.]{1,10})", re.I), 1),
                (re.compile("MIDP", re.I), ""),
                (re.compile("UP\.(Browser|Link)", re.I), ""),
                (re.compile("ibisBrowser", re.I), "")
            ]
        },
        {
            "icon": "os_question.png",
            "title": "other",
            "rule" : [
                (re.compile(".*", re.I), "")
            ]
        }
    ]


    def os_from_browserstring(self, browserstring):
        """ Identify the os from a browserstring

            You get a dict describing the os with the following fields:
                'title'       The name of the os
                'icon'        An identifier for an icon describing the os
                'uri'         A Internet URL that is associated with the os
                'version'     An additional string that gives the version info
        """
        for os in self.oslist:
            for rule_tuple in os["rule"]:
                rule = rule_tuple[0]
                versionrule = rule_tuple[1]
                match = rule.search(browserstring)
                if match:
                    title = os["title"]
                    icon = os["icon"]
                    uri = ""
                    if os.has_key("uri"):
                        uri = os["uri"]
                    version = ""
                    if isinstance(versionrule, int):
                        version = match.group(versionrule)
                    else:
                        version = versionrule
                    return {
                        'title'   : title,
                        'icon'    : icon,
                        'uri'     : uri,
                        'version' : version
                    }
