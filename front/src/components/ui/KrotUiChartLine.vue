<template lang="pug">
.contentCanvas
	canvas(:id="`chartLine${$props.id}`")
</template>

<script>
import {Chart} from "chart.js/auto";

export default {
	props:{
		data:Array,
		id:{
			type:String,
			default:''
		},
		hidex:{
			type:Boolean,
			default:false
		}
	},
	data(){
		return{

		}
	},
	methods:{
		$_krot_ui_chart_line_set(){
			const el = window.document.getElementById(`chartLine${this.$props.id}`)
			const config = {
				type: 'line',
				data: {
					labels: this.$props.hidex?[1,2,3,4,5,6,7,8,9,10,11]:['Янв', 'Фев', 'Март', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сент', 'Окт', 'Нояб','Дек'],
					datasets: [{
						data: this.$props.data,
						fill: false,
						borderColor: '#9AACD0',
						tension: 0.5
					}]
				},
				options: {
					plugins: {
						legend: {
							display: false
						}
					},
					scales: {
						y: {display: false}
					}
				}
			}
			if(this.$props.hidex){
				config.options.scales.x = {display: false}
				config.data.labels.splice(0,1)
			}
			new Chart(el, config)
		}
	},
	mounted() {
		this.$_krot_ui_chart_line_set()
	}
}
</script>

<style scoped lang="scss">
	.contentCanvas{
		height: 240px;
		@media (max-width: 991px) {
			height: 180px;
		}
		@media (max-width: 576px) {
			height: auto;
			width: 100%;
		}
		@media (max-width: 385px) {
			scale: .9;
		}
		@media (max-width: 355px) {
			scale: .8;
		}
	}
</style>