#!/usr/bin/python2
import commands,cgi
import cgitb
cgitb.enable()
print "content-type: text/html"
print ""
print """
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ReserveChain</title>
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Bitter:400,700">
    <link rel="stylesheet" href="assets/css/Highlight-Clean.css">
    <link rel="stylesheet" href="assets/css/Navigation-Clean.css">
    <link rel="stylesheet" href="assets/css/styles.css">
</head>

<body>
    <div>
        <nav class="navbar navbar-light navbar-expand-md navigation-clean">
            <div class="container"><a class="navbar-brand" href="index.html">Blood Benefaction - Through Fair Means</a><button class="navbar-toggler" data-toggle="collapse" data-target="#navcol-1"><span class="sr-only">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
                <div
                    class="collapse navbar-collapse" id="navcol-1">
                    <ul class="nav navbar-nav ml-auto">
                        <li class="nav-item" role="presentation"><a class="nav-link" href="donor-org.py">Donate Blood</a></li>
                        <li class="nav-item" role="presentation"><a class="nav-link" href="blood-status.py">Check Status</a></li>
                        <li class="nav-item" role="presentation"><a class="nav-link active" href="reserves.py">City Reserves</a></li>
                    </ul>
            </div>
    </div>
    </nav>
    </div>
    <div class="highlight-clean">
        <div class="container">
            <div class="intro">
                <h2 class="text-center">BLOOD RESERVES WITHIN INDIA</h2>
                <p class="text-center">Get city-wise blood-group availability stats.</p>
            </div>
        </div>
    </div>
    <div>
        <div class="container">
            <div class="row">
                <div class="col-md-3"><img src="assets/img/1Asset 3.png" style="padding:10px;margin:0px;" onClick="location.href='dispcity.py?bg=APOS';"></div>
                <div class="col-md-3" style="margin:0px;"><img src="assets/img/1Asset 8.png" style="padding:10px;" onClick="location.href='dispcity.py?bg=ANEG';"></div>
                <div class="col-md-3"><img src="assets/img/1Asset 9.png" onClick="location.href='dispcity.py?bg=BPOS';"></div>
                <div class="col-md-3"><img src="assets/img/1Asset 10.png" style="padding:10px;" onClick="location.href='dispcity.py?bg=BNEG';"></div>
            </div>
        </div>
    </div>
    <div>
        <div class="container">
            <div class="row">
                <div class="col-md-3"><img src="assets/img/1Asset 11.png" onClick="location.href='dispcity.py?bg=ABPOS';"></div>
                <div class="col-md-3"><img src="assets/img/1Asset 12.png" style="padding:10px;" onClick="location.href='dispcity.py?bg=ABNEG';"></div>
                <div class="col-md-3"><img src="assets/img/1Asset 13.png" onClick="location.href='dispcity.py?bg=OPOS';"></div>
                <div class="col-md-3"><img src="assets/img/1Asset 7.png" onClick="location.href='dispcity.py?bg=ONEG';"></div>
            </div>
        </div>
    </div>
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
</body>

</html>
"""