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
    <link rel="stylesheet" href="assets/css/Contact-Form-Clean.css">
    <link rel="stylesheet" href="assets/css/Navigation-Clean.css">
    <link rel="stylesheet" href="assets/css/styles.css">
</head>

<body>
    <div>
        <nav class="navbar navbar-light navbar-expand-md navigation-clean">
            <div class="container"><a class="navbar-brand" href="#">Blood Benefaction - Through Fair Means</a><button class="navbar-toggler" data-toggle="collapse" data-target="#navcol-1"><span class="sr-only">Toggle navigation</span><span class="navbar-toggler-icon"></span></button>
                <div
                    class="collapse navbar-collapse" id="navcol-1">
                    <ul class="nav navbar-nav ml-auto">
                        <li class="nav-item" role="presentation"><a class="nav-link" href="donor-org.py">Donate Blood</a></li>
                        <li class="nav-item" role="presentation"><a class="nav-link active" href="blood-status.py">Check Status</a></li>
                        <li class="nav-item" role="presentation"><a class="nav-link" href="reserves.py">City Reserves</a></li>
                    </ul>
            </div>
    </div>
    </nav>
    </div>
    <div class="contact-clean">
        <form method="post">
            <h2 class="text-center">STATUS</h2>
            <div class="form-group"><input class="form-control" type="text" name="hash" placeholder="UNIQUE HASH / ID"></div>
            <div class="form-group"><button class="btn btn-primary float-none" type="submit" onClick="bStatus(hash.value);">CHECK STATUS</button></div>
        </form>
    </div>
    <div>
        <div class="container" style="display: none;">
            <div class="row">
                <div class="col-md-12">
                    <div class="table-responsive align-self-center my-auto visible" style="width:300px;padding:10px;">
                        <table class="table">
                            <thead>
                                <tr>
                                    <th colspan="2">Donate Status</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>Unit:</td>
                                    <td>1</td>
                                </tr>
                                <tr>
                                    <td>Donor Org/NGO/Hosp.:</td>
                                    <td>Org/NGO Name</td>
                                </tr>
                                <tr>
                                    <td>Contact No.:</td>
                                    <td>No.</td>
                                </tr>
                                <tr>
                                    <td>Location:</td>
                                    <td>City, State, Zip</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div>
        <div class="container"></div>
    </div>
    <div></div>
    <div></div>
    <script src="assets/js/jquery.min.js"></script>
    <script>
    function bStatus(hash){
        window.event.returnValue = false;
        document.location="checkstatus.py?hash=" + hash;
    }
    </script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
</body>

</html>
"""