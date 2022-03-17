function filterTables() {
    $('#tableFilter > option').each( function() { 
        if (this.selected) {
            var id = '.' + this.value;
            $(id).show();
        }
        else {
            var id = '.' + this.value;
            $(id).hide();
        }
    });
}