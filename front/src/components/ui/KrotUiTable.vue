<template lang="pug">
.scrolledBlockTable(:style="`--sizeTable:${getStyleTable};--heightScroll:${$props.heightScroll}`")
	.mainBlockTable
		.headBlock
			.col(v-for="item of $props.table" :class="item.class||''") {{item.name}}
		slot
</template>

<script>
export default {
	props:{
		table:{
			type:Array,
			default:()=>{return []}
		},
		heightScroll:{
			type:String,
			default:'calc(100vh - 250px)'
		},
		spinner:{
			type:Boolean,
			default:false
		},
		additionalWidth:{
			type:String,
			default:''
		}
	},
	computed:{
		getStyleTable(){
			return `${this.$props.additionalWidth?`${this.$props.additionalWidth} `:''}`+this.$props.table.map(i=>i.width).join(' ')
		}
	}
}
</script>

<style scoped lang="scss">
	.scrolledBlockTable{
		height: var(--heightScroll);
		overflow: auto;
		position: relative;
		&::-webkit-scrollbar, &::-webkit-scrollbar, &::-webkit-scrollbar {width: 8px;}
		&::-webkit-scrollbar-thumb, &::-webkit-scrollbar-thumb, &::-webkit-scrollbar-thumb{background: #6472EA;border-radius: 0;}
		&::-webkit-scrollbar-thumb:hover, &::-webkit-scrollbar-thumb:hover, &::-webkit-scrollbar-thumb:hover{background: #6472EA;}
		&::-webkit-scrollbar-thumb:focus, &::-webkit-scrollbar-thumb:focus, &::-webkit-scrollbar-thumb:focus{background: #6472EA;}
	}
	.mainBlockTable{
		min-width: 1000px;
		width: 100%;
	}
	.headBlock{
		display: grid;
		grid-auto-flow: column;
		grid-auto-columns: 1fr;
		gap: 24px;
		grid-template-columns: var(--sizeTable);
		position: sticky;
		top: 0;
		left: 0;
		z-index: 1;
		background-color: white;
		.col{
			font-weight: 500;
			font-size: 16px;
			line-height: 30px;
			color: #7E92A2;
			display: flex;
			align-items: flex-end;
			&.center{justify-content: center;}
			&.start{justify-content: flex-start;}
		}
	}
	.blockSpinner{
		width: 100%;
		display: flex;
		justify-content: center;
		height: var(--heightScroll);
		position: absolute;
		top: 0;
		left: 0;
		z-index: 2;
	}
</style>
<style>
	.scrolledBlockTable .mainBlockTable .rowTable{
		display: grid;
		grid-auto-flow: column;
		gap: 24px;
		grid-auto-columns: 1fr;
		grid-template-columns: var(--sizeTable);
		border-bottom: 1px solid #0000001A;
		transition: background-color .3s ease-out;
		.col{
			font-weight: 400;
			font-size: 16px;
			line-height: 30px;
			color: #092C4C;
			height: fit-content;
			margin: auto 0;
			&.center{
				display: flex;
				align-items: center;
				justify-content: space-between;
			}
			&.start{
				display: flex;
				align-items: center;
				justify-content: flex-start;
			}
		}
	}
</style>