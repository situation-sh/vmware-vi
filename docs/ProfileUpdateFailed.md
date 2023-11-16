# ProfileUpdateFailed

Errors were detected during Profile update.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure** | [**List[ProfileUpdateFailedUpdateFailure]**](ProfileUpdateFailedUpdateFailure.md) | Failures encountered during update/validation  ***Since:*** vSphere API 4.0  | 
**warnings** | [**List[ProfileUpdateFailedUpdateFailure]**](ProfileUpdateFailedUpdateFailure.md) | Warnings encountered during update/validation  ***Since:*** vSphere API 6.7  | [optional] 

## Example

```python
from vmware_vi.models.profile_update_failed import ProfileUpdateFailed

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileUpdateFailed from a JSON string
profile_update_failed_instance = ProfileUpdateFailed.from_json(json)
# print the JSON string representation of the object
print ProfileUpdateFailed.to_json()

# convert the object into a dict
profile_update_failed_dict = profile_update_failed_instance.to_dict()
# create an instance of ProfileUpdateFailed from a dict
profile_update_failed_form_dict = profile_update_failed.from_dict(profile_update_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


