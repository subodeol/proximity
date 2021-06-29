
from rest_framework import permissions

class IsInstructer(permissions.BasePermission):
    """
    permission check for Instructor.
    """

    def has_permission(self, request, view):
        return request.user.is_instructor


class IsStudent(permissions.BasePermission):
    """
    permission check for Student.
    """

    def has_permission(self, request, view):
        return not request.user.is_instructor