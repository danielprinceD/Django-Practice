from rest_framework import permissions

class Staff_Permissions(permissions.DjangoModelPermissions):
    def has_permissions(self, request):
        user = request.user
        print(user.get_all_permissions())
        if user.is_staff:
            if user.has_perm("Product.add_Product"):
                return True
            if user.has_perm("Product.delete_Product"):
                return True
            if user.has_perm("Product.change_Product"):
                return True
            if user.has_perm("Product.delete_Product"):
                return True
        return False