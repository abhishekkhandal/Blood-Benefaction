#!/usr/bin/python2
import commands,cgi
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
    <link rel="stylesheet" href="assets/css/Navigation-Clean.css">
    <link rel="stylesheet" href="assets/css/Registration-Form-with-Photo.css">
    <link rel="stylesheet" href="assets/css/styles.css">
</head>

<body>
    <div>
        <nav class="navbar navbar-light navbar-expand-md navigation-clean">
            <div class="container"><a class="navbar-brand" href="index.html"><strong>Blood Benefaction - Through Fair Means</strong></a><button class="navbar-toggler" data-toggle="collapse" data-target="#navcol-1"><span class="sr-only">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
                <div
                    class="collapse navbar-collapse" id="navcol-1">
                    <ul class="nav navbar-nav ml-auto">
                        <li class="nav-item" role="presentation"><a class="nav-link active" href="donor-org.py">Donate Blood</a></li>
                        <li class="nav-item" role="presentation"><a class="nav-link" href="blood-status.py">Check Status</a></li>
                        <li class="nav-item" role="presentation"><a class="nav-link" href="reserves.py">City Reserves</a></li>
                    </ul>
            </div>
    </div>
    </nav>
    </div>
    <div class="register-photo">
        <div class="form-container">
            <div class="image-holder" style="background-image:url(&quot;assets/img/bloodbottle-01.jpg&quot;);margin:0px;"></div>
            <form method="post">
                <h2 class="text-center"><strong>DONATION INFORMATION</strong></h2>
                <div class="table-responsive">
                    <table class="table">
                        <thead>
                            <tr></tr>
                        </thead>
                        <tbody>
                            <tr></tr>
                            <tr>
                                <td>
                                    <div class="dropdown"><button class="btn btn-light btn-sm dropdown-toggle" data-toggle="dropdown" aria-expanded="false" type="button">Blood Group</button>
                                        <div class="dropdown-menu" role="menu"><a class="dropdown-item" role="presentation" value="A">A</a><a class="dropdown-item" role="presentation" value="B">B</a><a class="dropdown-item" role="presentation" href="#">AB</a><a class="dropdown-item" role="presentation"
                                                href="#">O</a></div>
                                    </div>
                                </td>
                                <td>
                                    <div class="dropdown"><button class="btn btn-light btn-sm dropdown-toggle" data-toggle="dropdown" aria-expanded="false" type="button">Rh Factor&nbsp;</button>
                                        <div class="dropdown-menu" role="menu"><a class="dropdown-item" role="presentation" href="#"></a><a class="dropdown-item" role="presentation" href="#">-ve</a><a class="dropdown-item" role="presentation" href="#">+ve</a></div>
                                    </div>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <div class="table-responsive">
                                        <table class="table">
                                            <tbody>
                                                <tr>
                                                    <td>Unit:</td>
                                                </tr>
                                            </tbody>
                                        </table>
                                    </div>
                                </td>
                                <td><input type="number" placeholder="unit" class="form-control" min="0.1" step="0.1" value="1" max="1" name="unitNum" style="padding:0px;"/></td>
                            </tr>
                            <tr>
                                <td>Donation Date:</td>
                                <td><input class="form-control" type="date" required=""></td>
                            </tr>
                            <tr></tr>
                        </tbody>
                    </table>
                </div>
                <div class="form-group"><input class="form-control" type="text" name="dname" required="" placeholder="Donor Organisation/hospital name"><input class="form-control" type="text" name="number" required="" placeholder="Contact Number" inputmode="numeric"></div>
                <div
                    class="form-group"><input class="form-control" type="text" name="State" placeholder="State (eg. Rajasthan)"><input class="form-control" type="text" name="city" required="" placeholder="City (eg. Jaipur)"><input class="form-control" type="text" name="zipcode"
                        placeholder="Zipcode (eg. 302004)"></div>
        <div class="form-group">
            <div class="form-check"><label class="form-check-label"><input class="form-check-input" type="checkbox" required=""><strong>I confirm that the information given in this form is true, complete and accurate.</strong></label></div>
        </div>
        <div class="form-group"><button class="btn btn-primary btn-block" type="submit">Submit</button></div>
        </form>
    </div>
    </div>
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
</body>

</html>
"""