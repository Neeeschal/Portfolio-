<?php
include 'db.php';

if(isset($_POST['task'])){
    $task = $_POST['task'];
    $conn->query("INSERT INTO tasks (task) VALUES ('$task')");
}

header("Location: index.php");
?>
