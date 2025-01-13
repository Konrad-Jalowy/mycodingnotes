function log(strings, ...values) {
    const timestamp = new Date().toISOString();
    const message = strings.reduce((acc, str, idx) => acc + str + (values[idx] || ''), '');
    console.log(`[${timestamp}] ${message}`);
}

log`Server started on port ${3000}`;
// Wydrukuje np.:
// [2025-01-13T14:30:00.000Z] Server started on port 3000
