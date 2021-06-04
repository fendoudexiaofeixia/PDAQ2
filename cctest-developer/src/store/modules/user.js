import {getToken,getSpeed,getAngle,getDistance,getTestData,getName,getMenu} from '../../utils/auth'
const state = {
    token: getToken(),
    distance: getDistance(),
    angle:getAngle(),
    speed:getSpeed(),
    testData:getTestData(),
    name:getName(),
    menu:getMenu(),
};
const mutations = {
    SET_TOKEN: (state,token)=>{
        state.token = token
    },
    SET_DISTANCE: (state,distance)=>{
        state.distance = distance
    },
    SET_ANGLE: (state,angle)=>{
        state.angle = angle
    },
    SET_SPEED: (state,speed)=>{
        state.speed = speed
    },
    SET_TESTDATA: (state,testData)=>{
        state.testData = testData
    },
    SET_NAME: (state,name)=>{
        state.name = name
    },
    SET_MENU: (state,menu)=>{
        state.menu = menu
    },
}

export default {
    namespaced: true,
    state,
    mutations,
}

