document.addEventListener('DOMContentLoaded', function (event) {

    $('#table').DataTable({
        "searching": false,
        "order": [["2", "asc"]],
        "aLengthMenu": [2, 5, 10, 25],
        "iDisplayLength": 2,
        "pagingType": "numbers",
        "info":     false,
    });

    var element = document.getElementById("table_wrapper");
    element.addEventListener('click', addIcon);
    addIcon();
})

function addIcon() {
    var elements = $("td[scope$='row']");
    for (let index = 0; index < elements.length; index++) {
        let symbol = elements[index].innerText.toLowerCase().replace(/\s+/g, '');
        imagesource = `/static/images/symbols/${symbol}.png`;
        let el = elements[index].children;
        el[0].src = imagesource;
    }
}