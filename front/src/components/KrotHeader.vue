<template lang="pug">
.header
	img(src="/img/logo.svg")
</template>

<style scoped lang="scss">
	.header{
		height: 60px;
		background-color: #ffffff;
		display: flex;
		justify-content: center;
		align-items: center;
		@media (max-width: 991px) {
			height: 30px;
			img{height: 28px;}
			position: sticky;
			top: 0;
			z-index: 2;
		}
	}
</style>