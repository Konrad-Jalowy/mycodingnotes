# php simple -> dates
notes on dates in PHP

## today, week later, week ago
```php
<?php 
echo date("Y-m-d", strtotime("-1 week")) . "</br>";
echo date("Y-m-d") . "</br>";
echo date("Y-m-d", strtotime("+1 week")) . "</br>";
```