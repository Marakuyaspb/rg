function addSpace(){
	/* ADD space into prices */
	let price_display = document.getElementsByClassName('price_display');

	for (let i = 0; i < price_display.length; i++) {
	    let price = parseInt(price_display[i].textContent);
	    let formattedPrice = new Intl.NumberFormat('ru-RU').format(price);
	    
	    price_display[i].textContent = formattedPrice + ' ₽';
	}
}
addSpace();