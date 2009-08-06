#! /usr/bin/perl -w
use strict;

my $file = "/home/goerz/public_html/bbclone/lib/robot.php";

open(IN, $file) or die("Can't open $file");

sub strip{
    my $string = shift;
    $string =~ s/^\s*//;
    $string =~ s/\s*$//;
    return $string;
}


my $in_level1dict = 0;
my $in_level2dict = 0;
my $in_rule = 0;
my $in_known = 0;
my $last = '';
my $active = 0;
my $comment = undef;
# last can be any of the following constants:
#
# level1dict_beginning,
# level2dict_beginning,
# ruledict_beginning,
# knowndict_beginning,
# level1dict_end,
# level2dict_end
# ruledict_end
# knowndict_end
# level2dict_item
# ruledict_item
# knowndict_item

my $DEBUG = 0;



my $line = "";
print "import re\n\n";
my $linenumber = 0;

while (1){
    my $line = <IN>;
    exit unless (defined($line));
    $linenumber++;
    chomp $line; # remove newline
    $line = strip($line); # remove spaces on all side
    $line =~ s/,$//; # remove comma at the end
    warn("Processing: '$line'") if ($DEBUG);
    warn("    (last item: '$last'") if ($DEBUG);

    # $var = array(
    if ($line =~ m'^\$(.*)\s*=\s*array\(\s*(//(.*))?$$'){ # the beginning of the data structure
        $comment = $3;
        $in_level1dict = 1;
        $last = 'level1dict_beginning';
        print "$1 = [";
        print " #$comment" if ($comment);
        print "\n";
        $active = 1;
        next;
    }

    next if (not $active);

    # "bla" => array(
    if ($line =~ m'^"(.*)"\s*=>\s*array\s*\(\s*(//(.*))?$'){ # could be the beginning of the level2dict, the rule-dict, or the known-dict
        $comment = $3;
        if (($in_level1dict) and (not($in_level2dict))){ # has to be beginning of level2dict
            warn("    Handling as beginning of level2dict: '$line'") if ($DEBUG);
            $in_level2dict = 1;
            unless (($last eq 'level2dict_end') or  ($last eq 'level1dict_beginning')){
                warn("level2dict_beginning occured after something that's neither an level2dict_end nor an level1dict_beginning ($linenumber)\n");
            }
            if ($last eq 'level2dict_end'){
                print ",";
                print " #$comment" if ($comment);
                print "\n";
            }
            $last = 'level2dict_beginning';
            print "    {";
            print " #$comment" if ($comment);
            print "\n";
        } elsif (($in_level1dict) and ($in_level2dict)){ # could be beginning of rule-dict or known-dict
            if ($1 eq 'rule'){
                warn("    Handling as beginning of ruledict: '$line'") if ($DEBUG);
                $in_rule = 1;
                if (($last eq 'level2dict_item') or ($last eq 'knowndict_end')){
                    print ","; # close previous
                    print " #$comment" if ($comment);
                    print "\n";
                }
                $last = 'ruledict_beginning';
                print "        \"rule\" : [";
                print " #$comment" if ($comment);
                print "\n";
            } elsif ($1 eq 'known') {
                warn("    Handling as beginning of knowndict: '$line'") if ($DEBUG);
                $in_known = 1;
                if (($last eq 'level2dict_item') or ($last eq 'ruledict_end')){
                    print ","; # close previous
                    print " #$comment" if ($comment);
                    print "\n";
                }
                $last = 'knowndict_beginning';
                print "        \"known\" : [";
                print " #$comment" if ($comment);
                print "\n";
            } else {
                warn("Can't make out where to put some line '\"bla\" => array(' (# 1)($linenumber)\n");
            }
        } else {
            warn("Can't make out where to put some line '\"bla\" => array(' (# 2)($linenumber)\n");
        }
        next;
    }

    # "bla" => "blub"
    if ($line =~ m'^(".*")\s*=>\s*(".*"),?\s*(//(.*))?$'){ # could be a level2dict_item, or ruledict_item, or knowndict_item
        $comment = $4;
        if (($in_level2dict) and (not ($in_rule)) and (not ($in_known))){ # has to be a level2dict_item
            warn("    Handling as level2dict_item: '$line'") if ($DEBUG);
            if (($last eq 'level2dict_item') or ($last eq 'ruledict_end') or ($last eq 'knowndict_end')){
                print ","; # close previous
                print " #$comment" if ($comment);
                print "\n"
            }
            $last = 'level2dict_item';
            print "        $1: $2";
        } elsif (($in_level2dict) and ( ($in_rule) or ($in_known))){ # can be  ruledict_item or knowndict_item
            if ($in_rule){ # hast to be ruledict_item
                warn("    Handling as ruledict_item: '$line'") if ($DEBUG);
                if ($last eq 'ruledict_item'){
                    print ",";
                    print " #$comment" if ($comment);
                    print "\n";
                }
                $last = 'ruledict_item';
                my $pattern = $1;
                my $versiongrp = $2;
                if ($versiongrp =~ m'"..([0-9])"'){
                    print "            (re.compile($pattern, re.I), $1)"
                } else {
                    print "            (re.compile($pattern, re.I), $versiongrp)"
                }
            } elsif ($in_known) { # has to be knowndict_item
                warn("    Handling as knowndict_item: '$line'") if ($DEBUG);
                if ($last eq 'knowndict_item'){
                    print ",";
                    print " #$comment" if ($comment);
                    print "\n";
                }
                $last = 'knowndict_item';
                my $pattern = $1;
                my $versiongrp = $2;
                if ($versiongrp =~ m'"..([0-9])"'){
                    print "            (re.compile($pattern, re.I), $1)"
                } else {
                    print "            (re.compile($pattern, re.I), $versiongrp)"
                }
            } else {
                warn("Can't make out where to put some line '\"bla\" => \"blub\"' (# 1)($linenumber)\n");
            }
        } else{
            warn("Can't make out where to put some line '\"bla\" => \"blub\"' (# 2)($linenumber)\n");
        }
        next;
    }

    # closing bracket
    if ($line =~ m'^\),?;?\s*(//(.*))?$$'){ # could be level1dict_end, level2dict_end, ruledict_end, knowndict_end
        $comment = $2;
        if ($in_known){
            warn("    Handling as knowndict_end: '$line'") if ($DEBUG);
            $in_known = 0;
            $last = 'knowndict_end';
            print " #$comment" if ($comment);
            print "\n";
            print "        ]";
        } elsif ($in_rule){
            warn("    Handling as ruledict_end: '$line'") if ($DEBUG);
            $in_rule = 0;
            $last = 'ruledict_end';
            print " #$comment" if ($comment);
            print "\n";
            print "        ]";
        } elsif ($in_level2dict){
            warn("    Handling as level2dict_end: '$line'") if ($DEBUG);
            $in_level2dict = 0;
            $last = 'level2dict_end';
            print " #$comment" if ($comment);
            print "\n";
            print "    }";
        } elsif ($in_level1dict){
            warn("    Handling as level1dict_end: '$line'") if ($DEBUG);
            $in_level1dict = 0;
            $last = 'level1dict_end';
            print "\n";
            print "]";
            print " #$comment" if ($comment);
            print "\n";
        } else {
            warn("Can't make out where to put a closing bracket ($linenumber)\n");
        }
        next;
    }

    # comment line
    if ($line =~ m'^\w*//(.*)'){
        $comment = $1;
        next;
    }

    warn("The line '$line' was unparsable ($linenumber)\n");
}

