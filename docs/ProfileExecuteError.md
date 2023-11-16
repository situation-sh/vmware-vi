# ProfileExecuteError

The *ProfileExecuteError* data object describes an error encountered during host profile execution.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | [**ProfilePropertyPath**](ProfilePropertyPath.md) |  | [optional] 
**message** | [**LocalizableMessage**](LocalizableMessage.md) |  | 

## Example

```python
from vmware_vi.models.profile_execute_error import ProfileExecuteError

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileExecuteError from a JSON string
profile_execute_error_instance = ProfileExecuteError.from_json(json)
# print the JSON string representation of the object
print ProfileExecuteError.to_json()

# convert the object into a dict
profile_execute_error_dict = profile_execute_error_instance.to_dict()
# create an instance of ProfileExecuteError from a dict
profile_execute_error_form_dict = profile_execute_error.from_dict(profile_execute_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


