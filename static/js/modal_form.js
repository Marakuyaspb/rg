function showModal(element) {
	    element.querySelector('.thumb').classList.add('hide');
	    element.querySelector('.modal_full').classList.add('block');
	}


function closeModal(closeButton) {
    const modalContainer = closeButton.closest('.modal_container');
    if (modalContainer) {
        const modalFull = modalContainer.querySelector('.modal_full');
        const thumb = modalContainer.querySelector('.thumb');

        if (modalFull && thumb) {
            modalFull.classList.remove('block');
            thumb.classList.remove('hide');
        } else {
            console.error('Modal elements not found in the specified container.');
        }
    } else {
        console.error('Modal container not found.');
    }
}


document.addEventListener('click', function(event) {
    if (event.target.classList.contains('close')) {
        closeModal(event.target);
    }
});


document.querySelector('.modal_full').addEventListener('click', function(event) {
    event.stopPropagation();
});