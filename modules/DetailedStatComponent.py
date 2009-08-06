# -*- coding: utf-8 -*-
from visit import Visit
from TemplateProcessor import TemplateProcessor, LoopData
import ApacheLogParser
import os
import os.path
import sys
import HTMLCalendar

def warn(msg):
    """ print a warning message to stderr """
    sys.stderr.write(str(msg))
    sys.stderr.write("\n")



class DetailedStatComponent(object):
    """ Keep track of the detailed statistics of individual visits

        The options has the following option, to be set with set_option:
            outdir            [""]    from the perspective of the running program,
                                      the output directory
            imagedir          [""]    from the perspective of the output, the
                                      image directory
            title             [""]    A title string that appears in the output
            visits_per_page   [250]   The number of visits on one page
            write_visit_pages [True]  Write a page for each visit?
            html_template     [""]
            html_toc_template [""]

        Read-Only instance attributes are:
            number_of_visits
            number_of_pages
    """

    _outfilename = "detailstat.html"
    _visit_page_folder = "visits/" # the trailing slash is important
    _visit_filename_length = 12

    def __init__(self):
        import OptionManager
        self._options = OptionManager.OptionManager()
        self._options.validoptions = ['outdir', 'imagedir', 'visits_per_page',
                                     'write_visit_pages', 'html_template',
                                     'html_toc_template', 'title']
        self._options.set_rule('outdir', OptionManager.rule_ensure_dir)
        self._options.set_rule('imagedir', OptionManager.rule_ensure_dir)
        self._options.set_rule('visits_per_page', lambda n: (type(n) is int and n > 0))
        self._options.set_rule('write_visit_pages', lambda b: (type(b) is bool))
        self._options.set_rule('html_template', os.path.exists)
        self._options.set_rule('html_toc_template', os.path.exists)
        self.set_option('visits_per_page', 250)
        self.set_option('write_visit_pages', True)
        self.set_option('title', "")
        self._visits           = []
        self._openvisits       = 0
        self._number_of_visits  = 0
        self._number_of_pages   = 0
        self._anchors          = {} # data structure for anchors, will be filled as
                                    # _anchors[year][month][day]['uri']
        self._anchor_ids       = [] # list of visit ID's that are an anchor

    def __getattr__(self, attr):
        if attr == 'number_of_visits':
            return self._number_of_visits
        elif attr == 'number_of_pages':
            return self._number_of_pages
        raise AttributeError, "type object 'DetailedStatComponent' has no attribute '%s'" % attr


    def register_visit(self, visit):
        if isinstance(visit, Visit):
            self._number_of_visits += 1
            visit.number = self._number_of_visits
            if self.get_option('write_visit_pages'):
                Visit.outdir = os.path.join(self.get_option('outdir'), self._visit_page_folder)
                Visit.imagedir = os.path.join("../"*self._visit_page_folder.count("/"), self.get_option('imagedir'))
                visit.writeout( str(visit.number).zfill(self._visit_filename_length) + ".html" )
            self._visits.append(visit)
            self._test_and_set_anchor(len(self._visits)-1) # set anchor for visit, if applicable
            self._openvisits = len(self._visits)
            if self._openvisits >= self.get_option('visits_per_page'):
                self._writeout()
                self._visits = []
                self._openvisits = 0
        else:
            warn("You tried to pass something to the DetailedStatComponent that was not a Visit")

    def finish(self):
        """ Write out all unwritten visits, and create a TOC """
        self._writeout(is_last = True)
        self._visits = []
        self._openvisits = 0
        self._write_toc()

    def set_option(self, option, value):
        """ Set an option. See valid options in the class docstring."""
        return self._options.set_option(option, value)

    def get_option(self, option):
        """ Get an option. See valid options in the class docstring."""
        return self._options.get_option(option)

    def _test_and_set_anchor(self, index):
        """ Check if a visit is the first of the day, and mark as anchor position if so """
        visit = self._visits[index]
        visit_time = ApacheLogParser.extract_from_date(visit.begin_time, visit.pages[0].serveroffset)
        year = visit_time.tm_year
        month = visit_time.tm_mon
        day = visit_time.tm_mday
        day_of_year = visit_time.tm_yday
        prev_visit_day_of_year = day_of_year - 1
        if index > 0:
            prev_visit_day_of_year = \
                ApacheLogParser.extract_from_date(self._visits[index-1].begin_time).tm_yday
        if day_of_year > prev_visit_day_of_year: # there should be an anchor
            uri_filename = self._outfilename.replace( ".html", \
                   str(self._number_of_pages+1).zfill(6) +".html" )
            uri = uri_filename + "#a" + str(visit.number)
            if not self._anchors.has_key(year):
                self._anchors[year] = {}
            if not self._anchors[year].has_key(month):
                self._anchors[year][month] = {}
            if not self._anchors[year][month].has_key(day):
                self._anchors[year][month][day] = uri
                self._anchor_ids.append(visit.number)


    def _write_toc(self):
        """ Write the main table of contents file with a calendar"""
        tp = TemplateProcessor(template = self.get_option('html_toc_template'))
        # build list of the months, so that we can index it
        # we need three lists:
        monthlist = [] # to keep the dict that maps days to anchors for each month
        monthnamelist = [] # the names (number) of the corresponding months
        yearnamelist = [] # the names (number) of the corresponding years
        minyear = min(self._anchors.keys())
        maxyear = max(self._anchors.keys())
        for year in xrange(minyear, maxyear+1):
            if self._anchors.has_key(year):
                # try each month in every year, and see if an entry exists
                for month in xrange(1,13):
                    if self._anchors[year].has_key(month):
                        monthlist.append(self._anchors[year][month])
                        monthnamelist.append(month)
                        yearnamelist.append(year)

        def calendarloop(index, varname):
            loopreplacements = {
                'calendar'  : HTMLCalendar.MonthCal().render(yearnamelist[index], \
                                                             monthnamelist[index], \
                                                             monthlist[index])
            }
            if len(monthlist) > 2:
                loopreplacements['calendar'] = "<div style=\"float: left; width: 33%\">\n" \
                                               + loopreplacements['calendar']
            else:
                loopreplacements['calendar'] = "<div style=\"float: left; width: %s" % (100/len(monthlist)) \
                                               + "%\">\n" + loopreplacements['calendar']
            loopreplacements['calendar'] += "</div>\n"
            try:
                return loopreplacements[varname]
            except:
                return None

        replacements = {
            'headrow' : self.get_option('title') + "&nbsp;&nbsp;-&nbsp;&nbsp;TOC",
            'total_visits': str(self._number_of_visits),
            'link_to_prev': self._outfilename.replace( ".html", \
                            str(self._number_of_pages-1).zfill(6) +".html" ),
            'link_to_next': self._outfilename.replace( ".html", \
                            str(self._number_of_pages+1).zfill(6) +".html" )
        }
        tp.replacements = replacements
        tp.loops = {'calendars' : LoopData(\
                                  length=len(monthlist), \
                                  datafunction=calendarloop) }
        tp.output = os.path.join(self.get_option('outdir'), self._outfilename)

        tp.run()


    def _writeout(self, is_last=False):
        """ Write out all registered visits and clear the list """
        self._number_of_pages += 1
        is_first = (self._number_of_pages == 1)
        filename = self._outfilename.replace( ".html", \
                   str(self._number_of_pages).zfill(6) +".html" )
        tp = TemplateProcessor(template = self.get_option('html_template'))
        def visitloop(index, varname):
            loopreplacements = {
                'id'                : str(self._visits[index].number),
                'time'              : ApacheLogParser.stringdate( \
                                          self._visits[index].begin_time, \
                                          pattern="%m/%d/%y %H:%M:%S", \
                                          offset=self._visits[index].pages[-1].serveroffset),
                'countryicon'       : self._visits[index].country_icon,
                'countryname'       : self._visits[index].countryname,
                'countryextension'  : self._visits[index].countryextension,
                'hostname'          : self._visits[index].hostname,
                'hostname_short'    : self._visits[index].hostname[-27:],
                'number_of_pages'   : str(len(self._visits[index].pages)),
                'visitpage'         : os.path.join(
                                       self._visit_page_folder,
                                       str(self._visits[index].number).zfill(\
                                                  self._visit_filename_length) + ".html" ),
                'os_icon'           : self._visits[index].os_icon,
                'full_os'           : self._visits[index].os + ' ' + self._visits[index].os_version,
                'os'                : self._visits[index].os,
                'browser_icon'      : self._visits[index].browser_icon,
                'full_browser'      : self._visits[index].browser + ' ' \
                                      + self._visits[index].browser_version \
                                      + ' (' +  self._visits[index].fullbrowser + ')',
                'browser'           : self._visits[index].browser,
                'referer_url'       : self._visits[index].referer,
                'referer_site'      : self._visits[index].referer_site,
                'referer_page'      : self._visits[index].referer_page,
                'last_page'         : self._visits[index].pages[-1].file,
                'last_page_short'   : self._visits[index].pages[-1].file[\
                                            self._visits[index].pages[-1].file.rfind("/", 0, -2)+1:],
                'search_term'       : self._visits[index].search.replace(r'"',r'&quot;'),
                'search_term_short' : self._visits[index].search[:27],
                'is_bot'            : str(self._visits[index].is_bot),
                'anchor_name'       : 'a' + str(self._visits[index].number)
            }
            if len(loopreplacements['last_page_short']) > 30:
                loopreplacements['last_page_short'] = \
                    loopreplacements['last_page_short'][:27] + "..."
            if len(self._visits[index].search) > 27:
                loopreplacements['search_term_short'] = loopreplacements['search_term_short'] + "..."
            if len(self._visits[index].hostname) > 27:
                loopreplacements['hostname_short'] = "..." +  loopreplacements['hostname_short']
            if self._visits[index].is_bot == "Yes":
                loopreplacements['os_icon'] =  self._visits[index].bot_icon
                loopreplacements['os'] =  self._visits[index].botname
                loopreplacements['full_os'] =  self._visits[index].botname + self._visits[index].bot_version
                loopreplacements['browser_icon'] =  self._visits[index].bot_icon
                loopreplacements['browser'] =  self._visits[index].botname
                loopreplacements['full_browser'] =  self._visits[index].botname + self._visits[index].bot_version
            try:
                return loopreplacements[varname]
            except:
                return None
        replacements = {
            'headrow' : self.get_option('title'),
            'visits_per_page': str(self.get_option('visits_per_page')),
            'link_to_prev': self._outfilename.replace( ".html", \
                            str(self._number_of_pages-1).zfill(6) +".html" ),
            'link_to_next': self._outfilename.replace( ".html", \
                            str(self._number_of_pages+1).zfill(6) +".html" ),
            'link_to_toc' : self._outfilename,
            'write_visit_pages' : str(self.get_option('write_visit_pages'))
        }
        if is_first:
            replacements['link_to_prev'] = self._outfilename
        if is_last:
            replacements['link_to_next'] = self._outfilename
        tp.replacements = replacements
        tp.loops = {'visits' : LoopData(length=len(self._visits), datafunction=visitloop) }
        tp.output = os.path.join(self.get_option('outdir'), filename)

        tp.run()