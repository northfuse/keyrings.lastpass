from keyring.backend import KeyringBackend
from keyring import errors
from keyring.util import properties
from keyrings.lpass.lpass import lastpass_installed, lpass

PRIORITY = 10

class LastPassKeyring(KeyringBackend):
    @properties.ClassProperty
    @classmethod
    def priority(cls):
        if not lastpass_installed():
            raise RuntimeError(
                "Requires lastpass cli"
            )

        return PRIORITY

    def get_password(self, service, username):
        print("get: " + service + " " + username)
        return lpass(["foo"])

    def set_password(self, service, username, password):
        print("set: " + service + " " + username + " " + password)
        """Set password for the username of the service.
        If the backend cannot store passwords, raise
        NotImplementedError.
        """
        raise errors.PasswordSetError("reason")

    def delete_password(self, service, username):
        print("delete: " + service + " " + username)
        """Delete the password for the username of the service.
        If the backend cannot store passwords, raise
        NotImplementedError.
        """
        raise errors.PasswordDeleteError("reason")
