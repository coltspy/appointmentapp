function getAvailableTimes() {
    var userInput = document.getElementById('user-input').value;
    fetch(`http://localhost:5000/available_times?date=${userInput}`)
        .then(response => response.json())
        .then(data => {
            var chatWindow = document.getElementById('chat-window');
            chatWindow.innerHTML = '';  // Clear previous content
            if (data.success) {
                chatWindow.innerHTML += `<p>Available times:</p>`;
                data.available_times.forEach((time, index) => {
                    // Make each time clickable
                    chatWindow.innerHTML += `<p class="time-slot" onclick="bookTimeSlot('${userInput}', ${index})">${time}</p>`;
                });
            } else {
                chatWindow.innerHTML += `<p>${data.message}</p>`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function bookTimeSlot(date, timeSlotIndex) {
    fetch('http://localhost:5000/book_appointment', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ appointment_date: date, time_slot_index: timeSlotIndex })
    })
    .then(response => response.json())
    .then(data => {
        var chatWindow = document.getElementById('chat-window');
        if (data.success) {
            chatWindow.innerHTML += `<p>Booked appointment for ${data.booked_time}</p>`;
        } else {
            chatWindow.innerHTML += `<p>${data.message}</p>`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
