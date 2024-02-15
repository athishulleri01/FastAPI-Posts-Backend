   
    
 # students = {
#     1:{
#         "name":"nandu",
#         "age":22
#     },
#     2:{
#         "name":"athish",
#         "age":23
#     },
# }   
    
    # @app.get("/get-student/{student_id}")
# def get_student(student_id:int = Path(..., description="The ID of the student you want to view")): 
#     return students[student_id]    

# @app.get("/get-by-name")
# def get_by_name(*,name:Optional[str] = None,test:int):
#     for student_id in students:
#         if students[student_id]['name']==name:
#             return students[student_id]
#         return{
#             "status":"invalid student name"
#         }  
         
 # post request