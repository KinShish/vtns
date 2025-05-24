<template lang="pug">
.uploadBlock
	img.backImg(src="/img/upload/shadow.svg")
	.title Сервис для выявления
		div превышенных лимитов потребления
		div электроэнергии
	.container
		input#file(type="file" accept=".json" ref="refInputLoad" @change="$_krot_upload_files_changeFile")
		#dropZone.uploadZone(:class="{'active':showDropFiles}" v-show="!spinner")
			.blurBlock(v-if="showDropFiles")
				img(src="/img/upload/file.svg")
			.contnets(v-if="!showDropFiles && !file.name")
				img.typeFile(src="/img/upload/json.svg")
				label.labelUpload(for="file") Загрузить DATASET
				br
				KrotUiSwitch(label="Проверка на коммерцию" v-model="type" :chosen="1" notChosen="0")
				.text Или перетащите сюда необходимые файлы
			.contnets(v-if="!showDropFiles && file.name")
				.fileName
					img(src="/img/upload/json.svg")
					.name {{file.name}}
					.size {{file.size}}
				.error Ошибка! Файл имеет неправильный формат
				label.labelUpload(for="file") Загрузить DATASET
		.uploadZone.spinnerBlock(v-show="spinner")
			transition(name="fade" mode="out-in")
				img(src="/img/upload/krot1.gif" v-if="percent < 99")
				img(src="/img/upload/krot2.webp" v-else)
			transition(name="fade" mode="out-in")
				.text(v-if="percent < 99") Идёт загрузка {{percent}}%
				.text(v-else) Идёт обработка файла
			.loadBar(:style="`opacity:${percent===99?0:1}`")
				div(:style="`width:${percent}%`")
			.cancel(@click="$_krot_upload_files_cancel") Отменить
</template>

<script>
import KrotUiSwitch from "@/components/ui/KrotUiSwitch.vue";

export default {
	components: {KrotUiSwitch},
	emits:['upload','closeResult'],
	data(){
		return{
			timeOutHide: undefined,
			showDropFiles: false,
			spinner: false,
			percent: 0,
			type:0,
			controller: undefined,
			file: {
				name: '',
				size: ''
			}
		}
	},
	methods:{
		$_krot_upload_files_cancel(){
			this.spinner = false
			this.controller.abort()
		},
		$_krot_upload_files_dragAndDrop(){
			const el = window.document.getElementById('dropZone')
			el.addEventListener("dragenter", (e)=> {
				e.preventDefault();
				clearTimeout(this.timeOutHide)
				this.showDropFiles = true
				this.file.name = ''
				this.file.size = ''
			});

			el.addEventListener("dragover", (e)=> {
				e.preventDefault();
				clearTimeout(this.timeOutHide)
				this.showDropFiles = true
				this.file.name = ''
				this.file.size = ''
			});

			el.addEventListener("dragleave", (e)=> {
				e.preventDefault();
				clearTimeout(this.timeOutHide)
				this.timeOutHide=setTimeout(()=>{this.showDropFiles = false},200)
			});
			el.addEventListener("drop", (e) => {
				e.preventDefault();
				this.showDropFiles = false
				this.file.name = ''
				this.file.size = ''
				if (e.dataTransfer.files.length) {
					for(let file of e.dataTransfer.files){
						if((/\.(json)$/i.test(file.name))){
							this.$_krot_upload_files_uploadFile(file)
							break
						} else {
							this.$emit('closeResult')
							this.file.name = file.name
							this.file.size = this.$_krot_upload_files_getSizeFile(file.size)
						}
					}
				}
			});
		},
		$_krot_upload_files_getSizeFile(size){
			const units = ['bytes', 'KB', 'MB'];
			let l = 0, n = parseInt(size, 10) || 0;
			while(n >= 1024 && ++l){
				n = n/1024;
			}
			return(n.toFixed(n < 10 && l > 0 ? 1 : 0) + ' ' + units[l]);
		},
		$_krot_upload_files_changeFile(e){
			if(e.target.files.length) this.$_krot_upload_files_uploadFile(e.target.files[0])
			this.$refs.refInputLoad.value = ''
		},
		async $_krot_upload_files_uploadFile(file){
			this.$emit('closeResult')
			this.controller = new AbortController()

			this.spinner = true
			const formData = new FormData()
			formData.append('file',file)
			const res = await this.$makeRequest('POST','load/dataset/chek',formData,this.controller.signal,
				(e)=>{
				this.percent = ((e.loaded / e.total) * 100).toFixed(2);
				})
			if(res){
				for(let item of res){
					if(item.percent) {
						item.percent = item.percent*100
						item.percent = item.percent.toFixed(2)
						if(item.percent<25) item.status = 1
						else {
							if(item.percent>65) item.status = 3
							else item.status = 2
						}
					} else item.status = 0
					if(item.consumption){
						item.consumptionAll = 0
						for(let cons of Object.values(item.consumption)){
							item.consumptionAll += cons||0
						}
						item.consumptionAll = item.consumptionAll.toFixed(2).toLocaleString()
					} else item.consumptionAll = 0
				}


				this.$emit('upload', {rows:res,type:this.type})
			} else alert('Произошла ошибка, попробуйте позже')
			this.spinner = false
		}
	},
	mounted() {
		this.$_krot_upload_files_dragAndDrop()
	}
}
</script>

<style scoped lang="scss">
	.uploadBlock{
		min-height: 746px;
		height: calc(100vh - 225px);
		background: linear-gradient(83.79deg, #13A438 3.25%, #13A438 96.85%);
		display: flex;
		flex-direction: column;
		gap: 60px;
		align-items: center;
		justify-content: center;
		position: relative;
		overflow: hidden;
		.backImg{
			position: absolute;
			height: 562px;
			width: 1286px;
			left: 0;
			bottom: 0;
			z-index: 1;
		}
		.title{
			font-weight: 700;
			font-size: 40px;
			line-height: 110%;
			color: white;
			letter-spacing: -3%;
			text-align: center;
			z-index: 2;
		}
		.container{
			z-index: 2;
			#file{display: none}
			.uploadZone{
				overflow: hidden;
				height: 300px;
				width: 100%;
				background-color: #FFFFFFF2;
				z-index: 2;
				background-image: url("data:image/svg+xml,%3csvg width='100%25' height='100%25' xmlns='http://www.w3.org/2000/svg'%3e%3crect width='100%25' height='100%25' fill='none' rx='17' ry='17' stroke='%236472EAFF' stroke-width='1' stroke-dasharray='1%2c5%2c1' stroke-dashoffset='9' stroke-linecap='square'/%3e%3c/svg%3e");
				border-radius: 16px;
				display: flex;
				flex-direction: column;
				justify-content: center;
				align-items: center;
				transition: .3s ease-out;
				&.spinnerBlock{
					height: fit-content;
					padding: 24px 0;
					gap: 24px;
					img{height: 130px}
					.loadBar{
						position: relative;
						overflow: hidden;
						width: 400px;
						height: 14px;
						background-color: #E3E3E3;
						border-radius: 30px;;
						div{
							height: 100%;
							background-color: #7545FF;
							transition: .3s ease-out;
						}
					}
					.cancel{
						cursor: pointer;
						width: 130px;
						height: 50px;
						display: flex;
						justify-content: center;
						align-items: center;
						text-align: center;
						background-color: white;
						color: #7545FF;
						border: 1px solid #7545FF;
						border-radius: 60px;
						font-weight: 600;
						font-size: 16px;
						line-height: 150%;
						letter-spacing: -2%;
					}
				}
				&.active{
					border: 1px solid #6472EA;
				}
				.contnets{display: contents;}
				.typeFile{margin-bottom: 24px;}
				.labelUpload{
					cursor: pointer;
					border-radius: 60px;
					background: linear-gradient(112.8deg, #6A36FF -15.76%, #AC5FE6 102.86%);
					border: 1px solid #7545FF;
					width: 210px;
					height: 50px;
					display: flex;
					justify-content: center;
					align-items: center;
					font-weight: 600;
					font-size: 16px;
					line-height: 150%;
					letter-spacing: -2%;
					color: #FFFFFF;
				}
				.text{
					text-align: center;
					font-weight: 400;
					font-size: 16px;
					color: #1A202C;
					line-height: 24px;
					margin-top: 16px;
				}
				.blurBlock{
					width: 100%;
					height: 100%;
					display: flex;
					justify-content: center;
					align-items: center;
					background-color: #7545FF4D;
					backdrop-filter: blur(10px  );
					img{
						height: 80px;
						width: 80px;
					}
				}
				.fileName{
					display: flex;
					align-items: center;
					gap: 10px;
					.name{
						max-width: 200px;
						width: fit-content;
						font-weight: 400;
						font-size: 16px;
						color: #1A202C;
					}
					.size{
						font-weight: 400;
						font-size: 16px;
						color: #90A3BF;
					}
				}
				.error{
					font-weight: 400;
					font-size: 16px;
					color: #DB2719;
					margin: 24px 0;
				}
			}
		}
	}
</style>