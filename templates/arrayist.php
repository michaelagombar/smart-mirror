<?php
    $lines = file('soccerPost.txt', FILE_IGNORE_NEW_LINES);
    foreach($lines as $item)
        {
        echo "$item\n";
        }

?>