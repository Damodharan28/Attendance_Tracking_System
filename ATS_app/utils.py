# import matplotlib.pyplot as plt
# import base64
# from io import BytesIO

# def get_graph():
#     buffer = BytesIO()
#     plt.savefig(buffer, format='png')
#     buffer.seek(0)
#     image_png = buffer.getvalue()
#     graph = base64.b64encode(image_png)
#     graph = graph.decode('utf-8')
#     buffer.close()
#     return graph

# def get_plot(x,y):

#     graph = get_graph()
#     return graph


#     if request.method == 'POST':
#         start_date_str = request.POST.get('start_date')
#         end_date_str = request.POST.get('end_date')

#         start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

#         # Get all students
#         students = ATTENDANCE_DATA.objects.values('student_id', 'firstname', 'lastname').distinct()

#         # Prepare data for the plot
#         student_data = {}
#         for student in students:
#             student_name = f"{student['FIRST_NAME']} {student['LAST_NAME']}"
#             student_data[student_name] = {'dates': [], 'total_hours_present': []}
#             for date in ATTENDANCE_DATA.objects.filter(date__range=[start_date, end_date]).values_list('date', flat=True).distinct():
#                 total_hours_present = sum([
#                     F(f'HOUR{i}').eq('PRESENT') for i in range(1, 9)
#                 ])
#                 attendance = ATTENDANCE_DATA.objects.filter(STUDENT_ID=student['student_id'], DATE=date).aggregate(
#                     total_hours_present=total_hours_present
#                 )
#                 total_hours = attendance.get('total_hours_present', 0)
#                 student_data[student_name]['dates'].append(date)
#                 student_data[student_name]['total_hours_present'].append(total_hours)
            