import struct
import msal


class AADAuthAccessTokenRetrievalError(Exception):
    pass


class AADAuth(object):
    """
    Defines the Azure Active Directory authentication class.
    """

    @classmethod
    def _get_access_token(cls, authority, client_id, scopes, secret):
        """
        Retrieves the application's access token through AAD.

        Parameters½
        ----------
        authority : str
            The AAD authority url which is of the form
            `https://login.microsoftonline.com/<TENANT_ID>`.
        client_id : str
            The client identifier used to authenticate.
        scopest : list
            The list of scopes to use to authenticate. For database
            connections we should be using`["https://database.windows.net//.default"]`.
        secret : str
            The secret to authenticate with.

        Returns
        -------
        str
            The retrieved access token if present; otherwise, `None`.
        """
        app = msal.ConfidentialClientApplication(
            client_id, authority=authority, client_credential=secret
        )
        result = app.acquire_token_silent(scopes, account=None)
        if not result:
            result = app.acquire_token_for_client(scopes=scopes)
        access_token = result.get("access_token", None)
        return access_token

    @classmethod
    def _struct_from_access_token(cls, access_token):
        """
        Create a structure from the access token.

        Parameters
        ----------
        access_token : str
            The access token to convert.

        Returns
        -------
        str
            The expanded token structure required.
        """
        token_bytes = bytes(access_token, "UTF-8")
        expanded_token = b""
        for i in token_bytes:
            expanded_token += bytes({i})
            expanded_token += bytes(1)
        token_struct = struct.pack("=i", len(expanded_token)) + expanded_token
        return token_struct

    @classmethod
    def _construct_attrs_before_using_access_token(cls, access_token):
        """
        Constructs the `attrs_before` `pyodbc` parameter from an access token.

        Parameters
        ----------
        access_token : str
            The access token to construct the parameter with.

        Returns
        -------
        dict
            The `attrs_before` dictionary of values that will be used to authenticate
            using the access token.
        """
        SQL_COPT_SS_ACCESS_TOKEN = 1256
        token_struct = cls._struct_from_access_token(access_token)
        attrs_before = {SQL_COPT_SS_ACCESS_TOKEN: token_struct}
        return attrs_before

    @classmethod
    def create_attrs_before_with_access_token(cls, config):
        """
        Creates the `attrs_before` `pyodbc` parameter by first retrieving an AAD 
        access token for the application and then using it to build the parameter.

        Parameters
        ----------
        config : dict
            The dictionary of values needed to retrieve an application access token.
            Should contain `tenant_id`, `client_id` and `secret`.

        Returns
        -------
        dict
            The `attrs_before` dictionary of values that will be used to authenticate
            using the access token.

        Raises
        ------
        AADAuthAccessTokenRetrievalError
            When unable to retrieve a valid access token, the exception is raised.
        """
        tenant_id = config["tenant_id"]
        client_id = config["client_id"]
        secret = config["secret"]
        authority = "https://login.microsoftonline.com/" + tenant_id
        scopes = ["https://database.windows.net//.default"]
        access_token = cls._get_access_token(authority, client_id, scopes, secret)
        if not access_token:
            raise AADAuthAccessTokenRetrievalError("Unable to retrieve access token!")

        attrs_before = cls._construct_attrs_before_using_access_token(access_token)
        return attrs_before
