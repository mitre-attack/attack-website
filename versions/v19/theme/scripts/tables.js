const tables = Array.from(document.getElementsByTagName('table'));

tables.forEach(table => {
    table.className = 'table table-striped';
});