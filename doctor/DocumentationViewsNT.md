# Major Functions and Their Descriptions

## Paginator
### Location - views.py
#### Code

-       def get(self, request):
        
            self.doctors =      HealthCentreStaff.objects.filter(staff_type='DR').values()
            self.medicines = Medicine.objects.all().values()
            paginator = Paginator(self.medicines, 15) # Show 25 medicines per page
            page = request.GET.get('page')
            try:
                self.medicines = paginator.page(page)
            except PageNotAnInteger:
                self.medicines = paginator.page(1)
            except EmptyPage:
                self.medicines = paginator.page(paginator.num_pages)
            
            return render(request, self.template_name, {
                "doctors" : self.doctors,
                "medicines" : self.medicines
                })

### Used in template - index.html

-       <div class="pagination" style="padding-left:220px">
            
        {% if medicines.has_previous %}
            <button class="step-links">
                <a href="?page=1">&laquo; first</a>
            </button>
            <button>
                <a href="?page={{ medicines.previous_page_number }}">previous</a>
        {% endif %}
        </button>
        <span class="current">
            <b>Page {{ medicines.number }} of {{ medicines.paginator.num_pages }}. </b>
        </span>
            
        {% if medicines.has_next %}
            <button>
                <a href="?page={{ medicines.next_page_number }}">next</a>
            </button>
            <button>
                <a href="?page={{ medicines.paginator.num_pages }}">last &raquo;</a>
        {% endif %}
            </button>
        </div>


### Description 
It displays the medicines present in our database in the "Medicine" table in the form of pages. Each page displays 25 medicines with "previous", "next", "first" and "last" buttons at the end of the page wherever applicable. 


## Save Medicines Issued in a given prescription

### Location : views.py
### Code 

    -   def savePrescriptionMedicine(request):

            if request.method=='POST' and request.is_ajax():
                try:
                    psno = request.POST['psno']
                    mid = request.POST['mid']
                    issue = request.POST['issue']
                    if issue is "true":
                        issue = True
                    else:
                        issue = False
                    pid = MedicineIssue.objects.get(prescription_serial_no=psno, medicine_id=mid)
                    pid.issue_status = issue
                    pid.non_issue_reason = request.POST['reason']
                    pid.save()
                    return JsonResponse({'status':'Success', 'msg': 'save successfully'})
                except MedicineIssue.DoesNotExist:
                    return JsonResponse({'status':'Fail', 'msg': 'Object does not exist'})

### Used in template - pharmacist_screen.html

    -   $('.submit').click(function(e){
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

### Description
On click of the button "Save" in the template "pharmacist_screen.html" the jquery code given in the template is called. It takes the prescription serial number and one by one updates the entry of each medicine given in the prescription using the "savePrescriptionMedicine" function shown above in the MedicineIssue table using the fields "prescription_serial_no" and "medicine_id". Ajax is used because this updation needs to be done without page refresh.


## Search Function
### Location - views.py
### Code 

    - def getPatient(request):
            
        if request.method == "GET":
            search_text = request.GET['search_text']
            if search_text:
                search_text = request.GET['search_text']
                if RepresentsInt(search_text):
                    statuss = IndividualRecord.objects.filter(person_id__icontains=search_text).values('person_id','name')[:10]
                else:
                    statuss = IndividualRecord.objects.filter(name__icontains=search_text).values('person_id','name')[:10]
            else:
                statuss = []
        return render(request, 'ajax-search.html', {'statuss':statuss})

### Used in template - new_prescription.html

    - $(function(){
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
        }

        function enableReSearch(){
        $('#search-results').show();
    }

### Description
It's a live search implementation. The search function is to go through the "IndividualRecord" table in the database and find the records associated with the search string entered and display a list of ten such records in the format "person_id, person_name" at a time. The function "getPatient" renders an html file "ajax-search.html", with the entries from the database, which is appended to the div with the id "search-results". 

### Note 
Similar search is implemented for the medicine search on home screen i.e. "index.html" page. The function "getMedicinesList" is used for that in the views.py file. It displays entries similar to the search pattern from the "Medicine" table in the form "medicine_name".


## Get Details of Patient
### Location - views.py
### Code

    - def getPatientDetail(request):
            
        if request.method == "GET":
            search_text = request.GET['pid']
            if search_text:
                search_text = request.GET['pid']
                person = IndividualRecord.objects.filter(person_id=search_text).values('person_id','name','category').first()
            else:
                person = {}
        return JsonResponse({'person': person})

### Used in template - new_prescription.html

    - function getPerson(pid){
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

### Description 
Once the search for a given patient is done and the user selects a given entry from the list displayed from the search. the button calls the javascript function "getPerson(pid)" where pid is the person_id from the selected entry. This triggers an AJAX call and the function "getPatientDetail" is used to get details(person_id, name, category) of the patient from the "IndividualRecord" table.

### Note
Similar function to get the medicine details from the "Medicine" table is "getMedDetail" in the file "views.py". It searches for a medicine with the given medicine_id and returns the medicine_name, manufacturing company and quantity.

