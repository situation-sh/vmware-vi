# ProfileUpdateFailedUpdateFailure


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_path** | [**ProfilePropertyPath**](ProfilePropertyPath.md) |  | 
**err_msg** | [**LocalizableMessage**](LocalizableMessage.md) |  | 

## Example

```python
from vmware_vi.models.profile_update_failed_update_failure import ProfileUpdateFailedUpdateFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileUpdateFailedUpdateFailure from a JSON string
profile_update_failed_update_failure_instance = ProfileUpdateFailedUpdateFailure.from_json(json)
# print the JSON string representation of the object
print ProfileUpdateFailedUpdateFailure.to_json()

# convert the object into a dict
profile_update_failed_update_failure_dict = profile_update_failed_update_failure_instance.to_dict()
# create an instance of ProfileUpdateFailedUpdateFailure from a dict
profile_update_failed_update_failure_form_dict = profile_update_failed_update_failure.from_dict(profile_update_failed_update_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


