<template lang="pug">
.switchBlock
	label.switch
		input(type='checkbox' @change="$_krot_ui_switch_change" v-model="check")
		.slider.round
	.labelText(@click="check = !check;$_krot_ui_switch_change()") {{$props.label}}
</template>

<script>
export default {
	emits:['change','update:modelValue'],
	props:{
		modelValue:{
			type:[String,Number,Boolean],
			default:false
		},
		chosen:{
			type:[String,Number,Boolean],
			default:true
		},
		notChosen:{
			type:[String,Number,Boolean],
			default:false
		},
		label:{
			type:String,
			default:''
		}
	},
	data(){
		return{
			check: this.$props.modelValue === this.$props.chosen
		}
	},
	methods:{
		$_krot_ui_switch_change(){
			this.$emit('update:modelValue',(this.check?this.$props.chosen:this.$props.notChosen))
			this.$emit('change')
		}
	},
	watch:{
		'modelValue'(){
			this.check = this.$props.modelValue === this.$props.chosen
		}
	}
}
</script>

<style scoped lang="scss">
	.switchBlock{
		display: flex;
		align-items: center;
		gap: 10px;
		.labelText{
			font-weight: 400;
			font-size: 14px;
			color: #1A202C;
			cursor: pointer;
		}
	}
	.switch {
		position: relative;
		display: inline-block;
		width: 46px;
		height: 24px;
		input {
			display: none;
			&:checked + .slider {
				background-color: #7C0BFF;
				border-color: #7C0BFF;
			}
			&:checked + .slider:before {
				-webkit-transform: translateX(19px);
				-ms-transform: translateX(19px);
				transform: translateX(19px);
				background: white;
			}
		}
		.slider {
			position: absolute;
			cursor: pointer;
			top: 0;
			left: 0;
			right: 0;
			bottom: 0;
			-webkit-transition: 0.4s;
			transition: 0.4s;
			border: 1px solid #7545FF;
			background-color: white;
			&:before {
				position: absolute;
				content: "";
				height: 16px;
				width: 16px;
				left: 4px;
				bottom: 0;
				top: 0;
				margin: auto;
				background: linear-gradient(112.8deg, #6A36FF -15.76%, #AC5FE6 102.86%);
				-webkit-transition: 0.4s;
				transition: 0.4s;
				box-shadow: 0 4px 4px 0 #00000040;
			}
			&.round {border-radius: 34px;}
			&.round:before {border-radius: 50%;}
		}
	}
</style>