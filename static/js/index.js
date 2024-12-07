ymaps.ready(init);

function init() {
    // Создание карты.
    const map = new ymaps.Map('map', {
        center: [45.03547, 38.975313], // Центр Краснодара.
        zoom: 12,
        controls: ['zoomControl', 'fullscreenControl']
    });

    const points = JSON.parse(document.getElementById('problem_points').textContent);
    let problems = document.getElementById('problems');

    // Добавляем метки на карту.
    points.forEach(point => {
        const placemark = new ymaps.Placemark(
            point.coords,
            { hintContent: `Нажмите, чтобы открыть: ${point.name}` },
            { preset: 'islands#blueIcon' }
        );

        map.geoObjects.add(placemark);

        // При клике переходим на страницу с выбранной картой.
        placemark.events.add('click', () => {
            window.location.href = point.link;
        });

        let problem_item = document.createElement('div');
        problem_item.innerHTML = `<a href="/problem/${point.coords}/" target="_blank">${point.name}</a>`
        problems.appendChild(problem_item);
        
    });
}
