function setCheckInTime() {
   var now = new Date();
   var hh = now.getHours().toString().padStart(2, '0');
   var mm = now.getMinutes().toString().padStart(2, '0');

   var current_time = moment(moment(), "HH:mm:ss").format("H:mm");
   console.log(current_time);
   var timeString = hh + ':' + mm;
   document.querySelector('#check_in_time').value = current_time;
   document.querySelector('#check_in_form').submit();
 }

 function setCheckOutTime() {
  var now = new Date();
  var hh = now.getHours().toString().padStart(2, '0');
  var mm = now.getMinutes().toString().padStart(2, '0');

  var current_time = moment(moment(), "HH:mm:ss").format("H:mm");
  console.log(current_time);
  var timeString = hh + ':' + mm;
  document.querySelector('#check_out_time').value = current_time;
  document.querySelector('#check_out_form').submit();
  
}

