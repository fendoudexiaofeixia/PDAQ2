import  axios from 'axios'
import {getToken} from '@/utils/auth'
import store from "@/store/index";
import {Message} from 'element-ui'
import Router  from "@/router/index";
axios.defaults.timeout = 30000;

//创建axios实例
const service = axios.create({
    baseURL: process.env.VUE_APP_BASE_API, //api的base_url
    // withCredentials: true, // send cookies when cross-domain requests
    timeout:30000 //请求超时时间
});
service.baseURL=process.env.VUE_APP_BASE_API;
//http请求拦截器
service.interceptors.request.use(
    response=>{
        if (getToken){
            response.headers['token'] = getToken()   //让每个请求携带自定义token 
        }
        return response
    },error => {
        Message.error({
            message:'加载超时',
        });
        return Promise.reject(error)
    });

//http响应拦截器
service.interceptors.response.use(
    response => {
        //拦截响应，做统一处理
        if (response.data.code) {
            switch (response.data.code) {
                case 1002:
                    store.state.isLogin = false;
                    Router.replace({
                        path: '/',
                        query: {
                            redirect: Router.currentRoute.fullPath
                        }
                    })
            }
        }
        return response
    },
    //接口错误状态处理，也就是说无响应时的处理
    error => {
        return Promise.reject(error.response.status) // 返回接口返回的错误信息
    })


export default service
