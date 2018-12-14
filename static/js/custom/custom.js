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


(function(){
  function ontop() {
    $("#playerRow").toggleClass("hiddenRowDisplay");
  }
  $(function(){
    $("#addRow").click(ontop);
  });
})();


/* Handle removing player from team roster
------------------------------------------------ */
$(document).ready(function(){
var clicked;
$("#remove-player").click(function() {
    clicked = $(this).attr("data-id");
$.ajax({
    type : 'POST',
    dataType: 'json',
    url : '/remove_player',
    contentType: 'application/json;charset=UTF-8',
    data : JSON.stringify({'data': clicked})
});
 });
});