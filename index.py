#!/usr/bin/python2
import commands,cgi
print "content-type: text/html"
print ""
print  """
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ReserveChain</title>
    <link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Bitter:400,700">
    <link rel="stylesheet" href="assets/css/Article-List.css">
    <link rel="stylesheet" href="assets/css/Features-Boxed.css">
    <link rel="stylesheet" href="assets/css/Navigation-Clean.css">
    <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
    <div></div>
    <div>
        <div class="header-dark" style="background-image:url(&quot;assets/img/52148-O72TBI-02.png&quot;);height:800px;padding:0px;"></div>
    </div>
    <div class="features-boxed">
        <div class="container">
            <div class="intro"></div>
        </div>
    </div>
    <div class="article-list">
        <div class="container">
            <div class="intro">
                <h2 class="text-center">BLOOD BENEFACTION</h2>
                <p class="text-center">Nunc luctus in metus eget fringilla. Aliquam sed justo ligula. Vestibulum nibh erat, pellentesque ut laoreet vitae. </p>
            </div>
            <div class="row articles">
                <div class="col-sm-6 col-md-4 item"><a href="donor-org.py"><img class="img-fluid" src="assets/img/52148-O72TBI-02.png"></a>
                    <h3 class="name">DONORS</h3>
                    <p class="description">Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.</p><button class="btn btn-primary" type="button" onClick="location.href='donor-org.py';">donate now</button></div>
                <div
                    class="col-sm-6 col-md-4 item"><a href="blood-status.py"><img class="img-fluid" src="assets/img/52148-O72TBI-02.png"></a>
                    <h3 class="name">DONATION STATUS</h3>
                    <p class="description">Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.</p><button class="btn btn-primary" type="button" onClick="location.href='blood-status.py';">donation status</button></div>
            <div
                class="col-sm-6 col-md-4 item"><a href="reserves.py"><img class="img-fluid" src="assets/img/52148-O72TBI-02.png"></a>
                <h3 class="name">BLOOD RESERVES</h3>
                <p class="description">Aenean tortor est, vulputate quis leo in, vehicula rhoncus lacus. Praesent aliquam in tellus eu gravida. Aliquam varius finibus est, interdum justo suscipit id.</p><button class="btn btn-primary" type="button" onClick="location.href='reserves.py';">get stats</button></div>
    </div>
    </div>
    </div>
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
</body>
</html>
"""

