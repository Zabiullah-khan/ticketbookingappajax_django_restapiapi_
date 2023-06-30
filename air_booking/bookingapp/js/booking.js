
	var seat_selection = document.querySelector('#seatselection')
	var loc_a = document.querySelector('#loc-a')
	var loc_b = document.querySelector('#loc-b')
	var bor_time = document.querySelector('#bor-time')
	var dep_time = document.querySelector('#dep-time')
	var name = document.querySelector('#name')
	var gender = document.querySelector('#gender')
	var number = document.querySelector('#number')
	var identity = document.querySelector('#identity')


send_data.addEventListener('click',function(event){
	var seat_selection = document.querySelector('#seatselection')
	var loc_a = document.querySelector('#loc-a')
	var loc_b = document.querySelector('#loc-b')
	var bor_time = document.querySelector('#bor-time')
	var dep_time = document.querySelector('#dep-time')
	var name = document.querySelector('#name')
	var gender = document.querySelector('#gender')
	var number = document.querySelector('#number')
	var identity = document.querySelector('#identity')
	//send_data_submit_button
	var send_data = document.querySelector('#send_data')
	event.preventDefault();
	function post_data() {
		var xhrp = new XMLHttpRequest()
		xhrp.open('POST','http://127.0.0.1:8000/poster/postdata',true)
		xhrp.setRequestHeader("Content-Type", "application/json");

		console.log(seat_selection.value)
	var data = JSON.stringify({
		'name':String(name.value),
		'age':Number(age.value),
		'sex':String(gender.value),
		'number':String(number.value),
		'boarding':String(loc_a.value),
		'depature':String(loc_b.value),
		'seat_no':String(seat_selection.value),
		'adaar':Number(identity.value)

	})



	xhrp.onreadystatechange = () => {

			if(xhrp.readyState == XMLHttpRequest.DONE && xhrp.status == 200) {
				console.log(xhrp.responseText)
			}

		}
	xhrp.send(data)
	}post_data()
});

//get_data_ajax
function get_data(){
	
	var xhr = new XMLHttpRequest()

	xhr.open('GET','http://127.0.0.1:8000/clients/details',true)

	xhr.onreadystatechange = function() {
		if(xhr.readyState === XMLHttpRequest.DONE) {
			if(xhr.status === 200) {
				console.log('connection success')
				var data = JSON.parse(xhr.responseText)
				let num = data.seater
				let flight_loc = data.locs.loc
				console.log(num)

				if(flight_loc == 'delhi'){
					var loc_opt_a = document.createElement('option')
					var loc_opt_b = document.createElement('option')

					var bortime = document.createElement('option')
					var deptime = document.createElement('option')

					bortime.textContent='01:00PM'
					deptime.textContent='03:00PM'
					bor_time.appendChild(bortime)
					dep_time.appendChild(deptime)

					loc_opt_a.textContent='delhi'
					loc_opt_b.textContent='chennai'
					loc_a.appendChild(loc_opt_a)
					loc_b.appendChild(loc_opt_b)
				}

				else{
					var loc_opt_a = document.createElement('option')
					var loc_opt_b = document.createElement('option')

					var bortime = document.createElement('option')
					var deptime = document.createElement('option')

					bortime.textContent='10:00AM'
					deptime.textContent='12:00PM'
					bor_time.appendChild(bortime)
					dep_time.appendChild(deptime)

					loc_opt_a.textContent='chennai'
					loc_opt_b.textContent='delhi'
					loc_a.appendChild(loc_opt_a)
					loc_b.appendChild(loc_opt_b)
				}
				for(i in num){
					var opt = document.createElement('option')
					opt.textContent = num[i]
					seat_selection.appendChild(opt)
				}
				
			}
		}

		else {
			console.log('connection error')
		}
	}

	xhr.send()
}get_data()