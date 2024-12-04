// Helper function to format institution types
function affi_type(str) {
    const typeMap = {
        "department": "Department",
        "institution": "Institution",
        "laboratory": "Laboratory",
    };
    return typeMap[str] || str;
}

// Process fetched data and update the UI
function processFetchedData(data) {
    function chunkArray(array, chunkSize) {
        const chunks = [];
        for (let i = 0; i < array.length; i += chunkSize) {
            chunks.push(array.slice(i, i + chunkSize));
        }
        return chunks;
    }

    const dataChunks = chunkArray(data, 50);

    function processChunk(chunkIndex) {
        if (chunkIndex >= dataChunks.length) {
            reorderSoftwareMentions();
            return;
        }

        const chunk = dataChunks[chunkIndex];

        chunk.forEach(software_name => {
            const software = software_name ? software_name
                .replace(/\s/g, '')  // Remove all whitespace
                .replace(/\./g, '')  // Remove all periods
                .replace(/@/g, '')  // Escape '@'
                .replace(/\(/g, '')  // Escape '('
                .replace(/\)/g, '')  // Escape ')'
                .replace(/\*/g, '')  // Escape '*'
                .replace(/[0-9]/g, '')  // Escape [0,9]
                .replace(/\//g, '')  // Escape \
                .replace(/\+/g, '')  // Escape '+'
                .replace(/\'/g, '')  // Escape '
                .replace(/\"/g, '')  // Escape "
                : '';

            document.querySelectorAll(`#${software}.mention_doc_id`).forEach(element => {
                var dropdownBtn = element.querySelector('.dropbtn');
                dropdownBtn.style.color = 'red';
                element.parentNode.prepend(element);
            });
        });

        processChunk(chunkIndex + 1);
    }

    processChunk(0);
}

// Reorder software mentions based on their color and number
function reorderSoftwareMentions() {
    const listSoftwareContainers = document.querySelectorAll(".list-software");

    listSoftwareContainers.forEach(container => {
        const softwareDivs = Array.from(container.getElementsByClassName("mention_doc_id"));

        const redSoftware = [];
        const otherSoftware = [];

        softwareDivs.forEach(div => {
            const isRed = window.getComputedStyle(div.querySelector('button')).color === 'rgb(255, 0, 0)';
            if (isRed) {
                redSoftware.push(div);
            } else {
                otherSoftware.push(div);
            }
        });

        const sortByNumberDesc = (a, b) => {
            const aNumber = parseInt(a.querySelector(".dropbtn").getAttribute("number"));
            const bNumber = parseInt(b.querySelector(".dropbtn").getAttribute("number"));
            return bNumber - aNumber;
        };

        redSoftware.sort(sortByNumberDesc);
        otherSoftware.sort(sortByNumberDesc);

        redSoftware.forEach(div => container.appendChild(div));
        otherSoftware.forEach(div => container.appendChild(div));
    });
}
