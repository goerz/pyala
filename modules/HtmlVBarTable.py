# -*- coding: utf-8 -*-
from TemplateProcessor import *

def warn(msg):
    """ print a warning message to stderr """
    sys.stderr.write(str(msg))
    sys.stderr.write("\n")


class HtmlVBarTable(object):
    """ A html barchart creator that uses tables

        To use, just set the attributes, and then print the object to get the
        html output of the table

        Attributes:

            full_html [False]       Wrap the output in a complete html page, or not
            title     ["Title"]     The title of the barchart
            data                    A list of data for the bars. Each Item must be a
                                    tuple (value, label, color), where value is the
                                    number to be represented by the bar, label is a
                                    description that appears under the bar, and color
                                    is the html-coded color (as a string) that the bar
                                    should have (e.g.  "#c0cbeb")
            layout                  dictionary of layout options.

        Layout Options
        The following keys can be used for the layout attribute:

            layout['width']                      [100]          total width of output (min)
            layout['height']                     [100]          total height of output (min)
            layout['indent']                     [""]           string prepended to output
            layout['background_color']           ["#e5f2f7"]    color of bar background area
            layout['border_color']               ["#606680"]    color of border
            layout['unit']                       ['px']         unit of all numbers
            layout['blindpic']                   ['blank.png']  link to transparent pic
            layout['title']['height']            [14]           height of title area
            layout['title']['background_color']  ["#ffffff"]    color of title area
            layout['title']['fontsize']          [12]           size of title
            layout['title']['text_color']        ["#7f8499"]    color of title
            layout['label']['height']            [14]           height of label area
            layout['label']['background_color']  ["#808ebf"]    background color of label
            layout['label']['fontsize']          [12]           size of label
            layout['label']['text_color']        ["#ffffff"]    color of label
            layout['valuelabel']['fontsize']     [12]           size of valuelabel
            layout['valuelabel']['text_color']   ["#6c728a"]    color of valuelabel
    """
    def __init__(self):
        self.data = [] # tuples: (value, label, color)
        self.full_html = False
        self.title = "Title"
        self.layout = {
            'indent'           : "",
            'width'            : 100,
            'height'           : 100,
            'background_color' : "#e5f2f7",
            'border_color'     : "#606680",
            'unit'             : "px",
            'blindpic'         : 'blank.png',
            'title'            : {
                'height'           : 14,
                'background_color' : "#ffffff",
                'fontsize'         : 12,
                'text_color'       : "#7f8499"
            },
            'label'            : {
                'height'           : 14,
                'background_color' : "#808ebf",
                'fontsize'         : 12,
                'text_color'       : "#ffffff"
            },
            'valuelabel'       :{
                'fontsize'         : 12,
                'text_color'       : "#6c728a"
            }
        }
        self.templatestring = r'''<!-- if full_html == "True" -->
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=ISO-8859-1">
<title>[!-- var title --]</title>
</head>
<body>
<!-- endif -->
<!-- Begin Barchart-->
<table cellspacing="0" cellpadding="0" border="0" style="border-collapse:collapse; width: [!-- var barchart_width --]; height: [!-- var barchart_height --]; padding:0">
    <tr style="height:[!-- var titlefield_height --]; background-color:[!-- var title_backgroundcolor --]; font-family: Arial, Helvetica, sans-serif; font-size: [!-- var title_fontsize --]; text-align: center; font-weight: bold; padding: 0; white-space: nowrap; vertical-align:top; color: [!-- var title_fontcolor --]">
        <th colspan="[!-- var number_of_datapoints --]">[!-- var title --]</th>
    </tr>
    <tr style="border:solid 1px [!-- var bordercolor --]" > <!-- barchart row -->

        <!-- startloop data -->
        <td style="margin:0px; width=[!-- var bar_width --]"> <!-- vertical bar cell -->
            <table cellspacing="0" cellpadding="0" style="height:100%; width:100%; padding:0">
                <!-- if data.bar_height.find("0") != 0 -->
                <tr style="background-color:[!-- var backgroundcolor --]; text-align: center; vertical-align:bottom">
                    <td style="font-family: Arial, Helvetica, sans-serif; color: [!-- var valuelabel_color --]; font-size: [!-- var number_fontsize --]; padding: 0">[!-- loopvar data.value --]</td>
                </tr> <!-- the background -->
                <tr style="height:[!-- loopvar data.bar_height --]; background-color:[!-- loopvar data.bar_color --]; text-align: center; vertical-align:middle">
                    <td style="padding: 0; border:solid [!-- var bordercolor --]; border-width: [!-- loopvar data.topborder --] [!-- loopvar data.rightborder --] [!-- loopvar data.bottomborder --] [!-- loopvar data.leftborder --]; border-collapse:collapse">
                        <img src="[!-- var blindpic --]" width="[!-- var bar_width --]" height="[!-- loopvar data.bar_height --]" alt="">
                    </td>
                </tr> <!-- the bar -->
                <!-- else -->
                <tr style="background-color:[!-- var backgroundcolor --]; text-align: center; vertical-align:bottom">
                    <td style="font-family: Arial, Helvetica, sans-serif; color: [!-- var valuelabel_color --]; font-size: [!-- var number_fontsize --]; padding: 0"><img src="[!-- var blindpic --]" width="[!-- var bar_width --]" height="[!-- loopvar data.bar_height --]" alt=""></td>
                </tr> <!-- the background -->
                <!-- endif -->
            </table>
        </td>
        <!-- endloop data -->

    </tr>
    <tr style="height:[!-- var label_height --]; border-width:1px; border-style:solid; border-color:[!-- var bordercolor --]; background-color:[!-- var label_backgroundcolor --]; font-family: Arial, Helvetica, sans-serif; font-size: [!-- var label_fontsize --]; text-align: center; font-weight: bold; padding: 0; white-space: nowrap; vertical-align:top; color: [!-- var label_fontcolor --]"> <!-- label row at bottom -->
        <!-- startloop data -->
        <td>[!-- loopvar data.barlabel --]</td>
        <!-- endloop data -->
    </tr>
</table>
<!-- End Barchart -->
<!-- if full_html == "True" -->
</body>
<!-- endif -->
'''
    def _loopfunction(self, index, varname):
        if self._loopmapping.has_key(varname):
            return (self._loopmapping[varname])[index]
        else:
            if varname == 'topborder':
                return "1px"
            if varname == 'bottomborder':
                return "0px"
            if varname == 'leftborder':
                if index == 0:
                    return "0px"
                else:
                    if self.data[index-1][0] >= self.data[index][0]:
                        return "0px"
                    else:
                        return "1px"
            if varname == 'rightborder':
                if index == len(self.data)-1:
                    return "0px"
                else:
                    if self.data[index+1][0] <= self.data[index][0]:
                        return "1px"
                    else:
                        return "0px"
        return None

    def __str__(self):
        if len(self.data) > 0:
            self._available_bar_space = 0.9 * (self.layout['height']
                                        - self.layout['title']['height']
                                        - self.layout['label']['height'])
            self._maxdatavalue = max([ t[0] for t in self.data])
            self._loopmapping = {
                'value'            : [t[0] for t in self.data],
                'bar_color'  : [t[2] for t in self.data],
                'bar_height'        : \
                            [(str(int(((float(t[0]) / float(self._maxdatavalue))*self._available_bar_space)))\
                                +  self.layout['unit']) for t in self.data],
                'barlabel'         : [t[1] for t in self.data]
            }
            self._mappings = {
                'full_html'             : str(self.full_html),
                'barchart_width'        : str(self.layout['width']) + self.layout['unit'],
                'barchart_height'       : str(self.layout['height']) + self.layout['unit'],
                'backgroundcolor'       : self.layout['background_color'],
                'bordercolor'           : self.layout['border_color'],
                'title'                 : self.title,
                'number_of_datapoints'  : str(len(self.data)),
                'titlefield_height'     : str(self.layout['title']['height']) + self.layout['unit'],
                'title_backgroundcolor' : self.layout['title']['background_color'],
                'title_fontsize'        : str(self.layout['title']['fontsize']) + self.layout['unit'],
                'title_fontcolor'       : self.layout['title']['text_color'],
                'label_height'          : str(self.layout['label']['height']) + self.layout['unit'],
                'label_backgroundcolor' : self.layout['label']['background_color'],
                'label_fontsize'        : str(self.layout['label']['fontsize']) + self.layout['unit'],
                'label_fontcolor'       : self.layout['label']['text_color'],
                'number_fontsize'       : str(self.layout['valuelabel']['fontsize']) + self.layout['unit'],
                'valuelabel_color'      : self.layout['valuelabel']['text_color'],
                'blindpic'              : self.layout['blindpic'],
                'bar_width'             : str((self.layout["width"] / len(self.data))) + self.layout['unit']
            }
            processor = TemplateProcessor( memorytemplate=self.templatestring, \
                                           replacements=self._mappings,\
                                           loops={  'data': LoopData( len(self.data), self._loopfunction)  }, \
                                           indent=self.layout['indent'] \
                                         )
            return processor.run(to_memory=True)
        else:
            warn("No data to print out")
            return ""
