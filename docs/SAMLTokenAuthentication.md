# SAMLTokenAuthentication

SAMLTokenAuthentication contains the information necessary to authenticate within a guest using a SAML bearer token.  SAML token authentication relies on a guest alias that associates a guest account with the subject and certificate encoded in a SAML token obtained from the VMware SSO Server. - Use the *GuestAliasManager*.   *GuestAliasManager.AddGuestAlias* method to create a guest   alias. - Use a SAMLTokenAuthentication object for the   auth parameter to guest operations methods.    After you have created an alias, you can use SAML token authentication for guest operations methods. Do not use SAML token authentication for the *GuestAuthManager.AcquireCredentialsInGuest* and *GuestAuthManager.ReleaseCredentialsInGuest* methods.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | The SAML bearer token.  ***Since:*** vSphere API 6.0  | 
**username** | **str** | This is the guest user to be associated with the authentication.  If none is specified, a guest dependent mapping will decide what user account is applied.  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.saml_token_authentication import SAMLTokenAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of SAMLTokenAuthentication from a JSON string
saml_token_authentication_instance = SAMLTokenAuthentication.from_json(json)
# print the JSON string representation of the object
print SAMLTokenAuthentication.to_json()

# convert the object into a dict
saml_token_authentication_dict = saml_token_authentication_instance.to_dict()
# create an instance of SAMLTokenAuthentication from a dict
saml_token_authentication_form_dict = saml_token_authentication.from_dict(saml_token_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


