<?php
include 'db.php'; // Connect to the database

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $subject = $_POST['subject'];
    $teacher_id = 1; // Static for now, should use session data

    $query = "INSERT INTO subjects (teacher_id, name) VALUES (?, ?)";
    $stmt = $pdo->prepare($query);
    $stmt->execute([$teacher_id, $subject]);

    echo "Subject added successfully!";
}
?>
