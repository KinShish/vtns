import axios from "axios";

const server = import.meta.env.VITE_URL_SERVER
/**
 * @param {string} method - Метод запроса
 * @param {string} url - путь запроса
 * @param {object} formData - тело запроса
 * @param {string} cancel - токен отмены запроса (из AbortController())
 * @param {object} config - конфигурация и методы запроса
 * */
const makeRequest = async (method, url, formData, cancel = '',onUploadProgress=undefined) => {

	try {
		const { data } = await axios({
			method,
			url: encodeURI(`${server}${url}`),
			data: formData,
			signal: cancel,
			onUploadProgress
		})
		if(data&&!data.error) {
			return data
		}
		return false
	} catch (error) {
		console.error(new Error(error.message))
		return false
	}
};

export default makeRequest;