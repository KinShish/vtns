<template lang="pug">
.footerBlock
	.container
		a(href="https://team.prai.su/" target="_blank" title="PRAI")
			img(src="/img/prai.svg")
		.rowInfo
			.address
				.labelBlock Адрес
				.text Адрес 353560, г. Славянск-на-Кубани, ул Крупской 237/1, 2 этаж
			.additional
				.labelBlock Почта
				a(href="mailto:info@prai.su") info@prai.su
			.additional
				.labelBlock Наш сайт
				a(href="https://team.prai.su/" target="_blank" title="PRAI") team.prai.su
</template>

<style scoped lang="scss">
	.footerBlock{
		height: 165px;
		background-color: #F6F6F6;
		padding-top: 24px;
		padding-bottom: 24px;
		.rowInfo{
			display: flex;
			gap: 24px;
			align-items: flex-start;
			margin-top: 20px;
			.address{
				flex: auto;
				.text{
					font-weight: 400;
					font-size: 14px;
					line-height: 180%;
					color: #252525;
				}
			}
			.additional{
				width: 260px;
				flex: none;
				a{
					color: #0097FE;
					font-weight: 400;
					font-size: 14px;
					line-height: 180%;
				}
			}
			.labelBlock{
				text-transform: uppercase;
				font-weight: 600;
				font-size: 14px;
				line-height: 140%;
				color: #9AACD0;
			}
		}
	}
</style>