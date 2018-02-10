var item = new Item({
    completed: true
});

item.save().then((doc) => {
    console.log('Saved item', doc);
}, (err) => {
    console.log('Unable to save item', err);
});