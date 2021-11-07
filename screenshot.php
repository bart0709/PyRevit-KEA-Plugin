<?php
    require "includes/db_conn.inc.php";
    if (isset($_POST["moveOn"])) {
        if ($_POST["moveOn"] == "true") {
            $sql = "UPDATE `okbutton` SET Ready = 0;";
            $query = mysqli_query($conn,$sql);
        }
    } else
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link rel="icon" type="image/png" href="https://kea.dk/images/resources/kea_16.png">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SCREENSHOT</title>
    <link rel="stylesheet" href="main.css">
    <script
  src="https://code.jquery.com/jquery-3.6.0.min.js"
  integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
  crossorigin="anonymous"></script>
</head>
<body>
    <div class="fullscrn_cont">
        <div class="main_cont">
            <h1 class="main_header">SCREENSHOT</h1>
            <div id="reload">
            <div id="users_cont">
                <?php
                    $readyUsers = 0;

                    $sql = "SELECT * FROM `screenshots`";
                    $query = mysqli_query($conn,$sql);
                    $NumOfResults = mysqli_num_rows($query);
    
                    if($NumOfResults > 0) {
                        while($row = mysqli_fetch_assoc($query)) {
                            if($row["Ready"] == 1) {
                                $readyUsers = $readyUsers + 1;
                            }
                            
                            ?>
                                <div class="user_cont">
                                    <?php
                                        if($row["Ready"] == 1) {
                                            ?><a href="<?php echo $row["Link"]?>" style="text-decoration: none; color: black;">
                                                <div class="user_icon_cont">
                                                    <img class="user_icon" src="<?php echo $row["Link"] ?>">
                                                </div>
                                                <h3 class="user_name" ><?php echo $row["Names"] ?></h3>
                                            </a>
                                            <?php
                                        } else {
                                            ?>
                                            <a href="" style="text-decoration: none; color: black;">
                                                <div class="user_icon_cont">
                                                    <img class="user_icon" src="img/placeholder.jpg">
                                                </div>
                                                <h3 class="user_name" ><?php echo $row["Names"] ?></h3>
                                            </a>
                                            <?php
                                        }
                                    ?>
                                    
                                </div>
                            <?php
                        }
                    }
                    $readyPer = round(($readyUsers / $NumOfResults) * 100, 0);
                    
                ?>
                
            
            </div>
            <div class="all_bar">
                <div class="ready_bar" style="width: <?php echo $readyPer?>%">
                </div>
                <h3 class="ready_num"><?php echo $readyPer; ?>%</h3>
            </div>
                <?php $readyUsers = 0; ?>
            </div>
            <form action="button.php" method="POST">
                <input type="hidden" name="moveOn" value="true">
                <input class="main_btn" type="submit" value="MOVE ON">
            </form>
        </div>
    </div>
    <script>
      $(document).ready(() => {

        setInterval(() => {
            $("#reload").load(" #reload");
            
        },1000);

        
      });
  </script>
</body>
</html>