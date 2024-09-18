document.addEventListener('DOMContentLoaded', () => {
    const jobGrid = document.getElementById('job-grid');
    const jobCount = document.getElementById('job-count');

    // Fetch job data from the Flask API endpoint
    fetch('/api/joblisting')
        .then(response => response.json())
        .then(data => {
            // Update job count
            jobCount.textContent = data.length;

            // Generate job cards dynamically
            data.forEach(job => {
                const jobCard = document.createElement('div');
                jobCard.className = 'job-card';

                jobCard.innerHTML = `
                    <div class="job-card-header">
                        <span>${job.date_posted}</span>
                        <span>+</span>
                    </div>
                    <div class="company-logo"></div>
                    <div class="job-title">${job.job_name}</div>
                    <div class="job-company">${job.company}</div>
                    <div class="job-description">${job.job_description}</div>
                    <button class="apply-btn">Apply</button>
                `;

                jobGrid.appendChild(jobCard);
            });
        })
        .catch(error => {
            console.error('Error fetching job data:', error);
        });
});
