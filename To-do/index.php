<?php include 'db.php'; ?>

<!DOCTYPE html>
<html>
<head>
    <title>Task Manager</title>
</head>
<body>
<h2>Task Manager</h2>

<form method="POST" action="add.php">
    <input type="text" name="task" placeholder="Enter task" required>
    <button type="submit">Add Task</button>
</form>

<h3>Tasks</h3>
<ul>
<?php
$result = $conn->query("SELECT * FROM tasks");
while($row = $result->fetch_assoc()){
    echo "<li>" . $row['task'] . " 
    <a href='edit.php?id=".$row['id']."'>Edit</a> 
    <a href='delete.php?id=".$row['id']."'>Delete</a></li>";
}
?>
</ul>

</body>
</html>
