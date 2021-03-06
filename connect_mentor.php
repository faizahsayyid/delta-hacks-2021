<?php
$servername = 'localhost';
$user = 'root';
$pass = '';

$conn = new mysqli($servername, $user, $pass);

if ($conn->connect_error){
    die("Connection Failed: " . $conn->connect_error);
}
echo "Connected succesfully";

?>