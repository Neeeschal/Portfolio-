<?php
include 'db.php';

$id = $_GET['id'];
$result = $conn->query("SELECT * FROM tasks WHERE id=$id");
$row = $result->fetch_assoc();
?>

<form method="POST" action="update.php">
    <input type="hidden" name="id" value="<?php echo $row['id']; ?>">
    <input type="text" name="task" value="<?php echo $row['task']; ?>">
    <button type="submit">Update</button>
</form>
