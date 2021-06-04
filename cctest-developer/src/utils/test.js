import html2canvas from "html2canvas"
import JSPDF from "jspdf"
export default {
  install (Vue) {
    Vue.prototype.ExportSavePdf = function (htmlTitle) {
      var element = document.getElementById("pdfCentent")
      html2canvas(element, {
        logging: false
      }).then(function (canvas) {
          var contentWidth = canvas.width
          var contentHeight = canvas.height
          var pageHeight = contentWidth / 592.28 * 841.89
          var leftHeight = contentHeight
          var position = 0
          var imgWidth = 595.28
          var imgHeight = 592.28 / contentWidth * contentHeight
          var pageData = canvas.toDataURL('image/jpeg', 1.0)
          // eslint-disable-next-line
          var pdf = new JSPDF('', 'pt', 'a4')
          if (leftHeight < pageHeight) {
            pdf.addImage(pageData, 'JPEG', 0, 0, imgWidth, imgHeight)
        } else {
            while (leftHeight > 0) {
                pdf.addImage(pageData, 'JPEG', 0, position, imgWidth, imgHeight)
                leftHeight -= pageHeight
                position -= 841.89
                // 避免添加空白页
                if (leftHeight > 0) {
                    pdf.addPage()
                }
            }
        }
        pdf.save( htmlTitle + new Date().getTime()+'.pdf')
      })
  }
}

}


        



var shareContent = document.querySelector('#pdfCentent')
var width = shareContent.offsetWidth / 4
var height = shareContent.offsetHeight / 4
let _this = this;
html2canvas(element, {
  logging: false
}).then(function (canvas) {
  var context = canvas.getContext('2d')
  context.mozImageSmoothingEnabled = false
  context.webkitImageSmoothingEnabled = false
  context.msImageSmoothingEnabled = false
  context.imageSmoothingEnabled = false
  var pageData = canvas.toDataURL('image/jpeg', 1.0)
  var img = new Image()
  img.src = pageData
  img.onload = function () {
      // 获取dom高度、宽度
      img.width = img.width / 2
      img.height = img.height / 2
      img.style.transform = 'scale(0.5)'
      if (width > height) {
          // 此可以根据打印的大小进行自动调节
          // eslint-disable-next-line
          var pdf = new JSPDF('l', 'px', [
              width * 0.505,
              height * 0.545
          ])
      } else {
          // eslint-disable-next-line
          var pdf = new JSPDF('p', 'px', [
              width * 0.505,
              height * 0.545
          ])
      }
      pdf.addImage(
          pageData,
          'jpeg',
          0,
          0,
          width * 0.505,
          height * 0.545
      )
      pdf.save(_this.htmlTitle + '.pdf'+currentTime)
  }





  import html2canvas from "html2canvas"
import JSPDF from "jspdf"
export default {
  install (Vue) {
    Vue.prototype.ExportSavePdf = function (htmlTitle, currentTime) {
      var element = document.getElementById("pdfCentent")

      html2canvas(element, {
        logging: false
      }).then(function (canvas) {
        if(currentTime=='jpg'){
            var link = document.createElement('a');
            link.href = pageData;
            link.download = 'default.jpg';
            link.click();
        }else{
          var context = canvas.getContext('2d')
          context.mozImageSmoothingEnabled = false
          context.webkitImageSmoothingEnabled = false
          context.msImageSmoothingEnabled = false
          context.imageSmoothingEnabled = false    
          var pageData = canvas.toDataURL('image/jpeg', 1.0);
            var img = new Image()
            img.src = pageData;
            img.onload = function () {
            img.style.transform = 'scale(0.5)'              
              var pdf = new JSPDF('p', 'px', [
                img.width,
                img.height
            ]);
            pdf.addImage(pageData, "JPEG", 0, 0, img.width/2,img.height/2) 
            pdf.save(htmlTitle+ '.pdf' + currentTime)
          }
        }
    })
  }
}
}