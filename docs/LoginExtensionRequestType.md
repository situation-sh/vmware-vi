# LoginExtensionRequestType

The parameters of *SessionManager.LoginExtension*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_key** | **str** | Key of extension that is logging in.  | 
**base64_signed_credentials** | **str** | base-64 encoding of the SHA-1 digest of the string \&quot;login\&quot; signed with the extension&#39;s private RSA key using PKCS#1 padding.  | 
**locale** | **str** | A two-character ISO-639 language ID (like \&quot;en\&quot;) optionally followed by an underscore and a two-character ISO 3166 country ID (like \&quot;US\&quot;).  Examples are \&quot;de\&quot;, \&quot;fr\\_CA\&quot;, \&quot;zh\&quot;, \&quot;zh\\_CN\&quot;, and \&quot;zh\\_TW\&quot;. Note: The method uses the server default locale when a locale is not provided. This default can be configured in the server configuration file. If unspecified, it defaults to the locale of the server environment or English (\&quot;en\&quot;) if unsupported.  | [optional] 

## Example

```python
from vmware_vi.models.login_extension_request_type import LoginExtensionRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of LoginExtensionRequestType from a JSON string
login_extension_request_type_instance = LoginExtensionRequestType.from_json(json)
# print the JSON string representation of the object
print LoginExtensionRequestType.to_json()

# convert the object into a dict
login_extension_request_type_dict = login_extension_request_type_instance.to_dict()
# create an instance of LoginExtensionRequestType from a dict
login_extension_request_type_form_dict = login_extension_request_type.from_dict(login_extension_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


