document.addEventListener('DOMContentLoaded', function () {
    var addmedicine = document.getElementById("b1");
    var issuebtn = document.getElementById("b2");
    var checkrecord = document.getElementById("b3");
    var issuedmedicine = document.getElementById("b5");
    var profile = document.getElementById("b6");

    var registerUrl = addmedicine.getAttribute("data-url");
    var registerUrl2 = checkrecord.getAttribute("data-url");
    var registerUrl4 = issuebtn.getAttribute("data-url");
    var registerUrl5 = issuedmedicine.getAttribute("data-url");
    var registerUrl6 = profile.getAttribute("data-url");

    addmedicine.addEventListener("click", function () {
        window.location.href = registerUrl;
    });

    profile.addEventListener("click", function () {
        window.location.href = registerUrl6;
    });


    checkrecord.addEventListener("click", function () {
        window.location.href = registerUrl2;
    });

    issuebtn.addEventListener("click", function () {
        window.location.href = registerUrl4;
    });

    issuedmedicine.addEventListener("click", function () {
        window.location.href = registerUrl5;
    });
});

var backbtn = document.getElementById("b4");
var registerUrl3 = backbtn.getAttribute("data-url");
backbtn.addEventListener("click", function () {
    window.location.href = registerUrl3;
});


const quantity = document.getElementById('quantity');

quantity.addEventListener('input', function () {
    this.value = this.value.replace(/[^0-9]/g, '');
});

const quantityissue = document.getElementById('quantityissue');

quantityissue.addEventListener('input', function () {
    this.value = this.value.replace(/[^0-9]/g, '');
});

(function ($) {
    'use strict';
    /*==================================================================
        [ Daterangepicker ]*/
    try {
        $('.js-datepicker').daterangepicker({
            "singleDatePicker": true,
            "showDropdowns": true,
            "autoUpdateInput": false,
            locale: {
                format: 'DD/MM/YYYY'
            },
        });

        var myCalendar = $('.js-datepicker');
        var isClick = 0;

        $(window).on('click', function () {
            isClick = 0;
        });

        $(myCalendar).on('apply.daterangepicker', function (ev, picker) {
            isClick = 0;
            $(this).val(picker.startDate.format('DD/MM/YYYY'));

        });

        $('.js-btn-calendar').on('click', function (e) {
            e.stopPropagation();

            if (isClick === 1) isClick = 0;
            else if (isClick === 0) isClick = 1;

            if (isClick === 1) {
                myCalendar.focus();
            }
        });

        $(myCalendar).on('click', function (e) {
            e.stopPropagation();
            isClick = 1;
        });

        $('.daterangepicker').on('click', function (e) {
            e.stopPropagation();
        });


    } catch (er) { console.log(er); }
    /*[ Select 2 Config ]
        ===========================================================*/

    try {
        var selectSimple = $('.js-select-simple');

        selectSimple.each(function () {
            var that = $(this);
            var selectBox = that.find('select');
            var selectDropdown = that.find('.select-dropdown');
            selectBox.select2({
                dropdownParent: selectDropdown
            });
        });

    } catch (err) {
        console.log(err);
    }


})(jQuery);
