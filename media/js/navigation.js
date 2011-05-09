$(function()
{
    $("#categories ul").addClass("closed");
    $("#categories ul li.selected").parent("ul").removeClass("closed");
    
    $("#categories span").click(function(event)
    {
        $(this).next("ul").toggleClass("closed");
    });
})