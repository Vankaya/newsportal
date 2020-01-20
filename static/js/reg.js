

        $(document).ready(function () {

          let valid = true;
          let regExp1=/^[a-zA-Z][a-zA-Z0-9_\-]{5,16}$/;
          let regExp2=^(?=.*[A-Z])(?=.*[0-9])(?=.*[a-z])[A-Za-z0-9_\-]{8,16}$/;
        //   let regExp3=//;
          $('#login').blur(function(){
            let login = $(this).val();
            if (regExp1.test(login)){
            //рроверка правильности логина
            $.ajax({
                url:"/account/ajax_reg",
                data:"login=" + login,
                success:function(result){
                    if(result.mess == ''занят){
                     $('#login_img').attr('src', '../../static/img/cross.png')
                    }
                else{
                $('#login_img').attr('src', '../../static/img/ok.png')
                }
                }
            });
                $('#login_img').attr('src', '../../static/img/ok.png')
                <!--//$('#login_err').text('ok');//-->
            } else{
                $(this).css('border-color','red')
                $('#login_err').text('логин должен состоять из букв ил цифр (6-16)+()_\-');
            }


          });
          $('#login').focus(function(){
            $(this).css('border-color','silver')
             $('#login_err').text('');
          });

        });


    