export function getToken() {
    return localStorage.getItem("Token")
}

export function setToken(token) {
    return localStorage.setItem("Token", token)
}

export function removeToken() {
    return localStorage.removeItem("Token")
}


export function getDistance() {
    return JSON.parse(localStorage.getItem("distance"))
    // return localStorage.getItem("distance")

}
export function setDistance(distance) {
    return localStorage.setItem("distance",distance)
    
}
export function removDistance() {
    return localStorage.removeItem("distance")
}

export function getAngle() {
    // return localStorage.getItem("angle")

    return JSON.parse(localStorage.getItem("angle"))
}
export function setAngle(angle) {
    return localStorage.setItem("angle",angle)
}
export function removeAngle() {
    return localStorage.removeItem("angle")
}

export function getSpeed() {
    // return localStorage.getItem("speed")
    return JSON.parse(localStorage.getItem("speed"))
}
export function setSpeed(speed) {
    return localStorage.setItem("speed",speed)
}
export function removeSpeed() {
    return localStorage.removeItem("speed")
}
export function getTestData() {
    // return localStorage.getItem("speed")
    return JSON.parse(localStorage.getItem("testData"))
}
export function setTestData(testData) {
    return localStorage.setItem("testData",testData)
}
export function removeTestData() {
    return localStorage.removeItem("testData")
}
export function getName() {
    return JSON.parse(localStorage.getItem("name"))
}
export function setName(name) {
    return localStorage.setItem("name",name)
}
export function removeName() {
    return localStorage.removeItem("name")
}
export function getMenu() {
    return JSON.parse(localStorage.getItem("menu"))
}
export function setMenu(menu) {
    return localStorage.setItem("menu",menu)
}
export function removeMenu() {
    return localStorage.removeItem("menu")
}
