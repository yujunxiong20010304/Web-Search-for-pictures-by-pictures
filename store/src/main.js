import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import '../../store/src/assets/public.css'
import axios from 'axios'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css' // 创建app 实例子
const app = createApp(App)
app.config.globalProperties.$http = axios
axios.defaults.baseURL = 'http://localhost:8000' // 指向后端的请求端口
app.use(store).use(ElementPlus).use(router).mount('#app')
