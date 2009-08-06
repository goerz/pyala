# -*- coding: utf-8 -*-
from ApacheLogParser import ApacheLogParser, ApacheLogLine
from TemplateProcessor import TemplateProcessor, LoopData
from GeoIPWrapper import GeoIPWrapper
from HelperDataBrowser import BrowserIdentifier
from HelperDataOS import OSIdentifier
from HelperDataRobot import RobotIdentifier
from RefererAnalyzer import RefererAnalyzer
import cgi
import os
import os.path
import sys


def warn(msg):
    """ print a warning message to stderr """
    sys.stderr.write(str(msg))
    sys.stderr.write("\n")


class NoLoglineException(Exception):
    def __init__(self):
        self.message = "Visit tried to operate on an object that's not a ApacheLogLine"


class Visit (object):
    """
    Describes a visit to a website.
    It holds information associated with that visit, and can print out a template-based
    website describing the visit


    Class variables:
        html_template [templates/visit_template.html]    the template used for the website
        imagedir      [../images]                        image directory, for the website

    Instance variables:
        begin_time              the time in period secs that the visit started
        begin_time_string       a textual representation of begin_time
        end_time                the time in period secs that the visit ended
        end_time_string         a textual representation of end_time
        countryextension        the country extension of the visiting browser, two-letter-code
        countryname             the full country name that corresponds to the country extnsion
        country_icon            a link to an icon for the country (country flag)
        hostname                the hostname (or IP, if not available) of the visiting host
        os                      the operating system of the visiting host
        os_icon                 a link to an icon that symbolizes the OS
        os_version              version info for the OS, if any
        os_uri                  a uri that is associated with the os
        fullbrowser             the full browser description of the visiting browser
        browser                 a short name from the browser
        browser_icon            a link to an icon taht symbolizes the browser
        browser_version         version info for the browser
        browser_uri             a uri that is associated with the browser
        referer                 the full referer string
        referer_site            just the site name of the referer (e.g. www.google.com)
        referer_page            the page of the referrer, without var's (e.g. www.google.com/search)
        first_logline           the first line from the log
        search                  the search terms that brought the visitor here (if any)
        code                    the apache error code of the initial page
        code_description        the description of the apache error code
        user                    the user name, that was used to access the resource (if any)
        pages                   an array of pages that were accessed during the visit (ApacheLogLines)
        durations               an array that describes how many seconds each of the pages in the
                                pages array was visited
        reloads                 an array that describes how ofen each of the pages in the pages array
                                was reloaded
        is_bot                  was the visitor a bot?
        botname                 if applicable, the bot's name
        bot_icon                if applicable, a link to an icon associated with the bot
        bot_version             version info for the bot
        bot_uri                 a uri associated with the bot
        transferred_bytes       the total number of bytes transferred (sum of all registered pages)
        number                  intended to be set externally, e.g. to indicate the order in which
                                visits were pushed off a VisitManager instance
    """

    html_template = "../templates/visit.html"
    outmode = "html"
    imagedir = "images"
    outdir = "."
    _browserident = BrowserIdentifier()
    _osident = OSIdentifier()
    _robotident = RobotIdentifier()
    _countryident = GeoIPWrapper()
    _refererident = RefererAnalyzer()
    encoding='utf-8'

    def __init__(self, *params):
        self.begin_time = 0
        self.begin_time_string = ''
        self.end_time = 0
        self.end_time_string = ''
        self.countryextension = ''
        self.countryname = ''
        self.hostname = ''
        self.country_icon = ''
        self.os = ''
        self.os_icon = ''
        self.os_version = ''
        self.os_uri = ''
        self.fullbrowser = ''
        self.browser = ''
        self.browser_icon = ''
        self.browser_version = ''
        self.browser_uri = ''
        self.referer_site = ''
        self.referer_page = ''
        self.referer = ''
        self.first_logline = ''
        self.search = ''
        self.code = 0;
        self.code_description = ''
        self.user= ''
        self.pages = []
        self.durations = []
        self.reloads = []
        self.is_bot = "No"
        self.botname = ''
        self.bot_icon = ''
        self.bot_version = ''
        self.bot_uri = ''
        self.transferred_bytes = 0
        self.number = 0

        if len(params) > 0:
            logline = params[0]
            self.begin_from_line(logline);
    def begin_from_line(self, logline):
        """Start the visit from a ApacheLogLine"""
        if isinstance(logline, ApacheLogLine):
            self.pages.append(logline)
            self.first_logline = cgi.escape(logline.full_line)
            self.durations.append(0)
            self.reloads.append(0)
            self.begin_time = logline.accesstime_seconds
            self.begin_time_string = cgi.escape(logline.accesstime_string)
            self.end_time = self.begin_time
            self.end_time_string = self.begin_time_string
            self.code = logline.code
            self.code_description = logline.code_description
            self.user = cgi.escape(logline.user)
            self.transferred_bytes = int(logline.size)
            countryinfo = self._countryident.country_from_host(logline.hostname)
            self.countryextension = countryinfo['code']
            self.countryname = countryinfo['name']
            self.country_icon = os.path.join(self.imagedir, countryinfo['icon'])
            self.hostname = cgi.escape(logline.hostname)
            osinfo = self._osident.os_from_browserstring(logline.browser)
            self.os = cgi.escape(osinfo['title'])
            self.os_icon = os.path.join(self.imagedir, osinfo['icon'])
            self.os_version = cgi.escape(osinfo['version'])
            self.os_uri = cgi.escape(osinfo['uri'])
            self.fullbrowser = cgi.escape(logline.browser)
            self.referer = cgi.escape(logline.referer)
            if self.referer != "":
                self._refererident.analyze(logline.referer)
                self.referer_site = cgi.escape(self._refererident.referersite)
                self.referer_page = cgi.escape(self._refererident.refererpage)
                if (self._refererident.has_search):
                    self.search = cgi.escape(self._refererident.searchstring)
            robotinfo = None
            if self.os == 'other': # probably bot
                robotinfo = self._robotident.robot_from_browserstring(logline.browser)
                if robotinfo is not None:
                    self.is_bot = "Yes"
                    self.botname = cgi.escape(robotinfo['title'])
                    self.bot_icon = os.path.join(self.imagedir, robotinfo['icon'])
                    self.bot_version = cgi.escape(robotinfo['version'])
                    self.bot_uri = cgi.escape(robotinfo['uri'])
                    # fix the hostnames for the most common bots
                    if self.hostname.endswith("crawl.yahoo.net"):
                        self.hostname = "crawl.yahoo.net"
                    elif self.hostname.endswith("search.live.com"):
                        self.hostname = "search.live.com"
                    elif self.hostname.endswith("googlebot.com"):
                        self.hostname = "googlebot.com"
                    elif self.hostname.endswith("inktomisearch.com"):
                        self.hostname = "inktomisearch.com"
                    elif self.hostname.endswith("phx.gbl"):
                        self.hostname = "phx.gbl"
            if self.os != 'other' or robotinfo is None: # probably human
                browserinfo = self._browserident.browser_from_browserstring(logline.browser)
                self.browser = cgi.escape(browserinfo['title'])
                self.browser_icon = os.path.join(self.imagedir, browserinfo['icon'])
                self.browser_version = cgi.escape(browserinfo['version'])
                self.browser_uri = cgi.escape(browserinfo['uri'])

        else:
            raise NoLoglineException

    def add_line(self, logline):
        """Add another ApacheLogLines to the visit"""
        if isinstance(logline, ApacheLogLine):
            if logline.file == self.pages[-1].file:
                self.reloads[-1] += 1
            else: # new page
                self.reloads.append(0)
                self.durations[-1] = logline.accesstime_seconds - self.pages[-1].accesstime_seconds
                self.durations.append(0)
                self.pages.append(logline)
            self.transferred_bytes += int(logline.size)
            self.end_time = logline.accesstime_seconds
            self.end_time_string = logline.accesstime_string
            if logline.user != '':
                self.user = cgi.escape(logline.user)
        else:
            raise NoLoglineException
    def writeout(self, filename):
        tp = TemplateProcessor(template = self.html_template)
        if not os.path.isdir(self.outdir):
            os.makedirs(self.outdir)
        def pagedata(index, varname):
            loopreplacements = {
                'iteration' : str(index+1),
                'file': self.pages[index].file,
                'time': str(self.durations[index]),
                'reload': str(self.reloads[index]),
                'code': self.pages[index].code_description,
                'full_line': cgi.escape(self.pages[index].full_line)
            }
            try:
                return loopreplacements[varname]
            except:
                return None
        replacements = {}
        for (key, item) in self.__dict__.items():
            if isinstance(item, basestring):
                replacements[key] = item
            elif isinstance(item, int):
                replacements[key] = str(item)
        replacements['transferred_kb'] = "%.1f" % (float(self.transferred_bytes) / float(1024))
        replacements['transferred_mb'] = "%.1f" % (float(self.transferred_bytes) / float(1048576))
        tp.replacements = replacements
        tp.loops = {'pages' : LoopData(length=len(self.pages), datafunction=pagedata) }
        tp.output = os.path.join(self.outdir, filename)

        tp.run()
    def __str__(self): # for debugging
        result = str(type(self)) + "\n"
        for attribute in self.__dict__.keys():
            result =  result + "    " + attribute + ": " + str(self.__dict__[attribute]) + "\n"
        return result




class VisitManager(object):
    """  Create visits from ApacheLogLines and manage them.

         ApacheLogLines can be added to the manager with the
         add_logline method. Visits are created and (when closed)
         stored in the visits attribute, which is an array of Visits

         You can filter for any of the Visit-attributes with regular
         expressions

         There is one class attribute:
            visitduration [1800]    seconds until a visit times out
                                    and is declared closed

         There are the vollowing instance attributes:
            filtered        number of visits that were filtered
            registered      number of closed visits that were not filtered

         Visits that are not yet closed are stored separately internally.
         You may have to used the close_open_visits method to force them
         to close at the end
    """
    visitduration = 1800
    def __init__(self):
        self.visits = []
        self._openvisits = []
        self._done = False # have we found the visit the the logline belongs to?
        self._includepatterns = []
        self._excludepatterns = []
        self.registered = 0
        self.filtered = 0


    def add_logline(self, logline):
        """ Register an ApacheLogLine to the manager

            The logline will either be incorporated into an existing open
            visit, or will start a new visit. The following criteria decide
            if a new logline belongs to the an existing open visit:

                - access time is less then 1800 seconds (or what is set as
                  VisitManager.visitduration) later than the last access
                  in the open visit. If that is not the case, the open visit
                  will be closed
                - the hostnames match
                - the browser string matches

            Make sure to feed loglines in the order of progressing time.
        """
        self._done = False
        if isinstance(logline, ApacheLogLine):
            new_openvisits = []
            for openvisit in self._openvisits:
                if (logline.accesstime_seconds - openvisit.end_time) > self.visitduration:
                    if self._visit_fits_pattern(openvisit):
                        self.registered += 1
                        openvisit.number = self.registered
                        self.visits.append(openvisit) # visit is now closed
                    else:
                        self.filtered += 1
                    continue;
                else: # we're in the visitduration time-frame
                    if self._done:
                        new_openvisits.append(openvisit)
                        continue;
                    # find out if the line belongs to the visit
                    same_visit =     (logline.hostname.endswith(openvisit.hostname)) \
                                 and (logline.browser  == openvisit.fullbrowser)
                    if same_visit:
                        openvisit.add_line(logline)
                        new_openvisits.append(openvisit)
                        self._done = True
                        continue;
                    else:
                        new_openvisits.append(openvisit)
                        continue;
            if not self._done:
                # the logline must be the beginning of a new visit
                newvisit = Visit()
                newvisit.begin_from_line(logline)
                new_openvisits.append(newvisit)
            self._openvisits = new_openvisits
        else:
            raise NoLoglineException

    def close_open_visits(self):
        """ Finish all open visits. """
        for visit in self._openvisits:
            self.visits.append(visit)
        self._openvisits = []

    def clear_all(self):
        """ Delete all registered visits, both closed and open. """
        self._openvisits = []
        self.visits = []

    def clear_closed(self):
        """ Delete all closed visits. """
        self.visits = []

    def add_includepattern(self, patterntuple):
        """ Add an include filter.

            Visits will only be accepted if they match this filter

            patterntuple consists of
            ('fieldname' , re.compile('regex'))
            with 'fieldname' being a valid attribute of a Visit
        """
        if isinstance(patterntuple, tuple) and isinstance(patterntuple[0], str):
            self._includepatterns.append(patterntuple)
        else:
            warn("Include patterns must be tuples of a field name and a compiled regex.")

    def add_excludepattern(self, patterntuple):
        """ Add an exclude filter.

            Visits will rejected if they match this filter

            patterntuple consists of
            ('fieldname' , re.compile('regex'))
            with 'fieldname' being a valid attribute of a Visit
        """
        if isinstance(patterntuple, tuple) and isinstance(patterntuple[0], str):
            self._excludepatterns.append(patterntuple)
        else:
            warn("Exclude patterns must be tuples of a field name and a compiled regex.")

    def clear_includepatterns(self):
        """ Delete all include patterns. """
        self._excludepatterns = []

    def clear_excludepatterns(self):
        """ Delete all exclude patterns. """
        self._excludepatterns = []

    def _visit_fits_pattern(self, visit):
        """ Tests if a Apachevisit passes the include- and exclude-patterns"""
        for (fieldname, pattern) in self._excludepatterns:
            try:
                m = pattern.search(visit.__dict__[fieldname])
            except AttributeError:
                warn("Exclude patterns must be tuples of a field name and a compiled regex.")
                warn("The object that you provided as a regex seems not to have a 'search' method")
                exit(-1)
            except KeyError:
                warn("You tried to filter for a field that doesn't exist")
                m = False
            if m:
                return False
        if len(self._includepatterns) == 0:
            return True # no includepatterns means 'accept everything'
        for (fieldname, pattern) in self._includepatterns:
            try:
                m = pattern.search(visit.__dict__[fieldname])
            except AttributeError:
                warn("Exclude patterns must be tuples of a field name and a compiled regex.")
                warn("The object that you provided as a regex seems not to have a 'search' method")
                exit(-1)
            except KeyError:
                warn("You tried to filter for a field that doesn't exist")
                m = False
            if m:
                return True
        return False
