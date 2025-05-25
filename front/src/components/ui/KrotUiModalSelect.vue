<template lang="pug">
.backDrop(@click="$emit('close')")
.modal
	.title Выберите что вы хотите загрузить
	.item(@click="$_krot_ui_modal_select_change(0)") Файл тестового датасета
	.item(@click="$_krot_ui_modal_select_change(1)") Файл тренировочного датасета
	.item(@click="$_krot_ui_modal_select_change(2)") Выбрать свой файл
</template>

<script>
export default {
	emits:['close','change'],
	methods:{
		$_krot_ui_modal_select_change(type){
			this.$emit('change',type)
			this.$emit('close')
		}
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
	.modal {
		z-index: 1001;
		max-width: 500px;
		width: 100%;
		height: fit-content;
		position: fixed;
		top: 0;
		left: 0;
		right: 0;
		bottom: 0;
		margin: auto;
		border-radius: 16px;
		padding: 24px;
		overflow: hidden;
		display: flex;
		flex-direction: column;
		background-color: white;
		.title{
			font-weight: 700;
			font-size: 18px;
			line-height: 30px;
			color: #092C4C;
		}
		.item{
			margin-top: 15px;
			height: 40px;
			display: flex;
			justify-content: center;
			align-items: center;
			text-align: center;
			font-size: 15px;
			cursor: pointer;
			transition: .3s ease-out;
			&:hover{
				color: #7545FF;
			}
		}
	}
</style>