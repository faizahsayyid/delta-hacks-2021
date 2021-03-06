<?php
$servername = 'localhost';
$user = 'root';
$pass = '';

$conn = new mysqli($servername, $user, $pass);

if ($conn->connect_error){
    die("Connection Failed: " . $conn->connect_error);
}
echo "Connected succesfully";

$first_name = $_POST{'fname'};
$last_name = $_POST{'lname'};
$email = $_POST{'email'};
$experience_level = 'something';
$skills = 'something';
$field = 'something';
$mentor = TRUE;


$sql = "INSERT INTO application (first_name, last_name, email, experience_level, 
                                skills, field, mentor)
                VALUES ($first_name, $last_name, $email, $experience_level, 
                        $skills, $mentor)"

?>