function showUploadStatus(status) {
  const uploadStatus = document.getElementById('upload-status')
  uploadStatus.innerText = status
}

showUploadStatus('Standby')

const dataUriInput = document.getElementById('data-uri-input')
const titleInput = document.getElementById('title-input')
const uploadBtn = document.getElementById('upload-btn')
const inspectBtn = document.getElementById('inspect-btn')

uploadBtn.addEventListener('click', async () => {
  showUploadStatus('Uploading...')
  try {
    const response = await fetch('/api/import', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        uri: dataUriInput.value,
        title: titleInput.value,
      }),
    }).then(resp => resp.json())
    showUploadStatus(`Upload done, result was: ${response.result?.state}`)
  } catch (e) {
    showUploadStatus(`Upload failed: ${e.message}`)
  }
})

inspectBtn.addEventListener('click', async () => {
  try {
    const uri = dataUriInput.value
    const response = await fetch(`/api/inspect?source=${uri}`).then(resp => resp.json())
    showUploadStatus(`Inspect results:  
${response}`)
  } catch (e) {
    showUploadStatus(`Inspect failed: ${e.message}`)
  }
})
