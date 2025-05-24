import '@/config/css/reset.scss'

import { createApp } from 'vue'
import App from '@/App.vue'

import makeRequest from "@/config/mixins/makeRequest.js";
const app = createApp(App)
app
	.mount('#app')
app.config.globalProperties.$makeRequest = makeRequest