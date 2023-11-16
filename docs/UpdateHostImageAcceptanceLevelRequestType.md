# UpdateHostImageAcceptanceLevelRequestType

The parameters of *HostImageConfigManager.UpdateHostImageAcceptanceLevel*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_acceptance_level** | **str** | the new AcceptanceLevel to set.  | 

## Example

```python
from vmware_vi.models.update_host_image_acceptance_level_request_type import UpdateHostImageAcceptanceLevelRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHostImageAcceptanceLevelRequestType from a JSON string
update_host_image_acceptance_level_request_type_instance = UpdateHostImageAcceptanceLevelRequestType.from_json(json)
# print the JSON string representation of the object
print UpdateHostImageAcceptanceLevelRequestType.to_json()

# convert the object into a dict
update_host_image_acceptance_level_request_type_dict = update_host_image_acceptance_level_request_type_instance.to_dict()
# create an instance of UpdateHostImageAcceptanceLevelRequestType from a dict
update_host_image_acceptance_level_request_type_form_dict = update_host_image_acceptance_level_request_type.from_dict(update_host_image_acceptance_level_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


