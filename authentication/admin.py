from django.contrib import admin, messages
from .models import TblStudents, Classroom, AttendanceSession, Attendance
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Group

class TblStudentsInline(admin.TabularInline):
    model = TblStudents.classrooms.through
    extra = 1

class AttendanceInline(admin.TabularInline):
    model = Attendance
    extra = 1
    raw_id_fields = ('session', 'student')

class UserAdmin(BaseUserAdmin):
    actions = ['add_to_students_group']
    change_list_template = "user/button_form.html"

    def changelist_view(self, request, extra_context=None):
        if '_make-unique' in request.POST:
            self.make_users_unique(request)
        return super().changelist_view(request, extra_context)

    def make_users_unique(self, request):
        # Thêm logic của bạn ở đây
        self.message_user(request, "Make Unique button clicked!", messages.SUCCESS)

    def add_to_students_group(self, request, queryset):
        try:
            students_group = Group.objects.get(name='students')
        except Group.DoesNotExist:
            self.message_user(request, "Group 'students' does not exist.", messages.ERROR)
            return

        for user in queryset:
            user.groups.add(students_group)
        self.message_user(request, "Selected users have been added to the 'students' group.", messages.SUCCESS)
    add_to_students_group.short_description = "Add selected users to the 'students' group"

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(TblStudents)
class TblStudentsAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'email', 'phone', 'date_birth', 'iCap', 'display_classrooms')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('date_birth', 'classrooms', 'iCap')
    exclude = ('password',)

    def display_classrooms(self, obj):
        return ", ".join([classroom.class_name for classroom in obj.classrooms.all()])
    display_classrooms.short_description = 'Classrooms'

    readonly_fields = ('student_id',)
    filter_horizontal = ('classrooms',)

    actions = ['add_to_classrooms']

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            raw_password = form.cleaned_data.get('password')
            if raw_password and not obj.pk:
                obj.set_password(raw_password)
        super().save_model(request, obj, form, change)

    def add_to_classrooms(self, request, queryset):
        selected_classrooms = request.POST.getlist('_selected_action')
        if not selected_classrooms:
            self.message_user(request, "No classrooms selected", messages.WARNING)
            return
        classrooms = Classroom.objects.filter(pk__in=selected_classrooms)
        for student in queryset:
            for classroom in classrooms:
                student.classrooms.add(classroom)
        self.message_user(request, f"Selected students have been added to selected classrooms.", messages.SUCCESS)
    add_to_classrooms.short_description = "Add selected students to classrooms"

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('class_id', 'class_name', 'teacher_name')
    search_fields = ('class_name', 'teacher_name')
    list_filter = ('class_name', 'teacher_name')

    def display_students(self, obj):
        return ", ".join([student.name for student in obj.students.all()])
    display_students.short_description = 'Students'

class AttendanceSessionInline(admin.TabularInline):
    model = AttendanceSession
    extra = 1
    show_change_link = True

@admin.register(AttendanceSession)
class AttendanceSessionAdmin(admin.ModelAdmin):
    list_display = ('session_id', 'classroom', 'date', 'start_time', 'end_time')
    search_fields = ('classroom__class_name', 'date')
    list_filter = ('classroom', 'date')
    inlines = [AttendanceInline]

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('session', 'student', 'attended', 'datetime')
    search_fields = ('session__classroom__class_name', 'student__name', 'session__date')
    list_filter = ('session__classroom', 'session__date', 'attended')
    raw_id_fields = ('session', 'student')
    fields = ('session', 'student', 'datetime', 'attended')

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'student':
            session_id = request.GET.get('session')
            if session_id:
                kwargs['queryset'] = db_field.related_model.objects.filter(classrooms__attendance_sessions__id=session_id).distinct()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
