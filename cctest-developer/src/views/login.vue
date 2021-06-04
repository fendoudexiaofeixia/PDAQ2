<template>
    <div class="login-wrapper">
        <transition name="form-fade" mode="in-out">
        <div class="login-center-banner" v-show="showForm">
            <div class="login-left-banner">
                <transition name="form-fade" mode="in-out" class="log-trans">
                    <div class="login-center-title" v-show="showForm">
                        <h1>CalmCar云监控平台</h1>
                        <p>人工智能 <span>智能驾驶</span></p>
                    </div>
                </transition>
                <img src="../../src/assets/images/banner/login.jpg">
            </div>
            <div class="login-right-banner">
                <transition name="form-fade" mode="in-out">
                    <section class="login-form"  v-show="showForm">
                        <Form :model="loginForm" ref="loginForm" :rules="loginRules" >
                            <FormItem  prop="loginName">
                                <Input v-model="loginForm.loginName" placeholder="请输入用户名" @keyup.enter.native="submit('loginForm')">
                                    <Icon type="md-person" slot="prefix"></Icon>
                                </Input>
                            </FormItem>
                            <FormItem  prop="password">
                                <Input v-model="loginForm.password" placeholder="请输入密码"  :type="pwdType" @keyup.enter.native="submit('loginForm')" >
                                    <Icon type="md-lock"   class="login-icon" slot="prefix" />
                                    <i class="iconfont icon-yanjing_bi"  v-show="seen"  slot="suffix" @click="hidePassword"></i>
                                    <Icon type="md-eye" slot="suffix"  v-show="!seen" @click="showPassword"/>
                                </Input>
                            </FormItem>
                            <FormItem  prop="validateCode">
                                <Input v-model="loginForm.validateCode" placeholder="请输入验证码" class="code-input" @keyup.enter.native="submit('loginForm')">
                                    <Icon type="md-options"   class="login-icon" slot="prefix" />
                                </Input> 
                                <img class="codeImg" :src="this.codeUrl+this.randomUuid" id="codeImg"   @click="changeCodeImg" >
                                <div class="code-img">
                                    <span @click="changeCodeImg" class="changeCode">看不清,换一张</span>
                                </div>
                            </FormItem>
                            <!-- <FormItem>
                                <el-checkbox v-model="checked" class="login-check" >一周内自动登录</el-checkbox>
                            </FormItem> -->
                        </Form>
                         <el-button class="submit-btn" @click="submit">登   录</el-button>
                    </section>
                </transition>
            </div>
        </div>
        </transition>
    </div>
</template>

<script>
import request from '@/utils/request'
// mapGetters
    export default {
        name: "login",
        data(){
            return{
                codeUrl:request.baseURL+'/getValidateCode?uuid=',
                randomUuid:null,
                labelPostion:'left',
                checked:false,
                showForm:false,
                loading:false,
                seen:null,
                token:'',
                pwdType:'password',
                loginForm:{},
                loginRules:{
                    loginName:[{required:true,trigger: 'blur',message:'请输入用户名'}], 
                    password:[{required:true,trigger: 'blur',message:'请输入密码'}],
                    validateCode:[{required:true,trigger: 'blur',message:'请输入验证码'},  { min: 4, max: 4, message: '验证码长度为4位', trigger: 'blur' },],
                }
            }
        },
        mounted() {
            this.showForm = true;
            this.randomUuid =  this.setUUid();
        },
        methods:{
            setUUid(){
                var s = [];
                var hexDigits = "0123456789abcdef";
                for (var i = 0; i < 36; i++) {
                    s[i] = hexDigits.substr(Math.floor(Math.random() * 0x10), 1);
                }
                s[14] = "4"; // bits 12-15 of the time_hi_and_version field to 0010
                s[19] = hexDigits.substr((s[19] & 0x3) | 0x8, 1); // bits 6-7 of the clock_seq_hi_and_reserved to 01
                s[8] = s[13] = s[18] = s[23] = "-";
                var uuid = s.join("");
                return uuid;
            },
            changeCodeImg(){
                this.randomNum  = Math.random();
                this.codeUrl = request.baseURL+'/getValidateCode?uuid='+ this.randomUuid+'&&a='+this.randomNum;
            },
            showPassword(){
                this.seen = true;
                this.pwdType = this.pwdType ==='password'?'text':'password'
            },
            hidePassword(){
                this.seen = false;
                this.pwdType = this.pwdType ==='password'?'text':'password'
            },
            submit(){
                this.$refs.loginForm.validate((valid) => {
                    if(valid){
                        this.loginForm.uuid = this.randomUuid;
                        this.$store.dispatch('user/Login',this.loginForm)
                        .then(()=> {
                            this.$router.push({ path: '/dash-board' })
                        })
                        .error(()=>{
                        });
                        
                    }else{
                        this.$message({
                            type: 'error',
                            message: '请输入完整信息'
                        });
                        return false;
                    }
                })
            } 
        },
        computed:{
            error(){
                return this.$store.getters.error;
            }
        },
        watch:{
            error(){
                this.changeCodeImg();
            }
        }
    }
</script>

<style lang="less">
    @import "../../src/assets/styles/login";
    .code-input{
        float: left;
        // width: 157px;、
        position: relative;
    }
    .code-img{
        float: right;
        display: flex;
        align-items: center;
        flex-direction: column;
    }
    .code-img:hover{
        cursor: pointer;
    }
    .codeImg{
        position:absolute;
        width: 70px;
        height: 28px;
        top: 5px;
        right: 4px;
    }
    .codeImg:hover{
        cursor: pointer;
    }
    .changeCode{
        font-size: 12px;
        color: #A6B9C5;
    }
    .login-center-banner{
        // background: url("../assets/images/banner/float.png");
        // background-position: 100% 100%;
        // background-size: 100% 100%;
        // background-repeat: no-repeat;
        width: 91%;
        display: flex;
        align-items: center;
        justify-content: space-between;
        height: 100%;
    }
</style>
