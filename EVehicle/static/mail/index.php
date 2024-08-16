<?php 
prepare($query);
$statement->execute();
$result = $statement->fetchAll();
?>
 
  <br />
  <div class="live container">
   <h3 align="center">Send Bulk Email using PHPMailer with PHP Ajax Example</h3>
   <hr />
   <div class="live table-responsive">
    <table class="live table">
     <tr>
      <th>Student Name</th>
      <th>Student Email</th>
      <th>Student Select</th>
      <th>Student Action</th>
     </tr>
     <?php
     $count = 0;
     foreach($result as $dataRow)
     {
      $count++;
      echo '
      <tr>
       <td>'.$dataRow["student_name"].'</td>
       <td>'.$dataRow["student_email"].'</td>
       <td>
        
       </td>
       <td><button type="button" name="send_email" class="btn btn-primary btn-xs send_email" id="'.$count.'">Send Single</button></td>
      </tr>
      ';
     }
     ?>
     <tr>
      <td colspan="3"></td>
      <td><button type="button" name="data_lots_email" class="live btn btn-primary send_email" id="data_lots_email">Send Email</button></td></td>
     </td>
    </table>
   </div>
  </div>