<?php
include 'db.php';

$id = $_POST['id'];
$task = $_POST['task'];

$conn->query("UPDATE tasks SET task='$task' WHERE id=$id");

header("Location: index.php");
?>
