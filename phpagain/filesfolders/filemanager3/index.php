<?php
$directory = "files/";

if (!is_dir($directory)) {
    mkdir($directory, 0777, true);
}

$allowedImages = ['jpg', 'jpeg', 'png', 'gif', 'webp'];
$iterator = new DirectoryIterator($directory);
?>

<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menedżer plików</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        ul { list-style-type: none; padding: 0; }
        li { margin: 5px 0; }
        a { text-decoration: none; color: blue; }
        a:hover { text-decoration: underline; }
        form { margin-top: 10px; }
        img { max-width: 100px; max-height: 100px; display: block; margin-top: 5px; }
    </style>
</head>
<body>
    <h2>Menedżer Plików</h2>

    <h3>📂 Pliki i foldery:</h3>
    <ul>
        <?php foreach ($iterator as $file): ?>
            <?php if (!$file->isDot()): ?>
                <li>
                    <?php 
                    $filename = $file->getFilename();
                    $filePath = $directory . $filename;
                    $fileExt = strtolower(pathinfo($filename, PATHINFO_EXTENSION));
                    ?>

                    <?php if ($file->isDir()): ?>
                        📁 <strong><?php echo $filename; ?></strong>
                        - <a href="delete.php?folder=<?php echo urlencode($filename); ?>" style="color: red;">❌ Usuń</a>
                    <?php else: ?>
                        📄 <a href="<?php echo $filePath; ?>" download><?php echo $filename; ?></a>
                        - <a href="delete.php?file=<?php echo urlencode($filename); ?>" style="color: red;">❌ Usuń</a>

                        <!-- Podgląd obrazka -->
                        <?php if (in_array($fileExt, $allowedImages)): ?>
                            <br>
                            <a href="<?php echo $filePath; ?>" target="_blank">
                                <img src="<?php echo $filePath; ?>" alt="<?php echo $filename; ?>">
                            </a>
                        <?php endif; ?>
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
