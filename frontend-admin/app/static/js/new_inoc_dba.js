function newINOCDBA(element) {
    var divNoInoc = document.getElementById('no-inoc');
    var divYesInoc = document.getElementById('yes-inoc');

    if (element.checked) {
        if (element.value == 'sim') {
            divYesInoc.removeAttribute('hidden', '');
            divNoInoc.setAttribute('hidden', '')
        } else if (element.value == 'nao') {
            divNoInoc.removeAttribute('hidden', '');
            divYesInoc.setAttribute('hidden', '')
        }
    }
}