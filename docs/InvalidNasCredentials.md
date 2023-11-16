# InvalidNasCredentials

This fault is thrown when an operation to configure a CIFS volume fails because the credentials specified in the *spec* are incorrect.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | The username associated with the CIFS connection.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.invalid_nas_credentials import InvalidNasCredentials

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidNasCredentials from a JSON string
invalid_nas_credentials_instance = InvalidNasCredentials.from_json(json)
# print the JSON string representation of the object
print InvalidNasCredentials.to_json()

# convert the object into a dict
invalid_nas_credentials_dict = invalid_nas_credentials_instance.to_dict()
# create an instance of InvalidNasCredentials from a dict
invalid_nas_credentials_form_dict = invalid_nas_credentials.from_dict(invalid_nas_credentials_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


