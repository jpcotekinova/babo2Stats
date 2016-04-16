<?php // content="text/plain; charset=utf-8"
 
define('__ROOT__', dirname(dirname(__FILE__))); 
require_once ('jpgraph/jpgraph.php');
require_once ('jpgraph/jpgraph_bar.php');
require_once ('jpgraph/jpgraph_error.php');

$datazero=array(0,0,0,0);
 
$x_axis = array();
$y_axis = array();
$y2_axis = array();
$i = 0;

$name = $_GET["name"];
 
$con=mysqli_connect("localhost","root","issqlfun?","babostats");
// Check connection
if (mysqli_connect_errno()) {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}
 
$result = mysqli_query($con,"SELECT count(id), gametime FROM shot WHERE killerName = '".$name."' GROUP BY gametime");
 
$i = 0; 
while($row = mysqli_fetch_array($result)) {
$y_axis[$i] = $row["count(id)"];
$x_axis[$i] = $row["gametime"];
    $i++;
 
}

$result = mysqli_query($con,"SELECT count(id), gametime FROM shot WHERE killedName = '".$name."' GROUP BY gametime");
 
$i = 0; 
while($row = mysqli_fetch_array($result)) {
$y2_axis[$i] = $row["count(id)"];
    $i++;
 
}
     
     
 
     
    mysqli_close($con);
 
$ratio = array();
$ratio[0] = 0.0;
$label = array();
$label[0] = "";
for ($x = 1; $x <= $i; $x++) {
    $ratio[$x] = floatval($y_axis[$x-1])/floatval($y2_axis[$x-1]); 
	$label[$x] = $x_axis[$x-1];
} 

 
 // Create the graph. 
$graph = new Graph(450,200);
$graph->title->Set('Example with 2 scale bars');

// Setup Y and Y2 scales with some "grace"	
$graph->SetScale("intlin");
//$graph->SetY2Scale("lin");
$graph->yaxis->scale->SetGrace(1.0);
//$graph->y2axis->scale->SetGrace(30);

//$graph->ygrid->Show(true,true);
$graph->ygrid->SetColor('gray','lightgray@0.5');

$graph->xaxis->SetTickLabels($label);

// Setup graph colors
$graph->SetMarginColor('white');
//$graph->y2axis->SetColor('darkred');


// Create the "dummy" 0 bplot
$bplotzero = new BarPlot($datazero);

// Create the "Y" axis group
$ybplot1 = new BarPlot($ratio);
$ybplot1->value->Show();
$ybplot = new GroupBarPlot(array($ybplot1,$bplotzero));

// Create the "Y2" axis group
//$ybplot2 = new BarPlot($y2_axis);
//$ybplot2->value->Show();
//$ybplot2->value->SetColor('darkred');
//$ybplot2->SetFillColor('darkred');
//$y2bplot = new GroupBarPlot(array($bplotzero,$ybplot2));

// Add the grouped bar plots to the graph
$graph->Add($ybplot);
//$graph->AddY2($y2bplot);

// .. and finally stroke the image back to browser
$graph->Stroke();
 
?>