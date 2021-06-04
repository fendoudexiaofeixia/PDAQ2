const getters = {
    token: state=>state.user.token,
    distance:state=>state.user.distance,
    angle: state=>state.user.angle,
    speed: state=>state.user.speed,
    testData :state =>state.user.testData,
    name :state =>state.user.name,
    menu:state=>state.user.menu,
};
export  default getters
