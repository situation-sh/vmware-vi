# MergeDvsRequestType

The parameters of *DistributedVirtualSwitch.MergeDvs_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dvs** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 

## Example

```python
from vmware_vi.models.merge_dvs_request_type import MergeDvsRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of MergeDvsRequestType from a JSON string
merge_dvs_request_type_instance = MergeDvsRequestType.from_json(json)
# print the JSON string representation of the object
print MergeDvsRequestType.to_json()

# convert the object into a dict
merge_dvs_request_type_dict = merge_dvs_request_type_instance.to_dict()
# create an instance of MergeDvsRequestType from a dict
merge_dvs_request_type_form_dict = merge_dvs_request_type.from_dict(merge_dvs_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


