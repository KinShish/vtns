<template lang="pug">
.backDrop
.modal.status-1
	.title
		.text Подробнее о объекте
		.percent 90
			span %
			img(src="/img/result/light.svg")
		img.close(src="/img/modal/close.svg" @click="$emit('close')")
</template>

<script>
export default {
	emits:['close'],
	props:{
		data:{
			type:Object,
			default:()=>{return {}}
		}
	},
	data(){
		return{

		}
	},
	mounted() {
		window.document.body.style.overflow='hidden'
	},
	beforeUnmount() {
		window.document.body.style.overflow=''
	}
}
</script>

<style scoped lang="scss">
	.backDrop{
		z-index: 1000;
		background: #00000080;
		position: fixed;
		top: 0;
		left: 0;
		width: 1000vw;
		height: 100vh;
	}
	.modal{
		z-index: 1001;
		width: 500px;
		height: fit-content;
		max-height: calc(100vh - 100px);
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		margin: auto;
		border-radius: 16px;
		padding: 24px;
		&.status-1{
			background: #EEFFF2;
			border: 1px solid #EEFFF2;
			.percent{background-color: #13A438;}
		}
		&.status-2{
			background: #F2EFCF;
			border: 1px solid #EEFFF2;
			.percent{background-color: #F2B636;}
		}
		&.status-3  {
			background: #F2E9E4;
			border: 1px solid #EEFFF2;
			.percent{background-color: #FF5845;}
		}
		.percent{
			width: fit-content;
			height: 26px;
			padding: 0 12px;
			display: flex;
			justify-content: center;
			align-items: center;
			gap: 4px;
			border-radius: 10px;
			color: white;
			span{margin-left: -3px;}
		}
		.title{
			display: flex;
			gap: 14px;
			margin-bottom: 16px;
			.text{
				font-weight: 700;
				font-size: 18px;
				line-height: 30px;
				color: #092C4C;
			}
			.close{
				margin-left: auto;
				cursor: pointer;
			}
		}
	}
</style>