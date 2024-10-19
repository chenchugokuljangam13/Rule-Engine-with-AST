document.getElementById('rule-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const ruleString = document.getElementById('rule_string').value;
    const dataString = document.getElementById('data').value;

    // Parse the JSON data input
    let data;
    try {
        data = JSON.parse(dataString);
    } catch (e) {
        alert('Invalid JSON data format');
        return;
    }

    // Make an API call to evaluate the rule
    fetch('/api/evaluate/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ rule_string: ruleString, data: data })
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('result').innerText = 'Result: ' + result.result;
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error evaluating the rule');
    });
});
