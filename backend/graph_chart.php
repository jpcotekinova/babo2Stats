<?php 
/** 
 * Charts 4 PHP 
 * 
 * @author Shani <support@chartphp.com> - http://www.chartphp.com 
 * @version 1.2.3 
 * @license: see license.txt included in package 
 */ 
  
  define('__ROOT__', dirname(dirname(__FILE__))); 
include("chartphp/lib/inc/chartphp_dist.php"); 

$x_axis = array();
$y_axis = array();
$y2_axis = array();
$i = 0;
 
$con=mysqli_connect("localhost","root","issqlfun?","babostats");
// Check connection
if (mysqli_connect_errno()) {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
 
$result = mysqli_query($con,"SELECT count(id) FROM shot WHERE killerName = 'OLED'");
 
$i = 0; 
while($row = mysqli_fetch_array($result)) {
$y_axis[$i] = $row["count(id)"];
    $i++;
 
}

$result = mysqli_query($con,"SELECT count(id) FROM shot WHERE killedName = 'OLED'");
 
$i = 0; 
while($row = mysqli_fetch_array($result)) {
$y2_axis[$i] = 0-intval($row["count(id)"],10);
    $i++;
 
}
     
     
$ratio = floatval($y_axis[0])/floatval($y2_axis[0]); 
     
    mysqli_close($con);

$p = new chartphp(); 

$p->data = array(array(array("2016/04/08",$ratio),array("2011/01",238.75),array("2011/02",95.50),array("2011/03",300.50),array("2011/04",286.80),array("2011/05",400)));
$p->chart_type = "bar"; 

// Common Options 
$p->title = "Bar Chart"; 
$p->xlabel = "My X Axis"; 
$p->ylabel = "My Y Axis"; 
$p->export = false; 
$p->options["legend"]["show"] = true; 
$p->series_label = array('Q1','Q2','Q3');  

$out = $p->render('c1'); 
?> 
<!DOCTYPE html> 
<html> 
    <head> 
        <script src="../../lib/js/jquery.min.js"></script> 
        <script src="../../lib/js/chartphp.js"></script> 
        <link rel="stylesheet" href="../../lib/js/chartphp.css"> 
    </head> 
    <body> 
        <div style="width:40%; min-width:450px;"> 
            <?php echo $out; ?> 
        </div> 
    </body> 
</html> 