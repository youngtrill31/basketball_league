 $("#insert-more").click(function () {
     $("#roster_management").each(function () {
         var tds = '<tr>';
         jQuery.each($('tr:last td', this), function () {
             tds += '<td>' + $(this).html() + '</td>';
         });
         tds += '</tr>';
         if ($('tbody', this).length > 0) {
             $('tbody', this).append(tds);
         } else {
             $(this).append(tds);
         }
     });
});




$(document).ready(function() {
    $("#addRow").click(function(){
        $("#playerRow").toggleClass("hiddenRow hiddenRowDisplay")
    });
});

//(function(){
//  function ontop() {
//    $("#playerRow").toggleClass("hiddenRowDisplay");
//  }
//  $(function(){
//    $("#addRow").click(ontop);
//  });
//})();