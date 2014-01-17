/**
 * Created with PyCharm.
 * User: Gin
 * Date: 14-1-17
 * Time: 下午5:47
 * To change this template use File | Settings | File Templates.
 */
$(document).ready(function () {
    $('.todo_item').click(function () {
        if ($(this).children('input').length == 0) {
            //Create the HTML to insert into the div. Escape any " characters
            var inputbox = "<input type='text' class='inputbox' value=\"" + $(this).text() + "\">";
            //Insert the HTML into the div
            $(this).html(inputbox);
            //Immediately give the input box focus. The user
            //will be expecting to immediately type in the input box,
            //and we need to give them that ability
            $("input.inputbox").focus();
            //Once the input box loses focus, we need to replace the
            //input box with the current text inside of it.
            $("input.inputbox").blur(function () {
                var value = $(this).val();
                $(".todo_item").text(value);
            });
        }
    });
});