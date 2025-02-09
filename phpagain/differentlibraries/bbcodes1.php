<?php
require 'vendor/autoload.php';

$parser = new JBBCode\Parser();
$parser->addCodeDefinitionSet(new JBBCode\DefaultCodeDefinitionSet());

$bbcode = "[b]Witaj, świecie![/b] To jest [i]BBCode[/i].";
$parser->parse($bbcode);

echo $parser->getAsHtml();
?>
