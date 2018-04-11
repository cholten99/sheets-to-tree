$( document ).ready(function() {

  some_json = '{ "ID": 1, "Bill": "S Preston", "Ted": "Theadore Logan" }';

  $.post( "page-list.py", { action: "write", json: some_json })
    .done(function( data ) {

      $.get("page-list.py", { action: "read" }, function(data, status) {
        alert("Foobar!");
        alert(data);
      });

  });

});
