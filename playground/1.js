

// HH:MM:SS AM

// 11:05:04 AM

function validate(dateStr) {

   let res = /\d\d:\d\d:\d\d [AM|PM]/.match(dateStr)
   // if success
   if (res) {
     // get components of the parse 
     return true;
   } else {
     return false;
   }
}