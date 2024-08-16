$(document).ready(function(){
 $('.send_email').click(function(){
  $(this).attr('disabled', 'disabled');
  var id = $(this).attr("id");
  var data_action = $(this).data("data_action");
  var email_list_data = [];
  if(data_action == 'single')
  {
   email_list_data.push({
    email: $(this).data("email"),
    name: $(this).data("name")
   });
  }
  else
  {
   $('.single_student').each(function(){
    if($(this). prop("checked") == true)
    {
     email_list_data.push({
      email: $(this).data("email"),
      name: $(this).data('name')
     });
    }
   });
  }
  
  $.ajax({
   url:"send_mail.php",
   method:"POST",
   data:{email_list_data:email_list_data},
   beforeSend:function(){
    $('#'+id).html('Email Sending...');
    $('#'+id).addClass('live btn-danger');
   },
   success:function(data){
    if(data = 'ok')
    {
     $('#'+id).text('Good Luck Success');
     $('#'+id).removeClass('live btn-danger');
     $('#'+id).removeClass('live btn-primary');
     $('#'+id).addClass('live btn-success');
    }
    else
    {
     $('#'+id).text(data);
    }
    $('#'+id).attr('disabled', false);
   }
   
  });
 });
});