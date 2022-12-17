$.get('https://swapi-api.hbtn.io/api/films/?format=json', (films) => {
    for (const film of films.results) {
        $('ul#list_movies').append('<li>' + film.title + '</li>');
    }
});
