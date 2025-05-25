<template lang="pug">
KrotHeader
KrotUploadFiles(@upload="$_krot_app_setData" @closeResult="$_krot_app_closeResult")
KrotResult(v-if="showResult" :local_rows="rows" :type="type")
KrotFooter
</template>

<script>
import {defineAsyncComponent} from "vue";

import KrotHeader from "@/components/KrotHeader.vue";
import KrotUploadFiles from "@/components/KrotUploadFiles.vue";
import KrotFooter from "@/components/KrotFooter.vue";
export default {
	data(){
		return{
			rows: [],
			type:0,
			showResult: false
		}
	},
	methods:{
		$_krot_app_setData(data){
			this.showResult = false
			this.rows = data.rows
			this.type = data.type
			this.showResult = true
		},
		$_krot_app_closeResult(){
			this.showResult = false
			this.rows = []
		}
	},
	components:{
		KrotFooter, KrotHeader, KrotUploadFiles,
		KrotResult: defineAsyncComponent(()=> import("@/components/result/KrotResult.vue")),
	}
}
</script>

<style lang="scss">
	@font-face {
		font-family: 'Monteserrat';
		src: local('Monteserrat'), url('./config/css/font/Montserrat.ttf') format('truetype');
		font-style: normal;
		font-display: swap;
	}
	.fade-enter-active, .fade-leave-active {
		transition: opacity .5s;
	}
	.fade-enter, .fade-leave-to{
		opacity: 0;
	}
	body{
		background-color: #ffffff;
		color: #252525;
		font-family: 'Monteserrat',sans-serif;
		&::-webkit-scrollbar, &::-webkit-scrollbar, &::-webkit-scrollbar {width: 8px;}
		&::-webkit-scrollbar-thumb, &::-webkit-scrollbar-thumb, &::-webkit-scrollbar-thumb{background: #6472EA;border-radius: 0;}
		&::-webkit-scrollbar-thumb:hover, &::-webkit-scrollbar-thumb:hover, &::-webkit-scrollbar-thumb:hover{background: #6472EA;}
		&::-webkit-scrollbar-thumb:focus, &::-webkit-scrollbar-thumb:focus, &::-webkit-scrollbar-thumb:focus{background: #6472EA;}
		.container{
			max-width: 1048px;
			padding: 0 24px;
			width: 100%;
			margin: 0 auto;
		}
	}
</style>
