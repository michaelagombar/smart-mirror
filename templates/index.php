<!DOCTYPE html>
<html>

<head>
    <title>Mirror</title>
    <link rel="stylesheet" href="..\static\css\home.css">
</head>


<body>
    <div class="wrapper">
        <div class="boxTopLeft">none</div>
        <div class="boxTopRight">
            <div class="times">
                <p>{{time}}</p>
                <p>{{date}}</p>
            </div>
        </div>
        <div class="boxBottomRight"/>
           <?php
                  $lines = file('soccerPost.txt', FILE_IGNORE_NEW_LINES);
                       foreach ($lines as $item)
                       {
                             echo $item+"\n";
                    }
            ?>
        </div>
        <div class="boxBottomLeft">soccer
        </div>


    </div>

</body>

</html>
