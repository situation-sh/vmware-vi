# LoginByTokenRequestType

The parameters of *SessionManager.LoginByToken*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | A two-character ISO-639 language ID (like \&quot;en\&quot;) optionally followed by an underscore and a two-character ISO 3166 country ID (like \&quot;US\&quot;).  Examples are \&quot;de\&quot;, \&quot;fr\\_CA\&quot;, \&quot;zh\&quot;, \&quot;zh\\_CN\&quot;, and \&quot;zh\\_TW\&quot;. Note: The method uses the server default locale when a locale is not provided. This default can be configured in the server configuration file. If unspecified, it defaults to the locale of the server environment or English (\&quot;en\&quot;) if unsupported.  | [optional] 

## Example

```python
from vmware_vi.models.login_by_token_request_type import LoginByTokenRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of LoginByTokenRequestType from a JSON string
login_by_token_request_type_instance = LoginByTokenRequestType.from_json(json)
# print the JSON string representation of the object
print LoginByTokenRequestType.to_json()

# convert the object into a dict
login_by_token_request_type_dict = login_by_token_request_type_instance.to_dict()
# create an instance of LoginByTokenRequestType from a dict
login_by_token_request_type_form_dict = login_by_token_request_type.from_dict(login_by_token_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


