<template lang="pug">
.checkboxBlock(:class="{'disabled':$props.disabled}" :style="`--bg:${$props.bg};--border:${$props.border}`")
	input(:id="idLocal" type="checkbox" v-model="value" :true-value="$props.trueValue" :false-value="$props.falseValue"
		@change="$emit('update:modelValue',value)" :disabled="$props.disabled")
	label(:for="idLocal" v-if="$props.label") {{$props.label}}
</template>

<script>
export default {
	props:{
		trueValue:{
			type: [Boolean,Number],
			default: true
		},
		falseValue:{
			type: [Boolean,Number],
			default: false
		},
		label:{
			type:String,
			default:''
		},
		modelValue:{
			type: [Boolean,Number],
			default: false
		},
		id:{
			type:String,
			default:''
		},
		disabled:{
			type:Boolean,
			default:false
		},
		bg:{
			type:String,
			default:'#00B46F'
		},
		border:{
			type:String,
			default:'#EFEFEF'
		}
	},
	data(){
		return{
			idLocal:`inpCheck-${this.$props.id}-${Math.floor(Math.random() * 100)}`,
			value:this.$props.modelValue
		}
	},
	watch:{
		'$props.modelValue'(value){
			this.value = value
		}
	}
}
</script>

<style scoped lang="scss">
	.checkboxBlock{
		display: flex;
		align-items: flex-start;
		gap: 8px;
		&.disabled{
			opacity: .3;
			*{cursor: not-allowed;}
		}
		label{
			display: flex;
			flex-direction: column;
			gap: 4px;
			width: fit-content;
			user-select: none;
			font-weight: 400;
			font-size: 16px;
			line-height: 24px;
		}
	}
	input[type=checkbox]{
		width: 24px;
		flex: none;
		height: 24px;
		padding: 0;
		border: solid 1px var(--border);
		-webkit-appearance: none;
		-moz-appearance: none;
		appearance: none;
		print-color-adjust: exact;
		transition: .2s ease-in-out;
		cursor: pointer;
		border-radius: 6px;
	}
	input[type=checkbox]:hover{
		border: solid 1px #32323280;
	}
	input[type=checkbox]:active{
		border: solid 1px #32323280;
	}
	input[type=checkbox]:checked:active{
		background-color: var(--bg);
	}
	input[type=checkbox]:checked{
		background-image: url("data:image/svg+xml,%3csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 20 20%27%3e%3cpath fill=%27none%27 stroke=%27%23fff%27 stroke-linecap=%27round%27 stroke-linejoin=%27round%27 stroke-width=%273%27 d=%27m6 10 3 3 6-6%27/%3e%3c/svg%3e");
		background-color: var(--bg);
		border: none;
	}
</style>