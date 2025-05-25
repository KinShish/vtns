<template lang="pug">
.contentCanvas
	canvas(:id="`chartPie${$props.id}`")
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
		},
		labels:{
			type:Array,
			default:()=>{return []}
		},
		colors:{
			type:Array,
			default:()=>{return []}
		}
	},
	data(){
		return{

		}
	},
	methods:{
		$_krot_ui_chart_line_set(){
			const el = window.document.getElementById(`chartPie${this.$props.id}`)
			const config = {
				type: 'pie',
				data: {
					labels: this.$props.labels,
					datasets: [{
						data: this.$props.data,
						backgroundColor: ['#13A43878', '#F2B63678', '#FF584578', '#9F9D9D78'],
						borderWidth: 0
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
	}
</style>