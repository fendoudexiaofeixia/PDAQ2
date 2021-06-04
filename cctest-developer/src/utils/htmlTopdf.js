// import html2canvas from "html2canvas"
// import JSPDF from "jspdf"
// export default {
//   install (Vue) {
//     Vue.prototype.ExportSavePdf = function (htmlTitle, currentTime) {
//       var element = document.getElementById("pdfCentent");
//       html2canvas(element, {
//         allowTaint: true,
//         logging: false,
//         async:false,
//       }).then(function (canvas) {
//         var contentWidth = canvas.width;
//         var contentHeight = canvas.height;
//         var pageData = canvas.toDataURL('image/jpeg', 1.0)
//         var pdfX = (contentWidth + 10) / 2 * 0.75
//         var pdfY = (contentHeight + 500) / 2 * 0.75 
//         var imgX = pdfX;
//         var imgY = (contentHeight / 2 * 0.75);
//           if(currentTime=='jpg'){
//               var link = document.createElement('a');
//               link.href = pageData;
//               link.download = htmlTitle +'.jpg';
//               link.click();
//           }else{
//             var PDF = new JSPDF('', 'pt', [pdfX, pdfY])
//             PDF.addImage(pageData, 'jpeg', 0, 0, imgX, imgY)    
//             setTimeout(
//               PDF.save(htmlTitle +  '.pdf' + currentTime)
//               ,15000)
//           }
//       })
     
//     }
//   }
// }



// import html2canvas from "html2canvas"
// import JSPDF from "jspdf"
//     export default {
//       install (Vue) {
//           Vue.prototype.ExportSavePdf = function (htmlTitle, currentTime) {
//             var element = document.getElementById("pdfCentent")
//             html2canvas(element, {
//               logging: false
//             }).then(function (canvas) {
//                 var width = canvas.width;
//                 var height = canvas.height ;
//                 var pdf = new JSPDF('', 'pt',a4)        
//                 var pageData = canvas.toDataURL('image/jpeg', 1.0)    
//                 if(currentTime=='jpg'){
//                     var link = document.createElement('a');
//                     link.href = pageData;
//                     link.download = htmlTitle +'.jpg';
//                     link.click();
//                   }else{       
//                     pdf.addImage(pageData, "JPEG", 20, 20, width, height)         
//                     pdf.save(htmlTitle +  '.pdf' + currentTime)
//                   }
//               })
//         }
//     }
// }

import html2canvas from "html2canvas"
import JSPDF from "jspdf"
    export default {
      install (Vue) {
          Vue.prototype.ExportSavePdf = function (htmlTitle, currentTime) {
            var element = document.getElementById("pdfCentent")
            html2canvas(element, {
              logging: false
            }).then(function (canvas) {
                var width = canvas.width;
                var height = canvas.height ;
                var pdf = new JSPDF('', 'pt', [width, height])        
                var pageData = canvas.toDataURL('image/jpeg', 1.0)    
                if(currentTime=='jpg'){
                    var link = document.createElement('a');
                    link.href = pageData;
                    link.download = htmlTitle +'.jpg';
                    link.click();
                  }else{       
                    pdf.addImage(pageData, "JPEG", 20, 20, width, height)         
                    pdf.save(htmlTitle +  '.pdf' + currentTime)
                  }
              })
        }
    }
}




      //   var width = document.body.scrollWidth;
      //   var height =document.body.scrollHeight;
      //   var pdf = new JSPDF('', 'pt', [width,height])
      //   var pageData = canvas.toDataURL('image/jpeg', 1.0);
      //   // var img = new Image()
      //   // img.src = pageData;
      //   // img.onload = function () {
      //   // img.style.transform = 'scale(0.5)'              
      //   //   var pdf = new JSPDF('p', 'px', [
      //   //     img.width,
      //   //     img.height
      //   // ]);
      
      //   pdf.addImage(pageData, "JPEG", 0, 0, width,height) 
      //   pdf.save(htmlTitle+ '.pdf' + currentTime)
      // // }
    // })


        //   var context = canvas.getContext('2d')
        //   context.mozImageSmoothingEnabled = false
        //   context.webkitImageSmoothingEnabled = false
        //   context.msImageSmoothingEnabled = false
        //   context.imageSmoothingEnabled = false    
        //   var pageData = canvas.toDataURL('image/jpeg', 1.0);
        //     var img = new Image()
        //     img.src = pageData;
        //     img.onload = function () {
        //     img.style.transform = 'scale(0.5)'              
        //       var pdf = new JSPDF('p', 'px', [
        //         img.width,
        //         img.height
        //     ]);
        //     pdf.addImage(pageData, "JPEG", 0, 0, img.width/2,img.height/2) 
        //     pdf.save(htmlTitle+ '.pdf' + currentTime)
        //   }
        // })
    // })
  // }
// }
// }

