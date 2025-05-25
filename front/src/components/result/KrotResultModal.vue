<template lang="pug">
.backDrop(@click="$emit('close')")
.modal(:class="`status-${data.status}`")
	.title
		.text Подробнее о объекте
		.percent {{data.percent}}
			span %
			img(src="/img/result/light.svg")
		img.close(src="/img/modal/close.svg" @click="$emit('close')")
	.contentBody
		.line
			.halfBlock
				.rowInfo
					.greyText ID
					.text {{data.accountId}}
				.rowInfo
					.greyText Адрес:
					.text {{data.address}}
				.rowInfo
					.greyText Тип здания:
					.text {{data.buildingType}}
				.rowInfo
					.greyText Кол-во комнат::
					.text {{data.roomsCount||'-'}}
				.listCharts
					.whiteBlock
						.name Показания:
						.count {{data.consumptionAll}}
							span кВт
						KrotUiChartLine(:data="Object.values(data.consumption)" id="2")
					br
					.whiteBlock
						.name Апроксимация:
						KrotUiChartLine(:data="data.aproxima" id="1" hidex)
			.halfBlock
				.whiteBlock
					.mainName Подтверждающие ресурсы
					.pic(v-for="(_,item) of links")
						img(:src="`${url}uploads/account/${$props.data.accountId}/${item}`" v-if="images.includes(item)")
						a.resource(:href="`${links[item]}${$props.data.address}`" target="_blank")
							img(src="/img/result/link.svg")
							| Перейти к источнику
		.btnClose(@click="$emit('close')") Закрыть
</template>

<script>
import KrotUiChartLine from "@/components/ui/KrotUiChartLine.vue";

export default {
	components: {KrotUiChartLine},
	emits:['close'],
	props:{
		data:{
			type:Object,
			default:()=>{return {}}
		}
	},
	data(){
		return{
			url:import.meta.env.VITE_URL_SERVER,
			links:{
				'google-chrome.png':'https://www.google.com/maps?output=search&q=',
				'ya-chrome.png':'https://ya.ru/maps?text=',
				'list-org-chrome.png':'https://www.list-org.com/search?type=name&val=',
				'rusprofile-chrome.png':'https://www.rusprofile.ru/search?query=',
				'avito-chrome.png':'https://www.avito.ru/?q=',
			},
			images:[]
		}
	},
	methods:{
		async $_krot_result_modal_load(){
			const res = await this.$makeRequest('GET',`uploads/account/${this.$props.data.accountId}`)
			if(res) this.images = res
		},
	},
	created() {
		this.$_krot_result_modal_load()
	},
	mounted() {
		window.document.body.style = 'overflow:hidden;padding-right:5px'
	},
	beforeUnmount() {
		window.document.body.style = ''
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
		max-width: 1150px;
		width: 100%;
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
		overflow: hidden;
		display: flex;
		flex-direction: column;
		background-color: white;
		@media (max-width: 1182px) {
			width: calc(100vw - 16px);
			padding: 12px;
		}
		.listCharts{
			display: contents;
		}
		.contentBody{
			flex: auto;
			overflow: auto;
			&::-webkit-scrollbar, &::-webkit-scrollbar, &::-webkit-scrollbar {width: 8px;}
			&::-webkit-scrollbar-thumb, &::-webkit-scrollbar-thumb, &::-webkit-scrollbar-thumb{background: #6472EA;border-radius: 0;}
			&::-webkit-scrollbar-thumb:hover, &::-webkit-scrollbar-thumb:hover, &::-webkit-scrollbar-thumb:hover{background: #6472EA;}
			&::-webkit-scrollbar-thumb:focus, &::-webkit-scrollbar-thumb:focus, &::-webkit-scrollbar-thumb:focus{background: #6472EA;}
			.line{
				display: flex;
				gap: 24px;
				margin-bottom: 16px;
				.halfBlock{
					flex-basis: calc(50% - 12px);
					@media (max-width: 991px) {
						flex-basis: 100%;
						.listCharts{
							display: flex;
							width: 100%;
							gap: 8px;
							@media (max-width: 870px) {
								flex-wrap: wrap;
								.whiteBlock{
									flex-basis: 100%;
								}
							}
							.whiteBlock{flex: 1;}
						}
					}
				}
				@media (max-width: 991px) {
					gap: 12px;
					flex-wrap: wrap;
				}
			}
			.btnClose{
				width: 118px;
				height: 50px;
				display: flex;
				justify-content: center;
				align-items: center;
				font-weight: 600;
				font-size: 16px;
				line-height: 150%;
				letter-spacing: -2%;
				text-align: center;
				color: #7545FF;
				cursor: pointer;
				border-radius: 60px;
				background-color: white;
				margin: 0 auto;
			}
		}
		&.status-0{
			background-color: #EEFFF2;
			border: 1px solid #EEFFF2;
		}
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
		.rowInfo{
			display: flex;
			flex-direction: column;
			gap: 4px;
			margin-bottom: 10px;
			.greyText{
				font-weight: 500;
				font-size: 16px;
				line-height: 110%;
				letter-spacing: -3%;
				color: #9AACD0;
			}
			.text{
				font-weight: 400;
				font-size: 16px;
				line-height: 110%;
				letter-spacing: -3%;
				color: #1A202C;
			}
		}
		.whiteBlock{
			background-color: white;
			border-radius: 10px;
			border: 1px solid #F5F5F5;
			display: flex;
			flex-direction: column;
			padding: 16px;
			.mainName{
				margin-bottom: 16px;
				font-weight: 700;
				font-size: 16px;
				line-height: 110%;
				letter-spacing: -3%;
			}
			.name{
				font-weight: 500;
				font-size: 16px;
				line-height: 110%;
				letter-spacing: -3%;
				margin-bottom: 4px;
				color: #9AACD0;
			}
			.count{
				font-weight: 700;
				font-size: 24px;
				line-height: 110%;
				letter-spacing: -3%;
				color: #1B2559;
				margin-bottom: 24px;
				display: flex;
				align-items: center;
				gap: 10px;
				span{
					font-size: 18px;
				}
				@media (max-width: 576px) {
					font-size: 18px;
					span{font-size: 14px;}
				}
			}
		}
		.pic{
			padding-bottom: 16px;
			border-bottom: 1px solid #F1F1EF;
			margin-bottom: 16px;
			&:last-child{
				margin-bottom: 0;
				border-bottom: unset;
			}
			img{
				width: 100%;
			}
			.resource{
				cursor: pointer;
				display: flex;
				align-items: center;
				gap: 3px;
				font-weight: 500;
				font-size: 14px;
				line-height: 110%;
				letter-spacing: -3%;
				color: #007AFF;
				margin-top: 10px;
				img{width: auto}
			}
		}
	}
</style>