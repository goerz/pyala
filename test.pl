my $rx = qr'w(d|ords?)?$';

$string = @ARGV[0];

if ($string =~ $rx){
    print "Match for '$string'\n";
} else {
    print "No Match for '$string'\n";
}