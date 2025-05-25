<template lang="pug">
#resultBlock
.title Результат распознавания
.container
	.legend
		.info От 0% - 25%
			.status.status-1
		.greyLine
		.info От 25% - 65%
			.status.status-2
		.greyLine
		.info От 65% - 100%
			.status.status-3
	.rowFilter
		div
			.subtitle Распознано объектов: {{totalSumm}}
			.checkBoxList
				KrotUiCheckbox(:label="`- Не выявлено: ${filterCount[0]}`" bg="#13A438" border="#13A438" v-model="filter[0]"
					@update:modelValue="$_krot_result_filter")
				KrotUiCheckbox(:label="`- Есть подозрение: ${filterCount[1]}`" bg="#13A438" border="#13A438" v-model="filter[1]"
					@update:modelValue="$_krot_result_filter")
				KrotUiCheckbox(:label="`- Коммерческие организации: ${filterCount[2]}`" bg="#FF5845" border="#FF5845" v-model="filter[2]"
					@update:modelValue="$_krot_result_filter")
		.download Скачать JSON
			img(src="/img/result/arrowDown.svg")
	KrotUiTable(:table="table")
		.rowTable(v-for="item of rows.slice(0,page*100)" :class="`status-${item.status}`"
			@click="$_krot_result_openModal(item)")
			.col {{item.accountId}}
			.col {{item.address}}
			.col {{item.consumptionAll}} кВт
			.col.center
				.percent {{item.percent}}
					span %
					img(src="/img/result/light.svg")
				img.more(src="/img/result/arrowRight.svg")
		#downLazy(style="height:20px;width:20px;")
transition(name="fade" mode="out-in")
	KrotResultModal(v-if="modal.show" :data="modal.data")
</template>

<script>
import KrotUiCheckbox from "@/components/ui/KrotUiCheckbox.vue";
import KrotUiTable from "@/components/ui/KrotUiTable.vue";
import {defineAsyncComponent} from "vue";

export default {
	props:{
		local_rows:Array,
		type:Number
	},
	data(){
		return{
			filter: [true,true,true],
			filterCount: [0,0,0],
			rows: JSON.parse(JSON.stringify(this.local_rows)),
			page: 1,
			table: [
				{name:'ID', width:'70px', class:'center'},
				{name:'Адрес', width:'auto'},
				{name:'Кол-во, кВт ', width:'150px', class:'start'},
				{name:'Статус', width:'160px', class:'center'}
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
			let sum = this.filterCount[0] + this.filterCount[1] + this.filterCount[2]
			return sum.toLocaleString()
		}
	},
	methods:{
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
		this.$_krot_result_calc()
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
	}
	.container{
		margin-bottom: 60px;
		.legend{
			display: flex;
			justify-content: center;
			align-items: center;
			gap: 21px;
			height: 75px;
			background: #F6F6F6;
			border: 1px solid #EEFFF2;
			margin-bottom: 24px;
			border-radius: 16px;
			.info{
				display: flex;
				align-items: center;
				gap: 6px;
				font-weight: 500;
				font-size: 16px;
				line-height: 110%;
				color: #9AACD0;
			}
			.status{
				width: 12px;
				height: 12px;
				border-radius: 50%;
				&-1{background-color: #13A438;}
				&-2{background-color: #F2B636;}
				&-3{background-color: #FF5845;}
			}
			.greyLine{
				height: 44px;
				width: 1px;
				background-color: #B4B6C4;
			}
		}
		.rowFilter{
			display: flex;
			justify-content: space-between;
			margin-bottom: 15px;
			.subtitle {
				font-weight: 700;
				font-size: 16px;
				line-height: 30px;
				color: #092C4C;
			}
			.checkBoxList{
				display: flex;
				gap: 30px;
				margin-top: 10px;
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
</style>