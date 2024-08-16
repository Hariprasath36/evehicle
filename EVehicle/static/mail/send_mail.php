<?php 
IsSMTP();        //put PHP Mailer to send particuler comments using SMTP serever
  $sendMail->Host = 'smtpout.secureserver.net';  //put the SMTP serever some hosts set of your Email hosting any, this for like as a Godaddy
  $sendMail->Port = '80';        //put the default set SMTP server port
  $sendMail->SMTPAuth = true;       //put SMTP authentication. as well as Utilizes the phpmailer user Username and user Password variables
  $sendMail->Username = 'live24u@12258';     //put SMTP server username
  $sendMail->Password = 'live!@#hrt$%';     //put SMTP server password
  $sendMail->SMTPSecure = '';       //put data connection prefix. Options like as are "", "ssl" as well as "tls"
  $sendMail->From = 'primary@Pakainfo.com';   //put the From email user address for the comments
  $sendMail->FromName = 'live24u';     //put the HTML From name of the formname
  $sendMail->AddAddress($dataRow["email"], $dataRow["name"]); //simple add here a "To" address
  $sendMail->WordWrap = 50;       //put word wrapping on the html body of the comments to a given number of characters
  $sendMail->IsHTML(true);       //put comments type to HTML
  $sendMail->Subject = 'Live24u is the most popular Programming & Web Development blog.'; //put the Subject of the comments
  //An HTML all data or plain text send email comments body
  $sendMail->Body = '
  <p>Live24u is the most popular Programming & Web Development blog. Our mission is to provide the best online resources on programming and web development. We deliver the useful and best tutorials for web professionals — developers, programmers, freelancers and site owners. Any visitors of this site are free to browse our tutorials, live demos and download scripts.</p>
  <p>Our mission is to provide the best online resources on web development.
  We deliver the useful and best tutorials for web professionals — developers, programmers, freelancers and site owners.</p>';
  $sendMail->AltBody = '';
  $result = $sendMail->Send();      //Send an Email. and then Return true on data success or false on error generated
  if($result["code"] == '400')
  {
   $message_body .= html_entity_decode($result['full_error']);
  }
 }
 if($message_body == '')
 {
  echo 'ok';
 }
 else
 {
  echo $message_body;
 }
}
?>