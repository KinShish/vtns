<template lang="pug">
.thunder
	canvas#canvas
</template>

<script>
export default {
	data(){
		return{
			canvas: undefined,
			ctx: undefined,
			rainThroughnum: 500,
			rainTrough: [],
			lightning: [],
			lightTimeCurrent: 0,
			lightTimeTotal: 0,
			w: 0, h: 0
		}
	},
	methods:{
		$_crot_lights_init(){
			this.canvas = document.getElementById('canvas')

			this.ctx = this.canvas.getContext('2d')

			this.w = this.canvas.width = window.innerWidth
			this.h = this.canvas.height = window.innerHeight

			window.addEventListener('resize', ()=> {
				this.w = this.canvas.width = window.innerWidth
				this.h = this.canvas.height = window.innerHeight

				this.$_crot_lights_createRainTrough()
			})

			this.$_crot_lights_createRainTrough()
			this.$_crot_lights_animLoop()
		},
		$_crot_lights_random(min, max) {
			return Math.random() * (max - min + 1) + min
		},
		$_crot_lights_clearCanvas() {
			this.ctx.globalCompositeOperation = 'destination-out'
			this.ctx.fillStyle = 'rgba(0,0,0,' + this.$_crot_lights_random(1, 30) / 100 + ')'
			this.ctx.fillRect(0, 0, this.w, this.h)
			this.ctx.globalCompositeOperation = 'source-over'
		},
		$_crot_lights_createRainTrough() {
			for (let i = 0; i < this.rainThroughnum; i++) {
				this.rainTrough[i] = {
					x: this.$_crot_lights_random(0, this.w),
					y: this.$_crot_lights_random(0, this.h),
					length: Math.floor(this.$_crot_lights_random(1, 830)),
					opacity: Math.random() * 0.2,
					xs: this.$_crot_lights_random(-2, 2),
					ys: this.$_crot_lights_random(10, 20)
				};
			}
		},
		$_crot_lights_createLightning() {
			const x = this.$_crot_lights_random(100, this.w - 100)
			const y = this.$_crot_lights_random(0, this.h / 4)

			const createCount = this.$_crot_lights_random(1, 3)
			for (let i = 0; i < createCount; i++) {
				const single = {
					x: x,
					y: y,
					xRange: this.$_crot_lights_random(5, 30),
					yRange: this.$_crot_lights_random(10, 25),
					path: [{
						x: x,
						y: y
					}],
					pathLimit: this.$_crot_lights_random(40, 55)
				};
				this.lightning.push(single)
			}
		},
		$_crot_lights_drawLightning() {
			for (let i = 0; i < this.lightning.length; i++) {
				const light = this.lightning[i];

				light.path.push({
					x: light.path[light.path.length - 1].x + (this.$_crot_lights_random(0, light.xRange) - (light.xRange / 2)),
					y: light.path[light.path.length - 1].y + (this.$_crot_lights_random(0, light.yRange))
				});

				if (light.path.length > light.pathLimit) this.lightning.splice(i, 1)

				this.ctx.strokeStyle = 'rgba(255, 255, 255, .1)'
				this.ctx.lineWidth = 3
				if (this.$_crot_lights_random(0, 15) === 0) this.ctx.lineWidth = 6
				if (this.$_crot_lights_random(0, 30) === 0) this.ctx.lineWidth = 8

				this.ctx.beginPath()
				this.ctx.moveTo(light.x, light.y)
				for (let pc = 0; pc < light.path.length; pc++) {
					this.ctx.lineTo(light.path[pc].x, light.path[pc].y)
				}
				if (Math.floor(this.$_crot_lights_random(0, 30)) === 1) {
					this.ctx.fillStyle = 'rgba(255, 255, 255, ' + this.$_crot_lights_random(1, 3) / 100 + ')'
					this.ctx.fillRect(0, 0, this.w, this.h)
				}
				this.ctx.lineJoin = 'miter'
				this.ctx.stroke()
			}
		},
		$_crot_lights_animateLightning() {
			this.$_crot_lights_clearCanvas()
			this.lightTimeCurrent++
			if (this.lightTimeCurrent >= this.lightTimeTotal) {
				this.$_crot_lights_createLightning();
				this.lightTimeCurrent = 0
				this.lightTimeTotal = 200
			}
			this.$_crot_lights_drawLightning()
		},
		$_crot_lights_animLoop() {
			this.$_crot_lights_animateLightning()
			requestAnimationFrame(this.$_crot_lights_animLoop)
		}
	},
	mounted() {
		this.$_crot_lights_init()
	}
}
</script>

<style scoped lang="scss">
	canvas {
		display: block;
		position: absolute;
		top: 0;
		left: 0;
		z-index: -1;
	}
</style>