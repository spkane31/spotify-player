
// {/* <script>  */}
// {/* // Requiring fs module in which   */}
// {/* // readFile function is defined.  */}
const fs = require('fs') 

function readFile() {
  fs.readFile('../queue.txt', (err, data) => { 
      if (err) throw err; 
  
      console.log(data.toString()); 
      
  }) 
}
// </script> 
