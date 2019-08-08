## new_perscription.html

```javascript
<script type="text/javascript">
            var counter = 2;
            var counter2 = 2;
            $(function() {
              $('#txtSearch').keyup(function() {
                console.log($('#txtSearch').val());
                $.ajax({
                  type: "GET",
                  url: "/getPatient/",
                  data: {
                  'search_text' : $('#txtSearch').val(),
                  'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
                  },
                  success: searchSuccess,
                  dataType: 'html'
                });
              });
            });

            function searchSuccess(data, textStatus, jqXHR)
            {
              $('#search-results').html(data);
              // console.log(data);
            }
            function enableReSearch(){
              $('#search-results').show();
            }
          var setcnt = 0;
          function searchMedicine(cnt){
            setcnt = cnt;
            $('#myMed').attr("style", "display:block;");
            var input, filter, ul, li, a, i, txtValue;
            input = document.getElementById("meds"+cnt);
            filter = input.value.toUpperCase();
            ul = document.getElementById("myMed");
            li = ul.getElementsByTagName("li");
            for (i = 0; i < li.length; i++) {
                a = li[i].getElementsByTagName("a")[0];
                txtValue = a.textContent || a.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    li[i].style.display = "block";
                    // temp = ',' + cnt + ');';
                    // $(a).attr("onclick", $(a).attr("onclick") + temp);
                    // console.log("Here");
                }else{
                    li[i].style.display = "none";
                    // console.log("There");
                }
            }
          }

          function getMedName(name){
            console.log(setcnt);
            console.log(name);
            $("#meds" + setcnt).val(name);
            $('#myMed').attr("style", "display:none;");
          }
          function getPerson(pid){
            console.log(pid);
            $.ajax({
                  type: "GET",
                  url: "/getPatientDetail/",
                  data: {
                  'pid' : pid,
                  'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
                  },
                  dataType: 'json',
                  success: function(data){
                    // console.log(data);
                    $('#search-results').hide();
                    $('#name').html(data.person.name);
                    $('#txtSearch').val(data.person.name);
                    $('#category').html(data.person.category);
                    $('#pid2').html(data.person.person_id);
                  }
                });
          }
          
          $(document).ready(function(){
            // Tests dynamic fields
              // var medList = [];
              $.ajax({
                type: "GET",
                url: "/getMedicinesPrescription/",
                data: {
                'search_text' : "med",
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
                },
                success: function(data){
                  $('#medicine').html(data);
                },
                dataType: 'html'
              });

            $("#addTestButton").click(function() {
              if(counter>10){
                alert("Only 10 textboxes allow");
                return false;
              }   
              var newTextBoxDiv = $(document.createElement('div'))
                  .attr("id", 'TextBoxTestDiv' + counter);           
              newTextBoxDiv.after().html('<label>Test #'+ counter + ' : </label>' +
                    '<input type="text" name="test' + counter + 
                    '" id="test' + counter + '" value="" > ');   
              newTextBoxDiv.appendTo("#TextBoxesTestGroup");
              counter++;
            });


            
            $("#removeTestButton").click(function () {
              if(counter==1){
                      alert("No more textbox to remove");
                      return false;
                  }
              counter--;
                  
                    $("#TextBoxTestDiv" + counter).remove();
            });
              
            $("#getTestButtonValue").click(function () {
              var msg = '';
              for(i=1; i<counter; i++){
                  msg += "\n Test #" + i + " : " + $('#test' + i).val();
              }
                    alert(msg);
            });
            // Medicine dynamic fields
            
            $("#addMedsButton").click(function () {
              if(counter2>10){
                        alert("Only 10 medicines allowed");
                        return false;
              }   
              var newTextBoxDiv = $(document.createElement('div'))
                  .attr("id", 'TextBoxMedsDiv' + counter2);           
              newTextBoxDiv.after().html('<label>Medicine #'+ counter2 + ' : </label>' +
                    '<input type="text" class="meds" name="meds' + counter2 + 
                    '" id="meds' + counter2 + '" onkeyup="searchMedicine(' + counter2 + ')" value=""> <label>&nbsp;&nbsp;&nbsp;Quantity :</label><input type="number" id="quantitytextboxmeds' + counter2 + '" style="width:35px;" min="1"> <input type="button" value="X" onclick="removeDiv(' + counter2 + ')" id="removeMedsButton' + counter2 + '" style="float:right;color:red;background:white;">');   
              newTextBoxDiv.appendTo("#TextBoxesMedsGroup");
              counter2++;
            });
              
            $("#getMedsButtonValue").click(function () {
              var msg = '';
              for(i=1; i<counter2; i++){
                  msg += "\n Medicine #" + i + " : " + $('#meds' + i).val();
              }
                    alert(msg);
            });
          });

          function removeDiv(x){
            $("#TextBoxMedsDiv" + x).remove();
          }

          function saveData(){
            var pid = $('#pid2').text();
            var name = $('#name').text();
            var docid = "DR. BANIBRATA CHAKRABORTY";
            var medlist = "";
            var medqnt = "";
            var complaint = $('#complaint').val();
            var diagnosis = $('#diagnosis').val();
            for(var i=1;i<counter2;i++){
              if (typeof($('#meds'+i).val()) != "undefined"){
                medlist += $('#meds'+i).val() + ",";
                medqnt += $('#quantitytextboxmeds'+i).val() + ",";
              }
            }
            var testList = [];
            for(var i=1;i<counter;i++){
              testList.push($('#test'+i).val());
            }
            $.ajax({
              type: "POST",
                url: "/saveNewPrescription/",
                data: {
                'personid' : pid,
                'docid' : docid,
                'medlist' : medlist,
                'medqnt' : medqnt,
                'testList' : testList,
                'complaint' : complaint,
                'diagnosis' : diagnosis,
                'name' : name,
                csrfmiddlewaretoken: '{{ csrf_token }}'
                },
                success: function(data){
                  console.log(data);
                },
                dataType: 'html'
            });
          }

          var modal = document.getElementById('myModal');
          var btn = document.getElementById("modalbtn");
          var span = document.getElementsByClassName("close")[0];
          btn.onclick = function() {
            var name = $('#name').html();
            var pid = $('#pid2').html();
            $.ajax({
              type:"GET",
              url: "/getPatientPreviousRecord/",
              data: {
                'name' : name,
                'pid' : pid,
                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val(),
              },
              dataType: 'html',
              success: function(data){
                console.log(data);
              }
            });
            // modal.style.display = "block";
          }
          span.onclick = function() {
            modal.style.display = "none";
          }

          // When the user clicks anywhere outside of the modal, close it
          // window.onclick = function(event) {
          //   if (event.target == modal) {
          //     modal.style.display = "none";
          //   }
          // }
          
        </script>
```

## layout.html

```javascript
<script>
      var d = new Date();
      var n = d.getDate();
      var m = d.getMonth();
      var months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
      var y = d.getFullYear();
      $('#date').html(n +"-" + months[m] + "-" + y);
      var t = d.toLocaleTimeString();
      $('#time').html(t);
    </script>
```

## patient_history.html

```javascript
<script>
      function enableReSearch(){
        $('#search-results').show();
      }

        $('#txtSearch').keyup(function(e) {
        console.log($('#txtSearch').val());
          $.ajax({
            type: "GET",
            url: "/getMedicineList/",
            data: {
            'search_text' : $('#txtSearch').val(),
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            success: searchSuccess,
            dataType: 'html'
          });
        });

      function searchSuccess(data, textStatus, jqXHR)
      {
        $('#search-results').html(data);
        console.log(data);
      }
      function getMedDetail(mid){
      console.log(mid);
      $.ajax({
            type: "GET",
            url: "/getMedDetail/",
            data: {
            'mid' : mid,
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            dataType: 'json',
            // contentType: false,
            success: function(data){
              console.log(data);
              $('#search-results').hide();
              $('#med_name').html(data.med_details.medicine_name);
              $('#med_category').html(data.med_details.category);
              $('#med_quantity').html(data.med_details.quantity);
              $('#med_manufacturer').html(data.med_details.manufacturing_company);
              $('#med_details').show();
            }
        });
      }

      $(document).ready(function(){
        var pid = 9;
      });
      </script>
```

## pharmacist_screen.html

```javascript
        <script>

                function print_presription(buttonObject){
                  pres_id = buttonObject.value;
                  // alert(pres_id);
                  var mywindow = window.open('', 'my div', 'height=400,width=600');
                  mywindow.document.write('<html><head><title>my div</title>');
                  mywindow.document.write('<link rel="stylesheet" href="http://www.dynamicdrive.com/ddincludes/mainstyle.css" type="text/css" />');
                  mywindow.document.write('</head><body >');
                  mywindow.document.write("THIS IS THE PRINT STATEMENT!");
                  mywindow.document.write('</body></html>');

                  mywindow.print();
                  //  mywindow.close();

                  // return true;
                }
                var temp = document.getElementsByClassName("med");
                var psno = "";
                for (var i = 0; i < temp.length; i++){
                    psno += temp[i].value.toString() + ",";
                }
                $.ajax({
                  url: '/getMedicines/',
                  data: {
                    'psno': psno,
                    csrfmiddlewaretoken: '{{ csrf_token }}'
                  },
                  type: "POST", 
                  dataType: 'json',
                  success: function (data) {
                    var i;
                    for (var key in data) {
                      for(var i=0;i<data[key].length;i++){
                        // console.log(data[key][i][0]['prescription_serial_no_id']);
                        var add1 = "";
                        var temp = "#" + data[key][i][0]['prescription_serial_no_id'];
                        for(var j=0;j<data[key][i].length;j++){
                          var str = "<tr><td>" + data[key][i][j]['medicine_name'] + "</td><td>" + data[key][i][j]['medicine_quantity'] + "</td><td><input type=" + "checkbox" + " id=" + data[key][i][j]['medicine_id_id']  + "></label>" + "</td><td><input type=" + "text" + " id=dos" + data[key][i][j]['medicine_id_id'] + "></td><td><input type=" + "text" + " id=res" + data[key][i][j]['medicine_id_id'] + "></td></tr>"
                          $(temp).append(str);
                          add1 += data[key][i][j]['medicine_id_id'] + "/";
                        }
                        var xy = "#presmed" + data[key][i][0]['prescription_serial_no_id'];
                        $(xy).val(add1);
                        // console.log(add1);
                      }
                    }
                  }
                });

                $('.submit').click(function(e){
                  var pid = this.value;
                  var xy = "#presmed" + pid;
                  var vals = $(xy).val().split("/");
                  for(var i=0;i<vals.length;i++){
                    if(vals[i] != ""){
                      var temp = "#res" + vals[i];
                      var reason = $(temp).val();
                      temp = "#dos" + vals[i];
                      var dosage = $(temp).val();
                      var issue = $("#"+vals[i]).prop('checked');
                      console.log(issue);
                      $.ajax({
                        url: '/savePrescriptionMedicine/',
                        data: {
                          'psno': pid,
                          'mid' : vals[i],
                          'issue': issue,
                          'reason' : reason,
                          csrfmiddlewaretoken: '{{ csrf_token }}'
                        },
                        type: "POST", 
                        dataType: 'json',
                        success : function(data){
                          console.log(data);
                        }
                      });                      
                      console.log();
                    }
                  }
                });
            </script>
```

## stman_screen.html

```javascript
<script type="text/javascript">

    $(function() {
      $('#txtSearch').keyup(function(e) {
        console.log($('#txtSearch').val());
        $.ajax({
          type: "GET",
          url: "/getMedicineList/",
          data: {
          'search_text' : $('#txtSearch').val(),
          'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
          },
          success: searchSuccess,
          dataType: 'html'
        });
      });
    });

    function searchSuccess(data, textStatus, jqXHR)
    {
      $('#search-results').html(data);
      // console.log(data);
    }
    
    function getMedDetail(mid){
      // console.log(mid);
      $.ajax({
            type: "GET",
            url: "/getMedDetail/",
            data: {
            'mid' : mid,
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
            },
            dataType: 'json',
            // contentType: false,
            success: function(data){
              console.log(data);
              $('#search-results').hide();
              $('#med_name').html(data.med_details.medicine_name);
              $('#med_category').html(data.med_details.category);
              $('#med_quantity').html(data.med_details.quantity);
              $('#med_manufacturer').html(data.med_details.manufacturing_company);
              $('#med_details').show();
            }
      });
    }
    function openInNewTab(url) {
      var win = window.open(url, '_blank');
      win.focus();
    }
    function enableReSearch(){
      $('#search-results').show();
    }
</script>
```