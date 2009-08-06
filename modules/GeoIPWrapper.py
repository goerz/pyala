# -*- coding: utf-8 -*-
import re
import sys

# TODO: make this compatible with Windows

def warn(msg):
    """ print a warning message to stderr """
    sys.stderr.write(str(msg))
    sys.stderr.write("\n")


class GeoIP_dummy(object):
    """ A dummy object that stands in if the GeoIP module is not available """
    def country_code_by_name(self, s):
        """ Return 'N/A' """
        return "N/A"
    def  country_code_by_addr(self, s):
        """ Return 'N/A' """
        return "N/A"
    def country_name_by_name(self, s):
        """ Return 'Unknown' """
        return "Unknown"
    def country_name_by_addr(self, s):
        """ Return 'Unknown' """
        return "Unknown"


class GeoIPWrapper(object):
    """ Provide country identification for hostnames and ip's as a wrapper of GeoIP

        If the GeoIP module is not available, functionality will be severely crippled.

        The following class attributes are available:
            countrynames        a hash of country codes to country names
            pre_try             a list of frequent hostnames, with country code
            frequentfailures    a secondary list of frequent hostnames that are not
                                matched otherwise
    """

    countrynames = {
        'A1' : "Anonymous Proxy",
        'A2' : "Satellite Provider",
        'AD' : "Andorra",
        'AE' : "United Arab Emirates",
        'AF' : "Afghanistan",
        'AG' : "Antigua and Barbuda",
        'AI' : "Anguilla",
        'AL' : "Albania",
        'AM' : "Armenia",
        'AN' : "Netherlands Antilles",
        'AO' : "Angola",
        'AP' : "Asia/Pacific Region",
        'AQ' : "Antarctica",
        'AR' : "Argentina",
        'AS' : "American Samoa",
        'AT' : "Austria",
        'AU' : "Australia",
        'AW' : "Aruba",
        'AX' : "Aland Islands",
        'AZ' : "Azerbaijan",
        'BA' : "Bosnia and Herzegovina",
        'BB' : "Barbados",
        'BD' : "Bangladesh",
        'BE' : "Belgium",
        'BF' : "Burkina Faso",
        'BG' : "Bulgaria",
        'BH' : "Bahrain",
        'BI' : "Burundi",
        'BJ' : "Benin",
        'BM' : "Bermuda",
        'BN' : "Brunei Darussalam",
        'BO' : "Bolivia",
        'BR' : "Brazil",
        'BS' : "Bahamas",
        'BT' : "Bhutan",
        'BV' : "Bouvet Island",
        'BW' : "Botswana",
        'BY' : "Belarus",
        'BZ' : "Belize",
        'CA' : "Canada",
        'CC' : "Cocos (Keeling) Islands",
        'CD' : "Congo, The Democratic Republic of the",
        'CF' : "Central African Republic",
        'CG' : "Congo",
        'CH' : "Switzerland",
        'CI' : "Cote d'Ivoire",
        'CK' : "Cook Islands",
        'CL' : "Chile",
        'CM' : "Cameroon",
        'CN' : "China",
        'CO' : "Colombia",
        'CR' : "Costa Rica",
        'CS' : "Czechoslovakia",
        'CU' : "Cuba",
        'CV' : "Cape Verde",
        'CX' : "Christmas Island",
        'CY' : "Cyprus",
        'CZ' : "Czech Republic",
        'DE' : "Germany",
        'DJ' : "Djibouti",
        'DK' : "Denmark",
        'DM' : "Dominica",
        'DO' : "Dominican Republic",
        'DZ' : "Algeria",
        'EC' : "Ecuador",
        'EE' : "Estonia",
        'EG' : "Egypt",
        'EH' : "Western Sahara",
        'ER' : "Eritrea",
        'ES' : "Spain",
        'ET' : "Ethiopia",
        'EU' : "Europe",
        'FI' : "Finland",
        'FJ' : "Fiji",
        'FK' : "Falkland Islands (Malvinas)",
        'FM' : "Micronesia, Federated States of",
        'FO' : "Faroe Islands",
        'FR' : "France",
        'GA' : "Gabon",
        'GB' : "United Kingdom",
        'GD' : "Grenada",
        'GE' : "Georgia",
        'GF' : "French Guiana",
        'GG' : "Guernsey",
        'GH' : "Ghana",
        'GI' : "Gibraltar",
        'GL' : "Greenland",
        'GM' : "Gambia",
        'GN' : "Guinea",
        'GP' : "Guadeloupe",
        'GQ' : "Equatorial Guinea",
        'GR' : "Greece",
        'GS' : "South Georgia and the South Sandwich Islands",
        'GT' : "Guatemala",
        'GU' : "Guam",
        'GW' : "Guinea-Bissau",
        'GY' : "Guyana",
        'HK' : "Hong Kong",
        'HM' : "Heard Island and McDonald Islands",
        'HN' : "Honduras",
        'HR' : "Croatia",
        'HT' : "Haiti",
        'HU' : "Hungary",
        'ID' : "Indonesia",
        'IE' : "Ireland",
        'IL' : "Israel",
        'IM' : "Isle of Man",
        'IN' : "India",
        'IO' : "British Indian Ocean Territory",
        'IQ' : "Iraq",
        'IR' : "Iran, Islamic Republic of",
        'IS' : "Iceland",
        'IT' : "Italy",
        'JE' : "Jersey",
        'JM' : "Jamaica",
        'JO' : "Jordan",
        'JP' : "Japan",
        'KE' : "Kenya",
        'KG' : "Kyrgyzstan",
        'KH' : "Cambodia",
        'KI' : "Kiribati",
        'KM' : "Comoros",
        'KN' : "Saint Kitts and Nevis",
        'KP' : "Korea, Democratic People's Republic of",
        'KR' : "Korea, Republic of",
        'KW' : "Kuwait",
        'KY' : "Cayman Islands",
        'KZ' : "Kazakhstan",
        'LA' : "Lao People's Democratic Republic",
        'LB' : "Lebanon",
        'LC' : "Saint Lucia",
        'LI' : "Liechtenstein",
        'LK' : "Sri Lanka",
        'LR' : "Liberia",
        'LS' : "Lesotho",
        'LT' : "Lithuania",
        'LU' : "Luxembourg",
        'LV' : "Latvia",
        'LY' : "Libyan Arab Jamahiriya",
        'MA' : "Morocco",
        'MC' : "Monaco",
        'MD' : "Moldova, Republic of",
        'ME' : "Montenegro",
        'MG' : "Madagascar",
        'MH' : "Marshall Islands",
        'MK' : "Macedonia",
        'ML' : "Mali",
        'MM' : "Myanmar",
        'MN' : "Mongolia",
        'MO' : "Macao",
        'MP' : "Northern Mariana Islands",
        'MQ' : "Martinique",
        'MR' : "Mauritania",
        'MS' : "Montserrat",
        'MT' : "Malta",
        'MU' : "Mauritius",
        'MV' : "Maldives",
        'MW' : "Malawi",
        'MX' : "Mexico",
        'MY' : "Malaysia",
        'MZ' : "Mozambique",
        'NA' : "Namibia",
        'NC' : "New Caledonia",
        'NE' : "Niger",
        'NF' : "Norfolk Island",
        'NG' : "Nigeria",
        'NI' : "Nicaragua",
        'NL' : "Netherlands",
        'NO' : "Norway",
        'NP' : "Nepal",
        'NR' : "Nauru",
        'NU' : "Niue",
        'NZ' : "New Zealand",
        'OM' : "Oman",
        'PA' : "Panama",
        'PE' : "Peru",
        'PF' : "French Polynesia",
        'PG' : "Papua New Guinea",
        'PH' : "Philippines",
        'PK' : "Pakistan",
        'PL' : "Poland",
        'PM' : "Saint Pierre and Miquelon",
        'PN' : "Pitcairn",
        'PR' : "Puerto Rico",
        'PS' : "Palestinian Territory",
        'PT' : "Portugal",
        'PW' : "Palau",
        'PY' : "Paraguay",
        'QA' : "Qatar",
        'RE' : "Reunion",
        'RO' : "Romania",
        'RS' : "Serbia",
        'RU' : "Russian Federation",
        'RW' : "Rwanda",
        'SA' : "Saudi Arabia",
        'SB' : "Solomon Islands",
        'SC' : "Seychelles",
        'SD' : "Sudan",
        'SE' : "Sweden",
        'SG' : "Singapore",
        'SH' : "Saint Helena",
        'SI' : "Slovenia",
        'SJ' : "Svalbard and Jan Mayen",
        'SK' : "Slovakia",
        'SL' : "Sierra Leone",
        'SM' : "San Marino",
        'SN' : "Senegal",
        'SO' : "Somalia",
        'SR' : "Suriname",
        'ST' : "Sao Tome and Principe",
        'SU' : "Soviet Union",
        'SV' : "El Salvador",
        'SY' : "Syrian Arab Republic",
        'SZ' : "Swaziland",
        'TC' : "Turks and Caicos Islands",
        'TD' : "Chad",
        'TF' : "French Southern Territories",
        'TG' : "Togo",
        'TH' : "Thailand",
        'TJ' : "Tajikistan",
        'TK' : "Tokelau",
        'TL' : "Timor-Leste",
        'TM' : "Turkmenistan",
        'TN' : "Tunisia",
        'TO' : "Tonga",
        'TP' : "Timor-Leste",
        'TR' : "Turkey",
        'TT' : "Trinidad and Tobago",
        'TV' : "Tuvalu",
        'TW' : "Taiwan",
        'TZ' : "Tanzania, United Republic of",
        'UA' : "Ukraine",
        'UG' : "Uganda",
        'UM' : "United States Minor Outlying Islands",
        'US' : "United States",
        'UY' : "Uruguay",
        'UZ' : "Uzbekistan",
        'VA' : "Holy See (Vatican City State)",
        'VC' : "Saint Vincent and the Grenadines",
        'VE' : "Venezuela",
        'VG' : "Virgin Islands, British",
        'VI' : "Virgin Islands, U.S.",
        'VN' : "Vietnam",
        'VU' : "Vanuatu",
        'WF' : "Wallis and Futuna",
        'WS' : "Samoa",
        'YE' : "Yemen",
        'YT' : "Mayotte",
        'ZA' : "South Africa",
        'ZM' : "Zambia",
        'ZW' : "Zimbabwe",
        'ZR' : "Zaire",
        'N/A': 'Unknown'
    }

    pre_try = []


    frequentfailures = []

    def __init__(self):
        try:
            import GeoIP
            GeoIPavailable = True
        except ImportError:
            warn("GeoIP module is not available. Please get it from http://www.maxmind.com/app/python")
            GeoIPavailable = False
        if GeoIPavailable:
            try:
                self.gi = GeoIP.open("GeoIPData/GeoIP.dat",GeoIP.GEOIP_STANDARD)
            except SystemError:
                self.gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
        else:
            self.gi = GeoIP_dummy()
        self.ip_pattern = re.compile(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$")


    def country_from_host(self, host):
        """ Return country information for hostname or IP

            Result is a dict with the following keys:
                name        the full country name, or "Unknown"
                code        the two-letter country code, or "N/A"
                icon        an icon representing the country
        """
        host = host.strip()
        countrycode = "N/A"
        if self.ip_pattern.match(host): # it's an ip address
            countrycode = self.gi.country_code_by_addr(host)
        else: # it's a hostname
            countrycode = None
            # try the pre_try dict first of all
            for (key, cc_value) in self.pre_try:
                if host.endswith(key):
                    countrycode = cc_value
                    break
            if countrycode is None:
                # try the normal lookup
                countrycode = self.gi.country_code_by_name(host)
            if countrycode is None:
                # try the frequentfailures list
                for (key, cc_value) in self.frequentfailures:
                    if host.endswith(key):
                        countrycode = cc_value
                        break
            if countrycode is None:
                # maybe the country is in the hostname?
                countrycode = re.search(r'\.([^.]{2})$', host)
                if countrycode is not None:
                    countrycode = countrycode.group(1).upper()
                    if self.countryname_from_code(countrycode) == 'Unknown': # failed
                        countrycode = None
                else:
                    # try just the last part of the hostname
                    host_site = re.search(r'\.([^.]+\.[^.]{2,3})$', host)
                    if host_site is not None:
                        host_site = host_site.group(1)
                        countrycode = self.gi.country_code_by_name(host_site)
            if countrycode is None:
                # maybe there's an ip address encoded in the hostname
                ip_guess = re.search(r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).', host)
                if ip_guess is not None:
                    host =   ip_guess.group(1) + "." + ip_guess.group(2) + "." \
                           + ip_guess.group(3) + "." + ip_guess.group(4)
                    countrycode = self.gi.country_code_by_addr(host)
        if countrycode is None:
            # Give up
            countrycode = "N/A"
        return {'name':self.countryname_from_code(countrycode), 'code': countrycode, 'icon': self.icon_from_code(countrycode)}

    def countryname_from_code(self, code):
        """ Get full country name from two-letter country code """
        try:
            return self.countrynames[code]
        except KeyError:
            return 'Unknown'

    def icon_from_code(self, code):
        """ Get icon from two-letter country code"""
        if (code == "A1") or (code == "A2"):
            return "ext_com.png"
        if code == "N/A":
            return "ext_unknown.png"
        return "ext_" + code.lower() + ".png"



def _load_mapping_from_file(file, mappingvar):
    try:
       efm = open(file)
       for line in efm:
           rulepair = line.split(":")
           if len(rulepair) == 2:
               hostname = rulepair[0].strip()
               extension = rulepair[1].strip()
               if GeoIPWrapper.countrynames.has_key(extension):
                   mappingvar.append((hostname, extension))
               else:
                   warn("'%s' in the line line %s in %s is not a valid country extension" \
                              % ( extension, line.strip(), 'ext_failure_mappings.txt'))
           else:
               warn("Could not understand line %s in %s" \
                              % (line.strip(), 'ext_failure_mappings.txt'))
    except IOError:
        warn("File '%s' does not exist or is not readable" %  'ext_failure_mappings.txt')


_load_mapping_from_file('GeoIPData/ext_failure_mappings.txt', GeoIPWrapper.frequentfailures)
_load_mapping_from_file('GeoIPData/ext_pre_mappings.txt', GeoIPWrapper.pre_try)