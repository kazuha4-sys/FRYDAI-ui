async function loadDiskUsage() {
    const response = await fetch('/api/disk_usage');
    const data = await response.json();

    data.forEach((disk, index) => {
        const canvas = document.createElement('canvas');
        canvas.id = `diskChart-${index}`;
        document.getElementById('disk-usage').appendChild(canvas);

        new Chart(canvas, {
            type: 'doughnut',
            data: {
                labels: ['Usado', 'Livre'],
                datasets: [{
                    data: [disk.used, disk.free],
                    backgroundColor: ['#4CAF50', '#f44336'],
                    hoverOffset: 4
                }]
            },
            options: {
                plugins: {
                    title: {
                        display: true,
                        text: `${disk.device} - ${disk.mountpoint}`
                    }
                }
            }
        });
    });
}

async function loadFiles() {
    const dirPath = document.getElementById('directory-path').value;
    const response = await fetch(`/api/files/${encodeURIComponent(dirPath)}`);
    const data = await response.json();

    const fileList = document.getElementById('file-list');
    fileList.innerHTML = '';

    if (data.error) {
        fileList.innerHTML = `<p>${data.error}</p>`;
    } else {
        data.forEach(file => {
            const fileElement = document.createElement('div');
            fileElement.textContent = `${file.name} - ${file.size} bytes`;
            fileList.appendChild(fileElement);
        });
    }
}

window.onload = loadDiskUsage;
