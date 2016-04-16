<?php

error_reporting(-1);
ini_set('display_errors', 'On');

$mysqli = new mysqli("localhost", "root", "issqlfun?", "babostats");
if ($mysqli->connect_errno) {
    echo "Echec lors de la connexion à MySQL : (" . $mysqli->connect_errno . ") " . $mysqli->connect_error;
}

$res = $mysqli->query("SELECT name FROM player ORDER BY name ASC");

$date = $_GET["date"];
echo "Liste des joueurs :".$date."<br>";
$res->data_seek(0);
echo "<table>";
while ($row = $res->fetch_assoc()) {
	echo "<tr>";
	echo "<td>".$row['name']."</td>";
	$res2 = $mysqli->query("SELECT count(id) FROM shot WHERE killerName = '".$row['name']."' AND gametime = '".$date."'");
	$res2->data_seek(0);
	while ($row2 = $res2->fetch_assoc()) {
		$kill = floatval($row2['count(id)']);
		echo "<td>".$row2['count(id)']."</td>";
	}
	$res2 = $mysqli->query("SELECT count(id) FROM shot WHERE killedName = '".$row['name']."' AND gametime = '".$date."'");
	$res2->data_seek(0);
	while ($row2 = $res2->fetch_assoc()) {
		$death = floatval($row2['count(id)']);
		echo "<td>".$row2['count(id)']."</td>";
	}
	
	$divratio = $kill / $death;
	echo "<td>".$divratio."</td>";
	$diffratio = $kill - $death;
	echo "<td>".$diffratio."</td>";
	
	echo "</tr>";
}
echo "</table>";
echo "<hr>";



#intval ( mixed $var [, int $base = 10 ] )

?>