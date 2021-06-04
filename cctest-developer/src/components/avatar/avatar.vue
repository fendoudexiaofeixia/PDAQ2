<template>
<div class="container">
    <div class="pass-wrapper">
        <div class="pass-return-panel">
            <return-btn></return-btn>
        </div>
        <div class="pass-panel">
            <div class="pass-panel-wrapper">
                <div class="pass-left-panel">
                    <div class="pass-title">
                        <img src="../../assets/images/dash/title.png"> 
                        <h4>上传头像</h4>
                    </div>
                </div>
                <div class="upload-right-panel">
                    <div class="upload-img-card">
                        <div class="imgList" >
                             <img v-if="fileUrl" :src="fileUrl" class="avatar" style="width: 260px; height: 260px;">
                        </div>
                    </div>
                    <div class="upload-btn-panel">
                        <el-button @click="openDialog()" class="save-btn">选择图片</el-button>

                    </div>
                </div>
            </div> 
        </div>
        <Modal v-model="isShowCropper" class="add-modal avator-modal" :mask-closable="false" width="750">
            <h4 slot="header">
                <span>裁剪头像</span>
            </h4>
            <div class="vue-cropper-content">
                <div class="cropper">
                    <vueCropper ref="cropper" 
                            :img="option.img" 
                            :outputSize="option.size" 
                            :outputType="option.outputType" 
                            :info="true" 
                            :full="option.full" 
                            :canMove="option.canMove" 
                            :canMoveBox="option.canMoveBox" 
                            :original="option.original" 
                            :autoCrop="option.autoCrop" 
                            :autoCropWidth="option.autoCropWidth" 
                            :autoCropHeight="option.autoCropHeight" 
                            :fixedBox="option.fixedBox" 
                            @realTime="realTime" 
                            :fixed="option.fixed" 
                            :fixedNumber="option.fixedNumber">
                    </vueCropper>
                </div>
                <div class="show-preview" :style="{'width': previews.w + 'px', 'height': previews.h + 'px',  'overflow': 'hidden'}">
                    <div :style="previews.div" class="preview">
                    <img :src="previews.url" :style="previews.img">
                    </div>
                </div>
            </div>
            <div class="operate-wrap"> 
                <div class="lf">
                    <el-button class="scale-btn" icon="el-icon-refresh-left" @click="rotateLeft"></el-button>
                    <el-button class="scale-btn" icon="el-icon-refresh-right" @click="rotateRight"></el-button>
                    <el-button class="scale-btn" icon="el-icon-circle-plus-outline" @click="changeScale(1)"></el-button>
                    <el-button class="scale-btn" icon="el-icon-remove-outline" @click="changeScale(-1)"></el-button>
                </div> 
            </div>
            <input
                type="file"
                class="uploads"
                accept="image/png, image/jpeg, image/jpg"
                @change="uploadImg($event)"
            >
            <el-upload
                ref="avator"
                :auto-upload="false"
                class="avatar-uploader"
                action="/user/uploadIcon"
                :show-file-list="false"
                :on-change ="changeImage"
                :on-success="handleAvatarSuccess"
                :before-upload="beforeAvatarUpload">
                <img v-if="imageUrl" :src="imageUrl" class="avatar">
                <i v-else class="el-icon-plus avatar-uploader-icon"></i>
            </el-upload>
            <div slot="footer">
                <el-button @click="onCubeImg()" class="save-btn">上传</el-button>
                <el-button @click="cancleCropper()" class="reset-btn">取消</el-button>
            </div>
        </Modal>
    </div>
</div>
</template> 

<script>
    import axios from 'axios'
    Vue.prototype.$axios = axios;
    import Vue from 'vue'
    import { VueCropper } from "vue-cropper";
    Vue.use(VueCropper);
    import request from '@/utils/request'
    import ReturnBtn from "../btn-back/return-btn";
    export default {
        name: "avator",
        components: {ReturnBtn},
        data(){
            return{
                previews:{},
                crap: false,
                downImg: '#',
                imageUrl: '',
                imgFile:null,
                testUrl:'',
                dialogVisible:false,
                isShowCropper:false,
                fileUrl:null,
                fileImg:null,
                option: {
                    img: '', // 裁剪图片的地址
                    info: true, // 裁剪框的大小信息
                    outputSize: 1, // 剪切后的图片质量（0.1-1）
                    full: true, // 输出原图比例截图 props名full
                    outputType: 'png', // 裁剪生成额图片的格式
                    canMove: true,  // 能否拖动图片
                    original: false,  // 上传图片是否显示原始宽高
                    canMoveBox: true,  // 能否拖动截图框
                    autoCrop: true, // 是否默认生成截图框
                    autoCropWidth: 740, // 默认生成截图框宽度
                    autoCropHeight: 400, // 默认生成截图框高度
                    fixedBox: true // 截图框固定大小
                },
            }
        },
        mounted(){
            this.userInfo = this.$store.getters.user;
            this.fileUrl = config.ta + this.userInfo.imgUrl;
            this.testUrl = request.baseURL+'/user/uploadIcon';
            this.imgFile=config.ta + this.userInfo.imgUrl;
        },
        methods:{
            changeImage(file){
                console.log(file)
            },
            uploadImg(event) {
                var _this = this;
                //上传图片
                var file = event.target.files[0];
                _this.fileName = file.name;
                if (!/\.(jpg|jpeg|png|JPG|PNG)$/.test(event.target.value)) {
                    alert("图片类型必须是jpeg,jpg,png中的一种");
                    return false;
                }
                var reader = new FileReader();
                reader.onload = e => {
                    let data;
                    if (typeof e.target.result === "object") {
                    // 把Array Buffer转化为blob 如果是base64不需要
                    data = window.URL.createObjectURL(new Blob([e.target.result]));
                    } else {
                    data = e.target.result;
                    }
                    _this.option.img = data;
                    event.target.value = ''; //避免每次选择同样的文件时，input @change 方法不执行问题
                };
                // 转化为base64
                // reader.readAsDataURL(file)
                // 转化为blob
                reader.readAsArrayBuffer(file);
            } ,
            openDialog(){
                this.isShowCropper = true;
                this.$refs.avator.clearFiles();
            },
            changeScale(num) {
                num = num || 1
                this.$refs.cropper.changeScale(num)
            },
            rotateLeft() {
                this.$refs.cropper.rotateLeft()
            },
            rotateRight() {
                this.$refs.cropper.rotateRight()
            },
            // 实时预览函数 
            realTime(data) {
                this.previews = data
            },
            cancleCropper() {//取消截图
                this.isShowCropper = false;
            },
            onCubeImg() {//剪切上传
            // 获取cropper的截图的base64 数据
                this.$refs.cropper.getCropData(data => {
                    // this.fileinfo.url = data;
                    //先将显示图片地址清空，防止重复显示
                    this.option.img = "";
                    //将剪裁后base64的图片转化为file格式
                    let file = this.convertBase64UrlToBlob(data);
                    this.fileImg = URL.createObjectURL(file);
                    console.log(this.fileImg);
                    var formData = new FormData();
                    formData.append("userId",this.userInfo.id);
                    formData.append("icon", this.fileImg);
                    console.log(formData);
                    this.$axios.post(this.testUrl,formData).then(res=>{
                        if(res.status == "SUCCESS"){
                            this.$message({
                                type: 'success',
                                message: '头像上传成功'
                            });
                            this.isShowCropper = false;
                        }else{
                            this.$message({
                                type: 'error',
                                message: '头像上传失败'
                            });
                            this.isShowCropper = false;
                        }
                    });
                });
            },
            // 将base64的图片转换为file文件
            convertBase64UrlToBlob(urlData) {
                let bytes = window.atob(urlData.split(",")[1]); //去掉url的头，并转换为byte
                //处理异常,将ascii码小于0的转换为大于0
                let ab = new ArrayBuffer(bytes.length);
                let ia = new Uint8Array(ab);
                for (var i = 0; i < bytes.length; i++) {
                    ia[i] = bytes.charCodeAt(i);
                }
                return new Blob([ab], { type: "image/jpeg" });
            },
            uploads(file){
                this.option.img=URL.createObjectURL(file);

                console.log(this.option.img)
            },
            handleAvatarSuccess(res){
                if(res.status == "SUCCESS"){
                    this.$message({
                        type: 'success',
                         message: '头像上传成功'
                    });
                    this.btnShow = false;
                    this.uploadShow =true;
                    this.url = config.ta + res.data;
                }else{
                    this.$message({
                        type: 'error',
                        message: '头像上传失败'
                    });
                }
            },
            beforeAvatarUpload(file){
                const isImages = file.type== 'image/jpeg'||'image/png';
                const isLt1M = file.size / 1024 / 1024 < 1;
                  if (!isImages) {
                    this.$message.error('上传文件只能是图片格式');
                }
                if (!isLt1M) {
                    this.$message.error('上传头像图片大小不能超过 1MB!');
                }
                return isLt1M && isImages;
            },
            saveChange(){

            }
        },
        computed:{
            user(){
                return this.$store.getters.user;
            }
        },
    }
</script>

<style lang="less">
.avatar-modal{
    .ivu-modal-wrap{
        top: 42px !important;
    }   
 
}
.vue-cropper-content{
  display: flex;
  display: -webkit-flex;
  justify-content: flex-end;
  -webkit-justify-content: flex-end;
  .cropper {
    width: 300px;
    height: 300px;
  }
  .show-preview {
    flex: 1;
    -webkit-flex: 1;
    display: flex;
    display: -webkit-flex;
    justify-content: center;
    -webkit-justify-content: center;
    .preview {
      overflow: hidden;
      border: 1px solid #cccccc;
      background: #cccccc;
      margin-left: 20px;
    }
  }
}
.footer-btn {
  margin-top: 30px;
  display: flex;
  display: -webkit-flex;
  justify-content: flex-end;
  -webkit-justify-content: flex-end;
  .scope-btn {
    width: 350px;
    display: flex;
    display: -webkit-flex;
    justify-content: space-between;
    -webkit-justify-content: space-between;
  }
  .upload-btn {
    flex: 1;
    -webkit-flex: 1;
    display: flex;
    display: -webkit-flex;
    justify-content: center;
    -webkit-justify-content: center;
  }
  .btn {
    outline: none;
    display: inline-block;
    line-height: 1;
    white-space: nowrap;
    cursor: pointer;
    -webkit-appearance: none;
    text-align: center;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    outline: 0;
    margin: 0;
    -webkit-transition: 0.1s;
    transition: 0.1s;
    font-weight: 500;
    padding: 10px 15px;
    font-size: 12px;
    border-radius: 3px;
    color: #fff;
    background-color: #67c23a;
    border-color: #67c23a;
  }
}
.avatar-uploader{
  border: 1px dashed red;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  width: 178px;
  height: 178px;
  display: block;
}
.avatar-uploader:hover {
  border-color: #409EFF;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
    .upload-right-panel{
        width: 70%;
        height: 100%;
        display: -webkit-box;
        display: -ms-flexbox;
        display: flex;
        -webkit-box-align: center;
        -ms-flex-align: center;
        align-items: center;
        -webkit-box-pack: start;
        -ms-flex-pack: start;
        justify-content: space-between;
        flex-direction: column;
          .save-btn{
        margin: 0 25px;
        .back("../../assets/images/user/set-save.png");
        border: 0px solid rgba(17, 153, 238, 0.4);
        color: #fff;
        padding: 8px 40px;
        font-size: 12px;
        border-radius: 0px;
        line-height: 1
    }
    .save-btn:hover{
        .back("../../assets/images/user/set-save.png");
        border: 0px solid rgba(17, 153, 238, 0.4);
        color: #ffffff;
        padding: 8px 40px;
        font-size: 12px;
        border-radius: 0px;
        line-height: 1
    }
    }
    .upload-img-card{
        width: 100%;
        display: flex;
        align-items: center;
        // justify-content: center;

    }
    .upload-btn-panel{
        width: 100%;
        display: flex;
        align-items: center;
        // justify-content: center;
    }
    

    @import "../../assets/styles/pass";
    @import "../../assets/styles/system";
</style>
