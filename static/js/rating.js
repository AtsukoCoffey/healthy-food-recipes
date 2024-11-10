const recipe_id = recipe.id
const rate = (rating, recipe_id) => {
    fetch(`/recipes/rate/${recipe_id}/${rating}/`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(rest => {
        window.location.reload();
    })
}