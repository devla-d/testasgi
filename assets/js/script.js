(function($) {
    "use strict"; // Start of use strict

    $(document).ready(function() {
        NProgress.start();
        setTimeout(function() {
            NProgress.done();
            $('.fade').removeClass('out');
        }, 1500);

        /*$(document).on('page:fetch', function() {
            NProgress.start();
        });
        $(document).on('page:change', function() {
            NProgress.done();
        });
        $(document).on('page:restore', function() {
            NProgress.remove();
        });*/
    })


    $("#show-contact-information").on("click", function() {
        console.log(user.username)

    });



    $('.back-arrow').on('click', function() {
        window.history.back()
    })

    $('.chatroom').on('click', function() {
        var roomid = $(this).attr('id');
        get_chatroom(`room${roomid}`);
    })


    function get_chatroom(room) {
        console.log(room)
        window.location.href = '/chatroom/' + room
    }


    var user = {
        'username': $("#current-username").text(),
        'img': $("#current-img").attr('src'),
        'status': $('#current-status').text(),
        'userid': $("#current-username").data('userid')
    }











})(jQuery); // End of use strict