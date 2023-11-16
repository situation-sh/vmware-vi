# SetMultipathLunPolicyRequestType

The parameters of *HostStorageSystem.SetMultipathLunPolicy*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lun_id** | **str** | The logical unit ID  | 
**policy** | [**HostMultipathInfoLogicalUnitPolicy**](HostMultipathInfoLogicalUnitPolicy.md) |  | 

## Example

```python
from vmware_vi.models.set_multipath_lun_policy_request_type import SetMultipathLunPolicyRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of SetMultipathLunPolicyRequestType from a JSON string
set_multipath_lun_policy_request_type_instance = SetMultipathLunPolicyRequestType.from_json(json)
# print the JSON string representation of the object
print SetMultipathLunPolicyRequestType.to_json()

# convert the object into a dict
set_multipath_lun_policy_request_type_dict = set_multipath_lun_policy_request_type_instance.to_dict()
# create an instance of SetMultipathLunPolicyRequestType from a dict
set_multipath_lun_policy_request_type_form_dict = set_multipath_lun_policy_request_type.from_dict(set_multipath_lun_policy_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


