<?php
include 'database/db.php';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $chapter_id = $_POST['chapter'];
    $file = $_FILES['file'];

    $target_dir = "uploads/";
    $file_path = $target_dir . basename($file["name"]);

    if (move_uploaded_file($file["tmp_name"], $file_path)) {
        $query = "INSERT INTO syllabus (chapter_id, file_path) VALUES (?, ?)";
        $stmt = $pdo->prepare($query);
        $stmt->execute([$chapter_id, $file_path]);

        echo "File uploaded and saved!";
    } else {
        echo "File upload failed.";
    }
}
?>
