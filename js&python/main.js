function next_1() {
	value_com = document.querySelectorAll('input')[0].value
	if (value_com != "" && value_com != " " && value_com != 1){
		document.querySelector('.block-value-com').innerHTML = ''
		for (var i = value_com; i >= 1; i--) {
			document.querySelector('.block-value-com').insertAdjacentHTML('afterBegin',
			`<div class="block-name-com">
				<h2>Введите название команды №:${i}</h2>
		        <input type="text" name="TEXT_2">
		        <div id="last"></div>
			</div>`);
		}
		document.querySelectorAll('.block-name-com')[value_com-1].lastElementChild.insertAdjacentHTML('afterBegin',`<input type="submit" value="Далее" name="btn-next" onclick="next_2()"><input type="submit" value="Назад" name="btn-undo" onclick="window.location.reload()">`)

	}
}

function next_2() {

	let i_inp = 0
	obj_com = {}

	for (var i = 0; i < value_com; i++) {
		inp = document.querySelectorAll('.block-name-com')[i].querySelector('input[name="TEXT_2"]').value
		if (inp != "" && inp != " "){i_inp += 1;
			obj_com[i+1] = inp
		}
	}
	if (i_inp != value_com){
		obj_com = {}
	}
	else{
		console.log(obj_com)
		document.querySelector('.block-value-com').classList.add('anim-')
		setTimeout( () => {document.querySelector('.block-value-com').remove()}, 800)
		setTimeout( () => {document.querySelector('.block-ask_or_action').style.display = 'block';
		document.querySelector('.block-ask_or_action h2').innerText = `Играет команда: ${random_com()}`},1000)
	}
}

function next_3() {
	document.querySelector('.block-ask_or_action').style.display = 'block'
	document.querySelector('.block-game').style.display = 'none'
	document.querySelector('.block-ask_or_action h2').innerText = `Играет команда: ${random_com()}`
}
function random_com() {
	rc = getRandomIntInclusive(1, value_com)
	return obj_com[rc]
}


function getRandomIntInclusive(min, max) {
	min = Math.ceil(min);
	max = Math.floor(max);
	return Math.floor(Math.random() * (max - min + 1)) + min; //Максимум и минимум включаются
}
