const width = document.getElementById("width").value
const height = document.getElementById("height").value
const widthInput = document.getElementById("width")
const heightInput = document.getElementById("height")
const xScaleInput = document.getElementById("xScale")
const yScaleInput = document.getElementById("yScale")
const checkBox = document.getElementById("lockAspectRatio")

widthInput.addEventListener('input', (event) => {
    let changedWidth = event.target.value
    let changedXScale = Math.round((changedWidth / width) * 100)
    xScaleInput.value = changedXScale

    if(checkBox.checked)
    {
        widthChangePer = (changedWidth / width) * 100
        heightInput.value = Math.round((height / 100) * widthChangePer)

        yScaleInput.value = changedXScale
    }
})

heightInput.addEventListener('input', (event) => {
    let changedHeight = event.target.value
    let changedYScale = Math.round((changedHeight / height) * 100)
    yScaleInput.value = changedYScale

    if(checkBox.checked)
    {
        heightChangePer = (changedHeight / height) * 100
        widthInput.value = Math.round((width / 100) * heightChangePer)

        xScaleInput.value = changedYScale
    }
})

xScaleInput.addEventListener('input', (event) => {
    let changedScale = event.target.value
    let changedWidthInput = Math.round((width / 100) * changedScale)
    widthInput.value = changedWidthInput

    if(checkBox.checked)
    {
        heightInput.value = Math.round((height / 100) * changedScale)
        yScaleInput.value = changedScale
    }
})

yScaleInput.addEventListener('input', (event) => {
    let changedScale = event.target.value
    let changedHeightInput = Math.round((height / 100) * changedScale) 
    heightInput.value = changedHeightInput

    if(checkBox.checked)
    {
        widthInput.value = Math.round((width / 100) * changedScale)
        xScaleInput.value = changedScale
    }

})

function validateForm()
{
    let form = document.forms["resizeForm"]
    let width = parseInt(form["width"].value)
    let height = parseInt(form["height"].value)

    if(width < 16)
    {
        document.getElementById("modalHead").textContent = "This Size Is Too Small"
        document.getElementById("modalMsg").textContent = "Sorry, we don’t support resizing to less than 16px."
        return showModal()
    }
    else if(width > 5000)
    {
        document.getElementById("modalHead").textContent = "This Size Is Too Big"
        document.getElementById("modalMsg").textContent = "Sorry, we don’t support resizing to more than 5000px."
        return showModal()
    }
    else if(height < 16)
    {
        document.getElementById("modalHead").textContent = "This Size Is Too Small"
        document.getElementById("modalMsg").textContent = "Sorry, we don’t support resizing to less than 16px."
        return showModal()
    }
    else if(height > 5000)
    {
        document.getElementById("modalHead").textContent = "This Size Is Too Big"
        document.getElementById("modalMsg").textContent = "Sorry, we don’t support resizing to more than 5000px."
        return showModal()
    }

}

function closeModal() {
    document.getElementById("errorModal").classList.add("hide")
}

function showModal() {
    document.getElementById("errorModal").classList.remove("hide")
    return false
}