
    jQuery('#frmSubmit').on('submit',function(e){
      e.preventDefault();
      jQuery('#msg').html('Please wait...');
      jQuery('#btnSubmit').attr('disabled',true);
      jQuery.ajax({
          url:'https://script.google.com/macros/s/AKfycbyCmU0Cw2jSaGOdzS7OvzafsuaTLd2LfK-rfN9-IUWlf691rxltbpZtGgZxRIYgINEfIA/exec',
          type:'post',
          data:jQuery('#frmSubmit').serialize(),
          success:function(result){
              jQuery('#frmSubmit')[0].reset();
              jQuery('#msg').html('Submitted, Thank You');
              jQuery('#btnSubmit').attr('disabled',false);
            //window.location.href='';
          }
      });
    });
    