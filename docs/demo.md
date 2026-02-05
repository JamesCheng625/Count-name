# 🎮 Online Demo

You can try the counting logic right here in your browser!

<div style="border: 1px solid #ccc; padding: 20px; border-radius: 8px; background-color: #f9f9f9;">
    <h3>Try it out</h3>
    <p>Enter names below (one per line):</p>
    <textarea id="demoInput" rows="10" style="width: 100%; border: 1px solid #ddd; padding: 10px;" placeholder="Alice&#10;Bob&#10;Alice&#10;Charlie"></textarea>
    <br><br>
    <button onclick="countNames()" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Count Names</button>
    <div id="demoResult" style="margin-top: 20px; white-space: pre-wrap; display: none; background: white; padding: 15px; border: 1px solid #eee;"></div>
</div>

<script>
function countNames() {
    const input = document.getElementById('demoInput').value;
    const lines = input.split('\n').map(line => line.trim()).filter(line => line && line !== '"');
    
    const totalNames = lines.length;
    const nameCount = {};
    
    lines.forEach(name => {
        nameCount[name] = (nameCount[name] || 0) + 1;
    });
    
    const uniqueNamesCount = Object.keys(nameCount).length;
    const repeatedNames = Object.entries(nameCount)
        .filter(([name, count]) => count > 1)
        .map(([name, count]) => `${name}: ${count} times`);
        
    const sortedUnique = Object.keys(nameCount).sort();
    
    let report = `<strong>Total Names:</strong> ${totalNames}\n`;
    report += `<strong>Unique Names:</strong> ${uniqueNamesCount}\n\n`;
    
    if (repeatedNames.length > 0) {
        report += `<strong>Repeated Names:</strong>\n${repeatedNames.join('\n')}\n`;
    } else {
        report += `<strong>No repeated names found.</strong>\n`;
    }
    
    report += `\n<strong>Sorted Unique List:</strong>\n${sortedUnique.join('\n')}`;
    
    const resultDiv = document.getElementById('demoResult');
    resultDiv.innerHTML = report;
    resultDiv.style.display = 'block';
}
</script>
