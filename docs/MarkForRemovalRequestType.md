# MarkForRemovalRequestType

The parameters of *HostStorageSystem.MarkForRemoval*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hba_name** | **str** |  | 
**remove** | **bool** |  | 

## Example

```python
from vmware_vi.models.mark_for_removal_request_type import MarkForRemovalRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MarkForRemovalRequestType from a JSON string
mark_for_removal_request_type_instance = MarkForRemovalRequestType.from_json(json)
# print the JSON string representation of the object
print MarkForRemovalRequestType.to_json()

# convert the object into a dict
mark_for_removal_request_type_dict = mark_for_removal_request_type_instance.to_dict()
# create an instance of MarkForRemovalRequestType from a dict
mark_for_removal_request_type_form_dict = mark_for_removal_request_type.from_dict(mark_for_removal_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


