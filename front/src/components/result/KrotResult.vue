<template lang="pug">
#resultBlock
.title Результат распознавания
.container(:class="{'secondType':$props.type === 1}")
	.rowFilter.shadowBlock
		.chart
			KrotUiChartPie(:colors="$props.type?['#9F9D9D78','#13A43878']:['#13A43878', '#F2B63678', '#FF584578', '#9F9D9D78']"
				:data="$props.type?[filterCount[0],filterCount[3]]:filterCount"
				:labels="$props.type?['Коммерция','Частники']:['Не выявлено','Есть подозрение','Высокая вероятность','Коммерция']")
		.filters
			.subtitle Распознано объектов: {{totalSumm}}
			.checkBoxList(v-if="type === 0")
				KrotUiCheckbox(:label="`- Не выявлено: ${filterCount[0]}`" bg="#13A438" border="#13A438" v-model="filter[0]"
					desc="От 0% - 25%" @update:modelValue="$_krot_result_filter")
				KrotUiCheckbox(:label="`- Есть подозрение: ${filterCount[1]}`" bg="#F2B636" border="#F2B636" v-model="filter[1]"
					desc="От 26% - 65%" @update:modelValue="$_krot_result_filter")
				KrotUiCheckbox(:label="`- Высокая вероятность: ${filterCount[2]}`" bg="#FF5845" border="#FF5845" v-model="filter[2]"
					desc="От 66% - 100%" @update:modelValue="$_krot_result_filter")
				KrotUiCheckbox(:label="`- Коммерция: ${filterCount[3]}`" bg="#9F9D9D" border="#9F9D9D" v-model="filter[3]"
					@update:modelValue="$_krot_result_filter")
			.checkBoxList(v-else)
				KrotUiCheckbox(:label="`Частники: ${filterCount[0]}`" bg="#13A438" border="#13A438" v-model="filter[0]"
					@update:modelValue="$_krot_result_filter")
				KrotUiCheckbox(:label="`Коммерция: ${filterCount[3]}`" bg="#FF5845" border="#FF5845" v-model="filter[3]"
					@update:modelValue="$_krot_result_filter")
	.rowFilter
		.subtitle Список распознанных объектов
		.download(@click="$_krot_result_downloadFile") Скачать JSON
			img(src="/img/result/arrowDown.svg")
	KrotUiTable(:table="table" heightScroll="auto")
		.rowTable(v-for="item of rows.slice(0,(page*100))" :class="`status-${item.status}`" :key="item.accountId"
			@click="$_krot_result_openModal(item)")
			.col {{item.accountId}}
			.col {{item.address}}
			.col {{item.consumptionAll}} кВт
			.col.center(v-if="!$props.type")
				.percent(v-if="item.status !== 4") {{item.percent}}
					span %
					img(src="/img/result/light.svg")
				.percent(v-else style="width:fit-content;") Коммерция
					img(src="/img/result/light.svg")
				img.more(src="/img/result/arrowRight.svg")
			.col.center(v-else)
				.percent {{item.status === 4?'Коммерция':'Частник'}}
					img(src="/img/result/light.svg")
		#downLazy(style="height:20px;width:20px;")
KrotResultModal(v-if="modal.show" :data="modal.data" @close="modal.show = false ")
</template>

<script>
import KrotUiCheckbox from "@/components/ui/KrotUiCheckbox.vue";
import KrotUiTable from "@/components/ui/KrotUiTable.vue";
import {defineAsyncComponent} from "vue";
import KrotUiChartPie from "@/components/ui/KrotUiChartPie.vue";

export default {
	props:{
		local_rows:Array,
		type:Number
	},
	data(){
		return{
			filter: [true,true,true,false],
			filterCount: [0,0,0,0],
			rows: [],
			page: 1,
			table: [
				{name:'ID', width:'70px', class:'center'},
				{name:'Адрес', width:'auto'},
				{name:'Кол-во, кВт ', width:'150px', class:'start'},
				{name:'Статус', width:'200px', class:'center'}
			],
			observer: undefined,
			modal: {
				show: false,
				data: {}
			}
		}
	},
	computed:{
		totalSumm(){
			let sum = this.filterCount[0] + this.filterCount[1] + this.filterCount[2] + this.filterCount[3]
			return sum.toLocaleString()
		}
	},
	methods:{
		$_krot_result_downloadFile(){
			const data = JSON.parse(JSON.stringify(this.$props.local_rows))
			for(let item of data){
				delete item.percent
				delete item.status
				delete item.aproxima
			}
			const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(data))
			const downloadAnchorNode = document.createElement('a');
			downloadAnchorNode.setAttribute("href",dataStr);
			downloadAnchorNode.setAttribute("download", "AntiKrot.json");
			document.body.appendChild(downloadAnchorNode);
			downloadAnchorNode.click();
			downloadAnchorNode.remove();
			alert('Файл успешно скачан')
		},
		$_krot_result_filter(){
			this.page = 1
			const arrStatus = []
			for(let i in this.filter){
				if(this.filter[i]) arrStatus.push(+i+1)
			}
			this.rows = this.$props.local_rows.filter(i=>arrStatus.includes(i.status))
		},
		$_krot_result_lazy(){
			const handleIntersect = (entries)=>{
				for(let entry of entries){
					if (!entry.isIntersecting) return;
					else this.page++
				}
			}

			this.observer = new IntersectionObserver(handleIntersect, {threshold: .47});
			this.observer.observe(window.document.getElementById('downLazy'));
		},
		$_krot_result_openModal(item){
			this.modal.data = item
			this.modal.show = true
		},
		$_krot_result_calc(){
			for(let item of this.$props.local_rows){
				this.filterCount[item.status-1]++
			}
		}
	},
	created() {
		if(this.$props.type) this.filter[3] = true
		this.$_krot_result_calc()
		this.$_krot_result_filter()
	},
	mounted() {
		this.$_krot_result_lazy()
		this.$nextTick(()=>{
			const el = window.document.getElementById('resultBlock')
			el.scrollIntoView()
		})
	},
	beforeUnmount() {
		if(this.observer) {
			this.observer.unobserve(window.document.getElementById('downLazy'))
			this.observer = undefined
		}
	},
	components: {
		KrotUiChartPie,
		KrotUiTable, KrotUiCheckbox,
		KrotResultModal: defineAsyncComponent(()=> import("@/components/result/KrotResultModal.vue")),
	}
}
</script>

<style scoped lang="scss">
	.title{
		margin: 78px 0 48px 0;
		text-align: center;
		font-weight: 700;
		font-size: 40px;
		line-height: 110%;
		letter-spacing: -3%;
		color: #1A202C;
		@media (max-width: 991px) {
			font-size: 30px;
		}
		@media (max-width: 768px) {
			font-size: 24px;
		}
	}
	.container{
		margin-bottom: 60px;
		.rowFilter{
			display: flex;
			justify-content: space-between;
			margin-bottom: 15px;
			@media (max-width: 576px) {
				flex-wrap: wrap;
				gap: 8px;
				justify-content: space-between;
			}
			&.shadowBlock{
				background-color: white;
				box-shadow: 0px -6px 7px 0px #00000012;
				padding: 16px;
				border-radius: 16px 16px 0 0;
				gap: 30px;
				background-image: url('/img/result/lightBg.svg');
				background-repeat: no-repeat;
				background-position: 98% 16px;
				.chart{
					width: 140px;
					height: 140px;
					flex: none;
					@media (max-width: 576px) {
						margin: auto;
					}
				}
				.filters{
					flex: auto;
					display: flex;
					flex-direction: column;
					gap: 10px;
					.checkBoxList{
						display: flex;
						flex-wrap: wrap;
						gap: 30px;
						margin-top: 10px;
						@media (max-width: 991px) {
							gap: 16px;
						}
					}
				}
			}
			.subtitle {
				font-weight: 700;
				font-size: 16px;
				line-height: 30px;
				color: #092C4C;
			}
			.download {
				cursor: pointer;
				display: flex;
				align-items: center;
				gap: 6px;
				font-weight: 500;
				font-size: 14px;
				line-height: 30px;
				color: #7545FF;
				@media (max-width: 576px) {
					margin-left: auto;
				}
			}
		}
		.rowTable{
			height: 80px;
			cursor: pointer;
			&.status-1{
				background-color: #EEFFF2;
				.percent{background-color: #13A438;}
			}
			&.status-2{
				background-color: #FFFBD9;
				.percent{background-color: #F2B636;}
			}
			&.status-3{
				background-color: #FFF5F0;
				.percent{background-color: #FF5845;}
			}
			&.status-4{
				background-color: #F6F6F6;
				.percent{background-color: #858585;}
			}
			.col{
				overflow: hidden;
				text-overflow: ellipsis;
				-webkit-box-orient: vertical;
				-webkit-line-clamp: 1;
				display: -webkit-box;
				word-break: break-all;
				&:first-child{padding-left: 12px;}
				&:last-child{padding-right: 20px;}
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
			}
		}
	}
	.secondType{
		.status-1{
			background-color: #EEFFF2 !important;;
			.percent{background-color: #13A438 !important;;}
		}
		.status-4{
			background-color: #FFF5F0 !important;;
			.percent{background-color: #FF5845 !important;;}
		}
	}
</style>