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
                            <h4>修改密码</h4>
                        </div>
                    </div>
                    <div class="pass-right-panel">
                        <Form ref="passForm" :model="passForm"  class="passform" :rules="passRule" :label-position="labelPosition" :label-width="130">
                            <FormItem prop="oldPwd" label="原密码：">
                                <Input placeholder="请输入原密码"  class="pass-input" type="password" v-model="passForm.oldPwd">
                                </Input>
                            </FormItem>
                            <FormItem prop="newPwd" label="新密码：">
                                <Input placeholder="请输入新密码" class="pass-input" type="password" v-model="passForm.newPwd">
                                </Input>
                            </FormItem>
                            <FormItem prop="secPwd" label="确认新密码：">
                                <Input placeholder="请再次输入新密码"  class="pass-input" type="password" v-model="passForm.secPwd">
                                </Input>
                            </FormItem>
                        </Form>
                    </div>
                </div>
                <div  class="pass-btn-panel">
                    <Button @click="saveChange('passForm')" class="save-btn">确定</Button>
                    <Button @click="resetChange" class="reset-btn">重置</Button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {updatePass} from '@/api/user'

    import ReturnBtn from "../btn-back/return-btn";
    export default {
        name: "pass-word",
        components: {ReturnBtn},
        data(){
            var validateOld = (rule, value, callback) => {
                if (!value) {
                    callback(new Error('请输入密码'));
                } else if (!/^[A-Za-z0-9]+$/.test(value) || value.length < 6) {
                    callback(new Error('密码只能是6位以上英文或者数字'))
                } else {
                    callback();
                }
            };
            var validateNew = (rule, value, callback) => {
                if (!value) {
                    callback(new Error('请再次输入密码'));
                } else if (value !== this.passForm.newPwd) {
                    callback(new Error('两次输入密码不一致!'));
                } else {
                    callback();
                }
            };
            return{
                passForm:{},
                userInfo:{},
                labelPosition:"right",
                passRule:{
                    oldPwd:{required:true,message: '请输入原密码', trigger: 'blur' },
                    newPwd:[{validator: validateOld,required:true,trigger: 'blur' }],
                    secPwd:[{validator: validateNew,required:true,trigger: 'blur' }],
                }
            }
        },
        mounted(){
            this.userInfo = this.$store.getters.user;
        },
        methods:{
            saveChange(passForm){
               this.$refs[passForm].validate( valid =>{
                    if(valid){
                        updatePass({id:this.userInfo.id,oldPassword:this.passForm.oldPwd,newPassword:this.passForm.secPwd})
                        .then(res=>{
                            if(res.data.status=='SUCCESS'){
                                this.$message({
                                    type: 'success',
                                    message: '密码修改成功，需重新登录'
                                });
                                this.$router.push('/')
                            }else{
                                   this.$message({
                                    type: 'error',
                                    message: res.data.description
                                });
                            }
                        })
                   
                    }else{
                        this.$message({
                            type: 'error',
                            message: '请输入完整信息'
                        });
                    }
                });
            },
            resetChange(){
                this.passForm = {};
                this.$refs.passForm.resetFields();
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
@import "../../assets/styles/pass";

</style>
