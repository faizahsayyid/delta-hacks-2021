<?php
$servername = 'localhost';
$user = 'root';
$pass = '';
$dbname = 'deltahacks';

$conn = new mysqli($servername, $user, $pass, $dbname);

if ($conn->connect_error){
    die("Connection Failed: " . $conn->connect_error);
}
echo "Connected succesfully";

$first_name = $_REQUEST["fname"];
$last_name = $_REQUEST["lname"];
$email = $_REQUEST["email"];
$experience_level = $_REQUEST["grade"];
$skill1 = $_REQUEST["skill1"];
$skill2 = $_REQUEST["skill2"];
$skill3 = $_REQUEST["skill3"];
$skill4 = $_REQUEST["skill4"];
$field = $_REQUEST["field"];
$mentor = TRUE;

$skills = $skill1 . ',' . $skill2 . ',' . $skill3 . ',' . $skill4;

$sql = "INSERT INTO application (first_name, last_name, email, experience_level, skills, field, mentor) 
VALUES ('$first_name', '$last_name', '$email', '$experience_level', '$skills', '$field', '$mentor')";

if ($conn->query($sql) === TRUE) {
    echo "<br> Application Submitted";
} else {
    echo "<br> Error: " . $sql . "<br>" . $conn->error;
}

header("refresh:2; url=mentor_application.html");

$conn->close();

?>