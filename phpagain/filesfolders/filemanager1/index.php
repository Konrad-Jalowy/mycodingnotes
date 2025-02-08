<?php
$directory = "files/";

if (!is_dir($directory)) {
    mkdir($directory, 0777, true);
}

$files = scandir($directory);
?>

<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menedżer plików</title>
    <style>
    body {
        font-family: Arial, sans-serif;
        margin: 20px;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        margin: 5px 0;
    }
    a {
        text-decoration: none;
        color: blue;
    }
    a:hover {
        text-decoration: underline;
    }
    form {
        margin-top: 10px;
    }
</style>

</head>
<body>
    <h2>Menedżer Plików</h2>

    <h3>📂 Pliki i foldery:</h3>
    <ul>
        <?php foreach ($files as $file): ?>
            <?php if ($file !== "." && $file !== ".."): ?>
                <li>
                    <?php if (is_dir($directory . $file)): ?>
                        📁 <strong><?php echo $file; ?></strong>
                    <?php else: ?>
                        📄 <a href="<?php echo $directory . $file; ?>" download><?php echo $file; ?></a>
                        - <a href="delete.php?file=<?php echo urlencode($file); ?>" style="color: red;">❌ Usuń</a>
                    <?php endif; ?>
                </li>
            <?php endif; ?>
        <?php endforeach; ?>
    </ul>

    <h3>➕ Prześlij plik:</h3>
    <form action="upload.php" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Prześlij">
    </form>

    <h3>📂 Stwórz nowy folder:</h3>
    <form action="mkdir.php" method="post">
        <input type="text" name="folder_name" required>
        <input type="submit" value="Stwórz">
    </form>
</body>
</html>
